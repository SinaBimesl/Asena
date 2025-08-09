# DNS Tool 🧰🔐

A simple, Linux‑first DNS management tool with a modular backend, a friendly CLI, and optional DNS speed tests and DNSCrypt integration.

- Show / change / reset system DNS
- Manage custom presets from `server_list.JSON`
- Find the fastest DNS by ping
- Start/stop DNSCrypt and switch system DNS to `127.0.0.1` automatically

> CLI entrypoint: `python3 main.py`

---

## ✨ Features

- **Show current DNS** (reads `/etc/resolv.conf`)
- **Change DNS** (one or two servers)
- **Reset DNS to default** (editable default in code)
- **Preset management**: list / add / remove / apply (JSON file)
- **DNS speed test** (ping 4x, picks lowest avg)
- **DNSCrypt integration**: start/stop/status + set DNS to `127.0.0.1`

---

## 📦 Requirements

- **Python 3.8+**
- System tools (recommended):
  - `dnscrypt-proxy` (for DNSCrypt feature)
  - `dig` (for readiness check; optional)
  - `iputils` (for ICMP used in the speed test)
- **sudo/root** when modifying `/etc/resolv.conf` (the tool writes nameserver lines).

### Install `dnscrypt-proxy` (examples)

```bash
# Arch
sudo pacman -S dnscrypt-proxy    # or: yay -S dnscrypt-proxy

# Debian / Ubuntu
sudo apt update && sudo apt install dnscrypt-proxy

# Fedora
sudo dnf install dnscrypt-proxy
```

> Config is typically at `/etc/dnscrypt-proxy/dnscrypt-proxy.toml`. The tool expects that path by default.
"Change it ,if you need"

---

## 🚀 Quick Start

```bash
git clone https://github.com/SinaBimesl/Asena.git
cd ~/Asena
python3 main.py

#run with super user for all feature
```

Common flows:

- **Change DNS** → choose `2`, enter primary/secondary (optional).
- **Use a preset** → add/list/apply via options `4/5/7`.
- **Test fastest DNS** → option `8` (pings all IPs in presets and prints the fastest).
- **Enable DNSCrypt** → option `9` (starts proxy, waits until ready, sets DNS to `127.0.0.1`).
- **Disable DNSCrypt** → option `10` (kills proxy, optionally resets DNS).

---

## 🏎️ DNS Speed Test (CLI)

- Pings each IP 4 times: `ping -c 4 <ip>`
- Parses the `avg` latency line and picks the minimum  
- Shows progress lines like `Testing 1.1.1.1 from cloudflare ...`  
- Prints the winner: `Fastest: <ip> (<name>) ping: <ms>ms`

---

## 🔐 DNSCrypt

- Checks install & config, starts `dnscrypt-proxy` in the background
- Waits for readiness (uses `dig` if available)
- Sets system DNS to `127.0.0.1`  
  
> If port **53** is occupied (e.g., a local resolver), you may need to stop it or reconfigure DNSCrypt to another port.

---

## ⚠️ Notes & Permissions

- Modifying `/etc/resolv.conf` requires elevated privileges.
- Network managers may overwrite DNS. If changes don’t stick, disable auto‑DNS for your active profile and set `127.0.0.1` manually when using DNSCrypt.
