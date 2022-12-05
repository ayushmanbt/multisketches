# Importing the libraries
import os
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha256
import random
import time

'''
Whereever there is w it is a tuple of fingerprints

Also state has two things the matching algorithm L and the Database F
'''

number_of_fingers = 10

# Instead of creating a dedicated DB we are using a runtime variable for quick implementation
user_kv = {}
fingerprint_data = []


# Sketches function
def ssencrypt(w):

    aes_key = get_random_bytes(16)
    encryptor = AES.new(aes_key, AES.MODE_CBC)

    hash = []

    ct_bytes = encryptor.encrypt(pad(bytes(str(w), "utf-8"), AES.block_size))
    for w_bar in w:

        hash_of_current_w_bar = bytes(sha256(str(w_bar).encode('utf-8')).digest())

        special_key_encryptor = AES.new(hash_of_current_w_bar, AES.MODE_CBC)

        encrypted_key = special_key_encryptor.encrypt(pad(aes_key, AES.block_size))
        
        hash.append(encrypted_key)
    
    v = (hash, ct_bytes)

    return v


def ssdecrypt(w,v):
    
    hash,encrypted_text = v
    ws = []

    for i, w_bar in enumerate(w):
        this_hash = hash[i]
        hash_w_bar = bytes(sha256(str(w_bar).encode('utf-8')).digest())
        decryptor = AES.new(hash_w_bar, AES.MODE_CBC)
        
        try:
            key_prime = unpad(decryptor.decrypt(this_hash), AES.block_size)
            second_decryptor = AES.new(key_prime, AES.MODE_CBC)
            ww = second_decryptor.decrypt(encrypted_text)
            ws.append(ww)
        except:
            continue
    if(len(ws) == 0):
        return False
    return ws

# Utility Functions

def convert(filename, root):
    '''
    
    '''
    filename_without_extension = filename.split(".")[0]
    subprocess.run(["mindtct", os.path.join(root,filename), os.path.join(root,filename_without_extension)])

    with open(os.path.join(root,filename_without_extension + "." + "xyt"), "rb") as xyt:
        return xyt.read()
    



def compare(w1,w2):
    '''
    How bozorth3 works

    bozorth3 [options] <file1.xyt> <file2.xyt>
    '''


    #Compare the two sets of fingerprints
    with open("temp1.xyt","wb") as a:
        with open("temp2.xyt","wb") as b:
            a.write(w1)
            b.write(w2)

    res = subprocess.run(["bozorth3","temp1.xyt","temp2.xyt"], stdout=subprocess.PIPE)
    
    return_value = str(res.stdout, "utf-8").split("\n")[0]
    
    subprocess.run(["rm", "temp1.xyt"])
    subprocess.run(["rm", "temp2.xyt"])

    if(int(return_value) < 20):
        return False
    else:
        return True


def findMatches(w_i, i):
    for row in fingerprint_data:
        w_dash = row[i]
        if(compare(w_dash, w_i)):
            return w_dash

def MS(uid, w):
    v = ssencrypt(w)   
    user_kv[uid] = v

    new_row = [None] * number_of_fingers

    fingerprint_data.append(new_row)
    N = len(fingerprint_data) - 1

    for i in range(number_of_fingers):
        j = random.randint(0,N)
        if(j < N):
            fingerprint_data[N][i] = fingerprint_data[j][i]
        fingerprint_data[j][i] = w[i]



def MRec(uid, w):
    if(uid not in user_kv.keys()):
        print("User is not registered yet! Please register user using 1")
        return
    v = user_kv[uid]
    x = []
    for i in range(number_of_fingers):
        w_p = w[i]
        found_match = findMatches(w_p, i)
        if(found_match != None):
            x.append(found_match)
    return ssdecrypt(x,v)


if __name__ == "__main__":
    print("Starting program")
    #source_folder = input("Enter path to image source folder: ")
    source_folder = "fingerprint_data"
    while(True):
        print("1. Add user")
        print("2. Verify Fingerprint")
        print("3. Exit")

        option = input("Enter Choice: ")

        if(option == "1"):
            uid = input("Enter user number[1-7 except 6 cause data of user 6 is corrupted]: ")
            w = []
            start = time.time()
            for i in range(1,11):
                w.append(convert("{}_{}_{}.jpg".format(uid, i, 1), source_folder))
            MS(uid, w)
            print("User registered successfully")
            print("----It took {} seconds to register the user with {} users registered----".format(str(time.time() - start), str(len(user_kv) - 1)))
        elif(option == "2"):
            uid = input("Enter user number[1-7]: ")
            uid2 = input("Enter scanned fingerprint number[1-7 except 6 cause data of user 6 is corrupted]: ")
            start = time.time()
            w = []
            for i in range(1,11):
                w.append(convert("{}_{}_{}.jpg".format(uid2, i, random.randint(2,8)), source_folder))
            w_prime = MRec(uid,w)
            if(not w_prime):
                print("Fingerprints did not match")
            else:
                print("Fingerprints matched, you logged in")
            print("----It took {} seconds to find the user with {} users registered----".format(str(time.time() - start), str(len(user_kv))))
        else:
            break

    