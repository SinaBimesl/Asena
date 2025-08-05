import os
import json
from error_handler import handle_error

path = os.path.join(os.path.dirname(__file__), "server_list.JSON")

def find_fastest_dns():
    """
    Find the fastest DNS server from a list defined in `server_list.JSON` by measuring average ping time.
    ____
    Pings each IP address 4 times using the `ping` command.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            presets = json.load(file)

        fastest_result = None  

        for server_name, ip_list in presets.items():
            for ip in ip_list:
                
                try:   
                    command = (f"ping -c 4 {ip}")
                    print(f"\033[34mTesting {ip} from {server_name} ...")
                    output = os.popen(command).read()

                    for line in output.splitlines():
                        if "avg" in line:
                            avg_time = line.split('/')[4]
                            avg_time = float(avg_time)
     
                            if fastest_result is None or avg_time < fastest_result[2]:
                                fastest_result = (server_name, ip, avg_time)

                except Exception as e:
                    handle_error(e)

        if fastest_result:
            return (f"\033[32mFastest: {fastest_result[1]} ({fastest_result[0]}) ping: {fastest_result[2]}ms")
        else:
            return ("\033[31mNo successful ping results.")

    except Exception as err:
        handle_error(err)
        return None


