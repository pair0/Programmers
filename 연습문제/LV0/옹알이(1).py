# "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.

def spli(word, word_list):
    if word[0] == "a" or word[0] == "w":
        if word[:3] in word_list:
            if len(word[3:]) != 0:
                return spli(word[3:], word_list)
            else:
                return 1
        else:
            return 0
    elif word[0] == "y" or word[0] == "m":
        if word[:2] in word_list:
            if len(word[2:]) != 0:
                return spli(word[2:], word_list)
            else:
                return 1
        else:
            return 0
    else:
        return 0


def solution(babbling):
    answer = 0
    word_list = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        # 단어의 길이가 3보다 작으면 아기가 사용 가능한 단어에서 찾는다.
        if len(word) <= 3:
            if word in word_list:
                answer += 1
        else:
            answer += spli(word, word_list)

    return answer
