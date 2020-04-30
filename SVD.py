import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_top_n import get_top_n

#should put all requirements in a requirements.txt file so uploading necessary libraries is easy

#import data in format:
#user_id, interests, rating

#any data json manipulation goes here
#SVD input dataframe = user_interests_df with 'experience' column dropped
user_interest_df = pd.read_csv('user_interest_df.csv', index_col=0)
#user_interest_df.drop(['experience'], axis=1, inplace=True)

#using surprise for SVD
from surprise import Reader
#need this reader to handle the ratings in surprise
reader = Reader(rating_scale=(1, 5))

#need to convert the dataframe into a dataset compatible with the Surprise library
from surprise import Dataset
data = Dataset.load_from_df(user_interest_df[['user_id', 'interest_id', 'rating']], reader)

#bring in SURPRISE!
from surprise import SVD
#we will use default settings, no hypertuning yet

#converting data dataframe to a "trainset"
trainset = data.build_full_trainset()
#run the trainset through SVD
algo = SVD(n_epochs=4, lr_all=0.004)
algo.fit(trainset)
#no train or test set for this, using all data for now
#get predictions from SVD
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

from collections import defaultdict
#function to get top-N recommendations for each user
def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    # Then sort the predictions for each user and retrieve the n highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n


#get top 10 recommended projects, can change this to as many as we want later
top_n = get_top_n(predictions, n=3)

# Print the recommended items for specific user
# need to find the top_n for specific user, this will get all users
#uid = 1 #try first user?
for uid, user_ratings in top_n.items():
    #recs = [iid in user_ratings]
    print(uid, [iid for (iid, _) in user_ratings])
#current output looks like this:
#5c9d0a0f9e6b95d773ab0a3ea10dd06bd2629736 ['SOYWEJZ12AB0183988', 'SOLRGVL12A8C143BC3', 'SORZCRI12A8AE4807B', 'SOLXVSH12AB018BE14', 'SOVNREB12AB017ACAC', 'SODJJAU12A8C13A16F', 'SOAXKNC12AF72A4BF8', 'SOVHZVI12A8C14398A', 'SOEZUTY12A8C132CED', 'SOFMWSD12A8C13CE54']
#how to output to json for one user uid=1
import json
print(json.dumps(uid))
print(json.dumps(recs))

#then match user_interest to project_interest for project_id
#generate list of project_id's
#change interest to role
#need to search for one user at a time, need to match with the generated recommendations
#need to provide Tom the input arguments for our function. Send what we need, just need the user_id, 
#everything else is in the files for now

#why dont we get all users with recommendations?
# the users that don't have any recs are the ones that have "rated" all interests all ready

#PSEUDOCODE FOR CONVERTING PROJECT IDS TO JSON

Given a list of project ids -> return a JSON object of projects

For loops over project id list:
	For each project id get the following data:
		Name (from the projects table)
		Description (from the projects table)
		Time (from the projects table)
Duration (from the projects table)
User limit (from the projects table)
Project image url (from the projects table)
Number of views (from the projects table)
Project owner name (get the user_id from project then lookup the user’s name from the users table)
Number of current users working on project (get all the user ids for the given project id from the Project User table)
Project owner image url (get from the user table using project owner id)
List of roles + experiences (get all the role ids and associated experience_ids for the given project id from the Project Roles table)

Function convertToJson(data above)
X = {
“name”: name,
“description”: description,
“time”: time,
“duration”: duration,
“user_limit”: user_limit,
“project_image”: project image url,
“num_views” = number of views,
“project_owner_name” = project owner name,
“num_users” = number of current users,
“project_owner_image_url”: project owner image url,
“roles”: Func makeDicts(list of roles)
}

Return json.dumps(x)

makeDicts(list of roles):
list = []
loop over roles:
	list.append {“role”: role[i][0], “experience”: role[i][1])
return list
