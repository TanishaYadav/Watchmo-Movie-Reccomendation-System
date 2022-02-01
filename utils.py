import pickle
import pandas
import requests



api_key = "6a2476dc4dc9f8e785809f8790fa6f5e"

data = pandas.DataFrame(pickle.load(open('movies.pkl','rb')))
movies_list = data['title_x'].values

similarity = pickle.load(open('similarity.pkl','rb'))




def recommend(movie):
    recommendations = []
    posters = []
    try:
        # if title exists in the data
        movie_idx = data[data['title_x'] == movie].index[0]
        distance = similarity[movie_idx]
        movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]    # list of top 5 recommended movies as (movie_index,similarity_score)

        for movie_index,_ in movies:
            recommendations.append(data.iloc[movie_index]['title_x'])
            movie_id = data.iloc[movie_index]['movie_id']
            posters.append(get_poster(movie_id))
        return zip(recommendations,posters)
    except:
        return zip(recommendations, posters)
def get_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US").json()
    return f"https://image.tmdb.org/t/p/original{response['poster_path']}"



# https://api.themoviedb.org/3/movie/440?api_key=6a2476dc4dc9f8e785809f8790fa6f5e&language=en-US