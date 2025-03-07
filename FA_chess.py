from string import ascii_uppercase as alph
from string import ascii_lowercase as lower_alph

def convertPosition(pos):
    if pos[0].lower() in lower_alph:
        return str(lower_alph.index(pos[0].lower())) + str(int(pos[1])-1)
    else:
        return alph[int(pos[0])] + str(int(pos[1])+1)

class Table():
    def __init__(self,size): self.size = size
    #я хз какие ещё могут быть полЯ у пОля. вообще какой-то беспонтовый класс

    def getSize(self):return(self.size)
        

class Piece():
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position
        
        pieces_skins = {
            'wP' : '♙',  # белая пешка
            'wN' : '♘',  # белый конь
            'wB' : '♗',  # белый слон
            'wR' : '♖',  # белая ладья
            'wQ' : '♕',  # белый ферзь
            'wK' : '♔',  # белый король

            'bP' : '♟',  # чёрная пешка
            'bN' : '♞',  # чёрный конь
            'bB' : '♝',  # чёрный слон
            'bR' : '♜',  # чёрная ладья
            'bQ' : '♛',  # чёрный ферзь
            'bK' : '♚',  # чёрный король
        }

        self.skin = pieces_skins[self.color + self.type]

        self.white_pawns_spawns = ['A2','B2','C2','D2','E2','F2','G2','H2']
        self.black_pawns_spawns = ['A7','B7','C7','D7','E7','F7','G7','H7']
    
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getSkin(self):
        return self.skin

    def possibleMoves(self):
        possible_moves = []

        match self.type:
            case 'P':   # пешка
                if self.color == 'w':
                    if self.getPosition() in self.white_pawns_spawns:   # if pawn is at its spawn point
                        possible_moves.append(self.position[0] + str(int(self.position[1])+2))

                    possible_moves.append(self.position[0] + str(int(self.position[1])+1))
                else:
                    if self.getPosition() in self.black_pawns_spawns:   # if pawn is at its spawn point
                        possible_moves.append(self.position[0] + str(int(self.position[1])-2))

                    possible_moves.append(self.position[0] + str(int(self.position[1])-1))

            case 'N':   # конь
                pass

            case 'B':   # слон
                pass

            case 'R':   # ладья
                pass

            case 'Q':   # ферзь
                pass

            case 'K':   # король
                pass


        # проверки на то чтобы не уходил на лимит доски
        for i in possible_moves:
            if int(i[1]) not in range(1,9):
                possible_moves.pop(possible_moves.index(i))
            if alph.index(i[0]) not in range(0,8):
                possible_moves.pop(possible_moves.index(i))

        return (possible_moves)

class Game():
    def __init__(self):
        self.table = Table([8,8])

        self.white_score = 0
        self.black_score = 0

        self.setPieces()

        self.printField()

        print(self.black_figures[0].possibleMoves())

    def setPieces(self):
        # Документация наименования фигур
        # w - White, b - Black
        # P - пешка, 
        # N - конь
        # B - слон
        # R - ладья
        # Q - ферзь
        # K - король
        self.white_figures = [
            Piece('w', 'P', 'A2'),  # пешка
            Piece('w', 'P', 'B2'),  # пешка
            Piece('w', 'P', 'C2'),  # пешка
            Piece('w', 'P', 'D2'),  # пешка
            Piece('w', 'P', 'E2'),  # пешка
            Piece('w', 'P', 'F2'),  # пешка
            Piece('w', 'P', 'G2'),  # пешка
            Piece('w', 'P', 'H2'),  # пешка

            Piece('w', 'N', 'B1'),  # конь
            Piece('w', 'N', 'F1'),  # конь

            Piece('w', 'B', 'C1'),  # слон
            Piece('w', 'B', 'G1'),  # слон

            Piece('w', 'R', 'A1'),  # ладья
            Piece('w', 'R', 'H1'),  # ладья

            Piece('w', 'Q', 'D1'),  # ферзь
            Piece('w', 'K', 'E1'),  # король
        ]
        self.black_figures = [
            Piece('b', 'P', 'A7'),  # пешка
            Piece('b', 'P', 'B7'),  # пешка
            Piece('b', 'P', 'C7'),  # пешка
            Piece('b', 'P', 'D7'),  # пешка
            Piece('b', 'P', 'E7'),  # пешка
            Piece('b', 'P', 'F7'),  # пешка
            Piece('b', 'P', 'G7'),  # пешка
            Piece('b', 'P', 'H7'),  # пешка

            Piece('b', 'N', 'B8'),  # конь
            Piece('b', 'N', 'F8'),  # конь

            Piece('b', 'B', 'C8'),  # слон
            Piece('b', 'B', 'G8'),  # слон

            Piece('b', 'R', 'A8'),  # ладья
            Piece('b', 'R', 'H8'),  # ладья

            Piece('b', 'Q', 'D8'),  # ферзь
            Piece('b', 'K', 'E8'),  # король
        ]

    def printField(self):
        #drawing first line of letters
        print("    ",
              end='')
        for i in range(self.table.getSize()[0]): print(alph[i]+'  ', end='')
        print('\n',
              sep='', end='')

        print('  ',"_"*25)

        white_positions = []
        for figure in self.white_figures:
            white_positions.append(figure.getSkin())
            white_positions.append(figure.getPosition())

        black_positions = []
        for figure in self.black_figures:
            black_positions.append(figure.getSkin())
            black_positions.append(figure.getPosition())

        #drawing numbers(i loop) and figures(j loop)
        #i - номер строки
        #j - номер столбца
        for i in range(self.table.getSize()[0]):

            print(i+1, ' | ',
                  sep='',end='')

            for j in range(self.table.getSize()[1]):
                tile_num = alph[j]+str(i+1)

                #printing piece
                if tile_num in white_positions:    #white pieces
                    current_piece = white_positions[white_positions.index(tile_num)-1]
                    print(current_piece, ' ',
                        sep='',end='')
                elif tile_num in black_positions:  #black pieces
                    current_piece = black_positions[black_positions.index(tile_num)-1]
                    print(current_piece, ' ',
                        sep='',end='')
                else:                              #filling whats left with dots
                    print('. ',sep='',end='')
                    #print(tile_num,sep='',end='') #DEBUG: allows to see tile_num 
                

                #printing space between tiles
                print('',end=' ')#heheh did it the other way around B-)

            print('| ', i+1, '\n',
                  sep='',end='')


        print('  ',"‾"*25)

        #drawing second line of letters
        print("    ",
              end='')
        for i in range(self.table.getSize()[0]): print(alph[i]+'  ', end='')

        print('\n')
        


def main():
    print()
    game = Game()
    
if __name__=="__main__":main()#lolnospaces