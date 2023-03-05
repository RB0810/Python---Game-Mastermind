import tkinter
from Constants import Colors, keyList, rows, guesses, code_length, width, height
from game import Game
from time import sleep

class Interface():
    def __init__(self,canvas, board, pegs):
      self.canvas=canvas
      self.board = board
      self.row = 8
      self.column = 0
      self.p_row = -1
      self.game_obj = Game(board[self.row][:])
      self.pegs = pegs
    
    def start_game(self, start_frame_top, start_frame_bottom,frame, end_canvas, end_frame):
      self.start_frame_top = start_frame_top
      self.start_frame_bottom = start_frame_bottom
      self.frame = frame
      self.end_frame = end_frame
      self.end_canvas = end_canvas
      if self.start_frame_top is not None and self.start_frame_bottom is not None:
        self.start_frame_top.destroy()
        self.start_frame_bottom.destroy()
      self.frame.tkraise()
      self.frame.pack()
      self.action()

    def switch_row(self):
      self.column = 0
      self.p_row = 8
      l = []
      if self.row > 0:
        self.row -= 1
        self.p_row = self.row + 1
      else:
        self.check = list(self.check)
        self.p_row = 0
        l = []
        for i in range(code_length):
          if self.check[0] > 0:
            l.append('Red')
            self.check[0] -= 1
          elif self.check[1] > 0:
            l.append('White')
            self.check[1] -= 1
          else:
            l.append('Black')
            self.check[2] -= 1
        self.pegs[self.p_row] = l
        print(self.pegs)
        self.inaction()
        self.Pegs()
        self.LostGame()
      self.initBoard()
      self.check = self.game_obj.Update(self.board[self.p_row][:])
      if self.check == True:
        l = ['Red', 'Red', 'Red', 'Red']
        self.inaction()
        self.pegs[self.p_row] = l
        self.Pegs()
        self.WonGame()
      else:
        self.check = list(self.check)
        l = []
        for i in range(code_length):
          if self.check[0] > 0:
            l.append('Red')
            self.check[0] -= 1
          elif self.check[1] > 0:
            l.append('White')
            self.check[1] -= 1
          else:
            l.append('Black')
            self.check[2] -= 1
        self.pegs[self.p_row] = l
        print(self.pegs)
        self.Pegs()

    def switch_column(self, inc):
      if self.column == code_length-1 and inc == 1:
        self.column = 0
      elif self.column == 0 and inc == -1:
        self.column = code_length - 1
      else:
        self.column += inc
      self.initBoard()

    def initBoard(self):
      x = 0
      y = 0
      offsetx = 50
      for i in range(1, guesses+1):
        y = height / guesses * 2*i/3
        for j in range(1, code_length+1):
          x = width / code_length * 2*j/3
          if self.row == i-1 and self.column == j-1:
            self.canvas.create_oval(x - offsetx, y, x+30 - offsetx, y-30, fill=self.board[i-1][j-1], outline="black", width=5)
          else:
            self.canvas.create_oval(x - offsetx, y, x+30 - offsetx, y-30, fill=self.board[i-1][j-1], outline="pink", width=5)
      self.canvas.pack()    
      
    def inaction(self): 
      self.canvas.unbind("<Left>")
      self.canvas.unbind("<Right>")
      self.canvas.unbind("<Up>")
      self.canvas.unbind("<Down>")
      self.canvas.unbind("<Return>")

    def switch_colour(self, inc):
      if self.board[self.row][self.column] == keyList[-1] and inc == 1:
        self.board[self.row][self.column] = keyList[0]
      elif self.board[self.row][self.column] == keyList[0] and inc == -1:
        self.board[self.row][self.column] = keyList[-1]
      else:
        self.board[self.row][self.column] = keyList[keyList.index(self.board[self.row][self.column])+inc]
      self.initBoard()
    
    def action(self):
      self.canvas.focus_set()  
      self.canvas.bind('<Left>', lambda _:self.switch_column(-1))
      self.canvas.bind('<Right>', lambda _:self.switch_column(1))
      self.canvas.bind('<Up>', lambda _:self.switch_colour(1))
      self.canvas.bind('<Down>', lambda _:self.switch_colour(-1))
      self.canvas.bind('<Return>', lambda _:self.switch_row())
      self.initBoard()
      self.Pegs()

    def Pegs(self):
      print(self.pegs)
      x = 0
      y = 0
      offsetx = 300
      offsety = 10
      for i in range(1, guesses+1):
        y = (height / guesses * 2*i/3) - offsety 
        for j in range(1, code_length+1):
          x = (width / code_length * j/5) + offsetx
          self.canvas.create_oval(x, y, x+10, y-10, fill=self.pegs[i-1][j-1])
      self.canvas.pack()
    
    def WonGame(self):
      tkinter.Label(self.end_canvas, text = 'You won', bg = Colors['Black'], fg = Colors['White']).pack(side = 'bottom')
      self.end_canvas.pack()
      self.end_frame.pack()
      self.end_frame.tkraise()

    def LostGame(self):
      tkinter.Label(self.end_canvas, text = 'You Lost', bg = Colors['Black'], fg = Colors['White']).pack(side = 'bottom')
      self.end_canvas.pack()
      self.end_frame.pack()
      self.end_frame.tkraise()
  