import pyautogui as pt
import keyboard as kd
import time as tm

print('Pressione "1" para obter as coordenadas X e Y de um click, "2" para double click, "3" para botão direito, "e" para escrever um texto e "/" para fazer o comentario. Pressione = para parar.')

try:
    while True:
        x, y = pt.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if kd.is_pressed('='):
            print("""
Programa encerrado.
Feito por: Geovane Augusto
Git:Geo0703""")
            break
        if kd.is_pressed('1'):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.click({x},{y})')
        if kd.is_pressed('2'):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.doubleClick({x},{y})')
        if kd.is_pressed('3'):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.rightClick({x},{y})')
        if kd.is_pressed('e'):
            A= input("#O que deseja escrever ")
            print("pt.write('"+A+"')")
        if kd.is_pressed('/'):
            B=input('#Faça seu comentario')
            print("#",B)
except KeyboardInterrupt:
    print("""
Programa encerrado.
Feito por: Geovane Augusto
Git:Geo0703""")
    
