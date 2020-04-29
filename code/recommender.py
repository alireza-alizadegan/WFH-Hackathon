# The two recommender algorithms
# Load data here from csv

def getCurrent(user):
    # return a list of projects based off the users current interest ratings
    # and experience
    # !!! Needs to be passed back as JSON
    # return {"name": 'Paint-by-Numbers',
    #         "description": 'Create a paint-by-numbers blank image from any given picture',
    #         "time": 2,
    #         "user_id": 1,
    #         "user_limit": 3
    #         }

    projects = [
    {
    "name": "Paint-by-numbers",
    "description": 'Create a paint-by-numbers blank image from any given picture',
    "time": 3,
    "duration": "7 weeks",
    "project_owner": "Tom",
    "num_users":3,
    "user_limit": 5,
    "interests":[
    	{
    		"interest": "Gardening",
    		"experience": "Expert"
    	},
    	{
    		"interest": "Cooking",
    		"experience": "Beginner"
    	},
    	{
    		"interest": "Coding",
    		"experience": "Intermediate"
    	}
	]},
    {"name": "Paint-by-numbers",
    "description": 'Create a paint-by-numbers blank image from any given picture',
    "time": 3,
    "duration": "7 weeks",
    "project_owner": "Tom",
    "num_users":3,
    "user_limit": 5,
    "interests":[
    	{
    		"interest": "Gardening",
    		"experience": "Expert"
    	},
    	{
    		"interest": "Cooking",
    		"experience": "Beginner"
    	},
    	{
    		"interest": "Coding",
    		"experience": "Intermediate"
    	}
	]},
    {"name": "Paint-by-numbers",
    "description": 'Create a paint-by-numbers blank image from any given picture',
    "time": 3,
    "duration": "7 weeks",
    "project_owner": "Tom",
    "num_users":3,
    "user_limit": 5,
    "interests":[
    	{
    		"interest": "Gardening",
    		"experience": "Expert"
    	},
    	{
    		"interest": "Cooking",
    		"experience": "Beginner"
    	},
    	{
    		"interest": "Coding",
    		"experience": "Intermediate"
    	}
	]},
    {"name": "Paint-by-numbers",
    "description": 'Create a paint-by-numbers blank image from any given picture',
    "time": 3,
    "duration": "7 weeks",
    "project_owner": "Tom",
    "num_users":3,
    "user_limit": 5,
    "interests":[
    	{
    		"interest": "Gardening",
    		"experience": "Expert"
    	},
    	{
    		"interest": "Cooking",
    		"experience": "Beginner"
    	},
    	{
    		"interest": "Coding",
    		"experience": "Intermediate"
    	}
	]},
    {"name": "Paint-by-numbers",
    "description": 'Create a paint-by-numbers blank image from any given picture',
    "time": 3,
    "duration": "7 weeks",
    "project_owner": "Tom",
    "num_users":3,
    "user_limit": 5,
    "interests":[
    	{
    		"interest": "Gardening",
    		"experience": "Expert"
    	},
    	{
    		"interest": "Cooking",
    		"experience": "Beginner"
    	},
    	{
    		"interest": "Coding",
    		"experience": "Intermediate"
    	}
	]}
    ]

    return projects
    # return {"name": user["name"],
    #         "age": user["age"],
    #         "time": user["time"],
    #         "zipcode": user["zipcode"],
    #         "interests": user["interests"]
    #         }

def getFuture(user):
    # return a list of projects based off other users with similar interests
    # and experiences
    # !!! Needs to be passed back as JSON
    # return {"name": 'Spotify Concert Playlist',
    #         "description": 'Create a playlist of artists coming to your city in the next 3 months',
    #         "time": 4,
    #         "user_id": 2,
    #         "user_limit": 2
    #         }
    return {"name": user["name"],
            "age": user["age"],
            "time": user["time"],
            "zipcode": user["zipcode"],
            "interests": user["interests"]
            }
