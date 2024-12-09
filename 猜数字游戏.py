import random

anum=random.randint(1,99)
print(f"要猜的数字是: {anum}" )

num=int(input("猜猜这个是什么数字"))

while num!=anum:
    try:
        if num>anum:
            num=int(input("大了"))
        else: 
             num=int(input("小了"))
    except ValueError:
        print("请输入一个有效的数字!")
        continue

print("很好，猜对了")