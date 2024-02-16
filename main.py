import datetime
import PySimpleGUI as sg
import os
current_year=datetime.datetime.today().year
class chel:
    name=None
    date=None
    fakedate=None
    rasst=None
    def inf_get(self,spis):
        self.name=spis[0]
        self.date=datetime.datetime(spis[1],spis[2],spis[3])
        self.fakedate=datetime.datetime(current_year,spis[2],spis[3])
        self.rasst=(self.fakedate-datetime.datetime.today()).days
    def inf_write(self):
        print(self.name, str(self.date)[:-9], self.rasst)
def readinf():
    file=open('birth.txt')
    s=[x.split(',') for x in file if x != '\n']
    for x in s:
        x[1]=int(x[1])
        x[2]=int(x[2])
        x[3]=int(x[3])
    file.close()
    return s
def writeinf():
    file = open('birth.txt', 'a')
    file.write(input('Запишите данные в формате: Имя,год,месяц,день ')+'\n')
    file.close()

sp=readinf()
ans=[]
for x in sp:
    i=chel()
    i.inf_get(x)
    ans.append(i)
willBe = [x.rasst for x in ans if x.rasst>0]
minr = 100
if len(willBe)>0:
    minr=min(willBe)
posmin=[x.rasst for x in ans if x.rasst>minr]
if len(posmin)>0:
    posmin=min(posmin)
def bliz():
    for x in ans:
        if x.rasst==minr:
            if x.date.year<1000:
                return 'Ближайший день рождения: ' + str(x.name)+', через '+str(x.rasst)+' дней\nДата: '+ str(x.date.day) + '-'+str(x.date.month)
            else:
                return 'Ближайший день рождения: ' + str(x.name)+', через '+str(x.rasst)+' дней, исполняется '+str((datetime.datetime.today()-x.date).days//365+1) + ' лет\nДата: '+ str(x.date.day) + '-'+str(x.date.month) + '-'+str(x.date.year)
    return 'Ближайших др не предвидется, спокойного НГ!'
def sled():
    if posmin!=[]:
        for x in ans:
            if x.rasst==posmin:
                return '\nСледующий день рождения: '+ str(x.name) + '('+str(x.date.day) +'-'+ str(x.date.month)+') через ' + str(x.rasst) + ' дней'
    else:
        return ''
sg.theme('DarkAmber')
lay=[[sg.T(bliz())], [sg.T(sled())],[sg.B('OK'), sg.B('Внести изменения в список')]]
window=sg.Window('Birthday Helper', lay)
while True:
    event, value=window.read()
    if event in (sg.WINDOW_CLOSED, 'OK'): break
    if event=='Внести изменения в список':
        sg.popup('Вводите данные в формате: Имя, год, месяц, день')
        file_path = str(os.getcwd()) + r'\birth.txt'
        os.system("start " + file_path)

window.close()