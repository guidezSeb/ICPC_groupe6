def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == ' ':
                return i,j
                
def puzzle():
    error = False
    cases = 0
    x = 0
    y = 5
    while True:
        puzzle = []
        cases += 1
        print("Puzzle #" + str(cases) +":")
        mon_fichier = open("fichier.txt", "r")
        lines = mon_fichier.readlines()[x:y]
        for line in lines:
            puzzle.append(line)
        mon_fichier.close()
        mon_fichier = open("fichier.txt", "r")
        sequence_move = mon_fichier.readlines()[y:]
        mon_fichier.close()
        res =""
        for move in sequence_move:
            res += move
        result = res.split("0")
        nblines = result[0].count('\n')
        for i in range(len(result[0])):
            empty_pos = find_empty(puzzle)
            ligne = empty_pos[0]
            colonne = empty_pos[1]
            move = result[0][i]
            if move == "A":
                if ligne == 0: 
                    error = True
                    break
                else:
                    list1 = list(puzzle[ligne-1])
                    list2 = list(puzzle[ligne])
                    list1[colonne] , list2[colonne] = list2[colonne], list1[colonne]
                    puzzle[ligne-1] = "".join(list1)
                    puzzle[ligne] = "".join(list2)
            elif move == "B":
                if ligne == 4:
                    error = True
                    break
                else:
                    list1 = list(puzzle[ligne+1])
                    list2 = list(puzzle[ligne])
                    list1[colonne] , list2[colonne] = list2[colonne], list1[colonne]
                    puzzle[ligne+1] = "".join(list1)
                    puzzle[ligne] = "".join(list2)
            elif move == "R":
                if colonne == 4:
                    error = True
                    break
                else:
                    list1 = list(puzzle[ligne])
                    list1[colonne+1] , list1[colonne] = list1[colonne], list1[colonne+1]
                    puzzle[ligne] = "".join(list1)
            elif move == "L":
                if colonne == 0:
                    error = True
                    break
                else:
                    list1 = list(puzzle[ligne])
                    list1[colonne-1] , list1[colonne] = list1[colonne], list1[colonne-1]
                    puzzle[ligne] = "".join(list1)
        if error:
            print("  This Puzzle has no final configuration.")
            break
        else:
            for i in range(len(puzzle)):
                print("  ",end='')
                for j in range(len(puzzle)):
                    print(puzzle[i][j], end=' ')
                print("\n", end="")
        x = x + 6 + nblines
        y = y + 6 + nblines
        print('\n', end='')
puzzle()