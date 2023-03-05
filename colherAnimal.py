import time

import pyautogui
import pygetwindow
from interval import Interval


def fVerificarPato():
    while True:
        pato = pyautogui.locateOnScreen("pato.png", confidence=0.75)
        if pato != None:
        # for pato in pyautogui.locateOnScreen("pato.png", confidence=0.75):
            pyautogui.click(pato, duration=0.3)

            time.sleep(2)

            pa = pyautogui.locateOnScreen("pa.png", confidence=0.75)
            if pa != None:
                pyautogui.moveTo(pa, duration=0.3)
                pyautogui.mouseDown()
                pyautogui.move(0, 150, duration=0.3)
                pyautogui.mouseUp()
                time.sleep(1.5)
            
            # fVerificarAnimalMorto() 
        else:
            patoMorto = pyautogui.locateOnScreen("patoMorto2.png", confidence=0.75)
            if patoMorto != None:
                pyautogui.click(patoMorto, duration=0.3)

                time.sleep(2)

                pa = pyautogui.locateOnScreen("pa.png", confidence=0.75)
                if pa != None:
                    pyautogui.moveTo(pa, duration=0.3)
                    
                        # pyautogui.dragTo(0, 80, duration=0.6)
                    pyautogui.mouseDown()
                    pyautogui.move(0, 150, duration=0.3)
                    # pyautogui.move(400, 30, duration=0.3)
                    pyautogui.mouseUp()
                    time.sleep(1.5)    
                # fVerificarAnimalMorto()     
            else:
                pyautogui.mouseUp()
                pyautogui.moveTo(510, 670, duration=0.5)
                break
        
            
def fVerificarOvo():
    while True:
        egg = pyautogui.locateCenterOnScreen("egg.png", confidence=0.75)
        if egg == None:
            time.sleep(0.75)
            pyautogui.scroll(100)
            egg = pyautogui.locateCenterOnScreen("egg.png", confidence=0.75)
            time.sleep(0.75)
            pyautogui.scroll(-100)
        if egg != None:
            pyautogui.click(egg, duration=0.35)
            time.sleep(1)

            colher = pyautogui.locateOnScreen("colher.png", confidence=0.75)
            if colher != None:
                pyautogui.moveTo(colher, duration=0.3)
                pyautogui.drag(0, 200, duration=0.3)
                
                time.sleep(2)
                centroPato = pyautogui.locateCenterOnScreen("centroPato.png", confidence=0.75)
                if centroPato != None:
                    pyautogui.moveTo(centroPato, duration=0.3)
                    pyautogui.click()

                # pyautogui.click(686, 601, duration=0.3)
                um_dois = pyautogui.locateCenterOnScreen("1_2.png", confidence=0.75)
                if um_dois != None:
                    pyautogui.moveTo(616, 896, duration=0.3)
                    time.sleep(0.5)
                    pyautogui.mouseDown()
                    time.sleep(0.5)
                    pyautogui.moveTo(761, 616, duration=0.3)
                    time.sleep(0.5)
                    pyautogui.mouseUp()
        else: 
            pyautogui.mouseUp()
            time.sleep(1)
            break
        
        
def fVerificarProducaoAnimal(animal):
    while True:
        produto = pyautogui.locateCenterOnScreen(animal, confidence=0.75)
        if produto == None:
            time.sleep(0.75)
            pyautogui.scroll(100)
            produto = pyautogui.locateCenterOnScreen(animal, confidence=0.75)
            time.sleep(0.75)
            pyautogui.scroll(-100)
        if produto != None:
            pyautogui.click(produto, duration=0.35)
            time.sleep(1)

            colher = pyautogui.locateOnScreen("colher.png", confidence=0.75)
            if colher != None:
                pyautogui.moveTo(colher, duration=0.3)
                pyautogui.drag(0, 200, duration=0.3)
                
                time.sleep(2)
                fSairDoPato()
                
        else: 
            pyautogui.mouseUp()
            time.sleep(1)
            break
        
def fSairDoPato():
    centroPato = pyautogui.locateCenterOnScreen("centroPato.png", confidence=0.75)
    if centroPato != None:
        pyautogui.moveTo(centroPato, duration=0.3)
        pyautogui.click()

    # pyautogui.click(686, 601, duration=0.3)
    um_dois = pyautogui.locateCenterOnScreen("1_2.png", confidence=0.75)
    if um_dois != None:
        pyautogui.moveTo(616, 896, duration=0.3)
        time.sleep(0.5)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.moveTo(761, 616, duration=0.3)
        time.sleep(0.5)
        pyautogui.mouseUp()
        
def fVerificarInjecao():
    while True:
        injecao = pyautogui.locateCenterOnScreen("injecao.png", confidence=0.75)
        pyautogui.sleep(1)
        if injecao == None:
            injecao = pyautogui.locateCenterOnScreen("injecaoMini.png", confidence=0.75)
            if injecao == None:
                pyautogui.mouseUp()
                time.sleep(1)
                break
        pyautogui.moveTo(injecao)
        pyautogui.move(40,60,0.3)
        pyautogui.click()
        time.sleep(1)

        injecao2 = pyautogui.locateOnScreen("injecao2.png", confidence=0.75)
        if injecao2 != None:
            pyautogui.moveTo(injecao2, duration=0.3)
            pyautogui.drag(injecao, duration=0.3)
            pyautogui.drag(40, 60, duration=0.3)
        
        
def fVerificarCoco():
    while True:
        coco = pyautogui.locateCenterOnScreen("coco2.PNG", confidence=0.75)
        pyautogui.sleep(1)
        if coco == None:
            coco = pyautogui.locateCenterOnScreen("coco.PNG", confidence=0.75)
            if coco == None:
                pyautogui.mouseUp()
                time.sleep(1)
                break
        pyautogui.moveTo(coco)
        pyautogui.move(40,60,0.3)
        pyautogui.click()
        time.sleep(2)

        limpar = pyautogui.locateOnScreen("limparCoco.PNG", confidence=0.75)
        if limpar != None:
            pyautogui.moveTo(limpar, duration=0.3)
            pyautogui.mouseDown()
            pyautogui.moveTo(coco, duration=0.3)
            pyautogui.move(40, 60, duration=0.3)
            pyautogui.mouseUp()
            
        
def fVerificarMosca():
    while True:
        mosca = pyautogui.locateCenterOnScreen("mosca.png", confidence=0.75)
        pyautogui.sleep(0.8)
        if mosca == None:
            mosca = pyautogui.locateCenterOnScreen("mosca2.png", confidence=0.75)
            if mosca == None:
                pyautogui.mouseUp()
                time.sleep(1)
                break
        pyautogui.moveTo(mosca)
        pyautogui.move(40,60,0.3)
        pyautogui.click()
        time.sleep(1)

        mataMosca = pyautogui.locateOnScreen("mataMosca.png", confidence=0.75)
        if mataMosca != None:
            pyautogui.moveTo(mataMosca, duration=0.3)
            pyautogui.drag(mosca, duration=0.3)
            pyautogui.drag(40, 60, duration=0.3)

        
def fMoverProCentroPato():
    centroPato = pyautogui.locateCenterOnScreen("centroPato2.png", confidence=0.75)
    if centroPato != None:
        pyautogui.moveTo(centroPato, duration=0.3)
        pyautogui.click()
        
        
def fVerificarAnimalMorto():
    
    Zz = pyautogui.locateOnScreen("Zz.png", confidence=0.7)
    if (Zz == None):
        return
    
    pontoPato = pyautogui.locateOnScreen("pontoPato.png", confidence=0.75)
    pyautogui.sleep(0.8)
    # pato_compra = pyautogui.locateOnScreen("pato_compra.png", confidence=0.7)
    if pontoPato != None:
        pyautogui.moveTo(pontoPato, duration=0.4)
        pyautogui.move(-40,-300,0.4)
        pyautogui.click()
        time.sleep(1)

        comprarPato = pyautogui.locateOnScreen("comprarPato2.PNG", confidence=0.75)
        pyautogui.sleep(1.2)
        if comprarPato != None:
            coelho = pyautogui.locateOnScreen("coelho.png", confidence=0.7)
            if coelho != None:            
                pyautogui.moveTo(coelho, duration=0.3)
                pyautogui.drag(310,0,0.5)
                pyautogui.mouseUp()                
            
            pato_compra = pyautogui.locateOnScreen("pato_compra.png", confidence=0.7)
            if pato_compra != None:            
                pyautogui.moveTo(pato_compra, duration=0.3)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.move(50, -250)
                time.sleep(3)
                pyautogui.move(100, 200)
                time.sleep(3)
                pyautogui.move(-100, -200)
                # pyautogui.moveTo(736, 581, duration=0.3)
                # pyautogui.moveTo(780, 530, duration=0.3)
                time.sleep(2)
        pyautogui.mouseUp
        fMoverProCentroPato()
    else: 
        fMoverProCentroPato()
