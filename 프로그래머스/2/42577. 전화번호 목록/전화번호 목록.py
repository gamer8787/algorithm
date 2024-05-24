def solution(phone_book):
    a = set()
    for number in phone_book:
        a.add(number)
    for number in phone_book:
        for i in range(1,len(number)):
            if number[:i] in a:
                return False
    return True