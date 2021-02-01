'''
문제 설명 최신 마이크로콘트롤러를 최대한 저렴하게 만들기 위해 매우 간단한 캐쉬를 설계했다. 프로세서는 0에서부터 n-1로 숫자가 매겨진 n개의 바이트를 가진 느린 메모리 시스템과 연결된다. 캐쉬는 빠른 접근을 위해 이 중에서 k개의 카피를 한번에 가지고 있다. 캐쉬는 base address를 가지고 있으며 base, base+1, ..., base+k-1로 숫자 매겨진 바이트들의 카피를 가지고 있다. 프로그램이 바이트를 읽을 때, 캐쉬 제어기는 다음과 같은 알고리즘을 따라 동작한다:

기존의 base address와 차이를 최소화하여서 필요한 바이트를 가진 k개의 새로운 범위의 바이트를 찾는다. 필요한 바이트가 이미 캐쉬에 존재한다면 base address는 그대로 유지됨을 유의하라.
기존의 범위에는 포함이 안되고 새로운 범위에만 포함되는 바이트들을 메모리에서 읽어서 캐쉬를 새 범위로 업데이트하고 새로운 범위에는 없고 기존의 범위에만 있는 바이트들을 버린다.
필요한 바이트를 프로그램에 반환한다.
당신은 프로그램의 성능을 테스트하기 위해 얼마나 많은 바이트들이 메모리에서 읽어지는지 확인하고 싶다. 프로그램이 읽는 바이트의 개수는 읽어들이는 순서에 맞게 addresses에 주어져있다. 프로그램이 시작할 때 base address는 0이다.

'''

class Solution:
    def solution(self, n, k, addresses):
        mem = [i for i in range(0, n)]
        base_address = [i for i in range(0, k)]
        acc_count = 0

        for data in addresses:
            if data in base_address:
                continue
            else:
                if data > max(base_address):
                    new_address = [j for j in range(data - k + 1, data + 1)]
                else:
                    new_address = [j for j in range(data, data + k)]
                print(set(new_address) - set(base_address))
                acc_count += len(set(new_address) - set(base_address))
                base_address = new_address

        return acc_count
