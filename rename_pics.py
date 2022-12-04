import os
import sys
import subprocess

if __name__ == "__main__":
    dataset_folder = sys.argv[1]
    files = os.listdir(dataset_folder)
    
    files.sort()

    current_file = "1"
    current_finger = 0
    for file in files:
        extension = file.split(".")[1]
        if(extension != "jpg"):
            continue
        file_number = file.split("__")[0]
        
        if(current_file == file_number):
            current_finger = current_finger + 1
        else:
            current_finger = 0
            current_file = file_number

        new_filename = "{}_{}.{}".format(current_file,current_finger, extension)
        
        subprocess.run(["mv", "{}/{}".format(dataset_folder,file), "{}/{}".format(dataset_folder,new_filename)])

    print("Done!")