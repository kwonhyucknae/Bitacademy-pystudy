#point를 임포트 하여 사용

from point import Point #Point 모듈로 부터 Point를 불러온다

p1 = Point(10,10)
print("p1",p1)
print("reper",repr(p1))
print("instance count:",Point.instance_count)
p2=Point(20,20)
print("p2",p2)
print("reper",repr(p2)) #repr 메시지를 확인

print("instance count:",Point.instance_count)

p2_copy=eval(repr(p2))
print("p2_copy:",p2_copy)

