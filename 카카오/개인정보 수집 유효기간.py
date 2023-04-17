# (오늘 날짜<문자열>, 약관의 유효기간(달 수)<1차원 문자열 배열>, 수집된 개인정보의 정보 <1차원 문자열 배열>)
def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    count = 0
    now = today.split(".")

    # terms 이용하기 쉽게 딕셔너리
    for i in terms:
        terms_dict[i.split()[0]] = i.split()[1]

    for i in privacies:
        count += 1
        date_year = int(i.split()[0].split(".")[0])
        date_month = int(i.split()[0].split(".")[1])
        date_day = int(i.split()[0].split(".")[2])
        pre_info = i.split()[1]

        if date_month+int(terms_dict[pre_info]) > 12:
            date_month += int(terms_dict[pre_info])
            if date_month % 12 == 0:
                date_year += (date_month // 12 - 1)
                date_month = 12
            else:
                date_year += (date_month // 12)
                date_month = date_month % 12
        else:
            date_month += int(terms_dict[pre_info])

        # day 뺴기
        if date_day == 1:
            date_month -= 1
            date_day = 28
            if date_month == 0:
                date_year -= 1
                date_month = 12
        else:
            date_day -= 1

        print(date_year, date_month, date_day)

        if int(now[0]) < date_year:
            continue
        elif int(now[0]) == date_year:
            if int(now[1]) < date_month:
                continue
            elif int(now[1]) == date_month:
                if int(now[2]) <= date_day:
                    continue
                else:
                    answer.append(count)
            else:
                answer.append(count)
        else:
            answer.append(count)

    return answer
