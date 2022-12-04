import os
import subprocess
import wget
import zipfile

if __name__ == "__main__":
    dataset_folder = "fingerprint_data"


    if(os.path.exists(dataset_folder)):
        subprocess.run(["rm","-rf", dataset_folder])   
    os.makedirs(dataset_folder)

    if(not os.path.exists("UareU_sample_DB.zip")):
        url = "https://www.neurotechnology.com/download/UareU_sample_DB.zip"
        wget.download(url)

    zip = zipfile.ZipFile("UareU_sample_DB.zip")
    zip.extractall(dataset_folder)

    files = os.listdir(dataset_folder)
    files.sort()

    current_user = "012"
    current_actual_number = 1

    for file in files:
        extension = file.split(".")[1]
        if(extension != "tif"):
            continue
        filename_data = file.split("_")
        
        file_user_number = filename_data[0]
        file_finger_number = filename_data[1]
        file_take_number = filename_data[2]

        if(current_user != file_user_number):
            current_actual_number = current_actual_number + 1
            current_user = file_user_number

        new_filename = "{}_{}_{}".format(str(current_actual_number),file_finger_number, file_take_number)
        
        subprocess.run(["mv", "{}/{}".format(dataset_folder,file), "{}/{}".format(dataset_folder,new_filename)])

    subprocess.run(["mogrify", "-format", "jpg", "{}/*.tif".format(dataset_folder), "-depth", "8", "-strip"])
    subprocess.run(["rm", "{}/*.tif".format(dataset_folder)])

    print("Done!")