# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    for team_num in range(1,len(d)+1):
        if sum(d[:team_num])>budget :
            return team_num-1
        elif sum(d[:team_num])==budget :
            return team_num
    return len(d)