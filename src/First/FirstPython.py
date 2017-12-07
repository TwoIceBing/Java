'''
Created on 2017年12月6日

@author: Administrator
'''
print ("hello world", "你好", sep=',')
a = 5
print(a)
print('\n--------------')
    
# 斐波那契数列
a, b = 0, 1
list1 = []
while b < 1000:
    list1 += [b]
    a, b = b, a + b
print(list1)
print("list的ID是" + hex(id(list1)))
print('\n--------------')

age = 40
# age = int(input('请输入你的年龄：'))
if age < 30:
    print('%d岁是年轻人' % age)
elif age < 50:
    print('%d中年人%d' % (age, age - 20))
else:
    print('%d岁是%s' % (age, '老人'))
print('\n--------------')

# 1-100以内的质数
'''
优点：
    1、每五个质数换行
    2、制表，且最后一个指数后无制表符
'''
count = 0
for i in range(1, 101):
    for j in range(1, i):
#         if i % (i//2) == 1:
        if j == i // 2 and i % j == 1 or (i <= 3 and i != 1):
            if count == 4:
                print(i)
                count = 0
            else:
                print(i, end='\t')
                count += 1
            break
        if i % j == 0 and j != 1:
            break

print('\n--------------')

# 1-100以内的质数存入列表
list_prime = [];
for i in range(1, 101):
    if i <= 3 and i != 1:
        list_prime += [i]
    for j in range(2, i):
        if j == i // 2 and i % j == 1:
            list_prime += [i]
            break
        if i % j == 0:
            break
print(list_prime)

print('\n--------------')
print('1//2=', 1 // 2)
print('99//2=', 99 // 2)
print('99%49=', 99 % 49)
print('99 % (99//2)=', 99 % (99 // 2))
print('99 % 99//2=', 99 % 99 // 2)

print('\n--------------')

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        if i == j:
            print('{1}×{0}={2}'.format(i, j, i * j))
        else:
            print('{1}×{0}={2}'.format(i, j, i * j), end='\t')

print('\n','-'*30)
str1=r'hello\tworld'  # 原始字符串
print(str1,'\t',str1[0:5])
print(str,int)

print('\n','-'*30)

#可变参数
name,age,num = 'name','age',[]
def stu(name1,age1='',num1=''):
    name = 'Name'
    global age; age = 'Age'
    num.append(1)
    print(name1,age1,num1)
    
stu('1', '2', '3')
stu('q')
stu('1',age1='5')
print('name={},age={},num={}'.format(name,age,num))

print('\n','-'*30)

aa = 1
print(hex(id(aa)),aa)
aa = 2
print(hex(id(aa)),aa)

aa = [1]
print(hex(id(aa)),aa)
aa = [1,2]
print(hex(id(aa)),aa)
aa.append(3)
print(hex(id(aa)),aa)
    
