scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80 and score < 90:
        return 'B'
    if score >= 70 and score < 80:
        return 'C'
    if score >= 50 and score < 70:
        return 'D'
    if score < 50:
        return 'F'

def solution(scores):
    answer = ''
    for i in range(len(scores)):
        score_list = list(row[i] for row in scores[:])
        print('score_list : ', score_list)
        tmp_s = [min(score_list), max(score_list)]
        print('tmp_s : ',tmp_s)
        sum = 0
        m = len(scores)
        for j, s in enumerate(score_list):
            sum += s
            if i == j:
                if scores[i][j] in tmp_s:
                    if score_list.count(scores[i][j]) == 1: # 유일이면
                        print(score_list.count(scores[i][j]))
                        sum -= s
                        m -= 1
            print(j, sum)
        print('결과 ', sum/m , get_grade(sum/m))
        answer += get_grade(sum/m)

    print(answer)
    return answer

solution(scores)
