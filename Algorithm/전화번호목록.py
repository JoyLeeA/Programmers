def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                     answer = False
                     return answer
            else:
                if phone_book[i][0:len(phone_book[j])] == phone_book[j]:
                    answer = False
                    return answer
    return answer


phone_book = ["119","97674223", "1195524421"]
print(solution(phone_book))
