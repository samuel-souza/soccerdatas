from selenium import webdriver
from time import sleep 
import pandas as pd 
import numpy as np
import os 


url = 'https://globoesporte.globo.com/futebol/brasileirao-serie-a/'
driver = './python'
dir(driver)
browser = webdriver.Firefox()
browser.get(url)

browser.maximize_window()

m = browser.find_element_by_tag_name('main')
r = m.find_element_by_class_name('lista-jogos__navegacao--rodada')
rod = int(r.text.split()[0].replace('ª','')) 

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
    ['FLA','MARACANÃ'],
    ['BOT','NILTON SANTOS (ENGENHÃO)'],
    ['FLU','LARANJEIRAS'],
    ['VAS','SÃO JANUÁRIO'],
    ['FOR','CASTELÃO (CE)'],
    ['CFC','COUTO PEREIRA'],
    ['SPT','ILHA DO RETIRO'],
    ['SAN','VILA BELMIRO'],
    ['GRE','ARENA DO GRÊMIO'],
    ['COR','NEO QUÍMICA ARENA'],
    ['GOI','SERRINHA'],
    ['PAL','ALLIANZ PARQUE'],
    ['BGT','NABI ABI CHEDID'],
    ['CAM','MINEIRÃO'],
    ['CAP','ARENA DA BAIXADA'],
    ['BAH','ITAIPAVA ARENA FONTE NOVA'],
    ['ACG','ANTÔNIO ACCIOLY'],
    ['CEA','CASTELÃO (CE)'],
    ['SAO','MORUMBI'],
    ['INT','BEIRA-RIO']
]


botoes = browser.find_element_by_class_name('lista-jogos__navegacao')
botaodir = botoes.find_element_by_class_name('lista-jogos__navegacao--seta-direita')

botoes = browser.find_element_by_class_name('lista-jogos__navegacao')
botaoesq = botoes.find_element_by_class_name('lista-jogos__navegacao--seta-esquerda')


if rod >1:

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
        try:
            ul = m.find_element_by_class_name('lista-jogos') 
            lis = ul.find_elements_by_tag_name('li') 
            div1 = lis[i].find_element_by_class_name('jogo__transmissao--link')
            infjogo = div1.find_element_by_class_name('jogo__informacoes')
            lo = infjogo.find_element_by_class_name('jogo__informacoes--local')
            p = div1.find_element_by_class_name('placar')
            man = p.find_element_by_class_name('placar__equipes--mandante')
            placardiv = p.find_element_by_class_name('placar-box')
            pt1 = placardiv.find_element_by_class_name('placar-box__valor--mandante')
            vis = p.find_element_by_class_name('placar__equipes--visitante')
            pt2 = placardiv.find_element_by_class_name('placar-box__valor--visitante')
            checker(man.text,pt1.text,pt2.text,vis.text,lo.text)
        except: 
            break

    botaodir.click()
    sleep(0.5)

for j in range(38-rod):

    for i in range(10):
        try:          
            ul = m.find_element_by_class_name('lista-jogos') 
            lis = ul.find_elements_by_tag_name('li') 
            div1 = lis[i].find_element_by_class_name('jogo__transmissao--link')
            infjogo = div1.find_element_by_class_name('jogo__informacoes')
            lo = infjogo.find_element_by_class_name('jogo__informacoes--local')
            div11 = div1.find_element_by_class_name('placar')
            man = div11.find_element_by_class_name('placar__equipes--mandante')
            placardiv = div11.find_element_by_class_name('placar-box')
            pt1 = placardiv.find_element_by_class_name('placar-box__valor--mandante')
            pt2 = placardiv.find_element_by_class_name('placar-box__valor--visitante')
            vis = div11.find_element_by_class_name('placar__equipes--visitante')
            checker(man.text,pt1.text,pt2.text,vis.text,lo.text)
        except:
            break
    botaodir.click()
    sleep(0.5)

fm = np.array([mdt,p1,p2,vi])
fm = fm.transpose() 
future_matches = pd.DataFrame(fm, columns = ['Home','X','Y','Visitor'])
future_matches.to_csv('fmatches.csv', index = False)

dtb = np.array([mandante,placart1,placart2,visitante,c])
dtb = dtb.transpose()
database = pd.DataFrame(dtb, columns = ['Home','X','Y','Visitor','Local'])
database.to_csv('dtbase.csv',index = False)   

browser.quit()
