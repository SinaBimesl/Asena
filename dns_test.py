import os
from error_handler import handle_error
import json

path = os.path.join(os.path.dirname(__file__), "server_list.JSON")

def dns_ping(name):
    
    try:
        with open(f'{path}' , 'r',encoding='utf-8') as file:
            presets = json.load(file)
        
        for server, dns in presets.items():
            if name == server:
                test = dns[0]
                command = (f"ping -c 4 {test}")
                dns_test = os.system(command)
                ping_result = dns_test
                return ping_result
    except Exception as err:
        handle_error(err)
        return None
                    
    
sina = dns_ping("google")
print(sina)
