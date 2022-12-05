'''
The purpose of this program is to find -
1. the lowest score if two fingerprints match in our dataset
2. the highest score if two fingerprints do not match
'''


# Imports
import subprocess
import os
import time

min_match_score = 500
match_file1 = ""
match_file2 = ""
max_unmatch_score = 0
unmatch_file1 = ""
unmatch_file2 = ""


root = "fingerprint_data"

def convert(filename):
    filename_without_extension = filename.split(".")[0]
    subprocess.run(["mindtct", os.path.join(root,filename), os.path.join(root,filename_without_extension)])

def compare(f1,f2):
    res = subprocess.run(["bozorth3","fingerprint_data/{}".format(f1),"fingerprint_data/{}".format(f2)], stdout=subprocess.PIPE)
    return int(str(res.stdout, "utf-8").split("\n")[0])


if __name__ == "__main__":
    total_persons = 7   # 1 to 7
    total_fingers = 10 # 1 to 10
    total_takes = 8    # 1 to 8

    start_time = time.time()
    

    for person1 in range(1, total_persons + 1):
        for finger1 in range(1, total_fingers):
            for take1 in range(1, total_takes):
                for person2 in range(1, total_persons + 1):
                    for finger2 in range(1, total_fingers):
                        for take2 in range(1, total_takes):
                            if(person1 == 6 or person2 == 6):
                                continue
                            if(person1 == person2 and finger1 == finger2 and take1 == take2):
                                continue
                            file1 = "{}_{}_{}.xyt".format(str(person1), str(finger1), str(take1))
                            file2 = "{}_{}_{}.xyt".format(str(person2), str(finger2), str(take2))
                            
                            if(not os.path.exists("fingerprint_data/{}".format(file1))):
                                convert("{}.jpg".format(file1.split(".")[0]))

                            if(not os.path.exists("fingerprint_data/{}".format(file2))):
                                convert("{}.jpg".format(file2.split(".")[0]))
                            
                            score = compare(file1,file2)

                            if(person1 == person2 and finger1 == finger2 and score < min_match_score):
                                min_match_score = score
                                match_file1 = file1
                                match_file2 = file2
                            
                            elif(score > max_unmatch_score and (finger1 != finger2 or person1 != person2)):
                                max_unmatch_score = score
                                unmatch_file1 = file1
                                unmatch_file2 = file2
    
    print("Min match score: ", min_match_score, 'between', match_file1, match_file2)
    print("Max unmatch score: ", max_unmatch_score, 'between', unmatch_file1, unmatch_file2)
    # This roughly gives us the time to chew through all the possible fingerprints for an user
    print("--- %s seconds ---" % (time.time() - start_time))