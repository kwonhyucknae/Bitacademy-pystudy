lst=[1,2,3,4,5,6,7,8,9,10]

slice=lst[3:7]
print(slice)

slice.reverse()
print(slice)

print(lst)
lst[3:7]=slice

print(lst)