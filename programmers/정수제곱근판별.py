# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    data = n **0.5
    if int(data) == data and data > 0:
        return (data+1)**2
    else :
        return -1