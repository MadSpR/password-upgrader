import hashlib
import requests


#### FUNCTIONS

def decryptPass(password):
    plainPass = requests.get(f"https://www.nitrxgen.net/md5db/{password}") # send the hash and return (if found) the password using the ntrxgen API
    temp = plainPass.text
    if(len(temp) is 0): # check that it does not return an empty string, if returned it makes a line break
        temp = "\n"
    return temp


def encryptPass256(password):
    sha2=hashlib.sha256() # creates a SHA-256 hash object
    sha2.update(password.encode('utf-8')) # convert the string to bytes and update the hash object
    hash_hex=sha2.hexdigest() # get the hexadecimal representation of the hash
    return hash_hex


#### PROGRAM

# asks the user for the file's route
file_pass_route = input("Write the absolute route of the password's file: ")
file_plain_route = input("Write the route where you want to safe the passwords in plain (./ for the actual directory): ")
file_new_route = input("Write the route where you want to safe the new  hashed passwords (./ for the actual directory): ")

print("Reading file...")
file=open(file_pass_route, "rt")
fileplain=open(f"{file_plain_route}/plain.txt", "w")

lineas=file.readlines()
for linea in lineas:
    password = decryptPass(str(linea)) # decrypt the password by calling the function
    print(password)
    fileplain.write(f"{password}\n") # write the password to the unhashed file

file.close()
fileplain.close()

fileplain=open(f"{file_plain_route}/plain.txt", "r")
fileNew=open(f"{file_new_route}/new_passwords.txt", "w")

lineas=fileplain.readlines()
count = 0
for linea in lineas: 
    count+=1
    temp="{:04d}".format(count) # format the customer number
    nuevaPass=f"smthn{temp}{str(linea)}" # build the structured password
    print(nuevaPass)
    temp=encryptPass256(nuevaPass) # hashes the new password by calling the function
    fileNew.write(f"{temp}\n") # store the hashed password in SHA-256

fileplain.close()
fileNew.close()