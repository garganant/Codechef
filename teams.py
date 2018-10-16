T = int(input())

K_list = []
N_list = []
scores_list = []

number_of_qualified_teams = []

for i in range(0, T):
    temp = [int(number) for number in input().split(" ")]

    N_list += [temp[0]]
    K_list += [temp[1]]

    scores_list += [sorted([float(score) for score in input().split(" ")][:N_list[i]], reverse=True)]

for i in range(0, T):
    previous_score = scores_list[i][0]
    qualified_teams = 0
    place = 0

    for score in scores_list[i]:
        if K_list[i] == place:
            break

        if previous_score > score:
            previous_score = score
            place += 1

        qualified_teams += 1

    number_of_qualified_teams += [qualified_teams]

for noqt in number_of_qualified_teams:
    print(noqt - 1)
