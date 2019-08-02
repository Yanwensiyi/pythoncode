from os import system as sys
class Staff:
    def __init__(self,name,age,sex,addr):
        self.id=len(staffs)
        self.name=name
        self.age=age
        self.sex=sex
        self.addr=addr

def exit_system():
    print("即将退出系统，欢迎您的下次使用！")
    pause()
    exit(0)

def menu_restricted():
    print("受限功能菜单\n\n1:查询员工\n\n2:退出系统")
    c=input("请输入您选择的功能项的序号:")
    if c=="1":
        query_staff()
        return
    elif c=='2':
        exit_system()
        return
    else:
        print("请输入有效的功能编号！")
        pause()
        return()

def menu():
    print("功能菜单\n\n1:查询员工\n\n2:添加员工\n\n3:删除员工\n\n4:编辑员工\n\n5:退出系统")
    c=input("请输入您选择的功能项的序号:")
    if c=='1':
        query_staff()
        return
    elif c=='2':
        add_staff()
        return
    elif c=='3':
        del_staff()
        return
    elif c=='4':
        edit_staff()
        return
    elif c=='5':
        exit_system()
        return
    else:
        print("请输入有效的功能编号！")
        pause()
        return

def query_staff():
    cls()
    global staffs
    if len(staffs)==0:
        print("还没有任何员工哦，请先去添加员工！")
        pause()
        return
    print("ID\t姓名\t\t年龄\t性别\t家庭住址")
    for i in staffs:
        if len(i.name)<4:
            print(str(i.id)+"\t"+i.name+"\t\t"+i.age+"\t"+i.sex+"\t"+i.addr)
            pass
        else:
            print(str(i.id)+"\t"+i.name+"\t"+i.age+"\t"+i.sex+"\t"+i.addr)
    pause()
    return

def add_staff():
    cls()
    name=input("请输入待添加员工的姓名:")
    age=input("请输入待添加员工的年龄:")
    sex=input("请输入待添加员工的性别:")
    addr=input("请输入待添加员工的家庭住址:")
    staffs.append(Staff(name,age,sex,addr))
    return

def del_staff():
    cls()
    global staffs
    if len(staffs)==0:
        print("还没有任何员工哦，请先去添加员工！")
        pause()
        return
    print("ID\t姓名\t\t年龄\t性别\t家庭住址")
    for i in staffs:
        if len(i.name)<4:
            print(str(i.id)+"\t"+i.name+"\t\t"+i.age+"\t"+i.sex+"\t"+i.addr)
            pass
        else:
            print(str(i.id)+"\t"+i.name+"\t"+i.age+"\t"+i.sex+"\t"+i.addr)
    id=int(input("请输入欲删除的员工的ID:"))
    try:
        del staffs[id]
        temp=staffs
        staffs=[]
        for i in temp:
            staffs.append(Staff(i.name,i.age,i.sex,i.addr))
        print("删除员工完成！")
        pause()
        return
    except:
        print("ID不存在，请重新检查！")
        pause()
        return
    else:
        pass
def edit_staff():
    cls()
    global staffs
    if len(staffs)==0:
        print("还没有任何员工哦，请先去添加员工！")
        pause()
        return
    print("ID\t姓名\t\t年龄\t性别\t家庭住址")
    for i in staffs:
        if len(i.name)<4:
            print(str(i.id)+"\t"+i.name+"\t\t"+i.age+"\t"+i.sex+"\t"+i.addr)
            pass
        else:
            print(str(i.id)+"\t"+i.name+"\t"+i.age+"\t"+i.sex+"\t"+i.addr)
    try:
        id=int(input("请输入欲编辑的员工的ID:"))
        pass
    except:
        print("ID不存在，请重新检查！")
        pause()
        return
    else:
        if(id>=len(staffs)):
            print("ID不存在，请重新检查！")
            pause()
            return
        while(1):
            cls()
            print("请问您想要编辑员工的哪项信息呢？\n\n1:年龄\n\n2:家庭住址\n\n3:退出编辑\n\n")
            c=input("您的选择:")
            if c=='1':
                cls()
                staffs[id].age=input("请输入欲修改为的值:")
                pass
            elif c=='2':
                cls()
                staffs[id].addr=input("请输入欲修改为的值:")
                pass
            elif c=='3':
                break
            else:
                pass
        cls()
        print("编辑完毕！即将回到主菜单。")
        pause()
        return


def pause():
    print("按任意键返回……")
    sys("pause>nul")
    return

def cls():
    sys("cls")
    return

def login():
    cls()
    errc=0
    user=input("请输入您的用户名（匿名登录请输入Anonymous）:")
    if user=="Anonymous":
        cls()
        return False
    elif user=="Admin":
        pass
    else:
        print("您的用户名错误！")
        pause()
        return None
    while(errc<3):
        passwd=input("请输入您的密码(剩余次数："+str(3-errc)+"):")
        if passwd=="20010917":
            cls()
            return True
        else:
            errc+=1
            cls()
            print("密码错误！")
            pause()
    cls()
    print("您已经连续三次输入错误密码，系统即将退出！")
    pause()
    exit(0)
    return

if __name__!="__main__":
    exit(0)
staffs=[]
staffs.append(Staff("王宇昊",'17',"女","湖北省"))
staffs.append(Staff("伊藤诚",'15',"男","榊野县榊野学园"))
staffs.append(Staff("爱蜜莉雅",'107',"女","露格尼卡王国"))
staffs.append(Staff("藤原千花",'17',"女","秀知院学园"))
staffs.append(Staff("御坂美琴",'14',"女","学园都市第7学区常盘台中学学生寮208号室"))
staffs.append(Staff("上条当麻",'16',"男","某高中"))
staffs.append(Staff("一方通行",'15',"？","第十八学区长点上机学园"))
staffs.append(Staff("宫园薰",'14',"女","市立墨谷中学"))
staffs.append(Staff("卫宫切嗣",'29',"男","？"))
staffs.append(Staff("神座出流",'15',"男","私立希望之峰学园"))
while(1):
    logined=login()
    if logined!=None:
        break
if logined==True:
    print("欢迎您，尊贵的管理员用户！")
    while 1:
        menu()
        cls()
else:
    print("欢迎您，匿名用户！")
    while 1:
        menu_restricted()
        cls()
