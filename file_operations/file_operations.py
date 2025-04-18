# Update server.conf file when "MAX_CONNECTIONS=200" & modify it to "MAX_CONNECTIONS=500".


def update_srv_config(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readlines()
        #print(lines)
    
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_srv_config("server.conf", "MAX_CONNECTIONS", "500")
