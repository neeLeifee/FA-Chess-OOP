from string import ascii_uppercase as alph
from string import ascii_lowercase as lower_alph

def convertPosition(pos,mode):
    # pos - position (str witn lenght of two)
    # mode - 'hc' or 'ch'. 
    #   hc - human to computer (B3 -> 12);
    #   ch - computer to human (12 -> B3)
    match mode:
        case 'hc':
            return str(lower_alph.index(pos[0].lower())) + str(int(pos[1])-1)
        case 'ch':
            return alph[int(pos[0])] + str(int(pos[1])+1)
        case _:
            return -1
        
def isWithinField(pos, mode):
    if len(pos) > 2: return False
    match mode:
        case 'h':
            return isWithinField(convertPosition(pos, 'hc'), 'c')
        case 'c':
            if (int(pos[0]) in range(0,8)) and (int(pos[1]) in range(0,8)):
                return True
            else:
                return False
            
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

    def possibleMoves(self, white_figures, black_figures):
        possible_moves = []
        moves_to_eat = []
        existing_figures = []

        white_figures_pos = []
        black_figures_pos = []

        for i in white_figures: white_figures_pos.append(i.getPosition())
        for i in black_figures: black_figures_pos.append(i.getPosition())

        for i in white_figures: existing_figures.append(i.getPosition())
        for i in black_figures: existing_figures.append(i.getPosition())

        match self.type:
            case 'P':   # пешка
                if self.color == 'w':
                    if self.position in self.white_pawns_spawns:   # if pawn is at its spawn point
                        # движение на две клетки вперёд
                        tmpMove = self.position[0] + str(int(self.position[1])+2)
                        if isWithinField(tmpMove, 'h'):
                            if tmpMove not in existing_figures:
                                possible_moves.append(tmpMove)
                    
                    # движение на одну клетку вперёд
                    tmpMove = self.position[0] + str(int(self.position[1])+1)
                    if isWithinField(tmpMove, 'h'):
                        if tmpMove not in existing_figures:
                            possible_moves.append(tmpMove)
                    
                    # хавалка вниз влево
                    tmpMove = str(int(convertPosition(self.position, 'hc')[0]) + 1) + str(int(convertPosition(self.position, 'hc')[1]) + 1)
                    if isWithinField(tmpMove, 'c'):
                        if convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    # хавалка вниз вправо
                    tmpMove = str(int(convertPosition(self.position, 'hc')[0]) - 1) + str(int(convertPosition(self.position, 'hc')[1]) + 1)
                    if isWithinField(tmpMove, 'c'):
                        if convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))


                elif self.color == 'b':
                    if self.position in self.black_pawns_spawns:   # if pawn is at its spawn point
                        # движение на две клетки вперёд
                        tmpMove = self.position[0] + str(int(self.position[1])-2)
                        if isWithinField(tmpMove, 'h'):
                            if tmpMove not in existing_figures:
                                possible_moves.append(tmpMove)

                    # движение на одну клетку вперёд
                    tmpMove = self.position[0] + str(int(self.position[1])-1)
                    if isWithinField(tmpMove, 'h'):
                        if tmpMove not in existing_figures:
                            possible_moves.append(tmpMove)

                    # хавалка вверх вправо
                    tmpMove = str(int(convertPosition(self.position, 'hc')[0]) - 1) + str(int(convertPosition(self.position, 'hc')[1]) - 1)
                    if isWithinField(tmpMove, 'c'):
                        if convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    # хавалка вверх влево
                    tmpMove = str(int(convertPosition(self.position, 'hc')[0]) + 1) + str(int(convertPosition(self.position, 'hc')[1]) - 1)
                    if isWithinField(tmpMove, 'c'):
                        if convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))

            case 'N':   # конь
                # вверх влево
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])-1) + str(int(convertPosition(self.position, 'hc')[1])-2)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))

                # вверх вправо
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])+1) + str(int(convertPosition(self.position, 'hc')[1])-2)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))

                # вправо вверх
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])+2) + str(int(convertPosition(self.position, 'hc')[1])-1)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                
                # вправо вниз
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])+2) + str(int(convertPosition(self.position, 'hc')[1])+1)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))

                # вниз влево
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])-1) + str(int(convertPosition(self.position, 'hc')[1])+2)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                
                # вниз вправо
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])+1) + str(int(convertPosition(self.position, 'hc')[1])+2)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))

                # влево вверх
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])-2) + str(int(convertPosition(self.position, 'hc')[1])-1)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                
                # влево вниз
                tmpMove = str(int(convertPosition(self.position, 'hc')[0])-2) + str(int(convertPosition(self.position, 'hc')[1])+1)
                if isWithinField(tmpMove, 'c'):
                    if convertPosition(tmpMove, 'ch') not in existing_figures:
                        possible_moves.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                    elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                        moves_to_eat.append(convertPosition(tmpMove, 'ch'))

            case 'B':   # слон
                # общая идея просчёта хода слона/ладьи/ферзя
                # мы пускаем луч в каждую сторону пока не упрёмся в какую-то фигуру/край поля
                # клетка, которую просчитываем на данной итерации - tmpMove

                # вправо вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures:
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # вправо вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures:
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures:
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures:
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))


            case 'R':   # ладья
                # общая идея просчёта хода слона/ладьи/ферзя
                # мы пускаем луч в каждую сторону пока не упрёмся в какую-то фигуру/край поля
                # клетка, которую просчитываем на данной итерации - tmpMove

                # вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = tmpMove[0] + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: 
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # вправо
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + tmpMove[1]
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: 
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = tmpMove[0] + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: 
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + tmpMove[1]
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: 
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

            case 'Q':   # ферзь
                # общая идея просчёта хода слона/ладьи/ферзя
                # мы пускаем луч в каждую сторону пока не упрёмся в какую-то фигуру/край поля
                # клетка, которую просчитываем на данной итерации - tmpMove

                # вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = tmpMove[0] + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # вправо вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))
                
                # вправо
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + tmpMove[1]
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # вправо вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])+1) + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))
                    
                # вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = tmpMove[0] + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево вниз
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + str(int(tmpMove[1])+1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + tmpMove[1]
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

                # влево вверх
                tmpMove = convertPosition(self.position, 'hc')
                while True:
                    tmpMove = str(int(tmpMove[0])-1) + str(int(tmpMove[1])-1)
                    if isWithinField(tmpMove, 'c') == False: break
                    elif convertPosition(tmpMove, 'ch') in existing_figures: break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

            case 'K':   # король
                directions = [
                    (0, -1), (1, -1), (1, 0), (1, 1),
                    (0, 1), (-1, 1), (-1, 0), (-1, -1)
                ]
                for direction in directions:
                    tmpMove = str(int(convertPosition(self.position, 'hc')[0]) + direction[0]) + str(int(convertPosition(self.position, 'hc')[1]) + direction[1])
                    if isWithinField(tmpMove, 'c'):
                        tmpMove = convertPosition(tmpMove, 'ch')
                        if tmpMove not in existing_figures:
                            possible_moves.append(tmpMove)
                        elif self.color == 'w' and tmpMove in black_figures_pos:
                            moves_to_eat.append(tmpMove)
                        elif self.color == 'b' and tmpMove in white_figures_pos:
                            moves_to_eat.append(tmpMove)


        return (possible_moves, moves_to_eat)

class Game():
    def __init__(self):
        self.table = Table([8,8])

        self.white_score = 0
        self.black_score = 0

        self.setPieces()

        self.printField()

        print(f'Possible moves for {self.black_figures[13].getSkin(),  self.black_figures[13].getPosition()}: {self.black_figures[13].possibleMoves(self.white_figures, self.black_figures)}')

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
            Piece('w', 'N', 'G1'),  # конь

            Piece('w', 'B', 'C1'),  # слон
            Piece('w', 'B', 'F1'),  # слон

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
            Piece('b', 'N', 'G8'),  # конь

            Piece('b', 'B', 'C8'),  # слон
            Piece('b', 'B', 'F8'),  # слон

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