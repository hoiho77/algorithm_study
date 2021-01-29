# https://programmers.co.kr/learn/courses/30/lessons/12954#qna

def solution(x, n):
    return [x+x*(i-1) for i in range(1,n+1)]