def solution(id_pw, db):
    answer = ''
    flag = 0

    if id_pw in db:
        answer = "login"
    else:
        for i in db:
            if id_pw[0] == i[0]:
                flag = 1
        if flag == 1:
            answer = "wrong pw"
        else:
            answer = "fail"
    return answer
