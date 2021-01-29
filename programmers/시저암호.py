# https://programmers.co.kr/learn/courses/30/lessons/12926

from string import ascii_lowercase
from string import ascii_uppercase


def solution(s, n):
    answer = ''
    data = list(ascii_lowercase * 2)
    Data = list(ascii_uppercase * 2)
    s_list = list(s)

    for i in s_list:
        if not i == ' ':
            i = data[data.index(i) + n] if i.islower() else Data[Data.index(i) + n]
        answer += i
    return answer