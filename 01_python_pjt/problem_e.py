import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    import os
    file_list = os.listdir('data/movies')

    a = []
    for i in range(len(file_list)):

        movies_json = open('data/movies/'+ str(file_list[i]), encoding='utf-8')
        movies_list = json.load(movies_json)    
        a.append(movies_list)

    b = []
    for i in range(len(a)):
        if a[i]['release_date'][5:7] == '12':
            b.append(a[i]['title'])
            

    return b 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies('movies_list'))
