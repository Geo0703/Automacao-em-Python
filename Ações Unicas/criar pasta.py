import pyautogui as pt
import time as tm

# Numero que inicia a Seleção de Item
x = 1
# Numero que finaliza seleção de Item
Fim = 100
# Variavel de quantidade de loop (Favor não alterar)
i = 0
pt.FAILSAFE = True
pt.hotkey("alt", "tab")
while i < Fim:
    #tira o selecionado
    pt.press('esc')
    tm.sleep(2)
    #passa para o Próximo
    pt.press('enter')
    tm.sleep(2)
    #copia o Próximo
    pt.hotkey("ctrl", "c")
    tm.sleep(2)
    #Vai Para tela do Drive
    pt.hotkey("ctrl", "tab")
    tm.sleep(2)
    #Clicks para Criar pasta 
    pt.click(100, 180)
    tm.sleep(2)
    pt.click(189, 228)
    tm.sleep(2)
    #Cola o nome do copiado da Planilha
    pt.hotkey("ctrl", "v")
    tm.sleep(2)
    #Cria Pasta
    pt.press('enter')
    tm.sleep(2)
    #Volta Para Planilha
    pt.hotkey("ctrl", "tab")
    tm.sleep(1)
    #Incrementa
    i = i + 1
    x = x + 1
    print(x)