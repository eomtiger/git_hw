# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from xmlrpc.client import boolean


def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    lot = 1
    a= [n]
    b= []    
    while bool(a[0]) == False : 
         
        if int(a[0]) != 1:
            
            b.append(int(a[0]) % 2)
            a[0] = n // 2
            
        elif int(a[0]) == 1:
            b.append(1)
            a[0] = 0
            
       
        
        
    
    c = ''
    b.sort(reverse = True)
    for i in range(len(b)):
        c += str(b[i])

    return b


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010
    