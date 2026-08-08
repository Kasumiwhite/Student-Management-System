#学生成绩管理系统文件版
students = []   #空列表存储学生信息
#加载学生
def load_student():
    try:
        f = open('D:/学生成绩.txt','r',encoding='UTF-8')
        #确保程序运行结束后仍能重新读取文件
        content = f.read()
        parts = content.strip().split('\n')
        #数据解析
        for line in parts:
            if line == "":
                continue
            data = line.split(',')
            name = data[0].split(':')[1]
            score = int(data[1].split(':')[1])

            students.append({
                "name": name,
                "score": score
            })
        f.close()

    except:
        print("未找到该文件！")
#菜单功能
def show_menu():
    print("----------学生成绩管理系统----------\n1.添加学生\n2.查询学生\n3.显示全部学生\n4.退出系统")
    return int(input("请输入你的选择："))
#添加学生
def add_student():
    name = input("请输入学生姓名：")
    for i in students:
        if i["name"] == name:
            print("该学生已存在")
            return
    score = int(input("请输入学生成绩："))
    students.append({"name":name,"score":score})
    f = open("D:/学生成绩.txt",'a',encoding = 'UTF-8')
    f.write(f"name:{name},score:{score}")
    f.write('\n')   #一行一个学生信息
    f.close()
#查询学生
def search_student():
    found = False
    name = input("请输入查询学生姓名：")
    for i in students:
        if i["name"] == name:
            found = True
            print("学生姓名：%s\n成绩：%d"%(i["name"],i["score"]))
    if found == False:
            print("没有找到该学生")
#显示全部学生
def show_all():
    if len(students) == 0:
        print("暂无学生信息")
        return
    for i in students:
        print("姓名：%s 成绩：%d"%(i["name"],i["score"]))
#主程序循环
load_student()
while True:
    a = show_menu()
    if a == 1:
        add_student()
    elif a == 2:
        search_student()
    elif a == 3:
        show_all()
    elif a == 4:
        print("系统退出")
        break


