from urllib.request import urlopen,Request
from json import loads
class video:
  def __init__(self,av):
    av=str(av)
    self.av=av
    self.update(av)
    return
  def update(self,av):
    try:
      data=loads(urlopen("https://api.bilibili.com/x/player/pagelist?aid="+av).read())["data"]
      self.p=[]
      for i in data:
        self.p.append(i["part"])
        pass
      req=Request("https://api.bilibili.com/x/web-interface/archive/stat?aid="+av)
      req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
      data=loads(urlopen(req).read())["data"]
      self.view=data["view"]
      self.danmaku=data["danmaku"]
      self.reply=data["reply"]
      self.favorite=data["favorite"]
      self.coin=data["coin"]
      self.share=data["share"]
      self.like=data["like"]
      pass
    except:
      self.visible=False
      pass
    else:
      self.visible=True
      pass
    return
  pass

def showlist(video):
  j=0
  print("av%s的分P列表:"%video.av)
  for i in video.p:
    j+=1
    print("P"+str(j)+":"+i)
    pass
  return

def showinf(video):
  print("播放量:%s\n弹幕数:%s\n回复数:%s\n收藏数:%s\n投币数:%s\n分享数:%s\n点赞数:%s"%(video.view,video.danmaku,video.reply,video.favorite,video.coin,video.share,video.like))
  return

for i in range(100000,100051):
  v=video(i)
  if v.visible==False:
    continue
    pass
  print("av%s:"%v.av)
  showinf(v)
  showlist(v)
  print("")
  pass