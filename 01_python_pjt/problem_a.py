import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
    value_list = []
    for i in key_list:
        value_list.append(movie[i])
    
    new_dict = {}
    for i in range(len(key_list)):
        new_dict[key_list[i]] = value_list[i]  
    
    return new_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
