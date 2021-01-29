# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    part = collections.Counter(participant)
    comp = collections.Counter(completion)
    answer = part-comp
    return list(answer.keys())[0]