# Here are some results from this code discussed

`find_min_max_of_match_score.py` is a file programmed to find all the possible matches. It was used to find out in a dataset of fingerprints how much match can be found using bozorth3.

The min match score was found to be 4
The max unmatch score was found to be 42

The dataset obtained from [https://www.neurotechnology.com/download/UareU_sample_DB.zip](https://www.neurotechnology.com/download/UareU_sample_DB.zip) has 6 users (Cause data of user 6 is incomplete and not used) each user has 10 fingers and each finger has 8 readings.

Avg Match Score was - 108.20987654320987
Avg Unmatch Score Was - 7.329382906202313



Now coming to the main file. Which implements tensketches using bozorth3. Let's see how much user registration took - 

With different amount of users in the database these are the average time each user took to be registered -

User 1 - 
    Take 1 - 0.531272554397583
    Take 2 - 0.4919845104217529
    Take 3 - 0.5442854404449463         avg - 0.52251416842143
User 2 -
    Take 1 - 0.4736513137817383
    Take 2 - 0.4722503662109375
    Take 3 - 0.4371179580688477         avg - 0.46100654602051
User 3 -
    Take 1 - 0.3798471927642822
    Take 2 - 0.4498380661010742
    Take 3 - 0.4213234424591064         avg - 0.41700290044149
User 4 -
    Take 1 - 0.4973684787750244
    Take 2 - 0.4001959800720215         
    Take 3 - 0.4223965644836426         avg - 0.4399870077769
User 5 -
    Take 1 - 0.4856542587280273
    Take 2 - 0.4038876533508301
    Take 3 - 0.4699822902679443         avg - 0.4531747341156
User 7 -
    Take 1 - 0.4605618953704834
    Take 2 - 0.4679194927215576
    Take 3 - 0.5118607521057129         avg - 0.48011404673258

Average Time of registering user 0.46229990058475 = 0.46s


Now with database filled with the data of these 6 users let's see the average time to find login state of the user - 1.12s 

> datapoint used:
0.9993927478790283, 0.9458246231079102, 1.1843342781066895, 1.1330459117889404, 1.2335855960845947,
1.1533730030059814, 1.200667142868042, 1.3156702518463135,
0.9526662826538086, 1.108828067779541 

To keep in mind everything here is going on a local system, so we can say the system can be a bit faster