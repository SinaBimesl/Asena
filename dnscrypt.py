import os, shutil, subprocess, time
from dns_manager import change_dns, reset_dns
from error_handler import handle_error

CONFIG_PATH = "/etc/dnscrypt-proxy/dnscrypt-proxy.toml"
LISTEN_IP = "127.0.0.1"
LISTEN_PORT = 53 ##Change it in systmd (maybe)

def is_installed():
    """
    Check presence of dnscrypt-proxy binary and config file
    """
    return shutil.which("dnscrypt-proxy") is not None and os.path.isfile(CONFIG_PATH)

def is_running():
    """
    Return True if dnscrypt-proxy is already running.
    """
    result = subprocess.run(["pgrep", "-x", "dnscrypt-proxy"], stdout=subprocess.PIPE)
    return result.returncode == 0

def wait_ready(timeout=5):
    """
    Wait until local resolver replies. Uses 'dig' if available, else sleep
    """
    if shutil.which("dig"):
        start = time.time()
        while time.time() - start < timeout:
            r = subprocess.run(
                ["dig", f"@{LISTEN_IP}", "-p", str(LISTEN_PORT),
                 "example.com", "+time=1", "+tries=1"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            if r.returncode == 0 and "ANSWER SECTION" in r.stdout:
                return True
            time.sleep(0.4)
        return False
    else:
        time.sleep(min(timeout, 2))
        return True

def start_dnscrypt():
    """
    Start dnscrypt-proxy and set system DNS to 127.0.0.1
    """
    try:
        if not is_installed():
            print("dnscrypt-proxy not installed or config missing.")
            return False

        if not is_running():
            try:
                subprocess.Popen(
                    ["dnscrypt-proxy", "-config", CONFIG_PATH],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                print("dnscrypt-proxy started. Waiting for readiness …")
            except Exception as e:
                handle_error(e)
                return False
        else:
            print("dnscrypt-proxy already running.")

        if not wait_ready(timeout=6):
            print("dnscrypt-proxy may not be ready (check port 53 conflicts).")
            return False

        if change_dns(LISTEN_IP):
            print(f"System DNS set to {LISTEN_IP}")
            print("DNSCrypt active.")
            return True
        else:
            print("Failed to set system DNS (try sudo).")
            return False

    except Exception as e:
        handle_error(e)
        return False

def stop_dnscrypt(restore_dns=True):
    """
    Stop dnscrypt-proxy and optionally restore system DNS (reset_dns)
    """
    try:
        subprocess.run(["pkill", "-x", "dnscrypt-proxy"])
        print("dnscrypt-proxy stopped.")
        if restore_dns:
            if reset_dns():
                print("System DNS restored.")
            else:
                print("Could not restore system DNS.")
        return True
    except Exception as e:
        handle_error(e)
        return False
