from selenium import webdriver 
from time import sleep 
import numpy as np 
import pandas as pd 


url = 'https://globoesporte.globo.com/pb/futebol/campeonato-paraibano/'
driver = './python'
dir(driver)
browser = webdriver.Firefox()
browser.get(url)
browser.maximize_window()
m = browser.find_element_by_class_name('grid-24')
r = m.find_element_by_class_name('lista-jogos__navegacao--rodada')
rod = int(r.text.split()[0].replace('ª',''))

botesq = m.find_element_by_class_name('lista-jogos__navegacao--seta-esquerda')
botdir = m.find_element_by_class_name('lista-jogos__navegacao--seta-direita')

MAN = []
X = []
Y = []
VIS = []
local = []

man = []
x = []
y = []
vis = []

c = []

def checker(ho,pm,pv,vi,lo):
    b = [mandante.text,lcl.text]
    if pm and pv != '': 
        X.append(t1.text)
        MAN.append(mandante.text)
        Y.append(t2.text)
        VIS.append(visitante.text)
        if b in times_estadios:
            try: 
                a = 1
                c.append(a)
            except:
                None 
        else:
            try:
                a = 0
                c.append(a)
            except:
                None
    else:
        x.append(t1.text)
        man.append(mandante.text)
        y.append(t2.text)
        vis.append(visitante.text)





times_estadios = [
    ['BOT','ALMEIDÃO'],
    ['SPC','CARNEIRÃO (PB)'],
    ['TRZ','AMIGÃO'],
    ['SOU','MARIZÃO (PB)'],
    ['CAM','AMIGÃO'],
    ['NAP','JOSÉ CAVALCANTI'],
    ['PER','AMIGÃO'],
    ['ATL','PERPETÃO']
]

for i in range(rod):
    botesq.click()
    sleep(0.35)

for i in range(rod):
    for j in range(4):
        ul = m.find_element_by_class_name('lista-jogos')
        lis = ul.find_elements_by_tag_name('li')
        thm = lis[j].find_element_by_class_name('theme')
        inf = thm.find_element_by_class_name('jogo__informacoes')
        lcl = inf.find_element_by_class_name('jogo__informacoes--local')
        placar = thm.find_element_by_class_name('placar')
        mdt = placar.find_element_by_class_name('placar__equipes--mandante')
        mandante = mdt.find_element_by_class_name('equipes__sigla')
        vst = placar.find_element_by_class_name('placar__equipes--visitante')
        visitante = vst.find_element_by_class_name('equipes__sigla')
        plb = placar.find_element_by_class_name('placar-box')
        t1 = plb.find_element_by_class_name('placar-box__valor--mandante')
        t2 = plb.find_element_by_class_name('placar-box__valor--visitante')
        checker(mandante.text,t1.text,t2.text,visitante.text,lcl.text)

    botdir.click()
    sleep(0.3)




for i in range(7-rod):
    for j in range(4):
        ul = m.find_element_by_class_name('lista-jogos')
        lis = ul.find_elements_by_tag_name('li')
        thm = lis[j].find_element_by_class_name('theme')
        inf = thm.find_element_by_class_name('jogo__informacoes')
        lcl = inf.find_element_by_class_name('jogo__informacoes--local')
        placar = thm.find_element_by_class_name('placar')
        mdt = placar.find_element_by_class_name('placar__equipes--mandante')
        mandante = mdt.find_element_by_class_name('equipes__sigla')
        vst = placar.find_element_by_class_name('placar__equipes--visitante')
        visitante = vst.find_element_by_class_name('equipes__sigla')
        plb = placar.find_element_by_class_name('placar-box')
        t1 = plb.find_element_by_class_name('placar-box__valor--mandante')
        t2 = plb.find_element_by_class_name('placar-box__valor--visitante')
        checker(mandante.text,t1.text,t2.text,visitante.text,lcl.text)


    botdir.click()
    sleep(0.3)


fm = np.array([man,x,y,vis])
fm = fm.transpose() 
future_matches = pd.DataFrame(fm, columns = ['Home','X','Y','Visitor'])

db = np.array([MAN,X,Y,VIS,c])
db = db.transpose()
database = pd.DataFrame(db,columns=['MAN','X','Y','VIS','local'])
browser.quit()

database.to_csv('dtbase.csv',index=False)
future_matches.to_csv('fmatches.csv',index=False)