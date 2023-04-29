def solution(spell, dic):
    answer = 0

    for i in dic:
        if sorted(spell) == sorted(i):
            return 1

    return 2
