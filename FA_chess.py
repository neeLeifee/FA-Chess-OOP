﻿from string import ascii_uppercase as alph
from string import ascii_lowercase as lower_alph

from common.piece import Piece
from common.table import Table

class Game():
    def __init__(self):
        self.table = Table([8,8])

        self.turn_counter = 0
        self.white_score = 0
        self.black_score = 0

        self.setPieces()

        self.printField()

        print(f'Possible moves for {self.black_figures[14].getSkin(),  self.black_figures[14].getPosition()}: {self.black_figures[14].possibleMoves(self.white_figures, self.black_figures)}')

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
    
    def white_move(self):
        while True:
            move = input("Your move('exit' to quit): ").strip().upper()
            if move == "EXIT": exit()
            if len(move) != 5 or move[2] != ' ':
                print("Invalid move format. Please use the format 'E2 E4'.")

            start_pos, end_pos = move.split()
            piece = next((p for p in self.white_figures if p.getPosition() == start_pos), None)
            if not piece:
                print("No white piece at the starting position.")

            possible_moves, moves_to_eat = piece.possibleMoves(self.white_figures, self.black_figures)
            if end_pos not in possible_moves and end_pos not in moves_to_eat:
                print("Invalid move for the selected piece.")

            if end_pos in moves_to_eat:
                self.black_figures = [p for p in self.black_figures if p.getPosition() != end_pos]
                print(f"Captured black piece at {end_pos}!")

            piece.setPosition(end_pos)
            self.printField()
            break

    def black_move(self):
        while True:
            move = input("Your move('exit' to quit): ").strip().upper()
            if move == "EXIT":
                print("Exiting the game.")
                exit()
            if len(move) != 5 or move[2] != ' ':
                print("Invalid move format. Use 'E7 E5'.")

            start_pos, end_pos = move.split()
            piece = next((p for p in self.black_figures if p.getPosition() == start_pos), None)
            if not piece:
                print("No black piece at the starting position.")

            possible_moves, moves_to_eat = piece.possibleMoves(self.white_figures, self.black_figures)
            if end_pos not in possible_moves and end_pos not in moves_to_eat:
                print("Invalid move for the selected piece.")

            if end_pos in moves_to_eat:
                self.white_figures = [p for p in self.white_figures if p.getPosition() != end_pos]
                print(f"Captured white piece at {end_pos}!")

            piece.setPosition(end_pos)
            self.printField()
            break
        


def main():
    print()
    game = Game()
    while True:
        game.white_move()
        game.black_move()
    
if __name__=="__main__":main()#lolnospaces