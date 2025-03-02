import pyautogui as pt
import keyboard as kd
import time as tm
#_____________#
#Váriavel do Laço
I1 = 0
F1 = 19
I2 = 0
F2 = 4
I3 = 0
F3 = 11
#_____________#
#Váriavel de click
click1 = 473
click2 = 365
click3 = 426
#_____________#
#Novo modo de Segurança(Arrastar o mouse para o canto Superior esquerdo da tela )
pt.FAILSAFE = True
# Abre o Navegadr
pt.hotkey('Win','shift','5')
#abre o OFCWeb
tm.sleep(3)
pt.hotkey('Win','shift','up')
tm.sleep(1)
pt.write('https://homo-gcweb.prevnet/')
pt.press('enter')
tm.sleep(10)
#rola até o campo de despera
pt.moveTo(890,400)
pt.scroll(-520)
tm.sleep(2)
#Laços do Filtro de despesas
while I1<F1:
    #abre o link da despesa
    pt.click(888,click1)
    tm.sleep(3)
    #abre o filtro de contratos
    while I2<F3:
        tm.sleep(3)
        pt.click(1796,click2)
        tm.sleep(2)
        pt.scroll(-2350)
        I2=I2+1
        click2= click2 + 43
        #
        while I3<=F3:
            tm.sleep(1)
            #Click do rateio
            pt.click(1716,click3)
            tm.sleep(2)
            #Inspecionar
            pt.rightClick(943,313)
            tm.sleep(1.25)
            pt.click(1055,749)
            tm.sleep(1.25)
            pt.rightClick(1509,682)
            tm.sleep(1.25)
            pt.click(1600,300)
            tm.sleep(1.25)
            pt.click(1452,345)
            tm.sleep(1.25)
            pt.click(1904,103)
            
            #À definir como salvar e onde salvar os rateios!
            
            #Fecha o Rateio
            tm.sleep(3)
            pt.click(1788,279)
            print(I3)
            I3= I3+1
            click3= click3 +43
        I3 = 0
        click3 = 426
        pt.click(17,63) 
    #fecha a guia
    pt.click(492,21)
    tm.sleep(3)
    I1=I1+1
    click1=click1+27