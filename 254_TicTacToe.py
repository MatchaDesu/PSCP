"TicTacToe"
def find_win(table) :
    """
    Find who win and return 'O WIN' or 'X WIN'
    return 'DRAW' if no one win
    """

    for i in range(3) :
        if table[0][i] == table[1][i] == table[2][i] and table[0][i] != "-":
            return f'{table[0][i]} WIN'

    for i in range(3) :
        if table[i][0] == table[i][1] == table[i][2] and table[i][0] != "-":
            return f'{table[i][0]} WIN'

    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != "-":
        return f'{table[0][0]} WIN'

    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != "-":
        return f'{table[0][2]} WIN'

    return 'DRAW'

def main() :
    "main"
    table = []
    row = []
    for _ in range(3) :
        for i in input() :
            row.append(i)
        table.append(row)
        row = []

    #print(table)
    print(find_win(table))
main()
