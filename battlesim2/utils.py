# Transforms a list to a matrix
def listToMatrix(list, col):
    '''
    Takes a list and return a matrix
    args:
        list {list} - this will be returned as a matrix
        col {int} - the number of columns in the matrix
    return:
        {list} - a matrix with the specified number of columns
    '''
    rows = (len(list) + col - 1) // col
    matrix = []
    for i in range(rows):
        start = i * col
        end = min(start + col, len(list))
        matrix.append(list[start:end])
    return matrix

# Global variables
global title

# ASCII font from https://www.asciiart.eu/
title = '''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝

███████╗██╗███╗   ███╗    ██████╗
██╔════╝██║████╗ ████║    ╚════██╗
███████╗██║██╔████╔██║     █████╔╝
╚════██║██║██║╚██╔╝██║    ██╔═══╝
███████║██║██║ ╚═╝ ██║    ███████╗
╚══════╝╚═╝╚═╝     ╚═╝    ╚══════╝
___________________________________________________
'''

help = '''
How to play:
- Type in the option you want to select
- When fighting you can type the shortcuts in parentheses '()'
- Defeat the enemy before they defeat you!
- You can cycle through pages with "<" or ">"

Look at the GitHub!: https://github.com/GDSM8CZY/BattleSim2
___________________________________________________
'''
