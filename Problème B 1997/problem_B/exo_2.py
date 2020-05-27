
def noteRoad(arret, sol):
    tmp = 1
    sum = 0

    start = 0
    end = 0
    i = 2
    for i in range(arret-1):
        x = int(input('note de la route: '))
        sum += x
        if sum < 0:
            sum = 0
            tmp = i
        if sum >= sol:
            if sum > sol or (sum == sol and (i - tmp > end - start)):
                start = tmp + 2
                end = i + 2
        sol = sum
    i += 1
    return sol, start, end

def main():
    roads = 0
    testroad = int(input('le nombre de route: '))
    while testroad > 0:
        arret = int(input('nombre d\'arret de la route '+ str(testroad) +' : '))
        sol = 0
        sol = noteRoad(arret,sol)
        roads += 1
        if sol[0] > 0:
            print("The nicest part of route "+ str(roads) + " is between stops " + str(sol[1]) + " and " + str(sol[2]))  
        else:
            print("Route " + str(roads) + " has no nice parts")
        testroad -= 1



main()
