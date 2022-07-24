def max_score(scores):
    scores.sort()
    return(scores[-1])


def over(scores):

    a = []
    for i in range(len(scores)):
        if scores[i] >= 60 :
            a.append(scores[i])
    
    return(len(a))


scores = [90, 80, 15, 20]

# print(over(scores))
# print(max_score(scores))

def menu_count(rest):
    pass
    
    return len(rest['menus'])
weather = [1,3,4,5,6,7,3,7,89,76,4,5,4]
def turn(weather):
    pass 

    return {'maximum': max(weather), 'minimum' : min(weather)}
           # dict(maximum = max(weather), minimum = min(weather))

#print(turn(weather))
data = 1
def is_user_data_valid(data):
    id_data = input('id를 입력하세요 : ')
    password_data = input('비밀번호를 입력하세요 : ')

    #print(password_data)
    #print(id_data or password_data)
    if (id_data == '' or password_data == '') :
        return(False)
            
    else :
         return(True)

#print(is_user_data_valid(data))

user_id = input('id를 입력하세요 : ')
user_password = input('password를 입력하세요 : ')

user_data = dict(id = user_id, password = user_password)

def is_id_valid(user_data):

    a = []
    
    for i in range(10):
        a.append(str(i))

    if user_data['id'][-1] in a:
        return (True)
    else :
        return(False)
print(is_id_valid(user_data))