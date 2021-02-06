
#https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for h in range(1,int(yellow**0.5)+2) :
        if yellow%h == 0:
            w = yellow/h
            if (w+2)*2 + h*2  == brown :
                return [w+2, h+2]