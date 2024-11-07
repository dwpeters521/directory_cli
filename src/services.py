from directories import FileSystem

def process_commands(commands: str):
    fs = FileSystem()
    command_list = commands.splitlines()
    for command in command_list:
        directory_list = command.split(" ")
        directory_name = directory_list[1] if len(directory_list) > 1 else None
        
        if command.startswith("CREATE"):
            fs.create(directory_name)

        if command.startswith("DELETE"):
            fs.delete(directory_name)

        if command.startswith("MOVE"):
            destination_directory_name = directory_list[2]
            fs.move(directory_name, destination_directory_name)

        if command.startswith("LIST"):
            fs.list()

