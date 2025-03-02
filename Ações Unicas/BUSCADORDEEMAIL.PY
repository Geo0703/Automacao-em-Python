import pyautogui as pt
import time as tm
#Numero que inicia a Seleço de Item
x=1
#Numero que finaliza seleção de Item
Fim=191
#Variavel de quantidade de loop(Favor não alterar)
i=0
#Novo modo de Segurança(Arrastar o mouse para o canto Superior esquerdo da tela )
pt.FAILSAFE = True
#Inicio de Loop

tm.sleep(2)
pt.hotkey('alt','tab')
tm.sleep(1)
while i<Fim:
    pt.hotkey('ctrl','c')
    tm.sleep(0.5)
    pt.click(2409,98)
    tm.sleep(0.75)
    pt.hotkey('ctrl','v')
    tm.sleep(1.5)
    pt.click(2397,224)
    tm.sleep(1.5)
    pt.click(2408,152)
    tm.sleep(1.75)
    pt.click(2439,547)
    tm.sleep(2)
    pt.click(2990,150)
    pt.tripleClick(2535,92)
    tm.sleep(1.75)
    pt.press('delete')
    tm.sleep(2)
    pt.click(970,16)
    tm.sleep(1.75)
    pt.hotkey('esc')
    tm.sleep(0.5)
    pt.hotkey('tab')
    tm.sleep(1.75)
    pt.hotkey('ctrl','v')
    tm.sleep(1.75)
    pt.hotkey('esc')
    tm.sleep(1.75)
    pt.press('left')
    pt.press('enter')
    #Mostra no Termianl Qual a posição da ultima planilha
    print(x)
    #incrementa 1 para continuar o Loop
    i=i+1
    x=x+1