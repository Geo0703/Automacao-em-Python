import pyautogui as pt
import keyboard as kd
import mouse as ms
import time as tm
ms.is_pressed("LEFT")
print("""
Para obter as coordenadas X e Y de um clique do mouse, basta clicar com o botão esquerdo ou direito no local desejado. 
Se precisar de um clique duplo, pressione "2" antes de clicar. Para escrever texto, pressione "e" e comece a digitar. 
Para adicionar um comentário, pressione "/" e escreva o comentário. 
Para parar, pressione "=". Simples assim!""")

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
        if ms.is_pressed("left"):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.click({x},{y})')
        if ms.is_pressed("right"):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.rightClick({x},{y})')
        if kd.is_pressed("2"):
            tm.sleep(0.25)
            x, y = pt.position()
            print(f'pt.doubleClick({x},{y})')
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
