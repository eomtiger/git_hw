# 여기에 필요한 모듈을 추가합니다.


class Lotto:
    
   
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []
        
        pass

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):

        import random
        
        for i in range(n):
            values = []
            while len(values) != 6:
                j = random.randint(1,45)
                if j in values:
                    pass
                else:
                    values.append(j)
            values.sort()
            self.number_lines.append(values)
        
            
        
        pass
    
    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        pass

        print('=========================================')
        print('         ' + '제' + str(draw_number)+ '회 로또')  
        print('=========================================')
        date = Lotto.get_draw_date(draw_number)
        print('추첨일 : ' , str(date[0])+'/'+str(date[1])+'/'+ str(date[2])+ '(토)' )
        print('=============================================')
        a = ['A', 'B', 'C', 'D', 'E']
        
        for i in range(len(self.number_lines)):
            print(a[i] + ':' , self.number_lines[i])

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):

        print('====================================')
        main_numbers = Lotto.get_lotto_numbers(draw_number)[0]
        bnusNo = Lotto.get_lotto_numbers(draw_number)[1]
        print('당첨번호 :', main_numbers, '+', bnusNo)
       
        print('======================================')
        
        a = ['A', 'B', 'C', 'D', 'E']
        for i in range(len(self.number_lines)):

            same_main_counts = Lotto.get_same_info(main_numbers, bnusNo, self.number_lines[i])[0]
            is_bonus = Lotto.get_same_info(main_numbers, bnusNo, self.number_lines[i])[1]

            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            if ranking in (1,2,3,4,5):
                print(a[i], ':', same_main_counts, '개 일치'+'(',ranking, '등 당첨!)' )
            elif ranking == -1:
                print(a[i], ':', same_main_counts, '개 일치'+'(낙첨)' )
                

        pass

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        pass

        import json
        a = open('data/lotto_' + str(draw_number)+ '.json', encoding ='utf-8')
        b = json.load(a)
        year = b["drwNoDate"][0:4]
        month = b["drwNoDate"][5:7]
        day = b["drwNoDate"][8:]
        return (year, month, day)

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        pass
        import json
        a = open('data/lotto_' + str(draw_number)+ '.json', encoding ='utf-8')
        b = json.load(a)
        key_list = list(b.keys())

        main_numbers = []
        dwrt_list = []
        for i in key_list:
            if i.startswith('drwt'):
                dwrt_list.append(i)
        
        for i in dwrt_list:
            main_numbers.append(b.get(i))
        main_numbers.sort()

        bonus_number = b['bnusNo']

        return (main_numbers, bonus_number)
        
        

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        pass
        
        a = []
        for i in range(6):
            if line[i] in main_numbers:
                a.append(line[i])
        same_main_counts = len(a)

        if bonus_number in line:
            is_bonus = True
        else :
            is_bonus = False

        return (same_main_counts, is_bonus)
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        pass
        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5 and is_bonus ==True:
            ranking = 2
        elif same_main_counts == 5:
            ranking = 3
        elif same_main_counts == 4:
            ranking =4
        elif same_main_counts == 3:
            ranking =5
        elif same_main_counts <= 2:
            ranking = -1
        return ranking
