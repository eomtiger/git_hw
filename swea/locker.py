# def rotation(N, K, S):
    
#     S = list(S)

#     s = []
#     for i in range(4):
#         s.append(S[int(N/4)*i :int(N/4)*(i+1)])

#     #print(s)
#     a = []
#     for i in range(len(s)):
#         a.append(int(s[i][0], 16)*16**2 + int(s[i][1], 16)*16 + int(s[i][2],16))
    
#     for i in range(3):
#         b = S.pop(0)
    
#         S.append(b)

#         s = []
#         for i in range(4):
#             s.append(S[int(N/4)*i :int(N/4)*(i+1)])
   
#         for i in range(len(s)):
#             a.append(int(s[i][0], 16)*16**2 + int(s[i][1], 16)*16 + int(s[i][2],16))

#     #print(a)
#     sett = set(a)
#     #print(sett)
#     rt_list = list(sett)
#     rt_list.sort()
#     print(rt_list[K-1])
    
    

#rotation(16,4,'1A3456789456ABED')

def rotation(N, K, S):
    
    S = list(S)

    s = []
    for i in range(4):
        s.append(S[int(N/4)*i :int(N/4)*(i+1)])

    #print(s)
    a = []
    for i in range(len(s)):
        a.append(int(s[i][0], 16)*16**2 + int(s[i][1], 16)*16 + int(s[i][2],16))
    
    for i in range(3):
        b = S.pop(0)
    
        S.append(b)

        s = []
        for i in range(4):
            s.append(S[int(N/4)*i :int(N/4)*(i+1)])
   
        for i in range(len(s)):
            a.append(int(s[i][0], 16)*16**2 + int(s[i][1], 16)*16 + int(s[i][2],16))

    #print(a)
    sett = set(a)
    #print(sett)
    rt_list = list(sett)
    rt_list.sort()
    return rt_list[K-1]

print(rotation(16,4,'1A3456789456ABED'))   
# T = int(input())

# for i in range(T):
# 	N, K = map(int, input().split())
# 	S = input()
#     print(f'#{i+1} ',rotation(N,K,S))