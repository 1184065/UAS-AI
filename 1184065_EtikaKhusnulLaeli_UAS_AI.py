# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:08:24 2021

@author: ANIF
"""

import speech_recognition as sr

engine = sr.Recognizer() #ngedeteksi suara
mic = sr.Microphone() #untuk microphone
hasil = "" #var untuk menyimpan hasil
engine.pause_treshold = 3

with mic as source: #mic otomatis aktif
    print("Ucapkan sesuatu!")
    rekaman = engine.listen(source) #setor rekaman di var rekaman
    print("Waktu habis")
    
try:
    hasil = engine.recognize_google(rekaman, language ="id-ID") #menggunakan api google
    print(hasil)
except engine.UnknownValueError:
    print("Google Speech Recognition tidak mengerti yang anda katakan")
except Exception as e:
    print("Tidak ada perkataan dari Google Speech Recognition service; {0}".format(e))
    
#Menyimpan hasil di txt    