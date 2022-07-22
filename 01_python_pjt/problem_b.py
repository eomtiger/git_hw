import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    value_list = []
    for i in key_list:
        value_list.append(movie[i])

    genre_names = []

    for  i in range(len(genres)):
        if genres[i]['id'] == value_list[-1][0]  :
            genre_names.append(genres[i]['name'])

        elif genres[i]['id'] == value_list[-1][-1] :
            genre_names.append(genres[i]['name'])
    
    new_dict = {}
    for i in range(len(key_list)):
        new_dict[key_list[i]] = value_list[i]  
    
    new_dict['genre_names'] = genre_names
    del new_dict['genre_ids']


    return new_dict



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
