
def main():
    n = int(input())
    uneceptable_counter = 0
    five_counter = 0
    max_five = -1  
    #max_pos = -1
    
    if n < 7:
        print(-1)
        return

    marks = [int(x) for x in input().split()]
    
    for i in range(7):
        mark = marks[i]
        if mark <= 3:
            uneceptable_counter += 1
        elif mark == 5:
            five_counter += 1

    if uneceptable_counter == 0:
        max_five = five_counter
        #max_pos = 0

    for i in range(7, n):
        front = marks[i]
        back = marks[i - 7]
        if front <= 3: uneceptable_counter += 1
        elif front == 5: five_counter += 1

        if back <= 3: uneceptable_counter -= 1
        elif back == 5: five_counter -= 1

        if uneceptable_counter == 0:
            max_five = max(max_five, five_counter)
            #max_pos = i - 7
    
    #print(max_pos, max_five)
    print(max_five)
main()