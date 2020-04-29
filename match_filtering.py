def match_filtering(user):
    import numpy as np
    import pandas as pd
    user_interest_df = pd.read_csv('user_interest_df.csv', index_col=0)
    project_interest_df = pd.read_csv('project_interest_df.csv', index_col=0)
    user_interest_series = user_interest_df.groupby('user_id')['interest_id'].agg(lambda x: set(x))
    project_interest_series = project_interest_df.groupby('project_id')['interest_id'].agg(lambda x: set(x))
    interested_projects = project_interest_series[user_interest_series.iloc[user]==project_interest_series.values].index.tolist() 
    for project in interested_projects:
    for interest in project_interest_series.iloc[project]:
        if project_interest_df[(project_interest_df['project_id']==project) & (project_interest_df['interest_id']==interest)].experience.values > user_interest_df[(user_interest_df['user_id']==user) & (user_interest_df['interest_id']==interest)].experience.values:
            interested_projects.remove(project)
            break
    return interested_projects





