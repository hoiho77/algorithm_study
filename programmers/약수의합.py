#https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    num = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            num.append(i)
            if i != (int(n/i)):
                num.append(int(n/i))
        else:
            pass
    return sum(num)