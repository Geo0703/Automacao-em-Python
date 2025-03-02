import pyautogui as pt
import time as tm
# Numero que inicia a Seleção de Item
x = 1
# Numero que finaliza seleção de Item
Fim = 100
# Variavel de quantidade de loop (Favor não alterar)
i =0
pt.FAILSAFE = True
pt.hotkey('alt','tab')
while i < Fim:
# Pressione Shift + seta para cima duas vezes

 pt.click(2520,529)
 pt.hotkey('ctrl','c')
 tm.sleep(3)
 pt.click(2312,672)
 pt.hotkey('ctrl','v')
 tm.sleep(2)
 pt.press('enter')
 tm.sleep(3)
 pt.click(2646,391)
 pt.hotkey('ctrl','a')
 pt.press('Backspace')
 pt.hotkey('alt','tab')
 tm.sleep(1)
 pt.hotkey('ctrl','c')
 tm.sleep(1.5)
 pt.hotkey('alt','tab')
 tm.sleep(0.75)
 pt.hotkey('ctrl','v')
 pt.hotkey('alt','tab')
 pt.hotkey('esc')
 pt.hotkey('enter')
 pt.click(2738,562)
 tm.sleep(2)
 pt.click(2362,515)
 pt.hotkey('ctrl','c')
 tm.sleep(3)
 pt.click(2312,672)
 pt.hotkey('ctrl','v')
 tm.sleep(2)
 pt.click(2443,502)
 pt.hotkey('ctrl','c')
 tm.sleep(3)
 pt.click(2312,672)
 pt.hotkey('ctrl','v')
 tm.sleep(2)
 i = i + 1
 x = x + 1
 print(x)