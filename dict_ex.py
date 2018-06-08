#사전
#순서 없고, key-value 매칭 자료형
#len(),in,not in 정도만 가능하다

#사전 만들기


d=dict() # 빈 사전
print(d,type(d))

#방법 2 : {} 를 이용하여 만들기

d={}
print(d,type(d))


#방법 3 : key-value ang 를 이용하여 만들기
d=dict(one=1, two = 2 )
print(d,type(d))

#방법 4 : key, value 리스트들이 따로 있을때
#zip 함수를 이용한다
keys={"one","two","three"}
values={1,2,3,}

d=dict(zip(keys,values))
print(d,type(d))


#사전의 키
print("-------------Key")
# 키는 변경 불가 자료형을 사용해야한다 

d={}
d[10]="10"
#숫자형은 변경 불가라서 가능하다
d["baseball"]=9
d[("kim",10)]="학생"

print(d,type(d))

#리스트는 변경 가능 자료형이라 키로 사용 될 수 없다 . TypeEror 발생

'''
d[["lee",30]]="근로자"
'''

#사전 메서드
print("-----------------Methods")
#사전 생성
d={"baseball":9 ,"soccer":11,"basketball":5}
print(d,type(d))

#키 목록을 가져와 보겠음 : keys() 이용
print(d.keys())
#값의 목록을 가져옴 : values() 사용
print(d.values())
#키와 값의 쌍의 목록 : items() 사용
print(d.items())

#값 가져오기
print(d['baseball'])

#handball은 없기 때문에 KeyError
'''
print(d['handball'])
'''

#값가져오기 2 : get 으로 가져오기
#Error 는 안나는데 None 이 나온다
print(d.get('handball'))
print(d.get('handball',"?")) #기본값을 ? 로 설정


#값의 삭제 : del 함수 사용한다
del d['soccer']
print(d)

#사전 비우기 clear 함수 사용
d.clear()
print(d)


#사전의 순회
print("------------------순회")

d={"baseball":9 ,"soccer":11,"basketball":5}


# 방법 1 :키값을 순회하면서 받아와서 내용 처리
# d 가 key 값을 더이상 없을때까지 넘겨준다
for key in d:
    print(key,":",d[key])

#같은 방법
for key in d.keys():
    print(key,":",d[key])

#방법 2 : 키와 값을 함께 받아와서 활용: items()
# end 는 개행
for key,value in d.items():
    print("{0}:{1}".format(key,value),end=" ")
else:
    print()