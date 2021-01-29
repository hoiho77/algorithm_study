# https://programmers.co.kr/learn/courses/30/lessons/17681

import pandas as pd


def deci_binary(n, list):
    result = []
    for data in list:
        a = [0] * n
        for j in range(1, n + 1):
            a[-j] = data % 2
            data = data // 2
        result.append(a)
    return result


def solution(n, arr1, arr2):
    result = []
    arr1 = pd.DataFrame(deci_binary(n, arr1))
    arr2 = pd.DataFrame(deci_binary(n, arr2))
    answer = (arr1 + arr2).values.tolist()

    for i in answer:
        i = list(map(str, i))
        i = str(''.join(i))

        i = i.replace('0', ' ')
        i = i.replace('1', '#')
        i = i.replace('2', '#')
        result.append(i)

    return result