import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    api_key = 'eb91384b5d1bdc5b11f6949707f5381d'
    t = title
    URL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko&page=1&query={t}'
    response = requests.get(URL).json()
    #pprint(response)
    if bool(response.get('results')) == False : #response result값이 []라면 
        return None                             #none 반환

    elif bool(response.get('results')) == True : # elif 
        movie_id = response.get('results')[0].get('id') #response의 results가 존재하고 
                                                         #첫번째 영화의 아이디 값을 구함
        rec_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko&page=1'
        res = requests.get(rec_url).json() # id 값과 관련된 영화 추천
        

        if bool(res['results']) == True:  #추천영화가 있다면
            a=[]                                 #a에 제목을 담는다
            for i in range(len(res['results'])):
                a.append(res['results'][i].get('title'))
            return a
    
        elif bool(res['results']) == False: #추천이 없으면
            return []                        # []을 뱉는다
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
