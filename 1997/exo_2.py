def main():
    roads = 0
    testroad = int(input('le nombre de route: '))
    while testroad > 0:
        s = int(input('nombre d\'arret de la route {}: '.format(testroad)))
        tmp = 1
        start = 0
        end = 0
        sum = 0
        ans = 0
        i = 2
        for i in range(s-1):
            x = int(input('note de la route: '))
            sum += x
            if sum < 0:
                sum = 0
                tmp = i
            if sum >= ans:
                if sum > ans or (sum == ans and (i - tmp > end - start)):
                    start = tmp + 2
                    end = i + 2
            ans = sum
        i += 1
        roads += 1
        if ans > 0:
            print("The nicest part of route {} is between stops {} and {}".format(roads, start, end))
        else:
            print("Route {} has no nice parts".format(roads))
        testroad -= 1

main()
