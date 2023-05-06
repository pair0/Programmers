def solution(before, after):
    after = list(after)

    for i in before:
        if i in after:
            after.remove(i)
        else:
            return 0

    return 1
