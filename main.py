import os
import subprocess
import time
import pygame
import serial
import speech_recognition as sr

ser = serial.Serial('COM9', 9600, timeout=1)


def audio(caminho):
    pygame.init()
    pygame.mixer.music.load(f'audios/{caminho}.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def ligar_led(cor):
    ser.write(str(cor).encode())
    ser.write(b'1')


def desligar_led():
    ser.write('0')


def chamar(bit):
    rec = sr.Recognizer()
    with sr.Microphone(0) as mic:
        rec.adjust_for_ambient_noise(mic)
        while True:
            try:
                audi = rec.listen(mic)
                frases = rec.recognize_google(audi, language="pt-BR")
                return frases
            except sr.UnknownValueError:
                if bit == 1:
                    audio('nEntendi')
                    return 'nao entendi'
                else:
                    return 'nao entendi'


while True:
    frase = chamar(0)
    if frase == 'cortana' or frase == 'Cortana':
        audio('Oi')
        time.sleep(2)
        print('pode falar')
        frase = chamar(1)
        if frase == 'Ligar LED branco':
            audio('Ledbrancoligado')
            ligar_led('b')
        elif frase == 'Ligar LED azul':
            audio('Ledazulligado')
            ligar_led('a')
        elif frase == 'Ligar LED verde':
            audio('Led verde ligado')
            ligar_led('v')
        elif frase == 'Ligar LED laranja':
            audio('Led laranja ligado')
            ligar_led('l')
        elif frase == 'Ligar LED vermelho':
            audio('Ledvermelholigado')
            ligar_led('V')
        elif frase == 'Desligar LED' or frase == 'desligar led':
            desligar_led()

        elif frase == 'sair':
            break

        elif frase == 'Abrir Google Chrome':
            audio('AbrindoGoogleChrome')
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif frase == 'Abrir Python':
            audio('Abrindopython')
            os.startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2021.3.1/bin/pycharm64.exe")

        elif frase == 'Abrir YouTube':
            audio('AbrindoYouTube')
            subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", 'http://www.youtube.com'])

        elif frase == 'Jogo do Palmeiras':
            audio('JogodoPalmeiras')
            subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe",
                              'https://www.google.com/search?q=palmeiras&oq=palm&aqs=chrome.1.69i60j35i39i355j69i57j0i512j46i512j69i60l3.3135j1j7&sourceid=chrome&ie=UTF-8'])
