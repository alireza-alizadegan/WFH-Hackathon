def content_filtering(user):

    # frequently used libraries
    import numpy as np
    import pandas as pd
    
    # read user interest and project interest data entered by users
    user_interest_df = pd.read_csv('user_interest_df.csv', index_col=0)
    project_interest_df = pd.read_csv('project_interest_df.csv', index_col=0)
    
    # pivot tables to show ratings for each interest in columns suitable for similarity analysis
    user_rating_df = user_interest_df.pivot(index='user_id', columns='interest_id', values='rating')
    user_rating_df.fillna(0.0, inplace=True)
    project_rating_df = project_interest_df.pivot(index='project_id', columns='interest_id', values='rating')
    project_rating_df.fillna(0.0, inplace=True)
    
    # set of interests for each project
    project_interest_series = project_interest_df.groupby('project_id')['interest_id'].agg(lambda x: set(x))

    # libraries for sparse matrix and cosine similarity 
    from scipy.sparse import csr_matrix
    from sklearn.metrics.pairwise import cosine_similarity
    
    # dataframe of similar projects and similarity value for sorting 
    similar_projects = pd.DataFrame(columns=['project', 'similarity'])
        
    # go through all projects in database
    for project in project_rating_df.index:

        # calculate similarity of user interest with project interest
        user_rating_sparse = scipy.sparse.csr_matrix(user_rating_df.iloc[user, :].values)
        project_rating_sparse = scipy.sparse.csr_matrix(project_rating_df.iloc[project, :].values)
        similarity = cosine_similarity(user_rating_sparse, project_rating_sparse)
        similar_projects.loc[len(similar_projects)] = [project, similarity[0][0]]
    
    # sort projects based on similarity values 
    sorted_projects_float = similar_projects.sort_values(by='similarity', ascending=False)['project'].tolist()
    recommended_projects = list(map(int, sorted_projects_float))

    # subset of similar projects compatible with user skill level 
    for project in recommended_projects:
        for interest in project_interest_series.iloc[project]:
            required_skills = (project_interest_df['project_id']==project) & (project_interest_df['interest_id']==interest)
            qualified_skill = (user_interest_df['user_id']==user) & (user_interest_df['interest_id']==interest)
            if project_interest_df[required_skills].experience.values > user_interest_df[qualified_skill].experience.values:
                recommended_projects.remove(project)
                break
                
    return recommended_projects