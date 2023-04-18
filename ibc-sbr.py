'''Steuerung IBC-SBR-Versuchskläranlage MB2023-03'''

import time
import tkinter
import threading
from datetime import datetime, timedelta
import RPi.GPIO as GPIO

main = tkinter.Tk()
main.geometry('1000x700')
main.title('Steuerung IBC-Versuchskläranlage')

def ende():
    '''Close and End'''
    global hauptlauf, sbr1_lauf
    hauptlauf = "AUS"
    sbr1_lauf = "AUS"
    allout()
    GPIO.cleanup()
    main.destroy()

def tgesberechnen():
    '''calculate total time'''
    global t_z1, t_d1, t_n1, t_z2, t_d2, t_n2, t_z3, t_d3, t_n3, t_sed, t_abzug, t_still, t_ges
    t_ges = round(t_z1 + t_d1 + t_n1 + t_z2 + t_d2 + t_n2 + t_z3 + t_d3 + t_n3 + t_sed + t_abzug + t_still, 1)
    ausgabetges["text"] = str(t_ges)
    
def werteschreiben():
    global t_z1, t_d1, t_n1, t_z2, t_d2, t_n2, t_z3, t_d3, t_n3, t_sed, t_abzug, t_still, t_luftan, t_luftpause, t_stossan, t_stosspause
    liste = [str(t_z1), str(t_d1), str(t_n1), str(t_z2), str(t_d2), str(t_n2), str(t_z3), str(t_d3), str(t_n3), str(t_sed), str(t_abzug), str(t_still), str(t_luftan), str(t_luftpause), str(t_stossan), str(t_stosspause)]
    dateiobjekt = open("sicherung.txt", "w")
    for i in range(0,len(liste)):
        dateiobjekt.write(liste[i]+"\n")
    dateiobjekt.close()
    print("Aktuelle Werte in Sicherungsdatei gespeichert")
    
def uebernehmen(phasenzeit, eingabevariable, ausgabevariable, fehlermeldungsvariable):
    '''check input'''
    try:
        ganzzahl = float(eingabevariable.get())
        if 0 <= ganzzahl < 1000:
            phasenzeit = ganzzahl
            ausgabevariable["text"] = str(phasenzeit)
        else:
            t11 = threading.Thread(target = fehlermeldung, args = (fehlermeldungsvariable,))
            t11.start()
    except:
        t11 = threading.Thread(target = fehlermeldung, args = (fehlermeldungsvariable,))
        t11.start()
    return(phasenzeit)

def fehlermeldung(fehlermeldungsv):
    '''error message'''
    fehlermeldungsv["text"] = "Bitte eine Zahl zwischen 0 und 999 eingeben"
    time.sleep(3)
    fehlermeldungsv["text"] = ""

def luftanget():
    '''get input for Belüftung-An'''
    global t_luftan
    t_luftan = uebernehmen(t_luftan, eingabeluftan, ausgabeluftan, fehlerluftan)
    eingabeluftan.delete(0, 'end')
    werteschreiben()

def luftpauseget():
    '''get input for Belüftung-Pause'''
    global t_luftpause
    t_luftpause = uebernehmen(t_luftpause, eingabeluftpause, ausgabeluftpause, fehlerluftpause)
    eingabeluftpause.delete(0, 'end')
    werteschreiben()

def stossanget():
    '''get input for Stossbelüftung-An'''
    global t_stossan
    t_stossan = uebernehmen(t_stossan, eingabestossan, ausgabestossan, fehlerstossan)
    eingabestossan.delete(0, 'end')
    werteschreiben()

def stosspauseget():
    '''get input for Stossbelüftung-Pause'''
    global t_stosspause
    t_stosspause = uebernehmen(t_stosspause, eingabestosspause, ausgabestosspause, fehlerstosspause)
    eingabestosspause.delete(0, 'end')
    werteschreiben()

def zulauf1get():
    '''get input for Zulauf1'''
    global t_z1
    t_z1 = uebernehmen(t_z1, eingabe1, ausgabezulauf1, fehlerzulauf1)
    tgesberechnen()
    eingabe1.delete(0, 'end')
    werteschreiben()

def deni1get():
    '''get input for Deni1'''
    global t_d1
    t_d1 = uebernehmen(t_d1, eingabe2, ausgabedeni1, fehlerdeni1)
    tgesberechnen()
    eingabe2.delete(0, 'end')
    werteschreiben()

def nitri1get():
    '''get input for Nitri1'''
    global t_n1
    t_n1 = uebernehmen(t_n1, eingabe3, ausgabenitri1, fehlernitri1)
    tgesberechnen()
    eingabe3.delete(0, 'end')
    werteschreiben()

def zulauf2get():
    '''get input for Zulauf2'''
    global t_z2
    t_z2 = uebernehmen(t_z2, eingabe4, ausgabezulauf2, fehlerzulauf2)
    tgesberechnen()
    eingabe4.delete(0, 'end')
    werteschreiben()

def deni2get():
    '''get input for Deni2'''
    global t_d2
    t_d2 = uebernehmen(t_d2, eingabe5, ausgabedeni2, fehlerdeni2)
    tgesberechnen()
    eingabe5.delete(0, 'end')
    werteschreiben()

def nitri2get():
    '''get input for Nitri2'''
    global t_n2
    t_n2 = uebernehmen(t_n2, eingabe6, ausgabenitri2, fehlernitri2)
    tgesberechnen()
    eingabe6.delete(0, 'end')
    werteschreiben()

def zulauf3get():
    '''get input for Zulauf3'''
    global t_z3
    t_z3 = uebernehmen(t_z3, eingabe7, ausgabezulauf3, fehlerzulauf3)
    tgesberechnen()
    eingabe7.delete(0, 'end')
    werteschreiben()

def deni3get():
    '''get input for Deni3'''
    global t_d3
    t_d3 = uebernehmen(t_d3, eingabe8, ausgabedeni3, fehlerdeni3)
    tgesberechnen()
    eingabe8.delete(0, 'end')
    werteschreiben()

def nitri3get():
    '''get input for Nitri3'''
    global t_n3
    t_n3 = uebernehmen(t_n3, eingabe9, ausgabenitri3, fehlernitri3)
    tgesberechnen()
    eingabe9.delete(0, 'end')
    werteschreiben()

def sedget():
    '''get input for Sedimentation'''
    global t_sed
    t_sed = uebernehmen(t_sed, eingabe10, ausgabesed, fehlersed)
    tgesberechnen()
    eingabe10.delete(0, 'end')
    werteschreiben()

def klabzugget():
    '''get input for clarification'''
    global t_abzug
    t_abzug = uebernehmen(t_abzug, eingabe11, ausgabeklabzug, fehlerklabzug)
    tgesberechnen()
    eingabe11.delete(0, 'end')
    werteschreiben()

def stillget():
    '''get input for waiting time'''
    global t_still
    t_still = uebernehmen(t_still, eingabe12, ausgabestillstand, fehlerstillstand)
    tgesberechnen()
    eingabe12.delete(0, 'end')
    werteschreiben()

def GPIO_initialisieren():
    '''initialise GPIOs'''
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(23, GPIO.OUT) #Verdichter 400V
    GPIO.setup(22, GPIO.OUT) #Zulaufpumpe 230V
    GPIO.setup(27, GPIO.OUT) #Ablaufventil 230 V
    # nicht genutzt GPIO.setup(24, GPIO.OUT)

def allout():
    '''put all out'''
    GPIO.output(23, GPIO.HIGH) #Ausschalten Verdichter
    GPIO.output(22, GPIO.HIGH) #Ausschalten Zulaufpumpe
    GPIO.output(27, GPIO.HIGH) #Ausschalten Ablauf
    #nicht genutzt GPIO.output(24, GPIO.HIGH) 

def countdownSBR1():
    '''calculate and show time until next phase starts'''
    global sbr1_auto, sbr1_phaseendezeit
    while sbr1_auto == "AN":
        while datetime.now() < sbr1_phaseendezeit:
            restzeit = str((sbr1_phaseendezeit - datetime.now()))
            SBR1Restzeitlabel['text'] = restzeit[0:restzeit.find('.')]
            time.sleep(1)
        SBR1Restzeitlabel['text'] = ''

def SBR1an():
    '''run SBR1'''
    global t_z1, t_d1, t_n1, t_z2, t_d2, t_n2, t_z3, t_d3, t_n3, t_sed, t_abzug, t_still, sbr1_lauf, sbr1_phaseendezeit, sbr1_auto, sbr1_count, stossluft_lauf, belueftung_lauf
    sbr1_auto = "AN"
    t5 = threading.Thread(target = countdownSBR1)
    t5.start()
    while sbr1_lauf == "AN":
        #9. Nitriphase 3: 
        allout()
        belueftung_lauf = "AN"
        sbr1phase["text"] = "Belüftung 3"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_n3)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        belueftung_lauf = "AUS"
        
        #10. Sedimentations-/Absetzphase: alles aus
        allout()
        sbr1phase["text"] = "Sedimentation"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_sed)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)

        #11. Klarwasserabzug
        GPIO.output(27, GPIO.LOW) #Einschalten Ablaufventil
        sbr1phase["text"] = "Klarwasserabzug"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_abzug)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        allout()

        #12. Stillstandszeit
        allout()
        sbr1phase["text"] = "Stillstandszeit"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_still)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)

        if sbr1_lauf == "AN":
            sbr1_count += 1
        SBR1Durchganglabel["text"] = str(sbr1_count)
        
        #1. Zulaufphase 1: Zulaufpumpe an
        GPIO.output(22, GPIO.LOW)
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Zulauf 1"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_z1)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"
        allout()

        #2. Deniphase 1: 
        allout()
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Unbelüftet 1"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_d1)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"

        #3. Nitriphase 1: Beluefter an
        allout()
        belueftung_lauf = "AN"
        sbr1phase["text"] = "Belüftung 1"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_n1)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        belueftung_lauf = "AUS"
        
        #4. Zulaufphase 2: Zulaufpumpe an
        GPIO.output(22, GPIO.LOW)
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Zulauf 2"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_z2)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"
        allout()
        
        #5. Deniphase 2: Beluefter aus
        allout()
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Unbelüftet 2"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_d2)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"

        #6. Nitriphase 2: Beluefter an
        allout()
        belueftung_lauf = "AN"
        sbr1phase["text"] = "Belüftung 2"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_n2)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        belueftung_lauf = "AUS"

        #7. Zulaufphase 3:
        GPIO.output(22, GPIO.LOW)
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Zulauf 3"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_z3)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"
        allout()
        
        #8. Deniphase 3:
        allout()
        stossluft_lauf = "AN"
        sbr1phase["text"] = "Unbelüftet 3"
        sbr1phasestart["text"] = time.strftime("%H:%M:%S",time.localtime())
        sbr1_phaseendezeit = datetime.now() + timedelta(minutes = t_d3)
        sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
        while datetime.now() < sbr1_phaseendezeit and sbr1_lauf == "AN":
            time.sleep(1)
        stossluft_lauf = "AUS"

    sbr1phase["text"] = "Pause"
    sbr1_phaseendezeit = datetime.now()
    sbr1phaseende["text"] = sbr1_phaseendezeit.strftime('%H:%M:%S')
    sbr1phasestart["text"] = ""
    sbr1_auto = "AUS"

def belueftungan():
    global hauptlauf, belueftung_lauf, t_luftan, t_luftpause
    while hauptlauf == "AN":
        if belueftung_lauf == "AN":
            GPIO.output(23, GPIO.LOW)
            luftstatuslabel["text"] = 'An'
            luftstatuslabel["bg"] = 'lime'
            luftan_endezeit = datetime.now() + timedelta(minutes = t_luftan)
            while datetime.now() < luftan_endezeit and belueftung_lauf == "AN":
                time.sleep(1)
            GPIO.output(23, GPIO.HIGH)
            luftstatuslabel["text"] = 'Pause'
            luftstatuslabel["bg"] = 'orange'
            luftpause_endezeit = datetime.now() + timedelta(minutes = t_luftpause)
            while datetime.now() < luftpause_endezeit and belueftung_lauf == "AN":
                time.sleep(1)
            luftstatuslabel["text"] = 'Aus'
            luftstatuslabel["bg"] = 'red'
        else:
            time.sleep(1)

def stossluftan():
    global hauptlauf, stossluft_lauf, t_stossan, t_stosspause
    while hauptlauf == "AN":
        if stossluft_lauf == "AN":
            stossluftstatuslabel["text"] = 'Pause'
            stossluftstatuslabel["bg"] = 'orange'
            stossluftpause_endezeit = datetime.now() + timedelta(minutes = t_stosspause)
            while datetime.now() < stossluftpause_endezeit and stossluft_lauf == "AN":
                time.sleep(1)
            GPIO.output(23, GPIO.LOW)
            stossluftstatuslabel["text"] = 'An'
            stossluftstatuslabel["bg"] = 'lime'
            stossluftan_endezeit = datetime.now() + timedelta(minutes = t_stossan)
            while datetime.now() < stossluftan_endezeit and stossluft_lauf == "AN":
                time.sleep(1)
            GPIO.output(23, GPIO.HIGH)
            stossluftstatuslabel["text"] = 'Aus'
            stossluftstatuslabel["bg"] = 'red'
        else:
            time.sleep(1)

def schalten1():
    '''put SBR1 on or off'''
    global sbr1_lauf
    if sbr1_lauf == "AUS" and sbr1phase["text"] == "Pause":
        sbr1_lauf = "AN"
        schalter1['bg'] = 'lime'
        schalter1['text'] = 'An'
        t1 = threading.Thread(target = SBR1an)
        t1.start()
    else:
        sbr1_lauf = "AUS"
        schalter1['bg'] = 'red'
        schalter1['text'] = 'Aus'

def zeitstempelaktualisieren():
    '''update time stamp'''
    global hauptlauf
    while hauptlauf == "AN":
        zeitjetzt['text'] = time.strftime("%H:%M:%S",time.localtime())
        time.sleep(1)

def cputempaktualisieren():
    '''update temperatur for CPU'''
    global hauptlauf
    while hauptlauf == "AN":
        tempData = "/sys/class/thermal/thermal_zone0/temp"
        dateilesen = open(tempData, "r")
        temperatur = dateilesen.readline(5)
        dateilesen.close()
        temperatur = round(float(temperatur)/1000,1)
        cputemp['text'] = temperatur
        time.sleep(10)

#Programm Start
GPIO_initialisieren()
allout()
hauptlauf = "AN"
sbr1_lauf = "AN"
sbr1_auto = "AUS"
stossluft_lauf = "AUS"
belueftung_lauf = "AUS"
sbr1_count = 0
sbr1_phaseendezeit = datetime.now()

try:
    dateiobjektr = open("sicherung.txt", "r")
    lister = dateiobjektr.readlines()
    dateiobjektr.close()
    t_z1 = float(lister[0])
    t_d1 = float(lister[1])
    t_n1 = float(lister[2])
    t_z2 = float(lister[3])
    t_d2 = float(lister[4])
    t_n2 = float(lister[5])
    t_z3 = float(lister[6])
    t_d3 = float(lister[7])
    t_n3 = float(lister[8])
    t_sed = float(lister[9])
    t_abzug = float(lister[10])
    t_still = float(lister[11])
    t_luftan = float(lister[12])
    t_luftpause = float(lister[13])
    t_stossan = float(lister[14])
    t_stosspause = float(lister[15])
    print("Werte aus Sicherungsdatei übernommen")
except:
    t_z1 = 0.0 #Min
    t_d1 = 0.0 #Min
    t_n1 = 0.0 #Min
    t_z2 = 0.0 #Min
    t_d2 = 0.0 #Min
    t_n2 = 0.0 #Min
    t_z3 = 0.0 #Min
    t_d3 = 15.0 #Min
    t_n3 = 30.0 #Min
    t_sed = 60.0 #Min
    t_abzug = 60.0 #Min
    t_still = 0.0 # Min
    t_luftan = 5.0 #Min
    t_luftpause = 3.0 #Min    
    t_stossan = 0.1 #Min
    t_stosspause = 5.0 #Min 
    print("Keine Sicherungsdatei vorhanden, Standardwerte übernommen")

t_ges = t_z1 + t_d1 + t_n1 + t_z2 + t_d2 + t_n2 + t_z1 + t_d3 + t_n3 + t_sed + t_abzug + t_still

#Überschrift
tkinter.Label(main, text = 'IBC-Versuchskläranlage ', font = ('arial', 20,'bold')).place(x = 10, y = 10, anchor = 'nw')

#Schalter
schalter1 = tkinter.Button(main, width = 8, text = 'Schalten', command = schalten1, cursor = 'tcross', bg = 'lime', font = ('arial', 10, 'bold'))
schalter1.place(x = 450, y = 15, anchor = 'ne')

#Phase
tkinter.Label(main, text = 'Aktuelle Phase:', font = ('arial', 11, 'bold')).place(x = 10, y = 70, anchor = 'w')
sbr1phase = tkinter.Label(main, text = 'Pause', font = ('arial', 11, 'bold'))
sbr1phase.place(x = 250, y = 70, anchor = 'center')

tkinter.Label(main, text = 'Start Phase:', font = ('arial', 11, 'bold')).place(x = 10, y = 90, anchor = 'w')
sbr1phasestart = tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
sbr1phasestart.place(x = 250, y = 90, anchor = 'center')

tkinter.Label(main, text = 'Ende Phase:', font = ('arial', 11, 'bold')).place(x = 10, y = 110, anchor = 'w')
sbr1phaseende = tkinter.Label(main, text = '-',  font = ('arial', 11, 'bold'))
sbr1phaseende.place(x = 250, y = 110, anchor = 'center')

tkinter.Label(main, text = 'Restzeit:', font = ('arial', 11, 'bold')).place(x = 10, y = 130, anchor = 'w')
SBR1Restzeitlabel = tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
SBR1Restzeitlabel.place(x = 250, y = 130, anchor = 'center')

tkinter.Label(main, text = 'Durchgang:', font = ('arial', 11, 'bold')).place(x = 10, y = 150, anchor = 'w')
SBR1Durchganglabel = tkinter.Label(main, text = str(sbr1_count), font = ('arial', 11, 'bold'))
SBR1Durchganglabel.place(x = 250, y = 150, anchor = 'center')

#Belüftung
tkinter.Label(main, text = 'Belüftung', font = ('arial', 11, 'bold', 'underline')).place(x = 550, y = 230, anchor = 'w')

#Belüftung - An
tkinter.Label(main, text = 'Belüftung an: ', font = ('arial', 11, 'bold')).place(x = 550, y = 260, anchor = 'w')
ausgabeluftan = tkinter.Label(main, text = str(t_luftan), font = ('arial', 11, 'bold'))
ausgabeluftan.place(x = 745, y = 260, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 750, y = 260, anchor = 'w')
eingabeluftan = tkinter.Entry(main, width = 5)
eingabeluftan.place(x = 845, y = 260, anchor = 'e')
eingabeluftanbut = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = luftanget)
eingabeluftanbut.place(x = 850, y = 260, anchor = 'w')
fehlerluftan = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerluftan.place(x = 660, y = 260, anchor = 'w')

#Belüftung - Pause
tkinter.Label(main, text = 'Belüftung Pause: ', font = ('arial', 11, 'bold')).place(x = 550, y = 290, anchor = 'w')
ausgabeluftpause = tkinter.Label(main, text = str(t_luftpause), font = ('arial', 11, 'bold'))
ausgabeluftpause.place(x = 745, y = 290, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 750, y = 290, anchor = 'w')
eingabeluftpause = tkinter.Entry(main, width = 5)
eingabeluftpause.place(x = 845, y = 290, anchor = 'e')
eingabeluftpausebut = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = luftpauseget)
eingabeluftpausebut.place(x = 850, y = 290, anchor = 'w')
fehlerluftpause = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerluftpause.place(x = 660, y = 290, anchor = 'w')

#Belüftung Status
tkinter.Label(main, text = 'Belüftung Status:', font = ('arial', 11, 'bold')).place(x = 550, y = 320, anchor = 'w')
luftstatuslabel = tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
luftstatuslabel.place(x = 750, y = 320, anchor = 'center')

#Stossbelüftung
tkinter.Label(main, text = 'Stoßbelüftung', font = ('arial', 11, 'bold', 'underline')).place(x = 550, y = 430, anchor = 'w')

#Stossbelüftung - An
tkinter.Label(main, text = 'Stoßluft an: ', font = ('arial', 11, 'bold')).place(x = 550, y = 460, anchor = 'w')
ausgabestossan = tkinter.Label(main, text = str(t_stossan), font = ('arial', 11, 'bold'))
ausgabestossan.place(x = 745, y = 460, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 750, y = 460, anchor = 'w')
eingabestossan = tkinter.Entry(main, width = 5)
eingabestossan.place(x = 845, y = 460, anchor = 'e')
eingabestossanbut = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = stossanget)
eingabestossanbut.place(x = 850, y = 460, anchor = 'w')
fehlerstossan = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerstossan.place(x = 660, y = 460, anchor = 'w')

#Stossbelüftung - Pause
tkinter.Label(main, text = 'Stoßluft Pause: ', font = ('arial', 11, 'bold')).place(x = 550, y = 490, anchor = 'w')
ausgabestosspause = tkinter.Label(main, text = str(t_stosspause), font = ('arial', 11, 'bold'))
ausgabestosspause.place(x = 745, y = 490, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 750, y = 490, anchor = 'w')
eingabestosspause = tkinter.Entry(main, width = 5)
eingabestosspause.place(x = 845, y = 490, anchor = 'e')
eingabestosspausebut = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = stosspauseget)
eingabestosspausebut.place(x = 850, y = 490, anchor = 'w')
fehlerstosspause = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerstosspause.place(x = 660, y = 490, anchor = 'w')

#Stoßbelüftung Status
tkinter.Label(main, text = 'Stoßbelüftung Status:', font = ('arial', 11, 'bold')).place(x = 550, y = 520, anchor = 'w')
stossluftstatuslabel = tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
stossluftstatuslabel.place(x = 750, y = 520, anchor = 'center')

#Zulauf1
tkinter.Label(main, text = 'Zulauf 1: ', font = ('arial', 11, 'bold')).place(x = 150, y = 230, anchor = 'e')
ausgabezulauf1 = tkinter.Label(main, text = str(t_z1), font = ('arial', 11, 'bold'))
ausgabezulauf1.place(x = 245, y = 230, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 230, anchor = 'w')
eingabe1 = tkinter.Entry(main, width = 5)
eingabe1.place(x = 345, y = 230, anchor = 'e')
eingabe1but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = zulauf1get)
eingabe1but.place(x = 350, y = 230, anchor = 'w')
fehlerzulauf1 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerzulauf1.place(x = 160, y = 230, anchor = 'w')

#Deni1
tkinter.Label(main, text = 'Unbelüftet 1: ', font = ('arial', 11, 'bold')).place(x = 150, y = 260, anchor = 'e')
ausgabedeni1 = tkinter.Label(main, text = str(t_d1), font = ('arial', 11, 'bold'))
ausgabedeni1.place(x = 245, y = 260, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 260, anchor = 'w')
eingabe2 = tkinter.Entry(main, width = 5)
eingabe2.place(x = 345, y = 260, anchor = 'e')
eingabe2but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = deni1get)
eingabe2but.place(x = 350, y = 260, anchor = 'w')
fehlerdeni1 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerdeni1.place(x = 160, y = 260, anchor = 'w')

#Nitri1
tkinter.Label(main, text = 'Belüftung 1: ', font = ('arial', 11, 'bold')).place(x = 150, y = 290, anchor = 'e')
ausgabenitri1 = tkinter.Label(main, text = str(t_n1), font = ('arial', 11, 'bold'))
ausgabenitri1.place(x = 245, y = 290, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 290, anchor = 'w')
eingabe3 = tkinter.Entry(main, width = 5)
eingabe3.place(x = 345, y = 290, anchor = 'e')
eingabe3but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = nitri1get)
eingabe3but.place(x = 350, y = 290, anchor = 'w')
fehlernitri1 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlernitri1.place(x = 160, y = 290, anchor = 'w')

#Zulauf2
tkinter.Label(main, text = 'Zulauf 2: ', font = ('arial', 11, 'bold')).place(x = 150, y = 330, anchor = 'e')
ausgabezulauf2 = tkinter.Label(main, text = str(t_z2), font = ('arial', 11, 'bold'))
ausgabezulauf2.place(x = 245, y = 330, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 330, anchor = 'w')
eingabe4 = tkinter.Entry(main, width = 5)
eingabe4.place(x = 345, y = 330, anchor = 'e')
eingabe4but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = zulauf2get)
eingabe4but.place(x = 350, y = 330, anchor = 'w')
fehlerzulauf2 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerzulauf2.place(x = 160, y = 330, anchor = 'w')

#Deni2
tkinter.Label(main, text = 'Unbelüftet 2: ', font = ('arial', 11, 'bold')).place(x = 150, y = 360, anchor = 'e')
ausgabedeni2 = tkinter.Label(main, text = str(t_d2), font = ('arial', 11, 'bold'))
ausgabedeni2.place(x = 245, y = 360, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 360, anchor = 'w')
eingabe5 = tkinter.Entry(main, width = 5)
eingabe5.place(x = 345, y = 360, anchor = 'e')
eingabe5but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = deni2get)
eingabe5but.place(x = 350, y = 360, anchor = 'w')
fehlerdeni2 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerdeni2.place(x = 160, y = 360, anchor = 'w')

#Nitri2
tkinter.Label(main, text = 'Belüftung 2: ', font = ('arial', 11, 'bold')).place(x = 150, y = 390, anchor = 'e')
ausgabenitri2 = tkinter.Label(main, text = str(t_n2), font = ('arial', 11, 'bold'))
ausgabenitri2.place(x = 245, y = 390, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 390, anchor = 'w')
eingabe6 = tkinter.Entry(main, width = 5)
eingabe6.place(x = 345, y = 390, anchor = 'e')
eingabe6but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = nitri2get)
eingabe6but.place(x = 350, y = 390, anchor = 'w')
fehlernitri2 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlernitri2.place(x = 160, y = 390, anchor = 'w')

#Zulauf3
tkinter.Label(main, text = 'Zulauf 3: ', font = ('arial', 11, 'bold')).place(x = 150, y = 430, anchor = 'e')
ausgabezulauf3 = tkinter.Label(main, text = str(t_z3), font = ('arial', 11, 'bold'))
ausgabezulauf3.place(x = 245, y = 430, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 430, anchor = 'w')
eingabe7 = tkinter.Entry(main, width = 5)
eingabe7.place(x = 345, y = 430, anchor = 'e')
eingabe7but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = zulauf3get)
eingabe7but.place(x = 350, y = 430, anchor = 'w')
fehlerzulauf3 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerzulauf3.place(x = 160, y = 430, anchor = 'w')

#Deni3
tkinter.Label(main, text = 'Unbelüftet 3: ', font = ('arial', 11, 'bold')).place(x = 150, y = 460, anchor = 'e')
ausgabedeni3 = tkinter.Label(main, text = str(t_d3), font = ('arial', 11, 'bold'))
ausgabedeni3.place(x = 245, y = 460, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 460, anchor = 'w')
eingabe8 = tkinter.Entry(main, width = 5)
eingabe8.place(x = 345, y = 460, anchor = 'e')
eingabe8but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = deni3get)
eingabe8but.place(x = 350, y = 460, anchor = 'w')
fehlerdeni3 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerdeni3.place(x = 160, y = 460, anchor = 'w')

#Nitri3
tkinter.Label(main, text = 'Belüftung 3: ', font = ('arial', 11, 'bold')).place(x = 150, y = 490, anchor = 'e')
ausgabenitri3 = tkinter.Label(main, text = str(t_n3), font = ('arial', 11, 'bold'))
ausgabenitri3.place(x = 245, y = 490, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 490, anchor = 'w')
eingabe9 = tkinter.Entry(main, width = 5)
eingabe9.place(x = 345, y = 490, anchor = 'e')
eingabe9but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = nitri3get)
eingabe9but.place(x = 350, y = 490, anchor = 'w')
fehlernitri3 = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlernitri3.place(x = 160, y = 490, anchor = 'w')

#Absetz-/Sedimentation
tkinter.Label(main, text = 'Sedimentation: ', font = ('arial', 11, 'bold')).place(x = 150, y = 530, anchor = 'e')
ausgabesed = tkinter.Label(main, text = str(t_sed), font = ('arial', 11, 'bold'))
ausgabesed.place(x = 245, y = 530, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 530, anchor = 'w')
eingabe10 = tkinter.Entry(main, width = 5)
eingabe10.place(x = 345, y = 530, anchor = 'e')
eingabe10but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = sedget)
eingabe10but.place(x = 350, y = 530, anchor = 'w')
fehlersed = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlersed.place(x = 160, y = 530, anchor = 'w')

#Klarwasserabzug, Zulauf
tkinter.Label(main, text = 'Klarwasserabzug: ', font = ('arial', 11, 'bold')).place(x = 150, y = 560, anchor = 'e')
ausgabeklabzug = tkinter.Label(main, text = str(t_abzug), font = ('arial', 11, 'bold'))
ausgabeklabzug.place(x = 245, y = 560, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 560, anchor = 'w')
eingabe11 = tkinter.Entry(main, width = 5)
eingabe11.place(x = 345, y = 560, anchor = 'e')
eingabe11but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = klabzugget)
eingabe11but.place(x = 350, y = 560, anchor = 'w')
fehlerklabzug = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerklabzug.place(x = 160, y = 560, anchor = 'w')

#Stillstandszeit
tkinter.Label(main, text = 'Stillstandszeit: ', font = ('arial', 11, 'bold')).place(x = 150, y = 590, anchor = 'e')
ausgabestillstand = tkinter.Label(main, text = str(t_still), font = ('arial', 11, 'bold'))
ausgabestillstand.place(x = 245, y = 590, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 590, anchor = 'w')
eingabe12 = tkinter.Entry(main, width = 5)
eingabe12.place(x = 345, y = 590, anchor = 'e')
eingabe12but = tkinter.Button(main, text = "OK", font = ('arial', 8, 'bold'), width = 1, command = stillget)
eingabe12but.place(x = 350, y = 590, anchor = 'w')
fehlerstillstand = tkinter.Label(main, font = ('arial', 11, 'bold'), fg = 'red')
fehlerstillstand.place(x = 160, y = 590, anchor = 'w')

#Zyklus/ Gesamtzeit
tkinter.Label(main, text = 'Zykluszeit: ', font = ('arial', 11, 'bold')).place(x = 150, y = 650, anchor = 'e')
ausgabetges = tkinter.Label(main, text = str(t_ges), font = ('arial', 11, 'bold'))
ausgabetges.place(x = 245, y = 650, anchor = 'e')
tkinter.Label(main, text = 'Min.', font = ('arial', 11, 'bold')).place(x = 250, y = 650, anchor = 'w')

#Zeitstempel anzeigen und aktualisieren
zeitjetzt =tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
zeitjetzt.place(x = 625, y = 50, anchor = 'w')
threading.Thread(target = zeitstempelaktualisieren).start()

#bei Programmstart SBR-Steuerung anschalten
threading.Thread(target = SBR1an).start()

#bei Programmstart Thread Belüftung anschalten
threading.Thread(target = belueftungan).start()

#bei Programmstart Thread Stoßbelüftung anschalten
threading.Thread(target = stossluftan).start()

#CPU-Temperatur anzeigen und aktualisieren
tkinter.Label(main, text = 'CPU-Temp.: ', font = ('arial', 11, 'bold')).place (x = 625, y = 70, anchor = 'w')
tkinter.Label(main, text = '°C', font = ('arial', 11, 'bold')).place (x = 750, y = 70, anchor = 'w')
cputemp = tkinter.Label(main, text = '-', font = ('arial', 11, 'bold'))
cputemp.place(x = 750, y = 70, anchor = 'e')
threading.Thread(target = cputempaktualisieren).start()

#Beenden-Schalter anordnen
endeschalt =tkinter.Button(main, text = 'Beenden', command = ende, cursor = 'tcross', bg= 'white', font = ('arial', 11, 'bold'))
endeschalt.place(x = 625, y = 20, anchor = 'w')

# Programm auch beenden wenn das Fenster geschlossen wird
main.protocol("WM_DELETE_WINDOW", ende)

#loop
main.mainloop()
