record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    new_record = []
    temp = []
    dic = {}
    for rec in record:
        cnt = 0
        for i in range(len(rec)):
            if rec[i] == " ":
                temp.append(rec[cnt:i])
                cnt = i+1
            elif i==len(rec)-1:
                temp.append(rec[cnt:i+1])
                
        new_record.append(temp)
        temp = []

    for i in range(len(new_record)):
        if new_record[i][0] == "Leave":
            pass
        else:
            dic[new_record[i][1]] = new_record[i][2]

    for new_rec in new_record:
        if new_rec[0] == "Enter":
            answer.append(f"{dic[new_rec[1]]}님이 들어왔습니다.")
        elif new_rec[0] == "Leave":
            answer.append(f"{dic[new_rec[1]]}님이 나갔습니다.")
        if new_rec[0] == "Change":
            pass
    return answer

print(solution(record))