#数据结构
list=["a","d","m","i","n","s","t","r","a","t","o","r"]
print("list=",list)
print("--------------")
print("list=",list[::-1])

word="a"
if word in list:
    list[0]="A"
    list[-4]="A"
    print(list)
else:
    print("false")
