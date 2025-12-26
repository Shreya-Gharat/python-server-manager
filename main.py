import resource_manager

servers = []

while True:
    print(f"1. Add Server\n2. Remove Server\n3. Show Inventory\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1" or choice.lower() == "add server":
        server_name = input("Enter the name of the server you want to add: ")
        servers = resource_manager.add_server(servers,server_name)
    elif choice == "2" or choice.lower() == "remove server":
        server_name = input("Enter the name of the server you want to remove: ")
        servers = resource_manager.remove_server(servers,server_name)
    elif choice == "3" or choice.lower() == "show inventory":
        resource_manager.display_inventory(servers)
    elif choice == "4" or choice.lower() == "exit":
        break
    else:
        print("Invalid choice. Please try again.")       