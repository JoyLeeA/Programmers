s = "try hello world"

def solution(s):
    word = []
    cnt = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ' or i==len(s)-1:
            word.append(s[cnt:i+1])
            cnt = i+1

    for k in word:
        for l in range(len(k)):
            if l%2:
                answer += k[l].lower()
            else:
                answer += k[l].upper()
    return answer

print(solution(s))
