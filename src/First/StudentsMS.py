'''
Created on 2017年12月7日
这是一个学生管理系统
@author: Administrator
'''
def showMS():
    print('-' * 30)
    print('    学生管理系统1.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询指定学生信息')
    print('5.查询所有学生信息')
    print('6.退出系统')
    print('-' * 30)

students = []
# 1.添加学生信息
def addStuInfo(stuNum, stuName, stuAge):
    stuInfo = {'num':stuNum, 'name':stuName, 'age':stuAge}
    students.append(stuInfo)
    print('添加成功！！！')
    

def addStu():
    stuNum = input('请输入学生学号：')
    if checkStuInfo(stuNum):
        if input('此学生已存在，如果要修改请按3,否则按enter以继续') == '3':
            updateStu(stuNum)
        return
    stuName = input('请输入学生姓名：')
    stuAge = input('请输入学生年龄：')
    addStuInfo(stuNum, stuName, stuAge)
    if input('返回主页面请按0，否则按enter以继续') == '0':
        return
    else:
        addStu()

# 2.删除学生信息
def deleteStuInfo(stuNum):
    for stu in students:
        if stu['num'] == stuNum:
            students.remove(stu)
            input('删除成功')
            return
    input('此学生不存在')

# 3.修改学生信息
def updateStuInfo(stuNum, stuName='', stuAge=''):
    for stu in students:
        if stu['num'] == stuNum:
            if stuName != '':
                stu['name'] = stuName
            if stuAge != '':
                stu['age'] = stuAge
            input('修改成功')

def updateStu(stuNum):
    restuName = input('请输入要修改的学生姓名，不修改姓名请按enter以继续:')
    restuAge = input('请输入要修改的学生学号，不修改学号请按enter以继续:')
    updateStuInfo(stuNum,restuName,restuAge)
    
    
# 4.查询指定学生信息
def selectStuInfo(stuNum):
    for stu in students:
        if stu['num'] == stuNum:
            print('|学号\t', '|姓名\t', '|年龄\t|')
            print('|%s\t' % stu['num'], '|%s\t' % stu['name'], '|%s\t|' % stu['age'])
            input('按enter以继续')
            return
    input('此学生不存在')

# 5.查询所有学生信息
def queryStuInfo():
    if students == []:
        print('没有学生的信息')
        input('-----按enter以继续-----')
        return
    print('|学号\t', '|姓名\t', '|年龄\t|')
    for stu2 in students:
        print('|%s\t' % stu2['num'], '|%s\t' % stu2['name'], '|%s\t|' % stu2['age'])
    input('-----按enter以继续-----')

# 检查学生是否存在
def checkStuInfo(stuNum):
    for stu in students:
        if stu['num'] == stuNum:
            return True
    return False

while True:
    showMS()
    num1 = input('输入数字进入功能页面：')
    
    # 1.添加学生信息
    if num1 == '1':
        addStu()

    # 2.删除学生信息
    elif num1 == '2':
        stuNum = input('请输入要删除的学生学号：')
        deleteStuInfo(stuNum)

    # 3.修改学生信息
    elif num1 == '3':
        stuNum = input('请输入要修改的学生的学号：')
        selectStuInfo(stuNum)
        print()
        updateStu(stuNum)

    # 4.查询指定学生信息
    elif num1 == '4':
        stuNum = input('请输入要查询的学生学号')
        selectStuInfo(stuNum)

    # 5.查询所有学生信息
    elif num1 == '5':
        queryStuInfo()

    # 6.退出系统
    elif num1 == '6':
        break

    else:
        input('输入有误，请重写输入')
