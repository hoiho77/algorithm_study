#https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    key = arr[0]
    answer = [arr[0]]
    for i in arr :
        if key != i :
            answer.append(i)
            key = i
        else :
            pass
    return answer