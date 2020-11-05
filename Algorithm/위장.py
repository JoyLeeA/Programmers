# (한 옷의 종류수 + 1(안입는경우의수))* (한 옷의 종류수 + 1(안입는경우의수)) -(아무것도 안 입는경우의수)

# clothes = [["yellow_hat", "headgear"], 
# ["blue_sunglasses", "eyewear"], 
# ["green_turban", "headgear"]]

# clothes = [["crow_mask", "face"], 
# ["blue_sunglasses", "face"], 
# ["smoky_makeup", "face"]]

def solution(clothes):
    dic = {}
    for i in range(len(clothes)):
        if not dic.get(clothes[i][1]):
            dic[clothes[i][1]] = 1
        else:
            dic[clothes[i][1]] += 1

    answer = 1
    for value in dic.values():
        answer *= (value+1)
    return answer - 1