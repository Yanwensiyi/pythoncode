import urllib.request as u
from json import loads

users=[]

class biliuser:
  def __init__(self,uid):
    self.update(uid)
    return
  def update(self,uid):
    try:
      data=loads(u.urlopen("https://api.bilibili.com/x/space/acc/info?mid="+str(uid)).read().decode("utf-8"))["data"]
      self.mid=str(uid)
      self.name=data["name"]
      self.sex=data["sex"]
      self.sign=data["sign"]
      self.level=data["level"]
      self.birthday=data["birthday"]
      self.vain=False
      pass
    except:
      self.vain=True
      pass
    return
  pass
file = open("biliusers.txt","w")
for x in range(1,1001):
  i = biliuser(x)
  users.append(i)
  try:
    if i.vain==True:
      continue
    print("UID:%s\nName:%s\nGender:%s\nSign:%s\nLevel:%s\nBirthday:%s\n\n"%(i.mid,i.name,i.sex,i.sign,i.level,i.birthday))
    file.write("UID:%s\nName:%s\nGender:%s\nSign:%s\nLevel:%s\nBirthday:%s\n\n"%(i.mid,i.name,i.sex,i.sign,i.level,i.birthday))
    pass
  except:
    pass
  pass
file.close()
