def update_server_config(file_path,key,value):
    # Read the existing content of the server configuration file and store in a variable
    with open(file_path,"r") as file:
        lines = file.readlines()  # readlines() returns a list of all lines.

    # edit the file         
    # Opening a file in write mode 'w' truncates the file immediately — meaning all existing content is erased. Now, the file is empty, even if it had content before.
    with open(file_path,'w') as file: 
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)        # Keep the existing line as it is

server_file = "/media/dd/epic/Devops_shiva/git/repos/python/server.conf"
key = "MAX_CONNECTIONS"
value = "500"
update_server_config(server_file,key,value)
