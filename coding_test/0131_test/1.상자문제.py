'''
문제 설명 당신은 상자에 책을 넣고 있는데, 상자의 무게 제한을 넘지 않고 최대한 많이 넣어야 한다. 한 상자에 최대한 많이 책을 넣은 다음 상자를 닫고 봉인한 후, 다음 상자에 책을 넣을 수 있다. 책은 차곡차곡 쌓여있는데, 무조건 가장 위에서부터 책을 꺼내야 한다.

책들의 무게는 weights로써 주어진다. 이 배열의 첫 번째 요소가 쌓여있는 책 중에서 가장 위에 있는 책이고, 배열의 마지막 요소가 가장 밑에 있는 책이다. 상자에 담을 수 있는 최대 무게는 maxWeight로 주어진다. 책을 전부 담기 위한 상자의 최소 개수를 구하시오.

참고 / 제약 사항 Weights는 0개 이상 50개 이하의 요소를 가지고 있다. 1 <= maxWeight <= 1000 1 <= weights[n] <= maxWeight

weights = [5,5,5,5,5,5] maxWeight = 10리턴(정답): 3
'''

class Solution:
    def solution(self, weights, maxWeight):
        count = 1
        empty = maxWeight
        if len(weights) == 0:
            return 0

        for i in range(len(weights)):
            empty = empty - weights[i]
            try:
                next_book = weights[i + 1]
            except:
                break

            if empty >= next_book:
                continue

            elif empty < next_book:
                empty = maxWeight
                count += 1

        return count  # 최소 상자의 갯수