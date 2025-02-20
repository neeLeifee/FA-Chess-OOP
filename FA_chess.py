import string

class Game():
    def __init__(self):
        self.field_size = [8,8]

        self.pieces_list = {
            'wP' : '♙',  # пешка
            'wN' : '♘',  # конь
            'wB' : '♗',  # слон
            'wR' : '♖',  # ладья
            'wQ' : '♕',  # ферзь
            'wK' : '♔',  # король

            'bP' : '♟',  # пешка
            'bN' : '♞',  # конь
            'bB' : '♝',  # слон
            'bR' : '♜',  # ладья
            'bQ' : '♛',  # ферзь
            'bK' : '♚',  # король
        }
        self.white_positions = {
            'wP1' : 'A2',  # пешка
            'wP2' : 'B2',  # пешка
            'wP3' : 'C2',  # пешка
            'wP4' : 'D2',  # пешка
            'wP5' : 'E2',  # пешка
            'wP6' : 'F2',  # пешка
            'wP7' : 'G2',  # пешка
            'wP8' : 'H2',  # пешка

            'wN1' : 'B1',  # конь
            'wN2' : 'F1',  # конь

            'wB1' : 'C1',  # слон
            'wB2' : 'F1',  # слон

            'wR1' : 'A1',  # ладья
            'wR2' : 'H1',  # ладья

            'wQ' : 'D1',  # ферзь
            'wK' : 'E1',  # король
        }
        self.black_positions = {
            'bP1' : 'A7',  # пешка
            'bP2' : 'B7',  # пешка
            'bP3' : 'C7',  # пешка
            'bP4' : 'D7',  # пешка
            'bP5' : 'E7',  # пешка
            'bP6' : 'F7',  # пешка
            'bP7' : 'G7',  # пешка
            'bP8' : 'H7',  # пешка

            'bN1' : 'B8',  # конь
            'bN2' : 'F8',  # конь

            'bB1' : 'C8',  # слон
            'bB2' : 'F8',  # слон

            'bR1' : 'A8',  # ладья
            'bR2' : 'H8',  # ладья

            'bQ' : 'D8',  # ферзь
            'bK' : 'E8',  # король
        }

        self.white_score = 0
        self.black_score = 0


    def printField(self):
        print("   ",end='')
        for i in range(self.field_size[0]): print(string.ascii_uppercase[i]+'  ', end='')
        print('\n','\n', sep='', end='')


        for i in range(self.field_size[0]):
            print(i+1, '  ',
                  sep='',end='')

            for j in range(self.field_size[1]):
                print(".  ",end='')

            print(i+1, '\n',
                  sep='',end='')


        print("\n   ",end='')
        for i in range(self.field_size[0]): print(string.ascii_uppercase[i]+'  ', end='')
        

class Piece():
    def __init__(self):
        pass



def main():
    game = Game()
    game.printField()
    #print(string.ascii_uppercase)
    #print('♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ♔ ')
    #print('1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 ')
    #print('a b c d e f g e a b c d e f g e a b ')
    


if __name__=="__main__":main()#lolnospaces