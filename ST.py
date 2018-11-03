def st(q):
    a = [int(i) for i in input().split(" ")]

    def xor(arr, lower_limit, upper_limit):
        new_arr = []

        try:
            for j in range(lower_limit, upper_limit):
                new_arr.append(arr[j] ^ arr[j + 1])
        except IndexError:
            new_arr.append(arr[-1])

        return new_arr

    for i in range(q):
        k, x = (int(i) for i in input().split())

        lower = x - 1
        upper = x + k - 1

        temp = a
        for ii in range(k):
            temp = xor(temp, lower, upper)
            lower = 0
            upper = k - ii

        print(int(temp[0]))


try:
    N, Q = (int(i) for i in input().split(" "))
    st(Q)
except EOFError:
    N = 0
    Q = 0
