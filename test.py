a=int(input('Введи первую дату'))
b= int(input('Введи следущую дату'))
#Разница между двух дат
r=(a-b)
#присваиваем переменной кол. сек в дне
cek_day=86400
#вычисляем колл.дней
day= str(r//cek_day)
#вычисляем колл.часов
haur=str((r-cek_day)//3600)
#вычисляем колл.минут
minn=str(((r-cek_day)%3600)//60)
#вычисляем колл.секунд
sec=str(((r-cek_day)%3600)%60)
#задаем условие выводить или нет секунды
if int(sec)>0:
    print('%s day %s hour %s min and %s seconds'%(day, haur, minn, sec))
else:
    print('%s day %s hour %s min '%(day, haur, minn, ))


