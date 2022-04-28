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
