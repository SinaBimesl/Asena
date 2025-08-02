import os
import json
from error_handler import handle_error
from dns_manager import change_dns

path = os.path.join(os.path.dirname(__file__), "server_list.JSON")

def show_presets():
    """
    Reads the preset DNS list and returns it as a list of strings.
    """
    try:
        with open(f'{path}' , 'r',encoding='utf-8') as file:
            server_name = json.load(file)
        
        preset = server_name
        result = []
        counter = 1
        for name, dns in preset.items():
            dns1 = dns[0]
            dns2 = dns[1] if len(dns) > 1 else ''
            result.append (f"{counter}- {name}: {dns1} - {dns2}")
            counter += 1            
        return result
    
    except Exception as err:
        handle_error(err)
        return None
        
def remove_preset(name):
    """
    Delete a DNS server from server_list.JSON
    """
    try:
        with open (f'{path}' , 'r' ,encoding="utf-8") as file:
            server_list = json.load(file)
        
        if name in server_list:
            del server_list [name]
            with open(path, 'w', encoding="utf-8") as file:
                json.dump(server_list, file, indent=2)
            return (f"{name} preset successfully deleted.")
        
        else:
            return (f"{name} dosen't exist!")
        
        with open (f'{path}' , 'w' ,encoding="utf-8") as file:
            json.dump(server_list, file, indent=2)
            
    except Exception as err:
        handle_error(err)
        return None
        
def add_preset(name, primary, secondary = None):
    """
    Add new DNS preset and returns a status message.
    """
    
    try:
        with open (f'{path}' , 'r' ,encoding="utf-8") as file:
            server_list = json.load(file)
            
        if name in server_list:
            return (f"{name} is exist.")
                    
        server_list [name] = [primary] if secondary is None else [primary, secondary]

        with open (f'{path}' , 'w' ,encoding="utf-8") as file:
            json.dump(server_list, file, indent=2)
            return (f"{name} add to preset list successfully.")
            
    except Exception as err:
        handle_error(err)
        return None
        
def use_preset(name):
    """
    apply a preset with name parameter in server_list.JSON file
    """
    try:
        with open (f'{path}' , "r" , encoding = "utf-8") as file:
            server_list = json.load(file)
            
            preset = server_list
            available = False
            for n, server in preset.items():
                if n == name:
                    available = True
                    first_dns = server[0]
                    second_dns = (server[1] if len(server) > 1 else None)
                    
            if available:
                return change_dns(first_dns, second_dns)
            else:
                return (f"{name} doesn't exist in presets.")
            
    except Exception as err:
        handle_error(err)
        return None
    