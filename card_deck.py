def check_increasing(array):
    length = len(array)

    for i in range(0, length):
        try:
            if not NUMBERS[i] < NUMBERS[i + 1]:
                return i
        except IndexError:
            return length - 1

    return length - 1


T = int(input())

for ti in range(0, T):
    X = input()

    NUMBERS = [int(i) for i in input().split(" ")]

    first_increasing = check_increasing(NUMBERS)
    second_increasing = check_increasing(NUMBERS[first_increasing + 1:])

    if first_increasing + second_increasing == len(NUMBERS) - 2:
        print("YES")
    else:
        print("NO")
