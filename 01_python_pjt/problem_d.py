import json


def max_revenue(movies):
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
    for k in range(len(a)):
        b.append(a[k]['revenue'])
    
    c = []
    for i in range(len(b)):
        if b[i] == max(b):
            c.append(i)
    
            
    return a[c[0]]['title']    

#아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
