from sendmail import mail
import os
obj=mail(input("请输入您的smtp服务器地址："),input("请输入您的邮箱地址："),input("请输入您的授权码："))
while 1:
  os.system("cls")
  print("您的选择：\n\n1:发送邮件\n\n2:退出")
  c=input("请选择：")
  if c=="1":
    os.system("cls")
    obj.send(input("请输入收件人地址："),input("请输入邮件的正文："),input("请输入邮件的标题："))
    pass
  elif c=="2":
    exit()
    pass
  pass
