# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n): #reverse, reversed
    answer = list(map(int, str(n)))
    return answer[::-1]