#문자열 서식과 관련

#서식 문자

'''
%s : 문자열 
%d : 정수
%f : 부동소수
%% : % 리터럴  -> % 글자 한개
'''

format="I have %d apples"
print(format % 10)

print("Interest Rate is %f%%" % 1.24)

#1.240000을 1.24로 끊기
print("Interest Rate is %.2f%%" % 1.24)

# 두 개 이상의 값을 넣고 싶을 때
format = "total:%d개, get:%d개"
print(format %(10,3)) # 그냥은 안되고 튜플로 묶는다

# format 과 값의 형식이 일치하지 않으면 TypeError 발생

format_str = "I have {} apples, and I ate {} apples."
print(format_str.format(5,3))

#서식에 설정된 공간의 개수보다 실제 값의 개수가 적으면 IndexError 발생
print(format_str.format(10,3,1))
#넘치는건 된다
#print(format_str.format(10))    인덱스 에러 발생


#이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format(total=10,num=3))
#print(format_str.format(total=10)) 하나만 있으면 KeyError 발생


#dict 사전 객체를 이용한 포맷
print(format_str.format_map({"total":5,"num":2}))
