arr = [2,6,8,14]
def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        while a % b:
            a, b = b, a%b
        arr[i+1] = (arr[i] * arr[i+1])//b
    answer = arr[-1]
    return answer    
print(solution(arr))