a= int(input("연도를 입력하세요 :"))
print("%d년은 윤년입니다."%a) if ((a%4==0 and a%100!=0) or a%400==0) else print("%d년은 윤년이 아닙니다."%a)
