#Bibliotecas usadas
import pyautogui
import keyboard
import mouse
import time

print("""
Para obter as coordenadas X e Y de um clique do mouse, basta clicar com o botão esquerdo ou direito no local desejado. 
Se precisar de um clique duplo, pressione "2" antes de clicar. Para escrever texto, pressione "e" e comece a digitar. 
Para adicionar um comentário, pressione "/" e escreva o comentário. 
Para parar, pressione "=". Simples assim!""")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if keyboard.is_pressed('='):
            print("""
Programa encerrado.
Feito por: Geovane Augusto
Git:Geo0703""")
            break
        #Se apertar com o botão esquerdo do mouse aparece a posição
        if mouse.is_pressed("left"):
            time.sleep(0.25)
            x, y = pyautogui.position()
            print(f'pyautogui.click({x},{y})')
        #Se apertar com o botão direito do mouse aparece a posição
        if mouse.is_pressed("right"):
            time.sleep(0.25)
            x, y = pyautogui.position()
            print(f'pyautogui.rightClick({x},{y})')
        #Se apertar o 2 com o mouse em cima da onde deseja aparece a posição
        if keyboard.is_pressed("2"):
            time.sleep(0.25)
            x, y = pyautogui.position()
            print(f'pyautogui.doubleClick({x},{y})')
        #se apertar "e" e digitar no terminal ele imprimi o texto
        if keyboard.is_pressed('e'):
            A= input("#O que deseja escrever ")
            print('pyautogui.write('+A+')')
        #se apertar "/" e digitar no terminal ele imprimi o comentário
        if keyboard.is_pressed('/'):
            B=input('#Faça seu comentário')
            print("# ",B)
except KeyboardInterrupt:
    print("""
Programa encerrado.
Feito por: Geovane Augusto
Git:Geo0703""")
