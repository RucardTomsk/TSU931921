import requests
import time
from bs4 import BeautifulSoup as BS


#Строки ввода значений
print("Введите данные матча: ")
print("1 Команда: ")
Team1 = input()
print("2 Команда: ")
Team2 = input()
print("Дата: ")
Data = input()
print("Время: ")
Time = input()

#Парсинг (город - страна) 
r = requests.get('https://www.euro-football.ru/team')
html = BS(r.content,'html.parser')
time.sleep(0.5)
for el in html.select('.infoblock'):
    title = el.select('.infoblock > a')
    if(title[0].text == Team1):
       a = title[0].get('href') 
    if(title[0].text == Team2):
       b = title[0].get('href')
       
rTeam1 = requests.get('https://www.euro-football.ru' + a)
time.sleep(0.5)
rTeam2 = requests.get('https://www.euro-football.ru' + b)
time.sleep(0.5)
htmlS = BS(rTeam1.content,'html.parser')
time.sleep(0.5)
Town1 = ""
Town2 = ""
Country1 = ""
Country2 = ""

for el in htmlS.select('.team-about__info'):
    title = el.select('p')
    Town1 =title[0].text
    Country1 =title[1].text
time.sleep(0.5)
htmlD = BS(rTeam2.content,'html.parser')
time.sleep(0.5)
for el in htmlD.select('.team-about__info'):
    title = el.select('p')
    Town2 =title[0].text
    Country2 =title[1].text
time.sleep(0.5)    
Town1 = Town1[6:]
Town2 = Town2[6:]
Country1 = Country1[7:]
Country2 = Country2[7:]

if Data[3] == 0:
    rData = Data[3:]
else:
    rData = Data[2:]
    
print(Town1)
print(Country1)
print(Town2)
print(Country2)

time.sleep(0.5)

htmlSPos = BS(rTeam1.content,'html.parser')

for el in htmlSPos.select('.team-schedule__table'):
   title = el.select('td')
   
i = 0    
Teams = [0, 0]
for el in htmlSPos.select('td'):   
    try:
        if (i % 4 == 0):
            DataPole =  title[i].text
            DataPole = DataPole[:2]
            print(DataPole)
            TimePole =  title[i].text
            TimePole = TimePole[-5:]
            print(TimePole)
        if (i % 4 == 1):
            Teams[0] = title[i].text
            print(Teams[0])
        if (i % 4 == 3):
            Teams[1] = title[i].text
            print(Teams[1])
    except:
        print('---')
    else:
        if (i % 4 == 3):
            print(Teams, [Team1, Team2])
            print((DataPole == Data[:2]) , (TimePole == Time) , (Team1 in Teams , Team2 in Teams))
            if ((DataPole == Data[:2]) and (TimePole == Time) and (Team1 in Teams and Team2 in Teams)):
                Strect = title[i-1]
                Strect = str(Strect)
                Strect = Strect[72:-14]
                print(Strect)
                time.sleep(0.5)
                StrectPole = requests.get(Strect)
                Pole = BS(StrectPole.content,'html.parser')
                for ell in Pole.select('.match-info__description'):
                    titlel = ell.select('a')
                TownPole = titlel[0].get('href')
                print(TownPole)
                time.sleep(0.5)
                TownStrectPole = requests.get(TownPole)
                TownStrectPolePole = BS(TownStrectPole.content,'html.parser')
                for elll in TownStrectPolePole.select('.stadium-about__info'):
                    InfiTawn = elll.select('th')
                    StranaStadi = elll.select('td')
                print(InfiTawn)
                print(StranaStadi)
                ChekCTRANA = 0
                ChekGOROD = 0
                for pole in InfiTawn:
                    if "Страна" in pole.text:
                        j = InfiTawn.index(pole)
                        ChekCTRANA = 1
                        break
                for pole in InfiTawn:
                    if "Город" in pole.text:
                        g = InfiTawn.index(pole)
                        ChekGOROD = 1
                        break
                if(ChekCTRANA == 1):
                    CTRANAPOLE = StranaStadi[j].text;
                if(ChekGOROD == 1):
                    GORODPOLE = StranaStadi[g].text;
                break
        i = i + 1
        

       




   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   