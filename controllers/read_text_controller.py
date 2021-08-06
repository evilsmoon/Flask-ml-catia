import re
def readTxt(text):
  data = []
  f = open (text,'r',encoding='UTF-8')
  for i in f.readlines():
    # print(i.strip('\n'))
    data.append(i.strip('\n'))
  f.close()
  return data