import React from 'react'
import Profile from './Profile'

function Recommendation() {

    let profiles = 
[
    {
"name": "Paint-by-numbers",
"description": "Create a paint-by-numbers blank image from any given picture",
"time": 3,
"duration": "7 weeks",
"project_owner": "Tom",
"num_users": 3,
"user_limit": 5,
"interests": [
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
        ]
    },
    {
"name": "Paint-by-numbers",
"description": "Create a paint-by-numbers blank image from any given picture",
"time": 3,
"duration": "7 weeks",
"project_owner": "Tom",
"num_users": 3,
"user_limit": 5,
"interests": [
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
        ]
    },
    {
"name": "Paint-by-numbers",
"description": "Create a paint-by-numbers blank image from any given picture",
"time": 3,
"duration": "7 weeks",
"project_owner": "Tom",
"num_users": 3,
"user_limit": 5,
"interests": [
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
        ]
    },
    {
"name": "Paint-by-numbers",
"description": "Create a paint-by-numbers blank image from any given picture",
"time": 3,
"duration": "7 weeks",
"project_owner": "Tom",
"num_users": 3,
"user_limit": 5,
"interests": [
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
        ]
    },
    {
"name": "Paint-by-numbers",
"description": "Create a paint-by-numbers blank image from any given picture",
"time": 3,
"duration": "7 weeks",
"project_owner": "Tom",
"num_users": 3,
"user_limit": 5,
"interests": [
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
        ]
    }
]

let mappedProfile = profiles.map((profile, index) => {
    return (
      <div className="project__card">
        <h5 className="project__card-name">{profile.name}</h5>
        <p className="project__card-time">`${profile.time}hours/week` </p>
        <p className="project__card-description">{profile.description}</p>
      </div>
    );
})

    return (
      <>
        <div className="recommendation">
          <h2 className="recommendation__title">Suggested Projects For You</h2>
          <h4 className="recommendation__subtitle">Project List</h4>
          <div className="recommendation__projects">{mappedProfile}</div>
        </div>
      </>
    );
}

export default Recommendation
