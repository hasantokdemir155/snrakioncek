
from ssql import *
import pyodbc

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from syfx33 import *


I=1
def snrk(): 
    #print('mmmmmm')
    global I
    I=I+1
    print(I)
    if I == 100:
         I=1
    print('mmmmmm')
    crs.execute('exec [nxt] @s=?',I)
        
    print(crs)
    for i,strvr in enumerate(crs):
                
            #print(locale.format_string("%.f", int(sutver),grouping=True))
          ui.tableWidget.setItem(i,0,QTableWidgetItem(str(strvr[0])))
          ui.tableWidget.setItem(i,1,QTableWidgetItem(str(strvr[1])))                
          ui.tableWidget.setItem(i,2,QTableWidgetItem(str(strvr[2])))
    
    
def onck():
    global I
    I=I-1
    if I == 0:
        I=1
    print('mmmmmm')
    crs.execute('exec [nxt] @s=?',I)
        
    print(crs)
    for i,strvr in enumerate(crs):
                
            #print(locale.format_string("%.f", int(sutver),grouping=True))
        ui.tableWidget.setItem(i,0,QTableWidgetItem(str(strvr[0])))
        ui.tableWidget.setItem(i,1,QTableWidgetItem(str(strvr[1])))                
        ui.tableWidget.setItem(i,2,QTableWidgetItem(str(strvr[2])))
    

conn = pyodbc.connect(
       "Driver={SQL Server Native Client 11.0};"
       "Server=HASAN\SQLEXPRESS1;"
       "Database=verx;"
       "Trusted_Connection=yes;"
    )

crs=conn.cursor()

uyg=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()

ui.setupUi(penAna)




ui.pushButton.clicked.connect(onck)
ui.pushButton_2.clicked.connect(snrk)
print(I)


penAna.show()
    
