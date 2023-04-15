def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if list(phone_book[i]) == list(phone_book[i+1])[:len(list(phone_book[i]))]:
            return False

    return True
