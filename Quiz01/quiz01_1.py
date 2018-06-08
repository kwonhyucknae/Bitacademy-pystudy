str="Life is too short, You need Python"

str=str.lower()
print(str)

str=str.replace(" ","")
str=str.replace(",","")

print(str)

lst=str.split()
print(type(lst))

chars = set(lst)
print(chars)

lst=list(chars)
print(type(lst))

lst=lst.sort()
print(lst)
n=len(lst)
print(n)