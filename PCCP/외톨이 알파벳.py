
'''
문제 설명
알파벳 소문자로만 이루어진 어떤 문자열에서, 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.

문자열 "edeaaabbccd"를 예시로 들어보면,

a는 2회 이상 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ede(aaa)bbccd"
b, c도 a와 같은 이유로 외톨이 알파벳이 아닙니다.
d는 2회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"e(d)eaaabbcc(d)"
e도 d와 같은 이유로 외톨이 알파벳입니다.
문자열 "eeddee"를 예시로 들어보면,

e는 4회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"(ee)dd(ee)"
d는 2회 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ee(dd)ee"
문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요. 만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.

제한사항
1 ≤ input_string의 길이 ≤ 2,600
input_string은 알파벳 소문자로만 구성되어 있습니다..
'''
def solution(input_string):
    answer = ""
    check = []
    k = 0
    check.append(input_string[0])
    
    for i in range(1, len(input_string)):
        if check[k] != input_string[i]:
            check.append(input_string[i])
            k += 1
    
    for i in sorted(set(check)):
        if check.count(i) > 1:
            answer += i
    
    if len(answer) == 0:
        answer = "N"
        
    return answer
