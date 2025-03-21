from .base_funcs import isWithinField, convertPosition

class Piece():
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position

        # default skins
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
        # importing custom skins from gfx folder
        with open('gfx/skins.txt', 'r', encoding='utf-8') as file:
            for line in file:
                match line[:2]:
                    case 'wP': pieces_skins['wP'] = line[3]
                    case 'wN': pieces_skins['wN'] = line[3]
                    case 'wB': pieces_skins['wB'] = line[3]
                    case 'wR': pieces_skins['wR'] = line[3]
                    case 'wQ': pieces_skins['wQ'] = line[3]
                    case 'wK': pieces_skins['wK'] = line[3]

                    case 'bP': pieces_skins['bP'] = line[3]
                    case 'bN': pieces_skins['bN'] = line[3]
                    case 'bB': pieces_skins['bB'] = line[3]
                    case 'bR': pieces_skins['bR'] = line[3]
                    case 'bQ': pieces_skins['bQ'] = line[3]
                    case 'bK': pieces_skins['bK'] = line[3]

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
                    elif convertPosition(tmpMove, 'ch') in existing_figures: 
                        if self.color == 'w' and convertPosition(tmpMove, 'ch') in black_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        elif self.color == 'b' and convertPosition(tmpMove, 'ch') in white_figures_pos:
                            moves_to_eat.append(convertPosition(tmpMove, 'ch'))
                        break
                    possible_moves.append(convertPosition(tmpMove, 'ch'))

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