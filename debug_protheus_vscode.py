import pyautogui
from time import sleep
#### Para a execução desse programa, é necessário que o VsCode esteja em primeiro plano
#1 - Procura o botão start debugging
debug_button = pyautogui.locateOnScreen('playdebugbtn.png',confidence=0.9)
if debug_button:
   debug_button_center = pyautogui.center(debug_button)
   pyautogui.click(debug_button_center, duration=0.3)
else:
#2 - Se não encontrar, clicar no botão run and debug e start debugging
    run_debug = pyautogui.locateOnScreen('run_debug.png',confidence=0.9)
    if run_debug:
        run_debug_center = pyautogui.center(run_debug)
        pyautogui.click(run_debug_center, duration=0.3)
        sleep(0.2)
        debug_button = pyautogui.locateOnScreen('playdebugbtn.png',confidence=0.9)
        debug_button_center = pyautogui.center(debug_button)
        pyautogui.click(debug_button_center, duration=0.3)
    else:
        print("botão não encontrado1.")
        exit()
#3 - Seleciona o ambiente SIGAADV
sleep(0.5)
sigaadv = pyautogui.locateOnScreen('sigaadv.png')
if sigaadv == None:
    sigaadv = pyautogui.locateOnScreen('sigaadv2.png')
    
sigaadv_center = pyautogui.center(sigaadv)
pyautogui.click(sigaadv_center,duration=0.3)
#4 - Espera o protheus abrir
login = pyautogui.locateOnScreen("tela_login.png",grayscale=True,confidence=0.9)
while login == None:
    sleep(0.2)
    login = pyautogui.locateOnScreen("tela_login.png",grayscale=True,confidence=0.9)

pyautogui.click(login.height+45,login.top+272,duration=0.5)
#5 - escreve o usuário e senha
pyautogui.hotkey('home')
pyautogui.typewrite('003979',interval=0.10) #escreve o usuário
pyautogui.hotkey('tab') #passa para o próximo campo
sleep(0.3)
pyautogui.typewrite('Rdg012023',interval=0.10) #preenche a senha

entrar = pyautogui.locateOnScreen("entrar_button.png",grayscale=True,confidence=0.9)
entrar_center = pyautogui.center(entrar)
pyautogui.doubleClick(entrar_center,duration=0.3)
sleep(1)
pyautogui.doubleClick(entrar_center,duration=0.3)

#6 - seleciona a empresa e filial
environment = pyautogui.locateOnScreen("select_env.png",grayscale=True,confidence=0.9)
while environment == None:
    sleep(0.3)
    environment = pyautogui.locateOnScreen("select_env.png",grayscale=True,confidence=0.9)

#pyautogui.click(environment.left,environment.top,duration=0.5)
#pyautogui.click(environment.left+12,environment.top+32,duration=0.5) #clica no campo de empresa
pyautogui.hotkey('tab') #passa para o próximo campo
pyautogui.typewrite('03',interval=0.10)
pyautogui.hotkey('tab') #passa para o próximo campo
pyautogui.typewrite('98')
sleep(1)
entrar = pyautogui.locateOnScreen("entrar_button.png",grayscale=True,confidence=0.9)
entrar_center = pyautogui.center(entrar)
pyautogui.doubleClick(entrar_center,duration=0.3)
sleep(1)
pyautogui.doubleClick(entrar_center,duration=0.3)

#clica no botão Atualizações no menu lateral
atualizacoes = pyautogui.locateOnScreen("atualizacoes.png",grayscale=True,confidence=0.9)
while atualizacoes == None:
    sleep(1)
    atualizacoes = pyautogui.locateOnScreen("atualizacoes.png",grayscale=True,confidence=0.9)

atualizacoes_center = pyautogui.center(atualizacoes)
pyautogui.click(atualizacoes_center,duration=0.5)
sleep(0.5)
#clica no botão Gestao de Acessos Gps no menu lateral
gestao_acesso = pyautogui.locateOnScreen("gestao_de_acessos.png",grayscale=True,confidence=0.9)
gestao_acesso_center = pyautogui.center(gestao_acesso)
pyautogui.click(gestao_acesso_center,duration=0.5)
pyautogui.click(gestao_acesso_center,duration=0.5)
sleep(0.5)
#clica no botão Gestao de Acessos Gps no menu lateral
formulas_gps = pyautogui.locateOnScreen("formulas_gps.png",grayscale=True,confidence=0.9)
formulas_gps_center = pyautogui.center(formulas_gps)
pyautogui.click(formulas_gps_center,duration=0.5)
pyautogui.click(formulas_gps_center,duration=0.5)
