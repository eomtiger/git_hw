import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    api_key = 'eb91384b5d1bdc5b11f6949707f5381d'
    t = title
    URL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko&page=1&query={t}'
    response = requests.get(URL).json()
    #pprint(response)
    if bool(response.get('results')) == False : 
        return None         #results가 없으면 None

    elif bool(response.get('results')) == True :  #result 있으면 
        movie_id = response.get('results')[0].get('id') #id 값 추출
   
        rec_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko'
        res = requests.get(rec_url).json() #무비크레딧 뽑음

        casting = []
        for i in range(len(res['cast'])):     
            if res['cast'][i]['cast_id'] < 10: #cast의 cast_id가 10보다 작으면
                casting.append(res['cast'][i]['name'])  #이름을 casting에 넣음

        direct = []
        for i in range(len(res['crew'])):       
            if res['crew'][i]['department'] == 'Directing': #crew 가 Directing소속이면
                direct.append(res['crew'][i]['name'])  #이름을 direct에 넣는다
        
        return {'cast' : casting, 'directing' : direct}

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
