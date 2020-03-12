import random
import numpy

class Game:
    def __init__(self):
        self.suitcases = [
            0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000
        ]
        self.round = 6
        self.user_ammount = 0
        self.offer = 0
        self.case_array = []
        self.cases_left = 26 - self.suitcases.count(0)
    

    def game_start(self):
        random.shuffle(self.suitcases)
        user_case = int(input('Choose a case to start! '))
        self.user_ammount = self.suitcases[user_case]
        self.suitcases[user_case] = 0
        print(user_case)
        return self.user_ammount

    def remaining_cases(self):
        counter = 0
        self.case_array = []
        while counter < len(self.suitcases):
            if self.suitcases[counter] > 0:
                self.case_array.append(counter)
                counter += 1
            else:
                counter += 1
        print(self.case_array)
        return self.case_array

    # def banker(self):
    #     '''
    #     Banker's offer = $12,275.30 + 
    #     (.748 * expected value) +
    #     (-2714.74 * number of cases left) +
    #     ( -.040 * maximum value left ) +
    #     (.0000006986 * expected value squared ) +
    #     ( 32.623 * number of cases left squared ).
    #     '''
    #     ex_val = [i * 1/26 for i in self.suitcases]
    #     self.offer = 12275.30 + (0.748 * sum(ex_val)) + (-2714.74 * self.cases_left) + (-0.040 * max(self.suitcases)) + (0.0000006986 * (sum(ex_val)*sum(ex_val))) + (32.623 * (self.cases_left*self.cases_left))
    #     return self.offer 
    def banker(self):
        base_offer = max(self.suitcases) - min(self.suitcases)
        self.offer = (base_offer /2) + min(self.suitcases)
        return self.offer

    def case_removal(self):
        count = self.round
        while count > 0:
            cases = self.remaining_cases()
            choose_case = int(input(f'Choose a case to remove! {count} cases left to remove!: '))
            print(self.suitcases[choose_case])
            self.suitcases[choose_case] = 0
            count -= 1
        return self.deal_no_deal()
        
        
    
    def deal_no_deal(self):
        banker_offer = self.banker()
        print(banker_offer)
        choice = input("Deal or No Deal? ")
        if choice == 'Deal':
            print(banker_offer)
            return "Thank you for playing!"
        elif choice == 'No Deal' and self.round == 0:
            keep_case = input('Keep or trade?')
            if (keep_case == 'Keep'):
                return self.user_ammount
            else:
                return self.suitcases[self.remaining_cases[0]]
            return self.user_ammount
        else:
            self.round -= 1
            self.case_removal()
            
# runner code
new_game = Game()
new_game.game_start()
new_game.case_removal()
new_game.deal_no_deal()        