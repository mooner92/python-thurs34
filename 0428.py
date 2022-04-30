"""
Score = [0,0,0]
for i in range(10):
    A,B,C = map(int,input().split())
    Pivot = [0,0,0]
    peo = "A"
    for j in range(3):
        Pivot[0]+=A%10
        A/=10
        Pivot[1]+=B%10
        B/=10
        Pivot[2]+=C%10
        C/=10
    Repo = sorted(Pivot)
    if Repo[1] == Repo[2] :
        print("무효판입니다 현재스코어 : { %d : %d : %d }"%(Score[0],Score[1],Score[2]))
    else:
        if Repo[2]==Pivot[0]:
            Score[0]+=1
        elif Repo[2]==Pivot[1]:
            Score[1]+=1
            peo = "B"
        else:
            Score[2]+=1
            peo = "C"
        print("승자는 %s 현재스코어 : { %d : %d : %d }"%(peo,Score[0],Score[1],Score[2]))

if(Score[0]==Score[1] || Score[1]==Score[2] || Score[0]==Score[2]):
    Rep = sorted(Score)
    pe1,pe2 = "A","B"
    
    
    print("최종승자는 %s와 %s가 각각 %d회 동률로 무효!"%())
print("최종승자는 %s 가 %d회 승리하여 우승!"%())

#AS+=1 if Repo[0]==Pivot[0] else (BS+=1 if Repo[0]==Pivot[1] else CS+=1)#
"""

Score = [0, 0, 0]
print("점수는 공백으로 구분하여 입력하시면 됩니다. ex:) 111 222 333 ")
for i in range(10):
    A, B, C = map(int, input().split())
    if A>999 or B>999 or C>999:  #Exeption1
        print("1000 페이지가 넘는 값이 입력되었기 때문에 종료됩니다.")
        quit()
    Pivot = [0, 0, 0]
    peo = "A"
    for j in range(3):
        Pivot[0] += A % 10  #일,십,백의 자리수를 뽑아냄
        A /= 10  #10으로 나눈 값을 저장해줌
        Pivot[1] += B % 10
        B /= 10
        Pivot[2] += C % 10
        C /= 10
    Repo = sorted(Pivot)  #오름차순을 정렬된 클론배열을 생성해줌
    if Repo[1] == Repo[2]:  #최고값과 차고값이 같다면 무효판임
        print("무효판입니다 현재스코어 : { %d : %d : %d }" % (Score[0], Score[1], Score[2]))
    else:
        if Repo[2] == Pivot[0]:  #딕셔너리를 쓰지 않았기 때문에 Repo를 value 처럼 Pivot을 key 처럼 사용해서 비교해줌
            Score[0] += 1  #peo의 default를 'A'로 지정해주었기 때문에 중복되는 명령을 피해줌
        elif Repo[2] == Pivot[1]:
            Score[1] += 1
            peo = "B"
        else:
            Score[2] += 1
            peo = "C"
        print("승자는 %s 현재스코어 : { %d : %d : %d }" % (peo, Score[0], Score[1], Score[2]))

Repo1 = sorted(Score)
if Repo1[1]==Repo1[2]:
    if Repo1[0]==Score[0]:  #위와 마찬가지로 최종승자를 가려낼 때도 딕셔너리를 사용하지 않았기 때문에 정렬된 배열을 value삼아 비교해준다.
        print("최종 승자는 B와 C가 각각 %d회 동률로 무효! "%Score[1])
    elif Repo1[0]==Score[1]:
        print("최종 승자는 A와 C가 각각 %d회 동률로 무효! " % Score[0])
    elif Repo1[0]==Score[2]:
        print("최종 승자는 A와 B가 각각 %d회 동률로 무효! " % Score[1])
else:
    for i in range(3):
        if Repo1[2] == Score[i]:
            print("승자 %s가 %d회 승리하여 우승!"%(chr(i+65),Score[i] ))
            #for문과 일정한 숫자를 더해 chr함수를 사용하여 아스키파싱을 통해 비교해주었다.

