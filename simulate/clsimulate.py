import random

class simulate(object):
    def __init__(self, bank=100, perc=1.00, stake=1):
        self.bank = bank
        self.perc = perc
        self.stake = stake
    def pick(self):
        i = random.randint(1, 100)
        return i
    def sim(self, start, stop, perc):
        win = 0
        lost = 0
        stake = 1
        for a in range(start, stop):
            stake = 5
            i = self.pick()
            if i <=  50:
                self.bank = self.bank + stake *(1 + perc)
                win += 1
                print('WIN: ', self.bank, stake)
            else:
                lost += 1
                self.bank = self.bank - stake
                print('LOST: ', self.bank, stake)
            if self.bank < 1:
                print('LOST!!!')
                break
        print('WIN: ', win, ' LOST: ', lost)
                #         print(self.bank)
if __name__ == '__main__':
    x = simulate()
    x.sim(1,1001, .1)
