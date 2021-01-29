# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    l = len(answers)

    answer1 = [i for i in [1, 2, 3, 4, 5] * ((l + 5) // 5)]

    answer2 = [i for i in [2, 1, 2, 3, 2, 4, 2, 5] * ((l + 8) // 8)]
    answer3 = [i for i in [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((l + 10) // 10)]

    result = [0, 0, 0]

    for j in range(l):
        if answer1[j] == answers[j]:
            result[0] += 1
        if answer2[j] == answers[j]:
            result[1] += 1
        if answer3[j] == answers[j]:
            result[2] += 1

    return [i + 1 for i in range(3) if result[i] == max(result)]