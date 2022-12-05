'''
The purpose of this program is to find -
1. the lowest score if two fingerprints match in our dataset
2. the highest score if two fingerprints do not match
'''


# Imports
import subprocess
import os
import time


root = "fingerprint_data"

def convert(filename):
    filename_without_extension = filename.split(".")[0]
    subprocess.run(["mindtct", os.path.join(root,filename), os.path.join(root,filename_without_extension)])

def compare(f1,f2):
    res = subprocess.run(["bozorth3","fingerprint_data/{}".format(f1),"fingerprint_data/{}".format(f2)], stdout=subprocess.PIPE)
    return int(str(res.stdout, "utf-8").split("\n")[0])


match_scores = []
unmatch_scores = []

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

                            if(person1 == person2 and finger1 == finger2):
                                match_scores.append((person1, finger1, [take1, take2], score))
                            else:
                                unmatch_scores.append(([person1,person2], [finger1, finger2], [take1, take2], score))
    
    
    avg_match = 0

    print("Match score: ")
    # Print Match Scores
    print("Person   Finger   Takes   Match Score")
    print("---------------------------------")
    for s in match_scores:
        avg_match += s[3]
        print("{}        {}        {}".format(s[0], s[1], s[2][0]))
        print("{}        {}        {}      {}".format(s[0], s[1], s[2][1], s[3]))
        print("---------------------------------")

    print()
    print("--------------------------------------------------------------------------------------------------------------")
    print()

    avg_match = avg_match / len(match_scores)

    # Print unmatch Scores

    avg_unmatch = 0
    print("Unmatch score: ")
    print("Person   Finger   Take   Match Score")
    print("---------------------------------")
    for s in unmatch_scores:
        avg_unmatch += s[3]
        print("{}        {}        {}".format(s[0][0], s[1][0], s[2][0]))
        print("{}        {}        {}      {}".format(s[0][1], s[1][1], s[2][1], s[3]))
        print("---------------------------------")

    avg_unmatch = avg_unmatch / len(unmatch_scores)
    # This roughly gives us the time to chew through all the possible fingerprints for an user
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Avg Match - {}".format(str(avg_match)))
    print("Avg Unmatch - {}".format(str(avg_unmatch)))
