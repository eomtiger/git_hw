import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
    movie_inf = []
    for i in range(len(movies)):
        
        value_list = []
        for key in key_list:
            value_list.append(movies[i][key])

        genre_names = []

        for  k in range(len(genres)):
            if genres[k]['id'] == value_list[-1][0]  :
                genre_names.append(genres[k]['name'])

            elif genres[k]['id'] == value_list[-1][-1] :
                genre_names.append(genres[k]['name'])
    
        new_dict = {}
        for j in range(len(key_list)):
            new_dict[key_list[j]] = value_list[j]  
    
        new_dict['genre_names'] = genre_names
        del new_dict['genre_ids']
        movie_inf.append(new_dict)

    return movie_inf


        
# 아래의 코드는 수정하지 않습니다.


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
