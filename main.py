from dns_manager import show_current_dns, change_dns, reset_dns
from presets_manager import show_presets, add_preset, remove_preset, use_preset
from dns_test import find_fastest_dns
from dnscrypt import start_dnscrypt , is_running , stop_dnscrypt

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

def menu():
    """
    Command-line interface.
    """
    while True:
        print(f"\n{BOLD}{CYAN}=== DNS Tool Menu ==={RESET}")
        print(f"{YELLOW}1{RESET}- Show current DNS")
        print(f"{YELLOW}2{RESET}- Change DNS")
        print(f"{YELLOW}3{RESET}- Reset DNS")
        print(f"{YELLOW}4{RESET}- Show presets")
        print(f"{YELLOW}5{RESET}- Add preset")
        print(f"{YELLOW}6{RESET}- Remove preset")
        print(f"{YELLOW}7{RESET}- Use preset")
        print(f"{YELLOW}8{RESET}- Test DNS Servers")
        print(f"{YELLOW}9{RESET}- DNSCrypt Enable")
        print(f"{YELLOW}10{RESET}- DNSCrypt Disable")
        print(f"{YELLOW}11{RESET}- DNSCrypt Status")
        print(f"{RED}0{RESET}- Exit")

        choice = input(f"{BOLD}Enter your choice: {RESET}").strip()

        if choice == "1":
            dns_list = show_current_dns()
            if dns_list:
                for dns in dns_list:
                    print(f"{BLUE}{dns}{RESET}")

        elif choice == "2":
            dns1 = input("Enter first DNS: ").strip()
            dns2 = input("Enter second DNS (or leave blank): ").strip() or None
            print(change_dns(dns1, dns2))

        elif choice == "3":
            print(reset_dns())

        elif choice == "4":
            presets = show_presets()
            if presets:
                for p in presets:
                    print(f"{BLUE}{p}{RESET}")

        elif choice == "5":
            name = input("Preset name: ").strip()
            dns1 = input("First DNS: ").strip()
            dns2 = input("Second DNS (or leave blank): ").strip() or None
            print(add_preset(name, dns1, dns2))

        elif choice == "6":
            name = input("Enter preset name to remove: ").strip()
            print(remove_preset(name))

        elif choice == "7":
            name = input("Enter preset name to use: ").strip()
            print(use_preset(name))
            
        elif choice == "8":
            result = find_fastest_dns()
            print(result)
        
        elif choice == "9":
            ok = start_dnscrypt()
            print("Done." if ok else "Failed.")
            
        elif choice == "10":
            ok = stop_dnscrypt(restore_dns=True)
            print("Stopped." if ok else "Failed.")
            
        elif choice == "11":
            
            print("DNSCrypt is running." if is_running() else "DNSCrypt is not running.")

        elif choice == "0":
            print(f"{RED}Exiting...{RESET}")
            break

        else:
            print(f"{RED}Invalid choice, try again.{RESET}")

if __name__ == "__main__":
    menu()





