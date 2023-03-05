import random as r
from Constants import Colors, guesses, code_length
from copy import deepcopy

class Game:
    def __init__(self, guess):
        self.code = []  
        self.guess = guess
        self.createCode()

    def createCode(self):
        for i in range(code_length):
            self.code.append(r.choice(list(Colors.keys())))
        print('Code :', end = '')
        print(self.code)

            
    def Update(self,c):
        self.guess = c
        check = self.checkCode()
        return check

    def Pegs(self):
        self.red_peg = 0
        self.white_peg = 0
        self.black_peg = 0
        self.codenew = deepcopy(self.code)
        self.guessnew = deepcopy(self.guess)
        for i in range(code_length):
            if self.code[i] == self.guess[i]:
                self.red_peg = self.red_peg+1
                self.guessnew.remove(self.guess[i])
                self.codenew.remove(self.code[i])
        self.guessnew2 = deepcopy(self.guess)
        for i in range(len(self.codenew)):
            a = self.codenew[i]
            if a in self.guessnew2:
                self.white_peg = self.white_peg+1
                self.guessnew2.remove(a)
        self.black_peg=code_length-(self.red_peg+self.white_peg)
        return self.red_peg ,self.white_peg ,self.black_peg
    
    def checkCode(self):
        if self.code == self.guess:
            return True
        else:
            pegs = self.Pegs()
            return pegs