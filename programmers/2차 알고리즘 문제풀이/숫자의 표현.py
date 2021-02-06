#https://programmers.co.kr/learn/courses/30/lessons/12924
def compare(n, i):
    global count
    if i == 0:
        return 0

    if n-i == i-1:
        count += 1
        return 0

    elif n-i < i-1:
        return 0

    else:
        n, i = n-i, i-1  #전체에서 뺀 나머지, 비교값
        compare(n, i)

def solution(n):
    global count  # 어짜피 자기 자신은 포함되니깐
    count = 1
    comp = int((n + 1) / 2)

    for i in range(comp, 1, -1):
        if compare(n, i) == 0: #15, 8
            continue

    return count

if __name__ == '__main__':
    print(f"답:{solution(15)}")
