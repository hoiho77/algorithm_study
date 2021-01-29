#https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    data = int(len(s)//2)
    return s[(data-1):data+1] if (len(s)%2) == 0 else s[data]