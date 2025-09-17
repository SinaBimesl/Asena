import os
from error_handler import handle_error

path = os.path.join(os.path.dirname(__file__), "server_list.JSON")


def show_current_dns():
    """
    Get the current DNS configuration from the system.

    Returns:
        list: A list of current DNS IP addresses
    """
    try:
        dns_list = []
        with open("/etc/resolv.conf", "r") as file:
            for line in file:
                if line.startswith("nameserver"):
                    dns_list.append(line.strip())
        return dns_list

    except Exception as err:
        handle_error(err)
        return None


def reset_dns():
    """
    Reset the system DNS to its default configuration.
    __
    defualt value: nameserver 192.168.1.1
    ___
    #Change "defualt_dns" value if you want another
    defualt value.
    """
    try:
        defualt_dns = "nameserver 192.168.1.1"
        reset_cmd = f"echo '{defualt_dns}' | sudo tee /etc/resolv.conf > /dev/null"
        os.system(reset_cmd)
        return f"System DNS reset successfully to {defualt_dns}"

    except Exception as err:
        handle_error(err)
        return None


def change_dns(dns1, dns2=None):
    """
    Set the system DNS to the provided IP addresses
    """
    try:
        messages = []
        content = f"nameserver {dns1}"
        cmd1 = f"echo {content} | sudo tee /etc/resolv.conf > /dev/null"
        os.system(cmd1)
        messages.append(f"Server: {dns1} add successfully.")

        if dns2:
            content2 = f"nameserver {dns2}"
            cmd2 = f"echo {content2} | sudo tee -a /etc/resolv.conf > /dev/null"
            os.system(cmd2)
            messages.append(f"Second server: {dns2} add successfully.")

        return "\n".join(messages)

    except Exception as err:
        handle_error(err)
        return None


if __name__ == "__main__":
    print("This is module!!!")
