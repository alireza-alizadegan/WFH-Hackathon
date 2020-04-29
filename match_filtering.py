def match_filtering(user):
    
    # frequently used libraries
    import numpy as np
    import pandas as pd

    # read user role and project role data entered by users
    user_role_df = pd.read_csv('user_role_df.csv', index_col=0)
    project_role_df = pd.read_csv('project_role_df.csv', index_col=0)
    
    # set of roles for each user and project
    user_role_series = user_role_df.groupby('user_id')['role_id'].agg(lambda x: set(x))
    project_role_series = project_role_df.groupby('project_id')['role_id'].agg(lambda x: set(x))
    
    # list of projects matching roles of inquiring user
    is_role_match = user_role_series.iloc[user]==project_role_series.values
    match_projects = project_role_series[is_role_match].index.tolist() 
    
    # subset of match projects compatible with user skill level 
    for project in match_projects:
        for role in project_role_series.iloc[project]:
            required_skill = (project_role_df['project_id']==project) & (project_role_df['role_id']==role)
            qualified_skill = (user_role_df['user_id']==user) & (user_role_df['role_id']==role)
            if project_role_df[required_skill].experience.values > user_role_df[qualified_skill].experience.values:
                match_projects.remove(project)
                break

    return match_projects