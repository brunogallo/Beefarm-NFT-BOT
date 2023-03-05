import msvcrt
import os
import threading
import time
from turtle import onrelease

import pyautogui
import pygetwindow
from interval import Interval
from pynput import keyboard

from colherAlimento import (fApenasMilho, fColherAlimento, fPlantacaoMorta,
                            fPlantarMilho, fVerificarErva, fVerificarMilho)

from colherAnimal import (fVerificarAnimalMorto, fVerificarCoco,
                          fVerificarInjecao, fVerificarMosca, fVerificarOvo,
                          fVerificarPato, fVerificarProducaoAnimal)

from movimentos import (fBuscarJanela, fMoverParaPato, fMovimentoInicial,
                        fVerificarCaptcha, vTelaInicial)

from windows import WindowMgr

def fVerificaKeyPress(): 
    while True:
        with keyboard.Events() as events:
            for event in events: 
                if event.key == keyboard.Key.esc:
                    os._exit(0)
    
def fMain():    
    if (fBuscarJanela() == False):
        exit
            
    pyautogui.FAILSAFE = False

    def fIniciar():
        jaLogado = pyautogui.locateOnScreen("logado.png", confidence=0.75)
        if jaLogado != None:
            confirm = pyautogui.locateOnScreen("confirmar.png", confidence=0.75)
            if confirm != None:
                pyautogui.click(confirm, duration=0.6)
                print("confirm")
        
        entrar = pyautogui.locateOnScreen("comecar.png", confidence=0.75)
        if entrar != None:
            pyautogui.click(entrar, duration=0.6)

            while True:
                c1 = pyautogui.locateOnScreen("pergunta.png", confidence=0.6)
                if c1 != None:
                    resposta = pyautogui.locateOnScreen("captcha.png", confidence=0.6)
                    pyautogui.sleep(0.61)
                    if (resposta != None):
                        pyautogui.click(545, 565, duration=0.7)

                c2 = pyautogui.locateOnScreen("mais-uma-vez.png", confidence=0.75)
                pyautogui.sleep(0.77)
                if c2 != None:
                    pyautogui.click(c2, duration=0.3)

                confirm = pyautogui.locateOnScreen("confirmar.png", confidence=0.75)
                pyautogui.sleep(0.77)
                if confirm != None:
                    pyautogui.click(confirm, duration=1)
                    print("confirm")
                    break
                
        
        while True:
            if (vTelaInicial() == False):
                fIniciar() 
            
            if (fVerificarCaptcha()):
                fIniciar();
                    
            fMovimentoInicial()
            fColherAlimento()
            fVerificarMilho()
            fVerificarErva()
            fPlantacaoMorta()
            fMoverParaPato()
            fVerificarPato()
            fVerificarOvo()
            fVerificarProducaoAnimal()
            fVerificarCoco()
            fVerificarInjecao()
            fVerificarMosca()
            fVerificarAnimalMorto() 
            
            pyautogui.sleep(2)
            
                
    fIniciar()
    
def fVerificarMouse():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
    
threading.Thread(target=fVerificaKeyPress).start()
threading.Thread(target=fVerificarMouse).start()
threading.Thread(target=fMain).start()