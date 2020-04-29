import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_top_n import get_top_n

#should put all requirements in a requirements.txt file so uploading necessary libraries is easy

#import data in format:
#user_id, interests, rating

#any data json manipulation goes here
#SVD input dataframe = interests_df
user_interests_df = pd.read_csv("./data/user_interests_df.csv")

#using surprise for SVD
from surprise import Reader
#need this reader to handle the ratings in surprise
reader = Reader(rating_scale=(1, 5))

#need to convert the dataframe into a dataset compatible with the Surprise library
from surprise import Dataset
data = Dataset.load_from_df(user_interests_df[['user_id', 'interest_id', 'rating']], reader)

#bring in SURPRISE!
from surprise import SVD
#we will use default settings, no hypertuning yet

#converting data dataframe to a "trainset"
trainset = data.build_full_trainset()
#run the trainset through SVD
algo = SVD(n_epochs=40, lr_all=0.004)
algo.fit(trainset)
#no train or test set for this, using all data for now
#get predictions from SVD
predictions = algo.test(trainset)

#get top 10 recommended projects, can change this to as many as we want later
top_n = get_top_n(predictions, n=10)

# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])
