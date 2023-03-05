import time
import pyautogui
import pygetwindow
from interval import Interval
from movimentos import fMovimentoInicial, fRotacao

def fColherAlimento():
    x = 0;
    while True: 
        milho = pyautogui.locateOnScreen("milho.png", confidence=0.75)
        if milho != None:
            x = 1
            x_milho, y_milho = pyautogui.center(milho)

            pyautogui.moveTo(x_milho, y_milho + 50, duration=0.6)
            pyautogui.click(x_milho, y_milho + 50, duration=0.6)
            
            top1 = pyautogui.locateOnScreen("top1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            top2 = pyautogui.locateOnScreen("top2Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot1 = pyautogui.locateOnScreen("bot1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot2 = pyautogui.locateOnScreen("bot2Plantacao.png", confidence=0.75)
            time.sleep(0.8)

            colher = pyautogui.locateOnScreen("colher.png", confidence=0.75)
            if colher != None:
                pyautogui.moveTo(colher, duration=0.3)
                fRotacao(x_milho, y_milho)
                pyautogui.mouseDown()
                pyautogui.moveTo(top1, duration=0.3)
                pyautogui.moveTo(bot1, duration=0.3)
                pyautogui.moveTo(bot2, duration=0.3)
                pyautogui.moveTo(top2, duration=0.3)
                pyautogui.move(0, 140, duration=0.2)
                pyautogui.move(400, 160, duration=0.2)
                pyautogui.move(-130, 80, duration=0.2)
                pyautogui.move(-600, -150, duration=0.2)
                pyautogui.move(940, 604, duration=1)
                pyautogui.mouseUp()
                pyautogui.drag(0, 160, duration=0.4)
            
            pyautogui.mouseUp()
            
        else:
                if(x > 0):
                    centroPlantacao = pyautogui.locateOnScreen("centroPlantacao.png", confidence=0.75)
                    if centroPlantacao != None:
                        pyautogui.moveTo(centroPlantacao, duration=0.3)
                        pyautogui.drag(0, -200, duration=0.4)
                        pyautogui.mouseUp()
            break
        
def fColherAlimento(tipo):
    x = 0;
    while True: 
        comida = pyautogui.locateOnScreen(tipo, confidence=0.75)
        if comida != None:
            x = 1
            x_comida, y_comida = pyautogui.center(comida)

            pyautogui.moveTo(x_comida, y_comida + 50, duration=0.6)
            pyautogui.click(x_comida, y_comida + 50, duration=0.6)
            
            top1 = pyautogui.locateOnScreen("top1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            top2 = pyautogui.locateOnScreen("top2Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot1 = pyautogui.locateOnScreen("bot1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot2 = pyautogui.locateOnScreen("bot2Plantacao.png", confidence=0.75)
            time.sleep(0.8)

            colher = pyautogui.locateOnScreen("colher.png", confidence=0.75)
            if colher != None:
                pyautogui.moveTo(colher, duration=0.3)
                pyautogui.mouseDown()
                pyautogui.moveTo(top1, duration=0.3)
                pyautogui.moveTo(bot1, duration=0.3)
                pyautogui.moveTo(bot2, duration=0.3)
                pyautogui.moveTo(top2, duration=0.3)
                pyautogui.mouseUp()

            pyautogui.mouseUp()
            
        else:
            if(x > 0):
                centroPlantacao = pyautogui.locateOnScreen("centroPlantacao.png", confidence=0.75)
                if centroPlantacao != None:
                    pyautogui.moveTo(centroPlantacao, duration=0.3)
                    pyautogui.drag(0, -200, duration=0.4)
                    pyautogui.mouseUp()
            break
        
def fApenasMilho():
    centroPlantacao = pyautogui.locateOnScreen("centroPlantacao.png", confidence=0.75)
    if centroPlantacao != None:
        pyautogui.moveTo(centroPlantacao, duration=0.3)
        pyautogui.drag(0, 200, duration=0.4)
        pyautogui.mouseUp()

def fPlantacaoMorta():
    while True: 
        milho_morto = pyautogui.locateOnScreen("milho_morto.png", confidence=0.75)
        if milho_morto != None:
            pyautogui.click(milho_morto, duration=0.38)
            print("milho morto")
            top1 = pyautogui.locateOnScreen("top1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            top2 = pyautogui.locateOnScreen("top2Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot1 = pyautogui.locateOnScreen("bot1Plantacao.png", confidence=0.75)
            time.sleep(0.8)
            bot2 = pyautogui.locateOnScreen("bot2Plantacao.png", confidence=0.75)
            time.sleep(0.8)

            pa = pyautogui.locateOnScreen("pa.png", confidence=0.75)
            if pa != None:
                pyautogui.moveTo(pa)
                pyautogui.mouseDown()
                pyautogui.moveTo(top1, duration=0.5)
                pyautogui.moveTo(bot1, duration=0.5)
                pyautogui.moveTo(bot2, duration=0.5)
                pyautogui.moveTo(top2, duration=0.5)
                pyautogui.mouseUp()
                pyautogui.sleep(3)
        else:
            break


def fVerificarMilho():
    while True: 
        Z = pyautogui.locateOnScreen("Z.png", confidence=0.75)
        pyautogui.sleep(0.77)
        if Z != None:
            pyautogui.click(Z, duration=0.32)
            
            time.sleep(0.5)
            x_pos, z_pos = pyautogui.center(Z)
            
            plantar_milho = pyautogui.locateOnScreen("plantar_milho.png", confidence=0.75)
            pyautogui.sleep(0.75)
            if plantar_milho == None:
                plantar_amendoin = pyautogui.locateOnScreen("amendoin.png", confidence=0.75)
                pyautogui.sleep(0.75)
                if plantar_amendoin == None:
                    pyautogui.move(-100,320, duration=0.4)
                    pyautogui.drag(310,0,0.5)
                    pyautogui.mouseUp()
                    pyautogui.sleep(0.4)
                    fPlantarMilho(x_pos, z_pos)
                else: 
                    pyautogui.moveTo(plantar_amendoin, duration=0.4)
                    pyautogui.drag(310,0,0.5)
                    pyautogui.mouseUp()
                    pyautogui.sleep(0.4)
                    fPlantarMilho(x_pos, z_pos)
                break
            else:
                fPlantarMilho(x_pos, z_pos)
        else:
            Z = pyautogui.locateOnScreen("z2.PNG", confidence=0.75)
            pyautogui.sleep(0.77)
            if Z != None:
                pyautogui.click(Z, duration=0.32)
            
                time.sleep(0.5)
                x_pos, z_pos = pyautogui.center(Z)
                
                plantar_milho = pyautogui.locateOnScreen("plantar_milho.png", confidence=0.75)
                if plantar_milho == None:
                    plantar_amendoin = pyautogui.locateOnScreen("amendoin.png", confidence=0.75)
                    pyautogui.sleep(0.75)
                    if plantar_amendoin == None:
                        pyautogui.move(-100,320, duration=0.4)
                        pyautogui.drag(310,0,0.5)
                        pyautogui.mouseUp()
                        pyautogui.sleep(0.4)
                        fPlantarMilho(x_pos, z_pos)
                    else: 
                        pyautogui.moveTo(plantar_amendoin, duration=0.4)
                        pyautogui.drag(310,0,0.5)
                        pyautogui.mouseUp()
                        pyautogui.sleep(0.4)
                        fPlantarMilho(x_pos, z_pos)
                    break
                else:
                    fPlantarMilho(x_pos, z_pos)
            break
        
def fVerificarErva():
    # while True: 
        erva = pyautogui.locateOnScreen("erva.png", confidence=0.75)
        pyautogui.sleep(0.77)
        if erva != None:
            pyautogui.moveTo(erva)
            pyautogui.move(0,70,0.3)
            pyautogui.click()
            
            time.sleep(0.5)
            x_pos, z_pos = pyautogui.center(erva)
            
            matarErva = pyautogui.locateOnScreen("matarErva.png", confidence=0.75)
            if matarErva == None:
                pyautogui.moveTo(580,885, duration=0.8)
                pyautogui.mouseDown()
                pyautogui.moveTo(x_pos, z_pos, duration=0.3)
                pyautogui.move(0, -80, duration=0.3)
                pyautogui.mouseUp()
            else:
                pyautogui.moveTo(matarErva, duration=0.8)
                pyautogui.mouseDown()
                pyautogui.moveTo(x_pos, z_pos, duration=0.3)
                pyautogui.move(0, -80, duration=0.3)
                pyautogui.mouseUp()
            fMovimentoInicial()

def fPlantarMilho(x_pos, y_pos):
    plantar_milho = pyautogui.locateOnScreen("plantar_milho.png", confidence=0.75)
    if plantar_milho != None:
        pyautogui.moveTo(plantar_milho, duration=0.8)
        pyautogui.mouseDown()
        pyautogui.moveTo(x_pos -700, y_pos -500, duration=0.3)
        pyautogui.moveTo(x_pos +900, y_pos +550, duration=0.3)
        pyautogui.moveTo(x_pos -150, y_pos +150, duration=0.3)
        pyautogui.moveTo(x_pos -900, y_pos -550, duration=0.3)
        pyautogui.moveTo(x_pos, y_pos, duration=0.3)
        pyautogui.mouseUp()
        return True
    else:
        return False
