# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    #answer = False
    #if len(s) in [4,6] :
    #    try :
    #        list(map(int,list(s)))
    #        answer = True
    #    except :
    #        answer = False
    return s.isdigit() and (len(s) in [4,6])