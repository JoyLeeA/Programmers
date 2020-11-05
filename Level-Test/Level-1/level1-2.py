n = 118372

def solution(n):
    str_n = list(str(n))
    str_n.sort(reverse = True)
    new = ''
    for i in str_n:
        new +=i
    answer = int(new)
    return answer

print(solution(n))