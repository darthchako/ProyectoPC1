import os

def tokenizar(texto):
    tokens = texto.split()
    return tokens


# folder path
dir_read_path = 'D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/TRANSCRIPT/RAW/'
dir_write_path = 'D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/TRANSCRIPT/TOKENS/'
# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_read_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_read_path, path)):
        res.append(path)

        file_read_path = dir_read_path + path
        file_write_path = dir_write_path + path
        text = ''

        ##Leemos el archivo de transcripción y guardamos el contenido en la variable text
        with open(file_read_path, 'r') as file_read:
            text = file_read.read().rstrip()

        ##Extraemos los token del texto    
        stringtokens = tokenizar(text)

        ##Leemos el archivo de transcripción y guardamos el contenido en la variable text
        file_write = open(file_write_path, "w")
        n = file_write.write(str(stringtokens))
        file_write.close()
        #print(stringtokens)

#print(res)