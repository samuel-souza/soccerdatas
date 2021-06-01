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
f = m.find_element_by_class_name('navegacao-fase')
fases = f.find_element_by_class_name('navegacao-fase__fase').text
fases = fases.upper()



if fases == 'FINAL':
    try:
        lb = m.find_element_by_class_name('navegacao-fase__seta-esquerda')
        for i in range(3):
            lb.click()
            sleep(0.5)

    except:
        None 
elif fases == 'SEMIFINAL':
    try:
        lb = m.find_element_by_class_name('navegacao-fase__seta-esquerda')
        for i in range(2):
            lb.click()
            sleep(0.5)

    except:
        None 
elif fases == 'SEGUNDA FASE':
    try:
        lb = m.find_element_by_class_name('navegacao-fase__seta-esquerda')
        lb.click()


    except:
        None 
else:
    botesq = m.find_element_by_class_name('lista-jogos__navegacao--seta-esquerda')
    botdir = m.find_element_by_class_name('lista-jogos__navegacao--seta-direita')


sleep(1)

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
l = []

def checker(ho,pm,pv,vi,lo):
    b = [ho,lo]
    if pm and pv != '': 
        X.append(pm)
        MAN.append(ho)
        Y.append(pv)
        VIS.append(vi)
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
        x.append(pm)
        man.append(ho)
        y.append(pv)
        vis.append(vi)
    
        if b in times_estadios:
            try: 
                a = 1
                l.append(a)
            except:
                None 
        else:
            try:
                a = 0
                l.append(a)
            except:
                None
        
        
    





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


if rod*4 == 28:
    rb = m.find_element_by_class_name('navegacao-fase__seta-direita')
    rb.click()
    for i in range(0,2,1):
        ul = m.find_element_by_class_name('tabela__mata-mata')
        lis = ul.find_elements_by_class_name('chave__jogos--1')
        thm = lis[i].find_element_by_class_name('theme')
        tl = thm.find_element_by_class_name('jogo__transmissao--link')
        inf = tl.find_element_by_class_name('jogo__informacoes')
        lcl = inf.find_element_by_class_name('jogo__informacoes--local')
        placar = tl.find_element_by_class_name('placar')
        mdt = placar.find_element_by_class_name('placar__equipes--mandante')
        mandante = mdt.find_element_by_class_name("equipes__sigla").get_attribute('textContent')
        vst = placar.find_element_by_class_name('placar__equipes--visitante')
        visitante = vst.find_element_by_class_name('equipes__sigla').get_attribute('textContent')
        plb = placar.find_element_by_class_name('placar-box')
        t1 = plb.find_element_by_class_name('placar-box__valor--mandante')
        t2 = plb.find_element_by_class_name('placar-box__valor--visitante')
        checker(mandante,t1.text,t2.text,visitante,lcl.text)
    
    sleep(2)
    rb.click()

    for i in range(0,2,1):
        ul = m.find_element_by_class_name('tabela__mata-mata')
        lis = ul.find_elements_by_class_name('chave__jogos--1')
        thm = lis[i].find_element_by_class_name('theme')
        tl = thm.find_element_by_class_name('jogo__transmissao--link')
        inf = tl.find_element_by_class_name('jogo__informacoes')
        lcl = inf.find_element_by_class_name('jogo__informacoes--local')
        placar = tl.find_element_by_class_name('placar')
        mdt = placar.find_element_by_class_name('placar__equipes--mandante')
        mandante = mdt.find_element_by_class_name("equipes__sigla").get_attribute('textContent')
        vst = placar.find_element_by_class_name('placar__equipes--visitante')
        visitante = vst.find_element_by_class_name('equipes__sigla').get_attribute('textContent')
        plb = placar.find_element_by_class_name('placar-box')
        t1 = plb.find_element_by_class_name('placar-box__valor--mandante')
        t2 = plb.find_element_by_class_name('placar-box__valor--visitante')
        checker(mandante,t1.text,t2.text,visitante,lcl.text)
    




fm = np.array([man,x,y,vis,l])
fm = fm.transpose() 
future_matches = pd.DataFrame(fm, columns = ['Home','X','Y','Visitor','Local'])



db = np.array([MAN,X,Y,VIS,c])
db = db.transpose()
database = pd.DataFrame(db,columns=['Home','X','Y','Visitor','Local'])


browser.quit()

database.to_csv('dtbase.csv',index=False)
future_matches.to_csv('fmatches.csv',index=False)



