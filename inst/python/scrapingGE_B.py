from selenium import webdriver 
from time import sleep 
import numpy as np 
import pandas as pd 
from webdriver_manager.firefox import GeckoDriverManager
import os 

url = "https://globoesporte.globo.com/futebol/brasileirao-serie-b/"
browser = webdriver.Firefox(executable_path = GeckoDriverManager().install(),service_log_path= os.devnull)
browser.get(url)

m = browser.find_element_by_tag_name('main')
r = m.find_element_by_class_name('lista-jogos__navegacao--rodada')
rod = int(r.text.split()[0].replace('ª',''))
print(rod)

mandante = []
placart1 = []
placart2 = []
visitante = []
mdt = []
p1 = []
p2 = []
vi = []
c = []

times_estadios = [
    ['CHA','ARENA CONDÁ'],
    ['AME','INDEPENDÊNCIA'],
    ['JUV','ALFREDO JACONI'],
    ['CUI','ARENA PANTANAL'],
    ['CSA','REI PELÉ'],
    ['SAM','CASTELÃO'],
    ['PON','MOISÉS LUCARELLI'],
    ['OPE','GERMANO KRÜGER'],
    ['AVA','RESSACADA'],
    ['CRB','REI PELÉ'],
    ['CRU','MINEIRÃO'],
    ['BRA','BENTO FREITAS'],
    ['GUA','BRINCO DE OURO'],
    ['VIT','BARRADÃO'],
    ['CON','BATISTÃO'],
    ['NAU','AFLITOS'],
    ['FIG','ORLANDO SCARPELLI'],
    ['PAR','DURIVAL BRITTO'],
    ['BSP','SANTA CRUZ'],
    ['OES','ARENA BARUERI']
]

botoes = browser.find_element_by_class_name('lista-jogos__navegacao')
botaodir = botoes.find_element_by_class_name('lista-jogos__navegacao--seta-direita')

botoes = browser.find_element_by_class_name('lista-jogos__navegacao')
botaoesq = botoes.find_element_by_class_name('lista-jogos__navegacao--seta-esquerda')



for i in range(rod):
    try:
        botaoesq.click()
        sleep(0.25)
    except:  
        if True:
            print('reinicie a automação e tente novamente!')
            break


def checker(h,x,y,v,l):
    b = [man.text,lo.text]
    if x and y != '': 
        placart1.append(pt1.text)
        mandante.append(man.text)
        placart2.append(pt2.text)
        visitante.append(vis.text)
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
        p1.append(pt1.text)
        mdt.append(man.text)
        p2.append(pt2.text)
        vi.append(vis.text)



for j in range(rod):

    for i in range(10):
        ul = m.find_element_by_class_name('lista-jogos') 
        lis = ul.find_elements_by_tag_name('li') 
        div1 = lis[i].find_element_by_tag_name('div')
        infjogo = div1.find_element_by_class_name('jogo__informacoes')
        lo = infjogo.find_element_by_class_name('jogo__informacoes--local')
        p = div1.find_element_by_class_name('placar')
        man = p.find_element_by_class_name('placar__equipes--mandante')
        placardiv = p.find_element_by_class_name('placar-box')
        pt1 = placardiv.find_element_by_class_name('placar-box__valor--mandante')
        vis = p.find_element_by_class_name('placar__equipes--visitante')
        pt2 = placardiv.find_element_by_class_name('placar-box__valor--visitante')
        checker(man.text,pt1.text,pt2.text,vis.text,lo.text)
    botaodir.click()
    sleep(0.3)

for j in range(38-rod):

    for i in range(10):          
        ul = m.find_element_by_class_name('lista-jogos') 
        lis = ul.find_elements_by_tag_name('li') 
        div1 = lis[i].find_element_by_tag_name('div')
        infjogo = div1.find_element_by_class_name('jogo__informacoes')
        lo = infjogo.find_element_by_class_name('jogo__informacoes--local')
        div11 = div1.find_element_by_class_name('placar')
        man = div11.find_element_by_class_name('placar__equipes--mandante')
        placardiv = div11.find_element_by_class_name('placar-box')
        pt1 = placardiv.find_element_by_class_name('placar-box__valor--mandante')
        pt2 = placardiv.find_element_by_class_name('placar-box__valor--visitante')
        vis = div11.find_element_by_class_name('placar__equipes--visitante')
        checker(man.text,pt1.text,pt2.text,vis.text,lo.text)
    botaodir.click()
    sleep(0.3)
       



jf = np.array([mdt,p1,p2,vi])
jf = jf.transpose()

bdd = np.array([mandante,placart1,placart2,visitante,c])
bdd = bdd.transpose()

teste = pd.DataFrame(bdd, columns = ['Home','X','Y','Visitor','Local'])
teste2 = pd.DataFrame(jf, columns = ['Home','X','Y','Visitor'])

teste.to_csv('bdds.csv',index = False,sep=',')
teste2.to_csv('jf.csv', index = False,sep=',')

print(teste)
print(teste2)
browser.quit()

