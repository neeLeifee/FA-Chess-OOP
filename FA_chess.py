from string import ascii_uppercase as alph

class Table():
    def __init__(self,size): self.size = size
    #я хз какие ещё могут быть полЯ у пОля. вообще какойто беспонтовый класс

    def getSize(self):return(self.size)

class Game():
    def __init__(self):
        self.table = Table([8,8])

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
        self.white_positions = [
            'wP1' , 'A2',  # пешка
            'wP2' , 'B2',  # пешка
            'wP3' , 'C2',  # пешка
            'wP4' , 'D2',  # пешка
            'wP5' , 'E2',  # пешка
            'wP6' , 'F2',  # пешка
            'wP7' , 'G2',  # пешка
            'wP8' , 'H2',  # пешка

            'wN1' , 'B1',  # конь
            'wN2' , 'F1',  # конь

            'wB1' , 'C1',  # слон
            'wB2' , 'G1',  # слон

            'wR1' , 'A1',  # ладья
            'wR2' , 'H1',  # ладья

            'wQ1' , 'D1',  # ферзь
            'wK1' , 'E1',  # король
        ]
        self.black_positions = [
            'bP1' , 'A7',  # пешка
            'bP2' , 'B7',  # пешка
            'bP3' , 'C7',  # пешка
            'bP4' , 'D7',  # пешка
            'bP5' , 'E7',  # пешка
            'bP6' , 'F7',  # пешка
            'bP7' , 'G7',  # пешка
            'bP8' , 'H7',  # пешка

            'bN1' , 'B8',  # конь
            'bN2' , 'F8',  # конь

            'bB1' , 'C8',  # слон
            'bB2' , 'G8',  # слон

            'bR1' , 'A8',  # ладья
            'bR2' , 'H8',  # ладья

            'bQ1' , 'D8',  # ферзь
            'bK1' , 'E8',  # король
        ]

        self.white_score = 0
        self.black_score = 0


    def printField(self):

        #drawing first line of letters
        print("   ",
              end='')
        for i in range(self.table.getSize()[0]): print(alph[i]+'  ', end='')
        print('\n','\n',
              sep='', end='')


        #drawing numbers(i loop) and figures(j loop)
        #i - номер строки
        #j - номер столбца
        for i in range(self.table.getSize()[0]):

            print(i+1, '  ',
                  sep='',end='')

            for j in range(self.table.getSize()[1]):
                tile_num = alph[j]+str(i+1)

                #printing piece
                if tile_num in self.white_positions:    #white pieces
                    current_piece_name = self.white_positions[self.white_positions.index(tile_num)-1]
                    print(self.pieces_list[current_piece_name[:2]], ' ',
                        sep='',end='')
                elif tile_num in self.black_positions:  #black pieces
                    current_piece_name = self.black_positions[self.black_positions.index(tile_num)-1]
                    print(self.pieces_list[current_piece_name[:2]], ' ',
                        sep='',end='')
                else:                                   #filling whats left with dots
                    print('. ',sep='',end='')
                    #print(tile_num,sep='',end='') #DEBUG: allows to see tile_num 
                

                #printing space between tiles
                print('',end=' ')#heheh did it the other way around B-)

            print(i+1, '\n',
                  sep='',end='')

        #drawing second line of letters
        print("\n   ",
              end='')
        for i in range(self.table.getSize()[0]): print(alph[i]+'  ', end='')
        

class Piece():
    def __init__(self):
        pass



def main():
    game = Game()
    game.printField()
    

    
if __name__=="__main__":main()#lolnospaces