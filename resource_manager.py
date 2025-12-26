def add_server(current_list, new_server):
   current_list.append(new_server)
   return current_list

def remove_server(current_list, server_to_remove):
    if server_to_remove in current_list:
        current_list.remove(server_to_remove)
    else:
        print(f"Server {server_to_remove} not found in the list.")
    return current_list

def display_inventory(current_list):
    for server in current_list:
        print(server)
   
    
    