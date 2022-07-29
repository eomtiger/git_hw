import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다. to
    
    api_key = 'eb91384b5d1bdc5b11f6949707f5381d'
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(URL).json()
    a = response.get('results')
    return len(a) #result 리스트의 항목의 개수를 구함
    #pprint(response)

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
