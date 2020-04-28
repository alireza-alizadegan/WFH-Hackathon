import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#should put all requirements in a requirements.txt file so uploading necessary libraries is easy

#import data in format:
#user_id, interests, rating

#any data json manipulation goes here
#SVD input dataframe = interests_df
interests_df = 

#using surprise for SVD
from surprise import Reader
#need this reader to handle the ratings in surprise
reader = Reader(rating_scale=(1, 5))

#need to convert the dataframe into a dataset compatible with the Surprise library
from surprise import Dataset
data = Dataset.load_from_df(interests_df[['user_id', 'interests', 'rating']], reader)

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
predictions = algo.test(trainset)

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
top_n = get_top_n(predictions, n=10)

# Print the recommended items for specific user
# need to find the top_n for specific user, this will get all users
uid = 1 #try first user?
for uid, user_ratings in top_n.items():
    recs = [iid in user_ratings]
    print(uid, [iid for (iid, _) in user_ratings])
#current output looks like this:
#5c9d0a0f9e6b95d773ab0a3ea10dd06bd2629736 ['SOYWEJZ12AB0183988', 'SOLRGVL12A8C143BC3', 'SORZCRI12A8AE4807B', 'SOLXVSH12AB018BE14', 'SOVNREB12AB017ACAC', 'SODJJAU12A8C13A16F', 'SOAXKNC12AF72A4BF8', 'SOVHZVI12A8C14398A', 'SOEZUTY12A8C132CED', 'SOFMWSD12A8C13CE54']
#how to output to json for one user uid=1
import json
print(json.dumps(uid))
print(json.dumps(recs))