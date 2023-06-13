# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from scada_ekran_4 import *
import sqlite3
import datetime
from pymodbus.client import ModbusTcpClient
import time
from time import sleep
from threading import Thread
import threading




uygulama= QApplication(sys.argv)
pencere= QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

baglanti =sqlite3.connect("sirnak_cimento_recete.db")
islem=baglanti.cursor()
baglanti.commit()
table=islem.execute("create table if not exists recete(recete_no int,recete_adi text, kum_1 int, kum_2 int, kum_3 int, cimento int, su int, katki int)")
baglanti.commit()



"""tarih=datetime.datetime.now()
ui.lb_date.setText(str(tarih))"""


#PLC_IP = "169.254.214.162"
PLC_IP = "127.0.0.1"
plc=502
UNIT=0x1
client = ModbusTcpClient(PLC_IP,plc  )
client.connect()




def tum_bitler_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil_1=client.read_coils(0,39)
    print("tum_bitler_guncelle")



    # TRTM_BND_Y
    if readcoil_1.bits[0]==False:
        ui.TRTM_BND_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[0]==True:
        ui.TRTM_BND_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # TRTM_VBR_Y
    if readcoil_1.bits[1]==False:
        ui.TRTM_VBR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[1]==True:
        ui.TRTM_VBR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # HDRLK_MTR_Y    
    if readcoil_1.bits[2]==False:
        ui.HDRLK_MTR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[2]==True:
        ui.HDRLK_MTR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # MKSR_ANA_Y 
    if readcoil_1.bits[3]==False:
        ui.MKSR_ANA_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[3]==True:
        ui.MKSR_ANA_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # HLZN_1_Y 
    if readcoil_1.bits[4]==False:
        ui.HLZN_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[4]==True:
        ui.HLZN_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # HLZN_2_Y 
    if readcoil_1.bits[5]==False:
        ui.HLZN_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[5]==True:
        ui.HLZN_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
        
    # KTK_PMP_1_Y 
    if readcoil_1.bits[6]==False:
        ui.KTK_PMP_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[6]==True:
        ui.KTK_PMP_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # KTK_PMP_2_Y
    if readcoil_1.bits[7]==False:
        ui.KTK_PMP_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[7]==True:
        ui.KTK_PMP_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # CMT_BNKR_VBR_Y
    if readcoil_1.bits[8]==False:
        ui.CMT_BNKR_VBR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[8]==True:
        ui.CMT_BNKR_VBR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # MKR_CKS_VB_Y    
    if readcoil_1.bits[9]==False:
        ui.MKR_CKS_VB_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[9]==True:
        ui.MKR_CKS_VB_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # BNKR_PSTN_1_Y 
    if readcoil_1.bits[10]==False:
        ui.BNKR_PSTN_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[10]==True:
        ui.BNKR_PSTN_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # BNKR_VBR_1_Y 
    if readcoil_1.bits[11]==False:
        ui.BNKR_VBR_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[11]==True:
        ui.BNKR_VBR_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # BNKR_PSTN_2_Y 
    if readcoil_1.bits[12]==False:
        ui.BNKR_PSTN_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[12]==True:
        ui.BNKR_PSTN_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
        
    # BNKR_VBR_2_Y 
    if readcoil_1.bits[13]==False:
        ui.BNKR_VBR_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[13]==True:
        ui.BNKR_VBR_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # BNKR_PSTN_3_Y 
    if readcoil_1.bits[14]==False:
        ui.BNKR_PSTN_3_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[14]==True:
        ui.BNKR_PSTN_3_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # BNKR_VBR_3_Y 
    if readcoil_1.bits[15]==False:
        ui.BNKR_VBR_3_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[15]==True:
        ui.BNKR_VBR_3_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # SRN_Y 
    if readcoil_1.bits[16]==False:
        ui.SRN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[16]==True:
        ui.SRN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
        
    # SU_DLM_VN_Y 
    if readcoil_1.bits[17]==False:
        ui.SU_DLM_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[17]==True:
        ui.SU_DLM_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # KTK_BSLT_VN_Y    
    if readcoil_1.bits[18]==False:
        ui.KTK_BSLT_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[18]==True:
        ui.KTK_BSLT_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # SU_BSLTM_VN_Y 
    if readcoil_1.bits[19]==False:
        ui.SU_BSLTM_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[19]==True:
        ui.SU_BSLTM_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # CMNT_BSLT_VN_Y 
    if readcoil_1.bits[20]==False:
        ui.CMNT_BSLT_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[20]==True:
        ui.CMNT_BSLT_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # TRNSFR_BND_Y 
    if readcoil_1.bits[21]==False:
        ui.TRNSFR_BND_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[21]==True:
        ui.TRNSFR_BND_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
        
    # MKSR_PSTN_ACM_Y 
    if readcoil_1.bits[22]==False:
        ui.MKSR_PSTN_ACM_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[22]==True:
        ui.MKSR_PSTN_ACM_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # MKSR_PSTN_KPTM_Y 
    if readcoil_1.bits[23]==False:
        ui.MKSR_PSTN_KPTM_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[23]==True:
        ui.MKSR_PSTN_KPTM_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # KMPRSR_Y 
    if readcoil_1.bits[24]==False:
        ui.KMPRSR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[24]==True:
        ui.KMPRSR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")

    # MANUEL_BİT 
    if readcoil_1.bits[25]==False:
        ui.mod_butonu.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[25]==True:
        ui.mod_butonu.setStyleSheet("background-color: rgb(0, 255, 127);")

    # proses_baslat_bit
    if readcoil_1.bits[26]==False:
        ui.proses_baslat_button.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[26]==True:
        ui.proses_baslat_button.setStyleSheet("background-color: rgb(0, 255, 127);")

    # acil_stop_bit
    if readcoil_1.bits[27]==False:
        ui.acil_stop_button.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[27]==True:
        ui.acil_stop_button.setStyleSheet("background-color: rgb(0, 255, 127);")

    # mikser_manuel_bosalt_button_bit
    if readcoil_1.bits[28]==False:
        ui.mikser_manuel_bosalt_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        ui.mikser_manuel_bosalt_button.setText("Mikser Boşaltma Kapağı Kapalı")
    elif readcoil_1.bits[28]==True:
        ui.mikser_manuel_bosalt_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        ui.mikser_manuel_bosalt_button.setText("Mikser Boşaltma Kapağı Açık")
client.close()
    
    


tum_bitler_guncelle()


def bunker_piston_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil_1=client.read_coils(33,3)
    # kum_1 piston 
    if readcoil_1.bits[0]==False:
        ui.kum_1_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[0]==True:
        ui.kum_1_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")
    # kum_2_piston_g
    if readcoil_1.bits[1]==False:
        ui.kum_2_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[1]==True:
        ui.kum_2_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")
    # kum_3_piston_g
    if readcoil_1.bits[2]==False:
        ui.kum_3_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[2]==True:
        ui.kum_3_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")







def bunker_vibro_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil_1=client.read_coils(36,3)
    # kum_1_vibro_g
    if readcoil_1.bits[0]==False:
        ui.kum_1_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[0]==True:
        ui.kum_1_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")
    # kum_2_vibro_g
    if readcoil_1.bits[1]==False:
        ui.kum_2_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[1]==True:
        ui.kum_2_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")
    # kum_3_vibro_g
    if readcoil_1.bits[2]==False:
        ui.kum_3_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil_1.bits[2]==True:
        ui.kum_3_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")





def Operation(arg):
    t1 = threading.currentThread()
    while getattr(t1, "x", True):
        tarih=datetime.datetime.now()
        ui.lb_date.setText(str(tarih))
        client = ModbusTcpClient(PLC_IP,plc  )
        client.connect()
        readcoil_1=client.read_coils(36,3)
        # kum_1_vibro_g
        if readcoil_1.bits[0]==False:
            ui.kum_1_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[0]==True:
            ui.kum_1_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        # kum_2_vibro_g
        if readcoil_1.bits[1]==False:
            ui.kum_2_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[1]==True:
            ui.kum_2_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        # kum_3_vibro_g
        if readcoil_1.bits[2]==False:
            ui.kum_3_vibro_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[2]==True:
            ui.kum_3_vibro_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        client = ModbusTcpClient(PLC_IP,plc  )
        client.connect()
        readcoil_1=client.read_coils(33,3)
        # kum_1 piston 
        if readcoil_1.bits[0]==False:
            ui.kum_1_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[0]==True:
            ui.kum_1_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        # kum_2_piston_g
        if readcoil_1.bits[1]==False:
            ui.kum_2_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[1]==True:
            ui.kum_2_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        # kum_3_piston_g
        if readcoil_1.bits[2]==False:
            ui.kum_3_piston_g.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif readcoil_1.bits[2]==True:
            ui.kum_3_piston_g.setStyleSheet("background-color: rgb(0, 255, 127);")
        client = ModbusTcpClient(PLC_IP,plc  )
        client.connect()
        receteler=client.read_holding_registers(19,1)
        su_sonuc_plc=receteler.registers[0]
        ui.lineEdit.setText(str(su_sonuc_plc))

        """bunker_vibro_oku()
        bunker_piston_oku()"""
        
        sleep(5)

        
t1 = threading.Thread(target=Operation, args=("task",))     

def thread():
    t1.start()
    
    
thread()






#***************************************************************************************************************************

#------------ÜRETİM PAGE-------------------------------------------------------------------------------

#***************************************************************************************************************************


#proses_baslat_click
def proses_baslat_click():


    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(26,1 )
    proses_baslat_bit=1-readcoil.bits[0]
    result=client.write_coils(26,[proses_baslat_bit])
    #tum_bitler_guncelle()
ui.proses_baslat_button.clicked.connect(proses_baslat_click)


#acil_stop_click
def acil_stop_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(27,1 )
    acil_stop_bit=1-readcoil.bits[0]
    result=client.write_coils(27,[acil_stop_bit])
    #tum_bitler_guncelle()
ui.acil_stop_button.clicked.connect(acil_stop_click)

#mikser_manuel_bosalt_button_click
def mikser_manuel_bosalt_button_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(28,1 )
    if readcoil.bits[0]==False:
        mikser_manuel_bosalt_button_onay = QMessageBox.question(pencere,"Mikser Boşaltma Kontrolü","Mikser Boşaltma Kapağını Açmak  İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)
    
        if mikser_manuel_bosalt_button_onay == QMessageBox.Yes:
            
            mikser_manuel_bosalt_button_bit=1-readcoil.bits[0]
            result=client.write_coils(28,[mikser_manuel_bosalt_button_bit])
            #tum_bitler_guncelle()
        else:
            ui.statusbar.showMessage("Mikser Boşaltma İşlemi İptal Edildi")
    elif readcoil.bits[0]==True:
        mikser_manuel_bosalt_button_bit=1-readcoil.bits[0]
        result=client.write_coils(28,[mikser_manuel_bosalt_button_bit])
        #tum_bitler_guncelle()



    
    
ui.mikser_manuel_bosalt_button.clicked.connect(mikser_manuel_bosalt_button_click)










#***************************************************************************************************************************

#------------REÇETE PAGE-------------------------------------------------------------------------------

#***************************************************************************************************************************


ui.tableWidget.clear()
ui.tableWidget.setHorizontalHeaderLabels(("Reçete No","Reçete Adı","Kum-1 Oranı","Kum-2 Oranı","Kum-3 Oranı","Çimento Oranı","Su Oranı","Katkı Oranı"))
ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
sorgu = "select * from recete"
islem.execute(sorgu)




def kayit_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    receteler=client.read_holding_registers(24,7)

    
    plc_kum_1=receteler.registers[0]
    plc_kum_2=receteler.registers[1]
    plc_kum_3=receteler.registers[2]
    plc_cimento=receteler.registers[3]
    plc_su=receteler.registers[4]
    plc_katki=receteler.registers[5]
    plc_recete_no=receteler.registers[6]
    plc_recete_adi_indis=int(plc_recete_no)-1
    
    
    #plc_recete_adi=ui.tableWidget.item(plc_recete_adi_indis,1).text()
    



    ui.tableWidget_2.clear()
    ui.tableWidget_2.setHorizontalHeaderLabels(("Reçete No","Kum-1 Oranı","Kum-2 Oranı","Kum-3 Oranı","Çimento Oranı","Su Oranı","Katkı Oranı"))
    ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    ui.tableWidget_2.setItem(0,0,QTableWidgetItem(str(plc_recete_no)))
    #ui.tableWidget_2.setItem(0,1,QTableWidgetItem(str(plc_recete_adi)))
    ui.tableWidget_2.setItem(0,1,QTableWidgetItem(str(plc_kum_1)))
    ui.tableWidget_2.setItem(0,2,QTableWidgetItem(str(plc_kum_2)))
    ui.tableWidget_2.setItem(0,3,QTableWidgetItem(str(plc_kum_3)))
    ui.tableWidget_2.setItem(0,4,QTableWidgetItem(str(plc_cimento)))
    ui.tableWidget_2.setItem(0,5,QTableWidgetItem(str(plc_su)))
    ui.tableWidget_2.setItem(0,6,QTableWidgetItem(str(plc_katki)))

kayit_guncelle()

def guncelle():
    
    

    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Reçete No","Reçete Adı","Kum-1 Oranı","Kum-2 Oranı","Kum-3 Oranı","Çimento Oranı","Su Oranı","Katkı Oranı"))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from recete"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
ui.vt_guncelle.clicked.connect(guncelle)

guncelle()

def vt_kaydet():

    ln_recete_no=ui.ln_recete_no.text()
    ln_recete_adi=ui.ln_recete_adi.text()
    ln_kum_1=ui.ln_kum_1.text()
    ln_kum_2=ui.ln_kum_2.text()
    ln_kum_3=ui.ln_kum_3.text()
    ln_cimento=ui.ln_cimento.text()
    ln_su=ui.ln_su.text()
    ln_katki=ui.ln_katki.text()
    sorgu = "select * from recete"
    islem.execute(sorgu)
    recete_no_liste=[]
    recete_no_scan=0
    for indexSatir, kayitNumarasi in enumerate(islem):
        recete_no_liste.append(kayitNumarasi[0])
    
    if (int(ln_recete_no) in recete_no_liste): 
        recete_no_scan=1

    try:
        if ln_recete_no=="" or ln_recete_adi==""  or    ln_kum_1=="" or ln_kum_2=="" or ln_kum_3=="" or ln_cimento=="" or ln_su=="" or ln_katki=="":
            recete_kayit_bos_uyari = QMessageBox.question(pencere,"Reçete Değerlerinde Hata","Lütfen Reçetenin Tüm Değerlerini Doldurunuz",QMessageBox.Yes )
        elif recete_no_scan==0 and int(ln_recete_no)>=1 and int(ln_recete_no) <=20 and int(ln_kum_1)>=0 and int(ln_kum_1)<=65535 and int(ln_kum_2)>=0 and int(ln_kum_2) <=65535 and int(ln_kum_3)>=0 and int(ln_kum_3)<=65535 and int(ln_cimento)>=0 and int(ln_cimento)<=65535 and int(ln_su)>=0 and int(ln_su)<=65535 and int(ln_katki)>=0 and int(ln_katki)<=65535:
            ekle="insert into recete (recete_no,recete_adi , kum_1 , kum_2 , kum_3 , cimento , su , katki ) values (?,?,?,?,?,?,?,?)"
            islem.execute(ekle,(int(ln_recete_no),ln_recete_adi,int(ln_kum_1),int(ln_kum_2),int(ln_kum_3),int(ln_cimento),int(ln_su),int(ln_katki)))
            baglanti.commit()
            islem.execute(sorgu)
        elif recete_no_scan==1:
            recete_kayit_bos_uyari = QMessageBox.question(pencere,"Reçete Değerlerinde Hata","Aynı Reçete Numarası Girdiniz",QMessageBox.Yes )
        else:
            recete_kayit_bos_uyari = QMessageBox.question(pencere,"Reçete Değerlerinde Hata","Reçetelerde Limit Dışında Değer Girdiniz",QMessageBox.Yes )
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Eklenemedi Hata Çıktı === "+str(error))
        recete_kayit_bos_uyari = QMessageBox.question(pencere,"Reçete Değerlerinde Beklenmedik Hata","Lütfen Reçete Bölümününün Tüm Değerlerini Tekrar Kontrol Ediniz...",QMessageBox.Yes )
    
    guncelle()


ui.vt_kaydet.clicked.connect(vt_kaydet)


def kayit_sil():

    sil_mesaj = QMessageBox.question(pencere,"Silme Onayı","Silmek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)
   
    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tableWidget.selectedItems()
        silinecek_kayit = secilen_kayit[0].text()
        
        sorgu = "delete from recete where recete_no = ?"
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Başarıyla Silindi")
            guncelle()
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Silinirken Hata Çıktı === "+str(error))
    
    else:
        ui.statusbar.showMessage("Silme İşlemi İptal Edildi")

ui.vt_sil.clicked.connect(kayit_sil)

def recete_gonder():
    

    try:
        client = ModbusTcpClient(PLC_IP,plc  )
        client.connect()
        ui.tableWidget_2.clear()
        ui.tableWidget_2.setHorizontalHeaderLabels(("Reçete No","Reçete Adı","Kum-1 Oranı","Kum-2 Oranı","Kum-3 Oranı","Çimento Oranı","Su Oranı","Katkı Oranı"))
        ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        secilen_kayit = ui.tableWidget.selectedItems()
        kayit_recete_no = secilen_kayit[0].text()
        kayit_recete_adi=secilen_kayit[1].text()
        kayit_kum_1=secilen_kayit[2].text()
        kayit_kum_2=secilen_kayit[3].text()
        kayit_kum_3=secilen_kayit[4].text()
        kayit_cimento=secilen_kayit[5].text()
        kayit_su=secilen_kayit[6].text()
        kayit_katki=secilen_kayit[7].text()
        print("PLC'ye Gönderilen Reçete No:",kayit_recete_no)
        print("PLC'ye Gönderilen Reçete Adı:",kayit_recete_adi)
        client.write_registers(24,int(kayit_kum_1))
        client.write_registers(25,int(kayit_kum_2))
        client.write_registers(26,int(kayit_kum_3))
        client.write_registers(27,int(kayit_cimento))
        client.write_registers(28,int(kayit_su))
        client.write_registers(29,int(kayit_katki))
        client.write_registers(30,int(kayit_recete_no))
        kayit_guncelle()


        
    except Exception as error:
        recete_gonder_secilmedi = QMessageBox.question(pencere,"Reçete Seçili Değil","Lütfen Reçete Kayıt Bölümünden Göndermek İstediğiniz Reçeteyi Seçiniz...",QMessageBox.Yes )
   


ui.recete_gonder.clicked.connect(recete_gonder)





#***************************************************************************************************************************

#------------KALİBRASYON PAGE-------------------------------------------------------------------------------

#***************************************************************************************************************************


#  ----CİMENTO KALİBRASYON DEGER OKU-----
def cmnt_kalibrasyon_deger_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    cmnt_oku=client.read_holding_registers(0,4)
    cmnt_oku_2=client.read_holding_registers(16,2)

    cmnt_bos_deger=cmnt_oku.registers[0]
    cmnt_dolu_deger=cmnt_oku.registers[1]
    cmnt_bos_kg=cmnt_oku.registers[2]
    cmnt_dolu_kg=cmnt_oku.registers[3]
    cmnt_olculen_deger_modbus=cmnt_oku_2.registers[0]
    cmnt_sonuc_kg=cmnt_oku_2.registers[1]

    ui.ln_cmnt_bos_deger.setText(str(cmnt_bos_deger))
    ui.ln_cmnt_dolu_deger.setText(str(cmnt_dolu_deger))
    ui.ln_cmnt_bos_kg.setText(str(cmnt_bos_kg))
    ui.ln_cmnt_dolu_kg.setText(str(cmnt_dolu_kg))
    ui.ln_cmnt_ham.setText(str(cmnt_olculen_deger_modbus))
    ui.ln_cmnt_sonuc_kg.setText(str(cmnt_sonuc_kg))

ui.lb_cmnt_kalibrasyon_deger_oku.clicked.connect(cmnt_kalibrasyon_deger_oku)


#  ----SU KALİBRASYON DEGER OKU-----
def su_kalibrasyon_deger_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    su_oku=client.read_holding_registers(4,4)
    su_oku_2=client.read_holding_registers(18,2)

    su_bos_deger=su_oku.registers[0]
    su_dolu_deger=su_oku.registers[1]
    su_bos_kg=su_oku.registers[2]
    su_dolu_kg=su_oku.registers[3]
    su_olculen_deger_modbus=su_oku_2.registers[0]
    su_sonuc_kg=su_oku_2.registers[1]

    ui.ln_su_bos_deger.setText(str(su_bos_deger))
    ui.ln_su_dolu_deger.setText(str(su_dolu_deger))
    ui.ln_su_bos_kg.setText(str(su_bos_kg))
    ui.ln_su_dolu_kg.setText(str(su_dolu_kg))
    ui.ln_su_ham.setText(str(su_olculen_deger_modbus))
    ui.ln_su_sonuc_kg.setText(str(su_sonuc_kg))

ui.lb_su_kalibrasyon_deger_oku.clicked.connect(su_kalibrasyon_deger_oku)

#  ----KATKI KALİBRASYON DEGER OKU-----
def katki_kalibrasyon_deger_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    katki_oku=client.read_holding_registers(8,4)
    katki_oku_2=client.read_holding_registers(18,2)

    katki_bos_deger=katki_oku.registers[0]
    katki_dolu_deger=katki_oku.registers[1]
    katki_bos_kg=katki_oku.registers[2]
    katki_dolu_kg=katki_oku.registers[3]
    katki_olculen_deger_modbus=katki_oku_2.registers[0]
    katki_sonuc_kg=katki_oku_2.registers[1]

    ui.ln_katki_bos_deger.setText(str(katki_bos_deger))
    ui.ln_katki_dolu_deger.setText(str(katki_dolu_deger))
    ui.ln_katki_bos_kg.setText(str(katki_bos_kg))
    ui.ln_katki_dolu_kg.setText(str(katki_dolu_kg))
    ui.ln_katki_ham.setText(str(katki_olculen_deger_modbus))
    ui.ln_katki_sonuc_kg.setText(str(katki_sonuc_kg))

ui.lb_katki_kalibrasyon_deger_oku.clicked.connect(katki_kalibrasyon_deger_oku)

#  ----TARTIM BANDI KALİBRASYON DEGER OKU-----
def tartim_bandi_kalibrasyon_deger_oku():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    tartim_bandi_oku=client.read_holding_registers(12,4)
    tartim_bandi_oku_2=client.read_holding_registers(20,2)

    tartim_bandi_bos_deger=tartim_bandi_oku.registers[0]
    tartim_bandi_dolu_deger=tartim_bandi_oku.registers[1]
    tartim_bandi_bos_kg=tartim_bandi_oku.registers[2]
    tartim_bandi_dolu_kg=tartim_bandi_oku.registers[3]
    tartim_bandi_olculen_deger_modbus=tartim_bandi_oku_2.registers[0]
    tartim_bandi_sonuc_kg=tartim_bandi_oku_2.registers[1]

    ui.ln_tartim_bandi_bos_deger.setText(str(tartim_bandi_bos_deger))
    ui.ln_tartim_bandi_dolu_deger.setText(str(tartim_bandi_dolu_deger))
    ui.ln_tartim_bandi_bos_kg.setText(str(tartim_bandi_bos_kg))
    ui.ln_tartim_bandi_dolu_kg.setText(str(tartim_bandi_dolu_kg))
    ui.ln_tartim_bandi_ham.setText(str(tartim_bandi_olculen_deger_modbus))
    ui.ln_tartim_bandi_sonuc_kg.setText(str(tartim_bandi_sonuc_kg))

ui.lb_tartim_bandi_kalibrasyon_deger_oku.clicked.connect(tartim_bandi_kalibrasyon_deger_oku)



#  ----CİMENTO KALİBRASYON GUNCELLE-----
def cmnt_kalibrasyon_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    cmnt_bos_deger=ui.ln_cmnt_bos_deger.text()
    cmnt_dolu_deger=ui.ln_cmnt_dolu_deger.text()
    cmnt_bos_kg=ui.ln_cmnt_bos_kg.text()
    cmnt_dolu_kg=ui.ln_cmnt_dolu_kg.text()


    try:
        if cmnt_bos_deger=="" or cmnt_dolu_deger=="" or cmnt_bos_kg=="" or cmnt_dolu_kg=="" :
            cmnt_bos_uyari = QMessageBox.question(pencere,"Çimento Değerlerinde Hata","Lütfen Çimento Bölümününün Tüm Değerlerini Doldurunuz",QMessageBox.Yes )
        elif int(cmnt_bos_deger)>=0 and int(cmnt_bos_deger) <=65535 and int(cmnt_dolu_deger)>=0 and int(cmnt_dolu_deger)<=65535 and int(cmnt_bos_kg)>=0 and int(cmnt_bos_kg) <=65535 and int(cmnt_dolu_kg)>=0 and int(cmnt_dolu_kg)<=65535:
            client.write_registers(0,int(cmnt_bos_deger))
            client.write_registers(1,int(cmnt_dolu_deger))
            client.write_registers(2,int(cmnt_bos_kg))
            client.write_registers(3,int(cmnt_dolu_kg))
            
        else:
            cmnt_bos_uyari = QMessageBox.question(pencere,"Çimento Değerlerinde Hata","Çimento Bölümününde Limit Dışında Değer Girdiniz",QMessageBox.Yes )
    except:
        cmnt_bos_uyari = QMessageBox.question(pencere,"Çimento Değerlerinde Beklenmedik Hata","Lütfen Çimento Bölümününün Tüm Değerlerini Tekrar Kontrol Ediniz...",QMessageBox.Yes )

ui.lb_cmnt_kalibrasyon_guncelle.clicked.connect(cmnt_kalibrasyon_guncelle)

#  ----SU KALİBRASYON GUNCELLE-----
def su_kalibrasyon_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    su_bos_deger=ui.ln_su_bos_deger.text()
    su_dolu_deger=ui.ln_su_dolu_deger.text()
    su_bos_kg=ui.ln_su_bos_kg.text()
    su_dolu_kg=ui.ln_su_dolu_kg.text()


    try:
        if su_bos_deger=="" or su_dolu_deger=="" or su_bos_kg=="" or su_dolu_kg=="" :
            su_bos_uyari = QMessageBox.question(pencere,"Su Değerlerinde Hata","Lütfen Su Bölümününün Tüm Değerlerini Doldurunuz",QMessageBox.Yes )
        elif int(su_bos_deger)>=0 and int(su_bos_deger) <=65535 and int(su_dolu_deger)>=0 and int(su_dolu_deger)<=65535 and int(su_bos_kg)>=0 and int(su_bos_kg) <=65535 and int(su_dolu_kg)>=0 and int(su_dolu_kg)<=65535:
            client.write_registers(4,int(su_bos_deger))
            client.write_registers(5,int(su_dolu_deger))
            client.write_registers(6,int(su_bos_kg))
            client.write_registers(7,int(su_dolu_kg))
        else:
            su_bos_uyari = QMessageBox.question(pencere,"Su Değerlerinde Hata","Su Bölümününde Limit Dışında Değer Girdiniz",QMessageBox.Yes )
    except:
        cmnt_bos_uyari = QMessageBox.question(pencere,"Su Değerlerinde Beklenmedik Hata","Lütfen Su Bölümününün Tüm Değerlerini Tekrar Kontrol Ediniz...",QMessageBox.Yes )


ui.lb_su_kalibrasyon_guncelle.clicked.connect(su_kalibrasyon_guncelle)

#  ----KATKI KALİBRASYON GUNCELLE-----
def katki_kalibrasyon_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    katki_bos_deger=ui.ln_katki_bos_deger.text()
    katki_dolu_deger=ui.ln_katki_dolu_deger.text()
    katki_bos_kg=ui.ln_katki_bos_kg.text()
    katki_dolu_kg=ui.ln_katki_dolu_kg.text()
    
    try:
        if katki_bos_deger=="" or katki_dolu_deger=="" or katki_bos_kg=="" or katki_dolu_kg=="" :
            katki_bos_uyari = QMessageBox.question(pencere,"Katkı Değerlerinde Hata","Lütfen Katkı Bölümününün Tüm Değerlerini Doldurunuz",QMessageBox.Yes )
        elif int(katki_bos_deger)>=0 and int(katki_bos_deger) <=65535 and int(katki_dolu_deger)>=0 and int(katki_dolu_deger)<=65535 and int(katki_bos_kg)>=0 and int(katki_bos_kg) <=65535 and int(katki_dolu_kg)>=0 and int(katki_dolu_kg)<=65535:
            client.write_registers(8,int(katki_bos_deger))
            client.write_registers(9,int(katki_dolu_deger))
            client.write_registers(10,int(katki_bos_kg))
            client.write_registers(11,int(katki_dolu_kg))
        else:
            katki_bos_uyari = QMessageBox.question(pencere,"Katki Değerlerinde Hata","Katkı Bölümününde Limit Dışında Değer Girdiniz",QMessageBox.Yes )
    except:
        cmnt_bos_uyari = QMessageBox.question(pencere,"Katki Değerlerinde Beklenmedik Hata","Lütfen Katki Bölümününün Tüm Değerlerini Tekrar Kontrol Ediniz...",QMessageBox.Yes )


ui.lb_katki_kalibrasyon_guncelle.clicked.connect(katki_kalibrasyon_guncelle)


#  ----TARTIM BANDI KALİBRASYON GUNCELLE-----
def tartim_bandi_kalibrasyon_guncelle():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    tartim_bandi_bos_deger=ui.ln_tartim_bandi_bos_deger.text()
    tartim_bandi_dolu_deger=ui.ln_tartim_bandi_dolu_deger.text()
    tartim_bandi_bos_kg=ui.ln_tartim_bandi_bos_kg.text()
    tartim_bandi_dolu_kg=ui.ln_tartim_bandi_dolu_kg.text()

    try:
        if tartim_bandi_bos_deger=="" or tartim_bandi_dolu_deger=="" or tartim_bandi_bos_kg=="" or tartim_bandi_dolu_kg=="" :
            tartim_bandi_bos_uyari = QMessageBox.question(pencere,"Tartım Bandı Değerlerinde Hata","Lütfen Tartım Bandı Bölümününün Tüm Değerlerini Doldurunuz",QMessageBox.Yes )
        elif int(tartim_bandi_bos_deger)>=0 and int(tartim_bandi_bos_deger) <=65535 and int(tartim_bandi_dolu_deger)>=0 and int(tartim_bandi_dolu_deger)<=65535 and int(tartim_bandi_bos_kg)>=0 and int(tartim_bandi_bos_kg) <=65535 and int(tartim_bandi_dolu_kg)>=0 and int(tartim_bandi_dolu_kg)<=65535:
            client.write_registers(12,int(tartim_bandi_bos_deger))
            client.write_registers(13,int(tartim_bandi_dolu_deger))
            client.write_registers(14,int(tartim_bandi_bos_kg))
            client.write_registers(15,int(tartim_bandi_dolu_kg))
        else:
            tartim_bandi_bos_uyari = QMessageBox.question(pencere,"Tartım Bandı Değerlerinde Hata","Tartım Bandı Bölümününde Limit Dışında Değer Girdiniz",QMessageBox.Yes )
    except:
        cmnt_bos_uyari = QMessageBox.question(pencere,"Tartım Bandı Değerlerinde Beklenmedik Hata","Lütfen Tartım Bandı Bölümününün Tüm Değerlerini Tekrar Kontrol Ediniz...",QMessageBox.Yes )


ui.lb_tartim_bandi_kalibrasyon_guncelle.clicked.connect(tartim_bandi_kalibrasyon_guncelle)




#***************************************************************************************************************************

#------------MANUEL PAGE-------------------------------------------------------------------------------

#***************************************************************************************************************************






#MANUEL click
def manuel_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(25,1 )
    manuel_bit=1-readcoil.bits[0]
    result=client.write_coils(25,[manuel_bit])
    #tum_bitler_guncelle()
ui.mod_butonu.clicked.connect(manuel_click)


#TRTM_BND_Y_click
def TRTM_BND_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(0,1 )
    TRTM_BND_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(0,[TRTM_BND_Y_bit])
    readcoil=client.read_coils(0,1 )
    if readcoil.bits[0]==False:
        ui.TRTM_BND_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.TRTM_BND_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
ui.TRTM_BND_Y.clicked.connect(TRTM_BND_Y_click)


#TRTM_VBR_Y_click
def TRTM_VBR_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(1,1 )
    TRTM_VBR_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(1,[TRTM_VBR_Y_bit])
    readcoil=client.read_coils(1,1 )
    # TRTM_VBR_Y
    if readcoil.bits[0]==False:
        ui.TRTM_VBR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.TRTM_VBR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
ui.TRTM_VBR_Y.clicked.connect(TRTM_VBR_Y_click)


#HDRLK_MTR_Y_click
def HDRLK_MTR_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(2,1 )
    HDRLK_MTR_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(2,[HDRLK_MTR_Y_bit])
    readcoil=client.read_coils(2,1 )
    # HDRLK_MTR_Y    
    if readcoil.bits[0]==False:
        ui.HDRLK_MTR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.HDRLK_MTR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.HDRLK_MTR_Y.clicked.connect(HDRLK_MTR_Y_click)


#MKSR_ANA_Y_click
def MKSR_ANA_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(3,1 )
    MKSR_ANA_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(3,[MKSR_ANA_Y_bit])
    readcoil=client.read_coils(3,1 )
    # MKSR_ANA_Y 
    if readcoil.bits[0]==False:
        ui.MKSR_ANA_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.MKSR_ANA_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.MKSR_ANA_Y.clicked.connect(MKSR_ANA_Y_click)

#HLZN_1_Y_click
def HLZN_1_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(4,1 )
    HLZN_1_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(4,[HLZN_1_Y_bit])
    readcoil=client.read_coils(4,1 )
    if readcoil.bits[0]==False:
        ui.HLZN_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.HLZN_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.HLZN_1_Y.clicked.connect(HLZN_1_Y_click)

#HLZN_2_Y_click
def HLZN_2_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(5,1 )
    HLZN_2_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(5,[HLZN_2_Y_bit])
    readcoil=client.read_coils(5,1 )
    if readcoil.bits[0]==False:
        ui.HLZN_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.HLZN_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.HLZN_2_Y.clicked.connect(HLZN_2_Y_click)

#KTK_PMP_1_Y_click
def KTK_PMP_1_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(6,1 )
    KTK_PMP_1_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(6,[KTK_PMP_1_Y_bit])
    readcoil=client.read_coils(6,1 )
    if readcoil.bits[0]==False:
        ui.KTK_PMP_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.KTK_PMP_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.KTK_PMP_1_Y.clicked.connect(KTK_PMP_1_Y_click)


#KTK_PMP_2_Y_click
def KTK_PMP_2_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(7,1 )
    KTK_PMP_2_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(7,[KTK_PMP_2_Y_bit])
    readcoil=client.read_coils(7,1 )
    if readcoil.bits[0]==False:
        ui.KTK_PMP_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.KTK_PMP_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.KTK_PMP_2_Y.clicked.connect(KTK_PMP_2_Y_click)


#CMT_BNKR_VBR_Y_click
def CMT_BNKR_VBR_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(8,1 )
    CMT_BNKR_VBR_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(8,[CMT_BNKR_VBR_Y_bit])
    readcoil=client.read_coils(8,1 )
    if readcoil.bits[0]==False:
        ui.CMT_BNKR_VBR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.CMT_BNKR_VBR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.CMT_BNKR_VBR_Y.clicked.connect(CMT_BNKR_VBR_Y_click)

#MKR_CKS_VB_Y_click
def MKR_CKS_VB_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(9,1 )
    MKR_CKS_VB_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(9,[MKR_CKS_VB_Y_bit])
    readcoil=client.read_coils(9,1 )
    if readcoil.bits[0]==False:
        ui.MKR_CKS_VB_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.MKR_CKS_VB_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.MKR_CKS_VB_Y.clicked.connect(MKR_CKS_VB_Y_click)


#BNKR_PSTN_1_Y_click
def BNKR_PSTN_1_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(10,1 )
    BNKR_PSTN_1_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(10,[BNKR_PSTN_1_Y_bit])
    readcoil=client.read_coils(10,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_PSTN_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_PSTN_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_PSTN_1_Y.clicked.connect(BNKR_PSTN_1_Y_click)


#BNKR_VBR_1_Y_click
def BNKR_VBR_1_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(11,1 )
    BNKR_VBR_1_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(11,[BNKR_VBR_1_Y_bit])
    readcoil=client.read_coils(11,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_VBR_1_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_VBR_1_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_VBR_1_Y.clicked.connect(BNKR_VBR_1_Y_click)


#BNKR_PSTN_2_Y_click
def BNKR_PSTN_2_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(12,1 )
    BNKR_PSTN_2_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(12,[BNKR_PSTN_2_Y_bit])
    readcoil=client.read_coils(12,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_PSTN_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_PSTN_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_PSTN_2_Y.clicked.connect(BNKR_PSTN_2_Y_click)


#BNKR_VBR_2_Y_click
def BNKR_VBR_2_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(13,1 )
    BNKR_VBR_2_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(13,[BNKR_VBR_2_Y_bit])
    readcoil=client.read_coils(13,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_VBR_2_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_VBR_2_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_VBR_2_Y.clicked.connect(BNKR_VBR_2_Y_click)

#BNKR_PSTN_3_Y_click
def BNKR_PSTN_3_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(14,1 )
    BNKR_PSTN_3_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(14,[BNKR_PSTN_3_Y_bit])
    readcoil=client.read_coils(14,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_PSTN_3_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_PSTN_3_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_PSTN_3_Y.clicked.connect(BNKR_PSTN_3_Y_click)

#BNKR_VBR_3_Y_click
def BNKR_VBR_3_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(15,1 )
    BNKR_VBR_3_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(15,[BNKR_VBR_3_Y_bit])
    readcoil=client.read_coils(15,1 )
    if readcoil.bits[0]==False:
        ui.BNKR_VBR_3_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.BNKR_VBR_3_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.BNKR_VBR_3_Y.clicked.connect(BNKR_VBR_3_Y_click)

#SRN_Y_click
def SRN_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(16,1 )
    SRN_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(16,[SRN_Y_bit])
    readcoil=client.read_coils(16,1 )
    if readcoil.bits[0]==False:
        ui.SRN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.SRN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.SRN_Y.clicked.connect(SRN_Y_click)

#SU_DLM_VN_Y_click
def SU_DLM_VN_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(17,1 )
    SU_DLM_VN_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(17,[SU_DLM_VN_Y_bit])
    readcoil=client.read_coils(17,1 )
    if readcoil.bits[0]==False:
        ui.SU_DLM_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.SU_DLM_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.SU_DLM_VN_Y.clicked.connect(SU_DLM_VN_Y_click)


#KTK_BSLT_VN_Y_click
def KTK_BSLT_VN_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(18,1 )
    KTK_BSLT_VN_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(18,[KTK_BSLT_VN_Y_bit])
    readcoil=client.read_coils(18,1 )
    if readcoil.bits[0]==False:
        ui.KTK_BSLT_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.KTK_BSLT_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.KTK_BSLT_VN_Y.clicked.connect(KTK_BSLT_VN_Y_click)


#SU_BSLTM_VN_Y_click
def SU_BSLTM_VN_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(19,1 )
    SU_BSLTM_VN_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(19,[SU_BSLTM_VN_Y_bit])
    readcoil=client.read_coils(19,1 )
    if readcoil.bits[0]==False:
        ui.SU_BSLTM_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.SU_BSLTM_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.SU_BSLTM_VN_Y.clicked.connect(SU_BSLTM_VN_Y_click)


#CMNT_BSLT_VN_Y_click
def CMNT_BSLT_VN_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(20,1 )
    CMNT_BSLT_VN_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(20,[CMNT_BSLT_VN_Y_bit])
    readcoil=client.read_coils(20,1 )
    if readcoil.bits[0]==False:
        ui.CMNT_BSLT_VN_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.CMNT_BSLT_VN_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.CMNT_BSLT_VN_Y.clicked.connect(CMNT_BSLT_VN_Y_click)

#TRNSFR_BND_Y_click
def TRNSFR_BND_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(21,1 )
    TRNSFR_BND_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(21,[TRNSFR_BND_Y_bit])
    readcoil=client.read_coils(21,1 )
    if readcoil.bits[0]==False:
        ui.TRNSFR_BND_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.TRNSFR_BND_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.TRNSFR_BND_Y.clicked.connect(TRNSFR_BND_Y_click)

#MKSR_PSTN_ACM_Y_click
def MKSR_PSTN_ACM_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(22,1 )
    MKSR_PSTN_ACM_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(22,[MKSR_PSTN_ACM_Y_bit])
    readcoil=client.read_coils(22,1 )
    if readcoil.bits[0]==False:
        ui.MKSR_PSTN_ACM_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.MKSR_PSTN_ACM_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.MKSR_PSTN_ACM_Y.clicked.connect(MKSR_PSTN_ACM_Y_click)

#MKSR_PSTN_KPTM_Y_click
def MKSR_PSTN_KPTM_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(23,1 )
    MKSR_PSTN_KPTM_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(23,[MKSR_PSTN_KPTM_Y_bit])
    readcoil=client.read_coils(23,1 )
    if readcoil.bits[0]==False:
        ui.MKSR_PSTN_KPTM_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.MKSR_PSTN_KPTM_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
ui.MKSR_PSTN_KPTM_Y.clicked.connect(MKSR_PSTN_KPTM_Y_click)

#KMPRSR_Y_click
def KMPRSR_Y_click():
    client = ModbusTcpClient(PLC_IP,plc  )
    client.connect()
    readcoil=client.read_coils(24,1 )
    KMPRSR_Y_bit=1-readcoil.bits[0]
    result=client.write_coils(24,[KMPRSR_Y_bit])
    readcoil=client.read_coils(24,1 )
    if readcoil.bits[0]==False:
        ui.KMPRSR_Y.setStyleSheet("background-color: rgb(255, 0, 0);")
    elif readcoil.bits[0]==True:
        ui.KMPRSR_Y.setStyleSheet("background-color: rgb(0, 255, 127);")
    #tum_bitler_guncelle()
    
ui.KMPRSR_Y.clicked.connect(KMPRSR_Y_click)


uygulama_kapandı=uygulama.exec()
if int(uygulama_kapandı)==0:
    print("uygulama_kapattın")
    t1.x=False
   


