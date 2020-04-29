def content_filtering(user):

    # frequently used libraries
    import numpy as np
    import pandas as pd
    
    # read user role and project role data entered by users
    user_role_df = pd.read_csv('user_role_df.csv', index_col=0)
    project_role_df = pd.read_csv('project_role_df.csv', index_col=0)
    
    # pivot tables to show ratings for each role in columns suitable for similarity analysis
    user_rating_df = user_role_df.pivot(index='user_id', columns='role_id', values='rating')
    user_rating_df.fillna(0.0, inplace=True)
    project_rating_df = project_role_df.pivot(index='project_id', columns='role_id', values='rating')
    project_rating_df.fillna(0.0, inplace=True)
    
    # set of roles for each project
    project_role_series = project_role_df.groupby('project_id')['role_id'].agg(lambda x: set(x))

    # libraries for sparse matrix and cosine similarity 
    from scipy.sparse import csr_matrix
    from sklearn.metrics.pairwise import cosine_similarity
    
    # dataframe of similar projects and similarity value for sorting 
    similar_projects = pd.DataFrame(columns=['project', 'similarity'])
        
    # go through all projects in database
    for project in project_rating_df.index:

        # calculate similarity of user role with project role
        user_rating_sparse = scipy.sparse.csr_matrix(user_rating_df.iloc[user, :].values)
        project_rating_sparse = scipy.sparse.csr_matrix(project_rating_df.iloc[project, :].values)
        similarity = cosine_similarity(user_rating_sparse, project_rating_sparse)
        similar_projects.loc[len(similar_projects)] = [project, similarity[0][0]]
    
    # sort projects based on similarity values 
    sorted_projects_float = similar_projects.sort_values(by='similarity', ascending=False)['project'].tolist()
    recommended_projects = list(map(int, sorted_projects_float))

    # subset of similar projects compatible with user skill level 
    for project in recommended_projects:
        for role in project_role_series.iloc[project]:
            required_skills = (project_role_df['project_id']==project) & (project_role_df['role_id']==role)
            qualified_skill = (user_role_df['user_id']==user) & (user_role_df['role_id']==role)
            if project_role_df[required_skills].experience.values > user_role_df[qualified_skill].experience.values:
                recommended_projects.remove(project)
                break
                
    return recommended_projects