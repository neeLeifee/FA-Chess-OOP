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