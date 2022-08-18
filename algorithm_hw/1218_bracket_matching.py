for tc in range(10):
    N = int(input())
    br = input()

    open_a = '['                    #
    close_a = ']'                   #
    open_b = '{'                    #
    close_b = '}'                   #괄호 할당
    open_c = '('                    #
    close_c = ')'                   #
    open_d = '<'                    #
    close_d = '>'                   #
    coa = br.count(open_a)
    cca = br.count(close_a)
    cob = br.count(open_b)
    ccb = br.count(close_b)
    coc = br.count(open_c)          # count open_c -> coc
    ccc = br.count(close_c)
    cod = br.count(open_d)
    ccd = br.count(close_d)

    if (coa == cca) and (cob==ccb ) and (coc == ccc) and (cod == ccd):
        print(f'#{tc+1} 1')         #괄호의 짝 개수가 맞으면
    else:
        print(f'#{tc+1} 0')






