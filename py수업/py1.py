print("100")
print("%d"%123)
print("%d"%(100+100))

print("%7.3f"%123.4567)
print("%3s"%"python") ######3자리를 지정했지만 그냥 출력 (유연하다)######

print("{0:s} {1:s} {2:d}".format("python","is",300))
print(r"\n")


myVar = 100              	# 정수형 변수로 인식했으나
myVar = 100.0   		# 실수형 변수로 바뀌었다가,
myVar = True    		# 다시 불형 변수로 바뀜
myVar = myVar * 2 		# 어떻게 출력될까요? 에러? TrueTrue?

print(myVar)

#print("%d년은 윤년입니다."%a)

#((a%4==0 and a%100!=0) or a%400==0)

