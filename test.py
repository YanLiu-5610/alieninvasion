import copy
a = [1,2,3,4,5]
for index,num in enumerate(a):
    print(index,num)
    a.remove(num)
print(a)
a = {[1,2,3,4,5],[1,2,3],[3,4]}
for index,num in enumerate(a.deepcopy()):
    print(index,num)
    a.remove(num)
print(a)