
#range : 순차적 정수를 만들어 내는 함수

# 값이 1개 있을 경우 = end: 0~end 미만의 순차적 정수
seq=range(10)
print(seq,type(seq))


seq=range(0,10,1) # 위의 선언과 동일하다

#순차 자료형
print(len(seq)) # 길이
print(seq[5])   #인덱싱
print(seq[3:7]) #슬라이싱

for i in seq: print(i) # for 이용 순환도 가능

# 거꾸로 가려면 step 값을 음수로 주면 됨
for i in range(10,0,-2) : print(i)

# enumerate 함수

print("--------------------enumerate")

colors=["red","blue","green","yello"]
#이 리스트의 객체를 모두 출력하려면
for color in colors:
    print(color)


#인덱스 값까지 가져오려면
i=0
for color in colors:
    print("{0}번 색상은 {1}".format(i,color))
    i+=1

#enumerate 를 이용하면 손쉽게 인덱스와 그 안의 값을 튜플로 묶어준다 
print(enumerate(colors))

for i,color in enumerate(colors):
    #print(color)
    print("{0}번 색상은 {1}".format(i,color))
    
