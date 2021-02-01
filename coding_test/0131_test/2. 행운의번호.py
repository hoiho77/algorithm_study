''' 행운의 번호는 2*n 자릿수를 가진 숫자인데, 왼쪽에서부터 n 개의 숫자의 합이 오른쪽에서부터 n 개의 숫자의 합과 같다.
당신에게 0을 제외한 숫자로만 이루어진 문자열 s가 주어진다.
이 문자열의 부분문자열 중 가장 긴 행운의 번호의 길이를 구하시오. 만약 행운의 번호가 없다면 0을 반환하시오.

참고 / 제약 사항 S의 길이는 1이상 50이하다. S는 0이 아닌 숫자로만 이루어져있다 (1-9).
테스트 케이스 s = "123231"리턴(정답): 6 여기서 문자열 전체, 123231가 행운의 숫자다.
왼쪽의 세 숫자의 합은 1 + 2+ 3 = 6이고 오른쪽의 세 숫자의 합은 2 + 3 + 1 = 6이다.
'''

class Solution:
    def solution(self, s):
        if len(s) % 2 == 1:
            start = len(s) - 1
        else:
            start = len(s)
        for length in range(start, 0, -2):
            print(length)
            for index in range(0, len(s) - length + 1):
                data = s[index:index + length]

                half = len(data) // 2
                half_1 = sum(list(map(int, data[:half])))
                half_2 = sum(list(map(int, data[half:])))

                if half_1 == half_2:
                    return length

        return 0