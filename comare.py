def recommend_function(search_term, search_type='title'):
    try:
        if search_type == 'title':
            # Search based on title
            index = movies[movies['title'] == search_term].index[0]
        else:
            search_term = search_term.lower().replace(' ', '')
            # Search based on 'tags' (combination of overview, genres, keywords, cast, and crew)
            index = \
                movies[movies['tags'].apply(lambda x: search_term in x.replace(' ', ''))].index[
                    0]

        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = []
        recommended_movie_posters = []
        for i in distances[1:21]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movies.append({'id': movie_id, 'title': movies.iloc[i[0]].title})

        return recommended_movies, recommended_movie_posters
    except IndexError:
        print("Movie or search term not found.")
        return []
