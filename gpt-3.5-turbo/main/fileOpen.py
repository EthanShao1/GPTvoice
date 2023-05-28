def fileRead(fileAddress):
    with open(fileAddress, mode= "r", encoding= "utf-8") as file:
        data = file.read()
    
    return data

def fileWrite(fileAddress, data):
    with open(fileAddress, mode= "w", encoding= "utf-8") as file:
        file.write(data)