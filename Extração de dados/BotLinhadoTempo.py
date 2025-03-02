import pyautogui as pt
import time as tm
#______________________________________________________________________________#
#Numero que inicia a Seleço de Item
x=1
#Numero que finaliza seleção de Item
Fim=2
#Variavel de quantidade de loop(Favor não alterar)
i=0
#______________________________________________________________________________#
#Novo modo de Segurança(Arrastar o mouse para o canto Superior esquerdo da tela )
pt.FAILSAFE = True
# Abre o Navegadr
pt.hotkey('Win','shift','5')
#abre o OFCWeb
tm.sleep(3)
pt.hotkey('Win','shift','up')
tm.sleep(1)
pt.write('Nome do Site')
pt.press('enter')
#segundo enter para abrir o login GOV
tm.sleep(2)
pt.press('enter')
tm.sleep(2.5)
# click para login gov
pt.click(1302,567)
#coloca CPF e senha
tm.sleep(4)
pt.write('Login')
pt.press('enter')
tm.sleep(6)
pt.write('Senha')
pt.press('enter')
#abre o link da linha do tempo
tm.sleep(8)
pt.hotkey('ctrl','t')
pt.write('Site')
pt.press('enter')
#______________________________________________________________________________#
#Inicio de Loop
while i<Fim:
   #seleciona 1 novo item
    tm.sleep(3)
    pt.click(1703,325)
    pt.press('down', presses=x)
    pt.press('enter')
    tm.sleep(3)
    #clica para consultar
    pt.click(948,430)
    tm.sleep(5)
    #inspecionar tabela
    tm.sleep(4)
    pt.doubleClick(111,569)
    pt.rightClick(111,569)
    pt.click(189,780)
    tm.sleep(2)
    pt.moveTo(1709,425)
    pt.click(1709,425)
    pt.rightClick(1709,425)
    pt.click(1514,576)
   #  pt.click(1744,592)
    pt.click(1903,95)
    tm.sleep(4)
    pt.click(1551,903)
    #Abre excel
    pt.hotkey('win','shift','6')
    tm.sleep(10)
    pt.click(270,211)
    #coloca na planilha
    tm.sleep(7)
    pt.hotkey('ctrl','v')
    tm.sleep(15)
    pt.press('enter')
    #volta para o Ofc web
    pt.hotkey('alt','tab')
    #inspeciona o nome
    tm.sleep(2.5)
    pt.rightClick(328,327)
    tm.sleep(0.75)
    pt.click(464,763)
    tm.sleep(1.15)
    pt.doubleClick(1844,488)
    tm.sleep(0.75)
    #copia o nome
    pt.hotkey('ctrl','c')
    tm.sleep(0.75)
    pt.click(1903,95)
    tm.sleep(0.5)
    #volta para o excel
    pt.hotkey('alt','tab')
    tm.sleep(1)
    #nomeia planilha
    pt.click(235,16)
    tm.sleep(3)
    pt.hotkey('ctrl','v')
    pt.click(931,552)
    tm.sleep(2)
    pt.click(982,961)
    tm.sleep(2)
    pt.click(280,126)
    tm.sleep(2)
    pt.click(593,172)
    tm.sleep(2)
   #  pt.click(618,500)
    tm.sleep(2)
    pt.click(1740,210)
    tm.sleep(2)
    pt.click(1890,20)
    tm.sleep(2)
    #Deleta o item
    pt.click(1703,325)
    pt.press('Backspace')
   #Mostra no Termianl Qual a posição da ultima planilha
    print(x)
    #incrementa 1 para continuar o Loop
    i=i+1
    x=x+1
#______________________________________________________________________#
#alerta de que o loop foi concluido
print("EXtração Concluída " + str(x) + " planilhas no excel")
pt.alert(text='Extração Concluída Temos: '+str(x)+' planilhas no excel',title='Extração finalizada',button="Ok")