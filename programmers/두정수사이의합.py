def solution(a, b):
    # https://programmers.co.kr/learn/courses/30/lessons/12912
    # if a < b :
    #    data = [i for i in range(a, b+1)]
    # else :
    #    data = [i for i in range(b, a+1)]
    # answer = sum(data)

    if a > b : a, b = b, a
    return sum(range(a, b + 1))