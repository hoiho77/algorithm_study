# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    a = [True] * (n+1) #사이값들 생성
    m = int(n**0.5) #비교값(정수)
    for i in range(2,m+1) :
        if a[i] == True :
            for j in range(i+i, n+1, i):
                a[j]=False
    answer = [i for i in range(2, n+1) if a[i] == True]
    return len(answer)