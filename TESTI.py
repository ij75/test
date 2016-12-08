from datetime import datetime
import time
#преобразовать  строку в дату
d = datetime.strptime('Thu, 18 Aug 2016 11:15:00 ', '%a, %d %b %Y %X ')
#преобразовать  дату в секунды
s = time.mktime(d.timetuple()) 
#обьявляем переменные
#все время
All_time=s+4320000
# час/сек 
#с=3600
#первый интервал
o_t=s+3600
#второй интервал
s_t=s+3600*5
#третий интервал
t_t=s+3600*12
#четвертый интервал
f_t=s+(3600*24)*6

while s<All_time:
  
  if s<=o_t:
    s+=900
    print(time.strftime('%a, %d %b %Y %X ', time.localtime(s)))

  elif s<s_t:
    s+=1800
    print(time.strftime('%a, %d %b %Y %X ', time.localtime(s)))
  elif s<t_t:
    s+=3600
    print(time.strftime('%a, %d %b %Y %X ', time.localtime(s)))
  elif s< f_t:
    s+=3600*24
    print(time.strftime('%a, %d %b %Y %X ', time.localtime(s)))