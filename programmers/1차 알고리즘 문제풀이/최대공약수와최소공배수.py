# https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(n,m):
    return m if n%m == 0 else gcd(m,n%m)

def solution(n, m):
    N,M = max(n,m), min(n,m)
    return gcd(N,M), (N*M/gcd(N,M))