#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Project   : Elevator Dispatch
# 
# @Purpose   : Assignment of Operaint System
#
# @Time      : 05/08/2019
#
# @Author    : Feifan Wang
#
# @Student ID: 1751694
#
# @Filename  : Dispatch.py

import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from Interface import Ui_MainWindow

class Elevator:
    def __init__(self,parent=None):
        super(Elevator,self).__init__()
        self.statusFree=True
        self.statusUp=False
        self.statusDown=False
        self.currentFloor=1
        self.goList=[]

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' interactions on interface '''
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1u.clicked.connect(lambda:self.up(1))
        self.ui.pushButton_2u.clicked.connect(lambda:self.up(2))
        self.ui.pushButton_3u.clicked.connect(lambda:self.up(3))
        self.ui.pushButton_4u.clicked.connect(lambda:self.up(4))
        self.ui.pushButton_5u.clicked.connect(lambda:self.up(5))
        self.ui.pushButton_6u.clicked.connect(lambda:self.up(6))
        self.ui.pushButton_7u.clicked.connect(lambda:self.up(7))
        self.ui.pushButton_8u.clicked.connect(lambda:self.up(8))
        self.ui.pushButton_9u.clicked.connect(lambda:self.up(9))
        self.ui.pushButton_10u.clicked.connect(lambda:self.up(10))
        self.ui.pushButton_11u.clicked.connect(lambda:self.up(11))
        self.ui.pushButton_12u.clicked.connect(lambda:self.up(12))
        self.ui.pushButton_13u.clicked.connect(lambda:self.up(13))
        self.ui.pushButton_14u.clicked.connect(lambda:self.up(14))
        self.ui.pushButton_15u.clicked.connect(lambda:self.up(15))
        self.ui.pushButton_16u.clicked.connect(lambda:self.up(16))
        self.ui.pushButton_17u.clicked.connect(lambda:self.up(17))
        self.ui.pushButton_18u.clicked.connect(lambda:self.up(18))
        self.ui.pushButton_19u.clicked.connect(lambda:self.up(19))
        self.ui.pushButton_2d.clicked.connect(lambda:self.down(2))
        self.ui.pushButton_3d.clicked.connect(lambda:self.down(3))
        self.ui.pushButton_4d.clicked.connect(lambda:self.down(4))
        self.ui.pushButton_5d.clicked.connect(lambda:self.down(5))
        self.ui.pushButton_6d.clicked.connect(lambda:self.down(6))
        self.ui.pushButton_7d.clicked.connect(lambda:self.down(7))
        self.ui.pushButton_8d.clicked.connect(lambda:self.down(8))
        self.ui.pushButton_9d.clicked.connect(lambda:self.down(9))
        self.ui.pushButton_10d.clicked.connect(lambda:self.down(10))
        self.ui.pushButton_11d.clicked.connect(lambda:self.down(11))
        self.ui.pushButton_12d.clicked.connect(lambda:self.down(12))
        self.ui.pushButton_13d.clicked.connect(lambda:self.down(13))
        self.ui.pushButton_14d.clicked.connect(lambda:self.down(14))
        self.ui.pushButton_15d.clicked.connect(lambda:self.down(15))
        self.ui.pushButton_16d.clicked.connect(lambda:self.down(16))
        self.ui.pushButton_17d.clicked.connect(lambda:self.down(17))
        self.ui.pushButton_18d.clicked.connect(lambda:self.down(18))
        self.ui.pushButton_19d.clicked.connect(lambda:self.down(19))
        self.ui.pushButton_20d.clicked.connect(lambda:self.down(20))
        self.ui.elevator1_1.clicked.connect(lambda:self.insidePush(1,1))
        self.ui.elevator1_2.clicked.connect(lambda:self.insidePush(1,2))
        self.ui.elevator1_3.clicked.connect(lambda:self.insidePush(1,3))
        self.ui.elevator1_4.clicked.connect(lambda:self.insidePush(1,4))
        self.ui.elevator1_5.clicked.connect(lambda:self.insidePush(1,5))
        self.ui.elevator1_6.clicked.connect(lambda:self.insidePush(1,6))
        self.ui.elevator1_7.clicked.connect(lambda:self.insidePush(1,7))
        self.ui.elevator1_8.clicked.connect(lambda:self.insidePush(1,8))
        self.ui.elevator1_9.clicked.connect(lambda:self.insidePush(1,9))
        self.ui.elevator1_10.clicked.connect(lambda:self.insidePush(1,10))
        self.ui.elevator1_11.clicked.connect(lambda:self.insidePush(1,11))
        self.ui.elevator1_12.clicked.connect(lambda:self.insidePush(1,12))
        self.ui.elevator1_13.clicked.connect(lambda:self.insidePush(1,13))
        self.ui.elevator1_14.clicked.connect(lambda:self.insidePush(1,14))
        self.ui.elevator1_15.clicked.connect(lambda:self.insidePush(1,15))
        self.ui.elevator1_16.clicked.connect(lambda:self.insidePush(1,16))
        self.ui.elevator1_17.clicked.connect(lambda:self.insidePush(1,17))
        self.ui.elevator1_18.clicked.connect(lambda:self.insidePush(1,18))
        self.ui.elevator1_19.clicked.connect(lambda:self.insidePush(1,19))
        self.ui.elevator1_20.clicked.connect(lambda:self.insidePush(1,20))
        self.ui.elevator2_1.clicked.connect(lambda:self.insidePush(2,1))
        self.ui.elevator2_2.clicked.connect(lambda:self.insidePush(2,2))
        self.ui.elevator2_3.clicked.connect(lambda:self.insidePush(2,3))
        self.ui.elevator2_4.clicked.connect(lambda:self.insidePush(2,4))
        self.ui.elevator2_5.clicked.connect(lambda:self.insidePush(2,5))
        self.ui.elevator2_6.clicked.connect(lambda:self.insidePush(2,6))
        self.ui.elevator2_7.clicked.connect(lambda:self.insidePush(2,7))
        self.ui.elevator2_8.clicked.connect(lambda:self.insidePush(2,8))
        self.ui.elevator2_9.clicked.connect(lambda:self.insidePush(2,9))
        self.ui.elevator2_10.clicked.connect(lambda:self.insidePush(2,10))
        self.ui.elevator2_11.clicked.connect(lambda:self.insidePush(2,11))
        self.ui.elevator2_12.clicked.connect(lambda:self.insidePush(2,12))
        self.ui.elevator2_13.clicked.connect(lambda:self.insidePush(2,13))
        self.ui.elevator2_14.clicked.connect(lambda:self.insidePush(2,14))
        self.ui.elevator2_15.clicked.connect(lambda:self.insidePush(2,15))
        self.ui.elevator2_16.clicked.connect(lambda:self.insidePush(2,16))
        self.ui.elevator2_17.clicked.connect(lambda:self.insidePush(2,17))
        self.ui.elevator2_18.clicked.connect(lambda:self.insidePush(2,18))
        self.ui.elevator2_19.clicked.connect(lambda:self.insidePush(2,19))
        self.ui.elevator2_20.clicked.connect(lambda:self.insidePush(2,20))
        self.ui.elevator3_1.clicked.connect(lambda:self.insidePush(3,1))
        self.ui.elevator3_2.clicked.connect(lambda:self.insidePush(3,2))
        self.ui.elevator3_3.clicked.connect(lambda:self.insidePush(3,3))
        self.ui.elevator3_4.clicked.connect(lambda:self.insidePush(3,4))
        self.ui.elevator3_5.clicked.connect(lambda:self.insidePush(3,5))
        self.ui.elevator3_6.clicked.connect(lambda:self.insidePush(3,6))
        self.ui.elevator3_7.clicked.connect(lambda:self.insidePush(3,7))
        self.ui.elevator3_8.clicked.connect(lambda:self.insidePush(3,8))
        self.ui.elevator3_9.clicked.connect(lambda:self.insidePush(3,9))
        self.ui.elevator3_10.clicked.connect(lambda:self.insidePush(3,10))
        self.ui.elevator3_11.clicked.connect(lambda:self.insidePush(3,11))
        self.ui.elevator3_12.clicked.connect(lambda:self.insidePush(3,12))
        self.ui.elevator3_13.clicked.connect(lambda:self.insidePush(3,13))
        self.ui.elevator3_14.clicked.connect(lambda:self.insidePush(3,14))
        self.ui.elevator3_15.clicked.connect(lambda:self.insidePush(3,15))
        self.ui.elevator3_16.clicked.connect(lambda:self.insidePush(3,16))
        self.ui.elevator3_17.clicked.connect(lambda:self.insidePush(3,17))
        self.ui.elevator3_18.clicked.connect(lambda:self.insidePush(3,18))
        self.ui.elevator3_19.clicked.connect(lambda:self.insidePush(3,19))
        self.ui.elevator3_20.clicked.connect(lambda:self.insidePush(3,20))
        self.ui.elevator4_1.clicked.connect(lambda:self.insidePush(4,1))
        self.ui.elevator4_2.clicked.connect(lambda:self.insidePush(4,2))
        self.ui.elevator4_3.clicked.connect(lambda:self.insidePush(4,3))
        self.ui.elevator4_4.clicked.connect(lambda:self.insidePush(4,4))
        self.ui.elevator4_5.clicked.connect(lambda:self.insidePush(4,5))
        self.ui.elevator4_6.clicked.connect(lambda:self.insidePush(4,6))
        self.ui.elevator4_7.clicked.connect(lambda:self.insidePush(4,7))
        self.ui.elevator4_8.clicked.connect(lambda:self.insidePush(4,8))
        self.ui.elevator4_9.clicked.connect(lambda:self.insidePush(4,9))
        self.ui.elevator4_10.clicked.connect(lambda:self.insidePush(4,10))
        self.ui.elevator4_11.clicked.connect(lambda:self.insidePush(4,11))
        self.ui.elevator4_12.clicked.connect(lambda:self.insidePush(4,12))
        self.ui.elevator4_13.clicked.connect(lambda:self.insidePush(4,13))
        self.ui.elevator4_14.clicked.connect(lambda:self.insidePush(4,14))
        self.ui.elevator4_15.clicked.connect(lambda:self.insidePush(4,15))
        self.ui.elevator4_16.clicked.connect(lambda:self.insidePush(4,16))
        self.ui.elevator4_17.clicked.connect(lambda:self.insidePush(4,17))
        self.ui.elevator4_18.clicked.connect(lambda:self.insidePush(4,18))
        self.ui.elevator4_19.clicked.connect(lambda:self.insidePush(4,19))
        self.ui.elevator4_20.clicked.connect(lambda:self.insidePush(4,20))
        self.ui.elevator5_1.clicked.connect(lambda:self.insidePush(5,1))
        self.ui.elevator5_2.clicked.connect(lambda:self.insidePush(5,2))
        self.ui.elevator5_3.clicked.connect(lambda:self.insidePush(5,3))
        self.ui.elevator5_4.clicked.connect(lambda:self.insidePush(5,4))
        self.ui.elevator5_5.clicked.connect(lambda:self.insidePush(5,5))
        self.ui.elevator5_6.clicked.connect(lambda:self.insidePush(5,6))
        self.ui.elevator5_7.clicked.connect(lambda:self.insidePush(5,7))
        self.ui.elevator5_8.clicked.connect(lambda:self.insidePush(5,8))
        self.ui.elevator5_9.clicked.connect(lambda:self.insidePush(5,9))
        self.ui.elevator5_10.clicked.connect(lambda:self.insidePush(5,10))
        self.ui.elevator5_11.clicked.connect(lambda:self.insidePush(5,11))
        self.ui.elevator5_12.clicked.connect(lambda:self.insidePush(5,12))
        self.ui.elevator5_13.clicked.connect(lambda:self.insidePush(5,13))
        self.ui.elevator5_14.clicked.connect(lambda:self.insidePush(5,14))
        self.ui.elevator5_15.clicked.connect(lambda:self.insidePush(5,15))
        self.ui.elevator5_16.clicked.connect(lambda:self.insidePush(5,16))
        self.ui.elevator5_17.clicked.connect(lambda:self.insidePush(5,17))
        self.ui.elevator5_18.clicked.connect(lambda:self.insidePush(5,18))
        self.ui.elevator5_19.clicked.connect(lambda:self.insidePush(5,19))
        self.ui.elevator5_20.clicked.connect(lambda:self.insidePush(5,20))

        self.work=WorkThread()
        self.work.trigger.connect(self.move)

    def up(self,num):
        # When the up buttons outside the elevators are pushed
        # Choose proper elevator to response
        # Priority : 1. closest
        #            2. going down
        #            3. free
        # If there are no elevators available currently,
        # append the request into upWaiting list
        elevatorDValue=[]
        if Elevator_1.statusDown==False:
            if Elevator_1.statusUp==False:
                elevatorDValue.append(abs(Elevator_1.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_1.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_2.statusDown==False:
            if Elevator_2.statusUp==False:
                elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_2.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_3.statusDown==False:
            if Elevator_3.statusUp==False:
                elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_3.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_4.statusDown==False:
            if Elevator_3.statusUp==False:
                elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_4.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_5.statusDown==False:
            if Elevator_5.statusUp==False:
                elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_5.currentFloor-num))
        else:
            elevatorDValue.append(20)

        if min(elevatorDValue)>20:
            upWaiting.append(num)
        else:
            if elevatorDValue.index(min(elevatorDValue))==0:
                Elevator_1.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==1:
                Elevator_2.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==2:
                Elevator_3.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==3:
                Elevator_4.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==4:
                Elevator_5.goList.append(num)

    def down(self,num):
        # When the down buttons outside the elevators are pushed
        # Choose proper elevator to response
        # Priority : 1. closest
        #            2. going down
        #            3. free
        # If there are no elevators available currently,
        # append the request into downWaiting list
        elevatorDValue=[]
        if Elevator_1.statusUp==False:
            if Elevator_1.statusDown==False:
                elevatorDValue.append(abs(Elevator_1.currentFloor-num)+1)  # set priority
            else:
                elevatorDValue.append(abs(Elevator_1.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_2.statusUp==False:
            if Elevator_2.statusDown==False:
                elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_2.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_3.statusUp==False:
            if Elevator_3.statusDown==False:
                elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_3.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_4.statusUp==False:
            if Elevator_4.statusDown==False:
                elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_4.currentFloor-num))
        else:
            elevatorDValue.append(20)
        if Elevator_5.statusUp==False:
            if Elevator_5.statusDown==False:
                elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
            else:
                elevatorDValue.append(abs(Elevator_5.currentFloor-num))
        else:
            elevatorDValue.append(20)

        if min(elevatorDValue)>=20:
            downWaiting.append(num)
        else:
            if elevatorDValue.index(min(elevatorDValue))==0:
                Elevator_1.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==1:
                Elevator_2.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==2:
                Elevator_3.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==3:
                Elevator_4.goList.append(num)
            elif elevatorDValue.index(min(elevatorDValue))==4:
                Elevator_5.goList.append(num)

    def insidePush(self,index,num):
        if index==1:
            Elevator_1.goList.append(num)
        elif index==2:
            Elevator_2.goList.append(num)
        elif index==3:
            Elevator_3.goList.append(num)
        elif index==4:
            Elevator_4.goList.append(num)
        elif index==5:
            Elevator_5.goList.append(num)

    def move(self):
        if Elevator_1.statusUp:
            self.ui.elevator1Slider.setValue(self.ui.elevator1Slider.value()+21)
        

class WorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        time.sleep(5)
        # 等待5秒后，给触发信号，并传递test
        self.trigger.emit('test2')

if __name__ == "__main__":
    Elevator_1=Elevator()
    Elevator_2=Elevator()
    Elevator_3=Elevator()
    Elevator_4=Elevator()
    Elevator_5=Elevator()
    upWaiting=[]
    downWaiting=[]

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())