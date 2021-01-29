# https://programmers.co.kr/learn/courses/30/lessons/12950

import pandas as pd

def solution(arr1, arr2):
    arr1 = pd.DataFrame(arr1)
    arr2 = pd.DataFrame(arr2)

    answer = arr1 + arr2
    return answer.values.tolist()