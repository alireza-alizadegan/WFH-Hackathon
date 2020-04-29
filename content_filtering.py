def content_filtering(user):
    import numpy as np
    import pandas as pd
    user_interest_df = pd.read_csv('user_interest_df.csv', index_col=0)
    project_interest_df = pd.read_csv('project_interest_df.csv', index_col=0)
    user_rating_df = user_interest_df.pivot(index='user_id', columns='interest_id', values='rating')
    user_rating_df.fillna(0.0, inplace=True)
    project_rating_df = project_interest_df.pivot(index='project_id', columns='interest_id', values='rating')
    project_rating_df.fillna(0.0, inplace=True)
    project_interest_series = project_interest_df.groupby('project_id')['interest_id'].agg(lambda x: set(x))
    import scipy
    from scipy.sparse import csr_matrix
    from sklearn.metrics.pairwise import cosine_similarity
    # store similar projects in this dataframe
    similar_projects = pd.DataFrame(columns=['project', 'similarity'])
        
    # go through all projects
    for project in project_rating_df.index:
                    
        # calculate similarity of two projects
        user_rating_sparse = scipy.sparse.csr_matrix(user_rating_df.iloc[user, :].values)
        project_rating_sparse = scipy.sparse.csr_matrix(project_rating_df.iloc[project, :].values)
        similarity = cosine_similarity(user_rating_sparse, project_rating_sparse)
        similar_projects.loc[len(similar_projects)] = [project, similarity[0][0]]

    recommended_projects=list(map(int, similar_projects.sort_values(by='similarity', ascending=False)['project'].tolist()))

    for project in recommended_projects:
        for interest in project_interest_series.iloc[project]:
            if project_interest_df[(project_interest_df['project_id']==project) & (project_interest_df['interest_id']==interest)].experience.values > user_interest_df[(user_interest_df['user_id']==user) & (user_interest_df['interest_id']==interest)].experience.values:
                recommended_projects.remove(project)
                break
                
    return recommended_projects