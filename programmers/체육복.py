# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    check = []
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))

    count = n - len(lost)
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i] - 1)
            count += 1
            continue

        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
            count += 1
            continue

    return count