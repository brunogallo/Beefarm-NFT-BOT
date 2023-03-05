import math
import time
import pyautogui
import pygetwindow
from interval import Interval


def fMovimentoInicial():
    pyautogui.moveTo(1100, 900, duration=0.3)
    pyautogui.click()
    for i in range(20):
        pyautogui.scroll(-100)
    pyautogui.sleep(1)
        
    for i in range(3):
        pyautogui.moveTo(900, 900, duration=0.3)        
        pyautogui.dragTo(10, 10, duration=0.3)
        pyautogui.sleep(0.5)

    for i in range(2):
        pyautogui.moveTo(216, 569, duration=0.3)
        pyautogui.dragTo(1000, 1100, duration=0.3)
        pyautogui.sleep(0.5)

    
    centro = pyautogui.locateOnScreen("centro.png", confidence=0.75)
    if centro != None:
        pyautogui.moveTo(centro, duration=0.3)
        pyautogui.drag(-100, 256, duration=0.3)
    
    pyautogui.keyUp

def fMoverParaPato():
    pyautogui.mouseUp()
    pyautogui.mouseUp()

    time.sleep(1)
    captcha = pyautogui.locateOnScreen("centro.png", confidence=0.75)
    if captcha != None:
        pyautogui.moveTo(captcha, duration=0.3)
        pyautogui.dragTo(1259, 256, duration=0.3)

    time.sleep(1)


def fVerificarCaptcha():
    captcha = pyautogui.locateOnScreen("captcha.png", confidence=0.75)
    time.sleep(0.77)
    if captcha != None:
        refresh = pyautogui.locateOnScreen("refreshPage.png", confidence=0.75)
        if refresh != None:
            pyautogui.click(refresh, duration=0.4)
            pyautogui.press('enter')
            time.sleep(25)
            return True       
        
def vTelaInicial():
    captcha = pyautogui.locateOnScreen("telaInicial.png", confidence=0.75)
    if captcha == None:
        return False

def fRotacao(posicaoX, posicaoY):
    R = 40
    (x,y) = pyautogui.size()
    (X,Y) = pyautogui.position(posicaoX,posicaoY)


    pyautogui.moveTo(X,R+Y)
    pyautogui.mouseDown();
    for i in range(180):  
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
    pyautogui.mouseUp()
    
def fBuscarJanela():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')    
    pyautogui.keyUp('alt')
    try:
        win = pygetwindow.getWindowsWithTitle('Cocos Creator | farm')[0]
        if win != None:
            fTamanhoTela(win)        
            win.moveTo(-6, 0)
            win.activate()
            return True
        else:
            return False
    except:
            win = pygetwindow.getWindowsWithTitle('Conexão de Área de Trabalho Remota')[0]
                if win != None:
                    return True
                else:
                    return False

def fTela():
    tamanho = pyautogui.size() 
    if tamanho == (1920,1080):
        return 1920
    else:
        return 1366

def fTamanhoTela(win):
    if (fTela() == 1920):
        win.size=(1548, 1049)
    else:
        win.size=(1250, 690)
