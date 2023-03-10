import pyautogui
from time import sleep
#### Para a execução desse programa, é necessário que o VsCode esteja em primeiro plano
#1 - Procura o botão start debugging
debug_button = pyautogui.locateOnScreen('playdebugbtn.png',confidence=0.9)
if debug_button:
   debug_button_center = pyautogui.center(debug_button)
   pyautogui.click(debug_button_center, duration=0.5)
else:
#2 - Se não encontrar, clicar no botão run and debug e start debugging
    run_debug = pyautogui.locateOnScreen('run_debug.png',confidence=0.9)
    if run_debug:
        run_debug_center = pyautogui.center(run_debug)
        pyautogui.click(run_debug_center, duration=0.5)
        sleep(0.2)
        debug_button = pyautogui.locateOnScreen('playdebugbtn.png',confidence=0.9)
        debug_button_center = pyautogui.center(debug_button)
        pyautogui.click(debug_button_center, duration=0.5)
    else:
        print("botão não encontrado1.")
        exit()
#3 - Seleciona o ambiente SIGAADV
sleep(0.5)
sigaadv = pyautogui.locateOnScreen('sigaadv.png')
if sigaadv == None:
    sigaadv = pyautogui.locateOnScreen('sigaadv2.png')
    
sigaadv_center = pyautogui.center(sigaadv)
pyautogui.click(sigaadv_center,duration=0.5)
#4 - Espera o protheus abrir
login = pyautogui.locateOnScreen("tela_login.png",grayscale=True,confidence=0.9)
while login == None:
    sleep(1)
    login = pyautogui.locateOnScreen("tela_login.png",grayscale=True,confidence=0.9)

pyautogui.click(login.height+45,login.top+272,duration=0.5)
#5 - escreve o usuário e senha
pyautogui.hotkey('home')
pyautogui.typewrite('003979',interval=0.10) #escreve o usuário
pyautogui.hotkey('tab') #passa para o próximo campo
sleep(0.5)
pyautogui.typewrite('Rdg012023',interval=0.10) #preenche a senha

entrar = pyautogui.locateOnScreen("entrar_button.png",grayscale=True,confidence=0.9)
entrar_center = pyautogui.center(entrar)
pyautogui.doubleClick(entrar_center,duration=0.5)
pyautogui.doubleClick(entrar_center,duration=0.5)

#6 - seleciona a empresa e filial
environment = pyautogui.locateOnScreen("select_env.png",grayscale=True,confidence=0.9)
while environment == None:
    sleep(1)
    environment = pyautogui.locateOnScreen("select_env.png",grayscale=True,confidence=0.9)

sleep(0.5)
pyautogui.click(environment.left+10,environment.top+30,duration=0.5) #clica no campo de empresa
pyautogui.typewrite('03',interval=0.10)
pyautogui.hotkey('tab') #passa para o próximo campo
pyautogui.typewrite('98')
sleep(1)
entrar = pyautogui.locateOnScreen("entrar_button.png",grayscale=True,confidence=0.9)
entrar_center = pyautogui.center(entrar)
pyautogui.doubleClick(entrar_center,duration=0.5)
