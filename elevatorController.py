#!/usr/bin/python3

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
# @Contact   : rootReturn0@outlook.com
#
# @Filename  : Controller.py

''' 
The Best User Experience in the Algorithm:
1. Assume that everyone presses the right ditection button
   before he enters the elevator
2. Assume that everyone presses the button of target floors
   when he enters the elevator immediately
'''

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from elevatorInterface import Ui_MainWindow


class Elevator:
    ''' define Elevator '''

    def __init__(self, parent=None):
        super(Elevator, self).__init__()
        self.statusFree = True
        self.statusUp = False
        self.statusDown = False
        self.busy = False  # thread busy
        self.open = False  # door open
        self.currentFloor = 1
        self.value = 0  # position value
        self.upList = []  # users need to go up
        self.downList = []  # users need to go down

    def move(self):
        ##
        # change status of Elevator
        # @param: self.statusFree;
        #         self.statusUp;
        #         self.statusDown
        #
        if len(self.downList):
            if self.currentFloor < min(self.downList):
                self.statusFree = False
                self.statusUp = True
                self.statusDown = False
            elif self.currentFloor >= max(self.downList) and len(self.upList) == 0:
                self.statusFree = False
                self.statusUp = False
                self.statusDown = True
        elif len(self.upList):
            if self.currentFloor > max(self.upList):
                self.statusFree = False
                self.statusUp = False
                self.statusDown = True
            elif self.currentFloor <= min(self.upList) and len(self.downList) == 0:
                self.statusFree = False
                self.statusUp = True
                self.statusDown = False
        else:
            self.statusFree = True
            self.statusUp = False
            self.statusDown = False

    def updateFloor(self):
        ##
        # change status of floors
        # @parma: self.upList;
        #         self.downList;
        #         self.currentFloor
        #
        if self.statusUp and self.currentFloor in self.upList:
            self.open = True
            self.upList.remove(self.currentFloor)
            return
        if self.statusDown and self.currentFloor in self.downList:
            self.open = True
            self.downList.remove(self.currentFloor)
            return

        if self.statusUp:
            self.currentFloor += 1
        elif self.statusDown:
            self.currentFloor -= 1


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' Interation Interface '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1u.clicked.connect(lambda: up(1))
        self.ui.pushButton_2u.clicked.connect(lambda: up(2))
        self.ui.pushButton_3u.clicked.connect(lambda: up(3))
        self.ui.pushButton_4u.clicked.connect(lambda: up(4))
        self.ui.pushButton_5u.clicked.connect(lambda: up(5))
        self.ui.pushButton_6u.clicked.connect(lambda: up(6))
        self.ui.pushButton_7u.clicked.connect(lambda: up(7))
        self.ui.pushButton_8u.clicked.connect(lambda: up(8))
        self.ui.pushButton_9u.clicked.connect(lambda: up(9))
        self.ui.pushButton_10u.clicked.connect(lambda: up(10))
        self.ui.pushButton_11u.clicked.connect(lambda: up(11))
        self.ui.pushButton_12u.clicked.connect(lambda: up(12))
        self.ui.pushButton_13u.clicked.connect(lambda: up(13))
        self.ui.pushButton_14u.clicked.connect(lambda: up(14))
        self.ui.pushButton_15u.clicked.connect(lambda: up(15))
        self.ui.pushButton_16u.clicked.connect(lambda: up(16))
        self.ui.pushButton_17u.clicked.connect(lambda: up(17))
        self.ui.pushButton_18u.clicked.connect(lambda: up(18))
        self.ui.pushButton_19u.clicked.connect(lambda: up(19))
        self.ui.pushButton_2d.clicked.connect(lambda: down(2))
        self.ui.pushButton_3d.clicked.connect(lambda: down(3))
        self.ui.pushButton_4d.clicked.connect(lambda: down(4))
        self.ui.pushButton_5d.clicked.connect(lambda: down(5))
        self.ui.pushButton_6d.clicked.connect(lambda: down(6))
        self.ui.pushButton_7d.clicked.connect(lambda: down(7))
        self.ui.pushButton_8d.clicked.connect(lambda: down(8))
        self.ui.pushButton_9d.clicked.connect(lambda: down(9))
        self.ui.pushButton_10d.clicked.connect(lambda: down(10))
        self.ui.pushButton_11d.clicked.connect(lambda: down(11))
        self.ui.pushButton_12d.clicked.connect(lambda: down(12))
        self.ui.pushButton_13d.clicked.connect(lambda: down(13))
        self.ui.pushButton_14d.clicked.connect(lambda: down(14))
        self.ui.pushButton_15d.clicked.connect(lambda: down(15))
        self.ui.pushButton_16d.clicked.connect(lambda: down(16))
        self.ui.pushButton_17d.clicked.connect(lambda: down(17))
        self.ui.pushButton_18d.clicked.connect(lambda: down(18))
        self.ui.pushButton_19d.clicked.connect(lambda: down(19))
        self.ui.pushButton_20d.clicked.connect(lambda: down(20))
        self.ui.elevator1_1.clicked.connect(lambda: insidePush(1, 1))
        self.ui.elevator1_2.clicked.connect(lambda: insidePush(1, 2))
        self.ui.elevator1_3.clicked.connect(lambda: insidePush(1, 3))
        self.ui.elevator1_4.clicked.connect(lambda: insidePush(1, 4))
        self.ui.elevator1_5.clicked.connect(lambda: insidePush(1, 5))
        self.ui.elevator1_6.clicked.connect(lambda: insidePush(1, 6))
        self.ui.elevator1_7.clicked.connect(lambda: insidePush(1, 7))
        self.ui.elevator1_8.clicked.connect(lambda: insidePush(1, 8))
        self.ui.elevator1_9.clicked.connect(lambda: insidePush(1, 9))
        self.ui.elevator1_10.clicked.connect(lambda: insidePush(1, 10))
        self.ui.elevator1_11.clicked.connect(lambda: insidePush(1, 11))
        self.ui.elevator1_12.clicked.connect(lambda: insidePush(1, 12))
        self.ui.elevator1_13.clicked.connect(lambda: insidePush(1, 13))
        self.ui.elevator1_14.clicked.connect(lambda: insidePush(1, 14))
        self.ui.elevator1_15.clicked.connect(lambda: insidePush(1, 15))
        self.ui.elevator1_16.clicked.connect(lambda: insidePush(1, 16))
        self.ui.elevator1_17.clicked.connect(lambda: insidePush(1, 17))
        self.ui.elevator1_18.clicked.connect(lambda: insidePush(1, 18))
        self.ui.elevator1_19.clicked.connect(lambda: insidePush(1, 19))
        self.ui.elevator1_20.clicked.connect(lambda: insidePush(1, 20))
        self.ui.elevator2_1.clicked.connect(lambda: insidePush(2, 1))
        self.ui.elevator2_2.clicked.connect(lambda: insidePush(2, 2))
        self.ui.elevator2_3.clicked.connect(lambda: insidePush(2, 3))
        self.ui.elevator2_4.clicked.connect(lambda: insidePush(2, 4))
        self.ui.elevator2_5.clicked.connect(lambda: insidePush(2, 5))
        self.ui.elevator2_6.clicked.connect(lambda: insidePush(2, 6))
        self.ui.elevator2_7.clicked.connect(lambda: insidePush(2, 7))
        self.ui.elevator2_8.clicked.connect(lambda: insidePush(2, 8))
        self.ui.elevator2_9.clicked.connect(lambda: insidePush(2, 9))
        self.ui.elevator2_10.clicked.connect(lambda: insidePush(2, 10))
        self.ui.elevator2_11.clicked.connect(lambda: insidePush(2, 11))
        self.ui.elevator2_12.clicked.connect(lambda: insidePush(2, 12))
        self.ui.elevator2_13.clicked.connect(lambda: insidePush(2, 13))
        self.ui.elevator2_14.clicked.connect(lambda: insidePush(2, 14))
        self.ui.elevator2_15.clicked.connect(lambda: insidePush(2, 15))
        self.ui.elevator2_16.clicked.connect(lambda: insidePush(2, 16))
        self.ui.elevator2_17.clicked.connect(lambda: insidePush(2, 17))
        self.ui.elevator2_18.clicked.connect(lambda: insidePush(2, 18))
        self.ui.elevator2_19.clicked.connect(lambda: insidePush(2, 19))
        self.ui.elevator2_20.clicked.connect(lambda: insidePush(2, 20))
        self.ui.elevator3_1.clicked.connect(lambda: insidePush(3, 1))
        self.ui.elevator3_2.clicked.connect(lambda: insidePush(3, 2))
        self.ui.elevator3_3.clicked.connect(lambda: insidePush(3, 3))
        self.ui.elevator3_4.clicked.connect(lambda: insidePush(3, 4))
        self.ui.elevator3_5.clicked.connect(lambda: insidePush(3, 5))
        self.ui.elevator3_6.clicked.connect(lambda: insidePush(3, 6))
        self.ui.elevator3_7.clicked.connect(lambda: insidePush(3, 7))
        self.ui.elevator3_8.clicked.connect(lambda: insidePush(3, 8))
        self.ui.elevator3_9.clicked.connect(lambda: insidePush(3, 9))
        self.ui.elevator3_10.clicked.connect(lambda: insidePush(3, 10))
        self.ui.elevator3_11.clicked.connect(lambda: insidePush(3, 11))
        self.ui.elevator3_12.clicked.connect(lambda: insidePush(3, 12))
        self.ui.elevator3_13.clicked.connect(lambda: insidePush(3, 13))
        self.ui.elevator3_14.clicked.connect(lambda: insidePush(3, 14))
        self.ui.elevator3_15.clicked.connect(lambda: insidePush(3, 15))
        self.ui.elevator3_16.clicked.connect(lambda: insidePush(3, 16))
        self.ui.elevator3_17.clicked.connect(lambda: insidePush(3, 17))
        self.ui.elevator3_18.clicked.connect(lambda: insidePush(3, 18))
        self.ui.elevator3_19.clicked.connect(lambda: insidePush(3, 19))
        self.ui.elevator3_20.clicked.connect(lambda: insidePush(3, 20))
        self.ui.elevator4_1.clicked.connect(lambda: insidePush(4, 1))
        self.ui.elevator4_2.clicked.connect(lambda: insidePush(4, 2))
        self.ui.elevator4_3.clicked.connect(lambda: insidePush(4, 3))
        self.ui.elevator4_4.clicked.connect(lambda: insidePush(4, 4))
        self.ui.elevator4_5.clicked.connect(lambda: insidePush(4, 5))
        self.ui.elevator4_6.clicked.connect(lambda: insidePush(4, 6))
        self.ui.elevator4_7.clicked.connect(lambda: insidePush(4, 7))
        self.ui.elevator4_8.clicked.connect(lambda: insidePush(4, 8))
        self.ui.elevator4_9.clicked.connect(lambda: insidePush(4, 9))
        self.ui.elevator4_10.clicked.connect(lambda: insidePush(4, 10))
        self.ui.elevator4_11.clicked.connect(lambda: insidePush(4, 11))
        self.ui.elevator4_12.clicked.connect(lambda: insidePush(4, 12))
        self.ui.elevator4_13.clicked.connect(lambda: insidePush(4, 13))
        self.ui.elevator4_14.clicked.connect(lambda: insidePush(4, 14))
        self.ui.elevator4_15.clicked.connect(lambda: insidePush(4, 15))
        self.ui.elevator4_16.clicked.connect(lambda: insidePush(4, 16))
        self.ui.elevator4_17.clicked.connect(lambda: insidePush(4, 17))
        self.ui.elevator4_18.clicked.connect(lambda: insidePush(4, 18))
        self.ui.elevator4_19.clicked.connect(lambda: insidePush(4, 19))
        self.ui.elevator4_20.clicked.connect(lambda: insidePush(4, 20))
        self.ui.elevator5_1.clicked.connect(lambda: insidePush(5, 1))
        self.ui.elevator5_2.clicked.connect(lambda: insidePush(5, 2))
        self.ui.elevator5_3.clicked.connect(lambda: insidePush(5, 3))
        self.ui.elevator5_4.clicked.connect(lambda: insidePush(5, 4))
        self.ui.elevator5_5.clicked.connect(lambda: insidePush(5, 5))
        self.ui.elevator5_6.clicked.connect(lambda: insidePush(5, 6))
        self.ui.elevator5_7.clicked.connect(lambda: insidePush(5, 7))
        self.ui.elevator5_8.clicked.connect(lambda: insidePush(5, 8))
        self.ui.elevator5_9.clicked.connect(lambda: insidePush(5, 9))
        self.ui.elevator5_10.clicked.connect(lambda: insidePush(5, 10))
        self.ui.elevator5_11.clicked.connect(lambda: insidePush(5, 11))
        self.ui.elevator5_12.clicked.connect(lambda: insidePush(5, 12))
        self.ui.elevator5_13.clicked.connect(lambda: insidePush(5, 13))
        self.ui.elevator5_14.clicked.connect(lambda: insidePush(5, 14))
        self.ui.elevator5_15.clicked.connect(lambda: insidePush(5, 15))
        self.ui.elevator5_16.clicked.connect(lambda: insidePush(5, 16))
        self.ui.elevator5_17.clicked.connect(lambda: insidePush(5, 17))
        self.ui.elevator5_18.clicked.connect(lambda: insidePush(5, 18))
        self.ui.elevator5_19.clicked.connect(lambda: insidePush(5, 19))
        self.ui.elevator5_20.clicked.connect(lambda: insidePush(5, 20))

        self.moveElevator1 = MoveThread1()
        self.moveElevator2 = MoveThread2()
        self.moveElevator3 = MoveThread3()
        self.moveElevator4 = MoveThread4()
        self.moveElevator5 = MoveThread5()
        self.work = WorkThread()
        self.change = ChangeThread()
        self.downWaitList = DownWaitListThread()
        self.upWaitList = UpWaitListThread()
        if Elevator_1.busy == False:
            self.work.trigger.connect(lambda: self.moveElevator1.start())
        if Elevator_2.busy == False:
            self.work.trigger.connect(lambda: self.moveElevator2.start())
        if Elevator_3.busy == False:
            self.work.trigger.connect(lambda: self.moveElevator3.start())
        if Elevator_4.busy == False:
            self.work.trigger.connect(lambda: self.moveElevator4.start())
        if Elevator_5.busy == False:
            self.work.trigger.connect(lambda: self.moveElevator5.start())
        if (Elevator_1.statusUp == False
                or Elevator_2.statusUp == False
                or Elevator_3.statusUp == False
                or Elevator_4.statusUp == False
                or Elevator_5.statusUp == False):
            self.work.trigger.connect(lambda: self.downWaitList.start())
        if (Elevator_1.statusDown == False
                or Elevator_2.statusDown == False
                or Elevator_3.statusDown == False
                or Elevator_4.statusDown == False
                or Elevator_5.statusDown == False):
            self.work.trigger.connect(lambda: self.upWaitList.start())

        self.moveElevator1.trigger.connect(lambda: self.stop_moveElevator1())
        self.moveElevator2.trigger.connect(lambda: self.stop_moveElevator2())
        self.moveElevator3.trigger.connect(lambda: self.stop_moveElevator3())
        self.moveElevator4.trigger.connect(lambda: self.stop_moveElevator4())
        self.moveElevator5.trigger.connect(lambda: self.stop_moveElevator5())
        self.work.trigger.connect(lambda: self.stop_work())
        self.change.trigger.connect(lambda: self.stop_change())
        self.downWaitList.trigger.connect(lambda: self.stop_downWaitList())
        self.upWaitList.trigger.connect(lambda: self.stop_upWaitList())
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.work.start())
        self.timer.start(1)
        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(lambda: self.change.start())
        self.timer_2.start(1)

    def stop_moveElevator1(self):
        self.moveElevator1.quit()

    def stop_moveElevator2(self):
        self.moveElevator2.quit()

    def stop_moveElevator3(self):
        self.moveElevator3.quit()

    def stop_moveElevator4(self):
        self.moveElevator4.quit()

    def stop_moveElevator5(self):
        self.moveElevator5.quit()

    def stop_work(self):
        self.work.quit()

    def stop_change(self):
        self.change.quit()

    def stop_downWaitList(self):
        self.downWaitList.quit()

    def stop_upWaitList(self):
        self.upWaitList.quit()


class MoveThread1(QThread):
    ''' activate the thread for Elevator_1 '''
    trigger = pyqtSignal()

    def __int__(self):
        super(MoveThread1, self).__init__()

    def run(self):
        Elevator_1.move()
        Elevator_1.updateFloor()
        move1()
        self.trigger.emit()


class MoveThread2(QThread):
    ''' activate the thread for Elevator_2 '''
    trigger = pyqtSignal()

    def __int__(self):
        super(MoveThread2, self).__init__()

    def run(self):
        Elevator_2.move()
        Elevator_2.updateFloor()
        move2()
        self.trigger.emit()


class MoveThread3(QThread):
    ''' activate the thread for Elevator_3 '''
    trigger = pyqtSignal()

    def __int__(self):
        super(MoveThread3, self).__init__()

    def run(self):
        Elevator_3.move()
        Elevator_3.updateFloor()
        move3()
        self.trigger.emit()


class MoveThread4(QThread):
    ''' activate the thread for Elevator_4 '''
    trigger = pyqtSignal()

    def __int__(self):
        super(MoveThread4, self).__init__()

    def run(self):
        Elevator_4.move()
        Elevator_4.updateFloor()
        move4()
        self.trigger.emit()


class MoveThread5(QThread):
    ''' activate the thread for Elevator_5 '''
    trigger = pyqtSignal()

    def __int__(self):
        super(MoveThread5, self).__init__()

    def run(self):
        Elevator_5.move()
        Elevator_5.updateFloor()
        move5()
        self.trigger.emit()


class WorkThread(QThread):
    ''' activate all threads of elevators '''
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        self.trigger.emit()


class DownWaitListThread(QThread):
    ''' assign tasks to elevators in downWaiting[] '''
    trigger = pyqtSignal()

    def __int__(self):
        super(DownWaitListThread, self).__init__()

    def run(self):
        if len(downWaiting):
            down(downWaiting.pop(0))
        self.trigger.emit()


class UpWaitListThread(QThread):
    ''' assign tasks to elevators in upWaiting[] '''
    trigger = pyqtSignal()

    def __int__(self):
        super(UpWaitListThread, self).__init__()

    def run(self):
        if len(upWaiting):
            up(upWaiting.pop(0))
        self.trigger.emit()


class ChangeThread(QThread):
    ''' the thread of refreshMainWindow() '''
    trigger = pyqtSignal()

    def __int__(self):
        super(ChangeThread, self).__init__()

    def run(self):
        refreshMainWindow()
        self.trigger.emit()


def refreshMainWindow():
    # change the display of MainWindow
    w.ui.floor_e1.setText(str(Elevator_1.currentFloor))
    w.ui.floor_e2.setText(str(Elevator_2.currentFloor))
    w.ui.floor_e3.setText(str(Elevator_3.currentFloor))
    w.ui.floor_e4.setText(str(Elevator_4.currentFloor))
    w.ui.floor_e5.setText(str(Elevator_5.currentFloor))
    w.ui.elevator1Slider.setValue(Elevator_1.value)
    w.ui.elevator2Slider.setValue(Elevator_2.value)
    w.ui.elevator3Slider.setValue(Elevator_3.value)
    w.ui.elevator4Slider.setValue(Elevator_4.value)
    w.ui.elevator5Slider.setValue(Elevator_5.value)
    if Elevator_1.open:
        w.ui.status_e1_closed.setHidden(True)
        w.ui.status_e1_open.setHidden(False)
        w.ui.status_e1_running.setHidden(True)
    elif Elevator_1.statusFree:
        w.ui.status_e1_closed.setHidden(False)
        w.ui.status_e1_open.setHidden(True)
        w.ui.status_e1_running.setHidden(True)
    elif Elevator_1.statusFree == False:
        w.ui.status_e1_closed.setHidden(True)
        w.ui.status_e1_open.setHidden(True)
        w.ui.status_e1_running.setHidden(False)
    if Elevator_2.open:
        w.ui.status_e2_closed.setHidden(True)
        w.ui.status_e2_open.setHidden(False)
        w.ui.status_e2_running.setHidden(True)
    elif Elevator_2.statusFree:
        w.ui.status_e2_closed.setHidden(False)
        w.ui.status_e2_open.setHidden(True)
        w.ui.status_e2_running.setHidden(True)
    elif Elevator_2.statusFree == False:
        w.ui.status_e2_closed.setHidden(True)
        w.ui.status_e2_open.setHidden(True)
        w.ui.status_e2_running.setHidden(False)
    if Elevator_3.open:
        w.ui.status_e3_closed.setHidden(True)
        w.ui.status_e3_open.setHidden(False)
        w.ui.status_e3_running.setHidden(True)
    elif Elevator_3.statusFree:
        w.ui.status_e3_closed.setHidden(False)
        w.ui.status_e3_open.setHidden(True)
        w.ui.status_e3_running.setHidden(True)
    elif Elevator_3.statusFree == False:
        w.ui.status_e3_closed.setHidden(True)
        w.ui.status_e3_open.setHidden(True)
        w.ui.status_e3_running.setHidden(False)
    if Elevator_4.open:
        w.ui.status_e4_closed.setHidden(True)
        w.ui.status_e4_open.setHidden(False)
        w.ui.status_e4_running.setHidden(True)
    elif Elevator_4.statusFree:
        w.ui.status_e4_closed.setHidden(False)
        w.ui.status_e4_open.setHidden(True)
        w.ui.status_e4_running.setHidden(True)
    elif Elevator_4.statusFree == False:
        w.ui.status_e4_closed.setHidden(True)
        w.ui.status_e4_open.setHidden(True)
        w.ui.status_e4_running.setHidden(False)
    if Elevator_5.open:
        w.ui.status_e5_closed.setHidden(True)
        w.ui.status_e5_open.setHidden(False)
        w.ui.status_e5_running.setHidden(True)
    elif Elevator_5.statusFree:
        w.ui.status_e5_closed.setHidden(False)
        w.ui.status_e5_open.setHidden(True)
        w.ui.status_e5_running.setHidden(True)
    elif Elevator_5.statusFree == False:
        w.ui.status_e5_closed.setHidden(True)
        w.ui.status_e5_open.setHidden(True)
        w.ui.status_e5_running.setHidden(False)


def move1():
    ##
    # Move Elevator_1 in MainWindow
    # @param: Elecator.busy;
    #         Elevator.value
    #
    if Elevator_1.busy == False:
        Elevator_1.busy = True  # processing
        if Elevator_1.open:
            time.sleep(1)
            Elevator_1.open = False
        elif Elevator_1.statusUp:
            for i in range(10):
                time.sleep(0.04)
                Elevator_1.value += 1
        elif Elevator_1.statusDown:
            for i in range(10):
                time.sleep(0.04)
                Elevator_1.value -= 1

        Elevator_1.busy = False  # process done


def move2():
    ##
    # Move Elevator_2 in MainWindow
    # @param: Elecator.busy;
    #         Elevator.value
    #
    if Elevator_2.busy == False:
        Elevator_2.busy = True
        if Elevator_2.open:
            time.sleep(1)
            Elevator_2.open = False
        elif Elevator_2.statusUp:
            for i in range(10):
                time.sleep(0.04)
                Elevator_2.value += 1
        elif Elevator_2.statusDown:
            for i in range(10):
                time.sleep(0.04)
                Elevator_2.value -= 1

        Elevator_2.busy = False  # process done


def move3():
    ##
    # Move Elevator_3 in MainWindow
    # @param: Elecator.busy;
    #         Elevator.value
    #
    if Elevator_3.busy == False:
        Elevator_3.busy = True
        if Elevator_3.open:
            time.sleep(1)
            Elevator_3.open = False
        elif Elevator_3.statusUp:
            for i in range(10):
                time.sleep(0.04)
                Elevator_3.value += 1
        elif Elevator_3.statusDown:
            for i in range(10):
                time.sleep(0.04)
                Elevator_3.value -= 1

        Elevator_3.busy = False  # process done


def move4():
    ##
    # Move Elevator_4 in MainWindow
    # @param: Elecator.busy;
    #         Elevator.value
    #
    if Elevator_4.busy == False:
        Elevator_4.busy = True
        if Elevator_4.open:
            time.sleep(1)
            Elevator_4.open = False
        elif Elevator_4.statusUp:
            for i in range(10):
                time.sleep(0.04)
                Elevator_4.value += 1
        elif Elevator_4.statusDown:
            for i in range(10):
                time.sleep(0.04)
                Elevator_4.value -= 1

        Elevator_4.busy = False  # process done


def move5():
    ##
    # Move Elevator_5 in MainWindow
    # @param: Elecator.busy;
    #         Elevator.value
    #
    if Elevator_5.busy == False:
        Elevator_5.busy = True
        if Elevator_5.open:
            time.sleep(1)
            Elevator_5.open = False
        elif Elevator_5.statusUp:
            for i in range(10):
                time.sleep(0.04)
                Elevator_5.value += 1
        elif Elevator_5.statusDown:
            for i in range(10):
                time.sleep(0.04)
                Elevator_5.value -= 1

        Elevator_5.busy = False  # process done


def up(num):
    ##
    # When the up buttons outside the elevators are pushed
    # Choose proper elevator to response
    # Priority : 1. shortest distance
    #            2. working
    #            3. free
    # If there are no elevators available currently, append the request into upWaiting list
    # @param: Elevator.upList
    #

    # check if there are elevators can work immediately
    if len(Elevator_1.downList) == 0 and Elevator_1.currentFloor == num:
        if not Elevator_1.open:
            Elevator_1.open = True
        return
    if len(Elevator_2.downList) == 0 and Elevator_2.currentFloor == num:
        if not Elevator_2.open:
            Elevator_2.open = True
        return
    if len(Elevator_3.downList) == 0 and Elevator_3.currentFloor == num:
        if not Elevator_3.open:
            Elevator_3.open = True
        return
    if len(Elevator_4.downList) == 0 and Elevator_4.currentFloor == num:
        if not Elevator_4.open:
            Elevator_4.open = True
        return
    if len(Elevator_5.downList) == 0 and Elevator_5.currentFloor == num:
        if not Elevator_5.open:
            Elevator_5.open = True
        return

    elevatorDValue = []  # the distance between each elevator and the target floor

    # make distance larger to lower the priority
    if Elevator_1.statusFree == True:
        elevatorDValue.append(abs(Elevator_1.currentFloor-num)+1)
    # the elevator is doing tasks in Elevator.upList
    elif len(Elevator_1.upList) and Elevator_1.statusUp:
        if Elevator_1.currentFloor > num:
            # realDistance = distance
            #                + 2 * maxWorkDistance
            #                + (openTime / runningTimeForASingleFloor) * len(Elevator.upList)
            elevatorDValue.append(
                Elevator_1.currentFloor-num
                + 2*(20-Elevator_1.currentFloor)
                + (1/0.4)*len(Elevator_1.upList))
        else:
            # realDistance = distance
            elevatorDValue.append(num-Elevator_1.currentFloor)
    # the elevator is possible doing or to do tasks in Elevator.downList
    else:
        # realDistance = distance
        #                + 2 * maxWorkDistance
        #                + (openTime / runningTimeForASingleFloor) * len(Elevator.downList)
        elevatorDValue.append(
            num-Elevator_1.currentFloor
            + 2*(Elevator_1.currentFloor)
            + (1/0.4)*len(Elevator_1.downList))
    if Elevator_2.statusFree == True:
        elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
    elif len(Elevator_2.upList) and Elevator_2.statusUp:
        if Elevator_2.currentFloor > num:
            elevatorDValue.append(
                Elevator_2.currentFloor-num
                + 2*(20-Elevator_2.currentFloor)
                + (1/0.4)*len(Elevator_2.upList))
        else:
            elevatorDValue.append(num-Elevator_2.currentFloor)
    else:
        elevatorDValue.append(
            num-Elevator_2.currentFloor
            + 2*(Elevator_2.currentFloor)
            + (1/0.4)*len(Elevator_2.downList))
    if Elevator_3.statusFree == True:
        elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
    elif len(Elevator_3.upList) and Elevator_3.statusUp:
        if Elevator_3.currentFloor > num:
            elevatorDValue.append(
                Elevator_3.currentFloor-num
                + 2*(20-Elevator_3.currentFloor)
                + (1/0.4)*len(Elevator_3.upList))
        else:
            elevatorDValue.append(num-Elevator_3.currentFloor)
    else:
        elevatorDValue.append(
            num-Elevator_3.currentFloor
            + 2*(Elevator_3.currentFloor)
            + (1/0.4)*len(Elevator_3.downList))
    if Elevator_4.statusFree == True:
        elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
    elif len(Elevator_4.upList) and Elevator_4.statusUp:
        if Elevator_4.currentFloor > num:
            elevatorDValue.append(
                Elevator_4.currentFloor-num
                + 2*(20-Elevator_4.currentFloor)
                + (1/0.4)*len(Elevator_4.upList))
        else:
            elevatorDValue.append(num-Elevator_4.currentFloor)
    else:
        elevatorDValue.append(
            num-Elevator_4.currentFloor
            + 2*(Elevator_4.currentFloor)
            + (1/0.4)*len(Elevator_4.downList))
    if Elevator_5.statusFree == True:
        elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
    elif len(Elevator_5.upList) and Elevator_5.statusUp:
        if Elevator_5.currentFloor > num:
            elevatorDValue.append(
                Elevator_5.currentFloor-num
                + 2*(20-Elevator_5.currentFloor)
                + (1/0.4)*len(Elevator_5.upList))
        else:
            elevatorDValue.append(num-Elevator_5.currentFloor)
    else:
        elevatorDValue.append(
            num-Elevator_5.currentFloor
            + 2*(Elevator_5.currentFloor)
            + (1/0.4)*len(Elevator_5.downList))

    # assign the task to some elevator or add it to upWaiting[]
    if min(elevatorDValue) == 100:
        upWaiting.append(num)
    else:
        if elevatorDValue.index(min(elevatorDValue)) == 0:
            if num not in Elevator_1.upList:
                if Elevator_1.currentFloor == num and Elevator_1.statusFree:
                    Elevator_1.open = True
                Elevator_1.upList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 1:
            if num not in Elevator_2.upList:
                if Elevator_2.currentFloor == num and Elevator_2.statusFree:
                    Elevator_2.open = True
                    Elevator_1.upList.append(num)
                Elevator_2.upList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 2:
            if num not in Elevator_3.upList:
                if Elevator_3.currentFloor == num and Elevator_3.statusFree:
                    Elevator_3.open = True
                Elevator_3.upList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 3:
            if num not in Elevator_4.upList:
                if Elevator_4.currentFloor == num and Elevator_4.statusFree:
                    Elevator_4.open = True
                Elevator_4.upList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 4:
            if num not in Elevator_5.upList:
                if Elevator_5.currentFloor == num and Elevator_5.statusFree:
                    Elevator_5.open = True
                Elevator_5.upList.append(num)


def down(num):
    ##
    # When the down buttons outside the elevators are pushed
    # Choose proper elevator to response
    # Priority : 1. shortest distance
    #            2. working
    #            3. free
    # If there are no elevators available currently, append the request into downWaiting list
    # @param: Elevator.downList
    #

    # check if there are elevators can work immediately
    if len(Elevator_1.upList) == 0 and Elevator_1.currentFloor == num:
        if not Elevator_1.open:
            Elevator_1.open = True
        return
    if len(Elevator_2.upList) == 0 and Elevator_2.currentFloor == num:
        if not Elevator_2.open:
            Elevator_2.open = True
        return
    if len(Elevator_3.upList) == 0 and Elevator_3.currentFloor == num:
        if not Elevator_3.open:
            Elevator_3.open = True
        return
    if len(Elevator_4.upList) == 0 and Elevator_4.currentFloor == num:
        if not Elevator_4.open:
            Elevator_4.open = True
        return
    if len(Elevator_5.upList) == 0 and Elevator_5.currentFloor == num:
        if not Elevator_5.open:
            Elevator_5.open = True
        return

    elevatorDValue = []  # the distance between each elevator and the target floor

    # make distance larger to lower the priority
    if Elevator_1.statusFree == True:
        elevatorDValue.append(abs(Elevator_1.currentFloor-num)+1)
    # the elevator is doing tasks in Elevator.downList
    elif len(Elevator_1.downList) and Elevator_1.statusDown:
            # realDistance = distance
            #                + 2 * maxWorkDistance
            #                + (openTime / runningTimeForASingleFloor) * len(Elevator.downList)
        if Elevator_1.currentFloor < num:
            elevatorDValue.append(
                num-Elevator_1.currentFloor
                + 2*(Elevator_1.currentFloor)
                + (1/0.4)*len(Elevator_1.downList))
        else:
            # realDistance = distance
            elevatorDValue.append(Elevator_1.currentFloor-num)
    # the elevator is possible doing or to do tasks in Elevator.upList
    else:
        # realDistance = distance
        #                + 2 * maxWorkDistance
        #                + (openTime / runningTimeForASingleFloor) * len(Elevator.downList)
        elevatorDValue.append(
            Elevator_1.currentFloor-num
            + 2*(20-Elevator_1.currentFloor)
            + (1/0.4)*len(Elevator_1.upList))
    if Elevator_2.statusFree == True:
        elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
    elif len(Elevator_2.downList) and Elevator_2.statusDown:
        if Elevator_2.currentFloor < num:
            elevatorDValue.append(
                num-Elevator_2.currentFloor
                + 2*(Elevator_2.currentFloor)
                + (1/0.4)*len(Elevator_2.downList))
        else:
            elevatorDValue.append(Elevator_2.currentFloor-num)
    else:
        elevatorDValue.append(
            Elevator_2.currentFloor-num
            + 2*(20-Elevator_2.currentFloor)
            + (1/0.4)*len(Elevator_2.upList))
    if Elevator_3.statusFree == True:
        elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
    elif len(Elevator_3.downList) and Elevator_3.statusDown:
        if Elevator_3.currentFloor < num:
            elevatorDValue.append(
                num-Elevator_3.currentFloor
                + 2*(Elevator_3.currentFloor)
                + (1/0.4)*len(Elevator_3.downList))
        else:
            elevatorDValue.append(Elevator_3.currentFloor-num)
    else:
        elevatorDValue.append(
            Elevator_3.currentFloor-num
            + 2*(20-Elevator_3.currentFloor)
            + (1/0.4)*len(Elevator_3.upList))
    if Elevator_4.statusFree == True:
        elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
    elif len(Elevator_4.downList) and Elevator_4.statusDown:
        if Elevator_4.currentFloor < num:
            elevatorDValue.append(
                num-Elevator_4.currentFloor
                + 2*(Elevator_4.currentFloor)
                + (1/0.4)*len(Elevator_4.downList))
        else:
            elevatorDValue.append(Elevator_4.currentFloor-num)
    else:
        elevatorDValue.append(
            Elevator_4.currentFloor-num
            + 2*(20-Elevator_4.currentFloor)
            + (1/0.4)*len(Elevator_4.upList))
    if Elevator_5.statusFree == True:
        elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
    elif len(Elevator_5.downList) and Elevator_5.statusDown:
        if Elevator_5.currentFloor < num:
            elevatorDValue.append(
                num-Elevator_5.currentFloor
                + 2*(Elevator_5.currentFloor)
                + (1/0.4)*len(Elevator_5.downList))
        else:
            elevatorDValue.append(Elevator_5.currentFloor-num)
    else:
        elevatorDValue.append(
            Elevator_5.currentFloor-num
            + 2*(20-Elevator_5.currentFloor)
            + (1/0.4)*len(Elevator_5.upList))

    # assign the task to some elevator or add it to downWaiting[]
    if min(elevatorDValue) == 100:
        downWaiting.append(num)
    else:
        if elevatorDValue.index(min(elevatorDValue)) == 0:
            if num not in Elevator_1.downList:
                if Elevator_1.currentFloor == num and Elevator_1.statusFree:
                    Elevator_1.open = True
                Elevator_1.downList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 1:
            if num not in Elevator_2.downList:
                if Elevator_2.currentFloor == num and Elevator_2.statusFree:
                    Elevator_2.open = True
                Elevator_2.downList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 2:
            if num not in Elevator_3.downList:
                if Elevator_3.currentFloor == num and Elevator_3.statusFree:
                    Elevator_3.open = True
                Elevator_3.downList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 3:
            if num not in Elevator_4.downList:
                if Elevator_4.currentFloor == num and Elevator_4.statusFree:
                    Elevator_4.open = True
                Elevator_4.downList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 4:
            if num not in Elevator_5.downList:
                if Elevator_5.currentFloor == num and Elevator_5.statusFree:
                    Elevator_5.open = True
                Elevator_5.downList.append(num)


def insidePush(index, num):
    ##
    # When the buttons inside the elevators are pushed
    # @param: Elevator.upList;
    #         Elevator.downList
    #

    if index == 1:
        # single click to assign the task
        if num == Elevator_1.currentFloor:
            Elevator_1.open = True
        elif num not in Elevator_1.upList and num not in Elevator_1.downList:
            if Elevator_1.statusUp:
                # if the target floor is upper than current floor when the elevator going up
                # then add the task to upList[]
                # else add the task to downList[]
                if Elevator_1.currentFloor < num:
                    Elevator_1.upList.append(num)
                else:
                    Elevator_1.downList.append(num)
            elif Elevator_1.statusDown:
                if Elevator_1.currentFloor > num:
                    Elevator_1.downList.append(num)
                else:
                    Elevator_1.upList.append(num)
            # the elevator is free
            elif Elevator_1.currentFloor > num:
                Elevator_1.downList.append(num)
            elif Elevator_1.currentFloor < num:
                Elevator_1.upList.append(num)
            # if the elevator is free and is on the target floor
            else:
                Elevator_1.open = True
        # double click to cancel the task
        elif num in Elevator_1.upList:
            Elevator_1.upList.remove(num)
        else:
            Elevator_1.downList.remove(num)
    elif index == 2:
        if num not in Elevator_2.upList and num not in Elevator_2.downList:
            if Elevator_2.statusUp:
                if Elevator_2.currentFloor < num:
                    Elevator_2.upList.append(num)
                else:
                    Elevator_2.downList.append(num)
            elif Elevator_2.statusDown:
                if Elevator_2.currentFloor > num:
                    Elevator_2.downList.append(num)
                else:
                    Elevator_2.upList.append(num)
            elif Elevator_2.currentFloor > num:
                Elevator_2.downList.append(num)
            elif Elevator_2.currentFloor < num:
                Elevator_2.upList.append(num)
            else:
                Elevator_2.open = True
        elif num in Elevator_2.upList:
            Elevator_2.upList.remove(num)
        else:
            Elevator_2.downList.remove(num)
    elif index == 3:
        if num not in Elevator_3.upList and num not in Elevator_3.downList:
            if Elevator_3.statusUp:
                if Elevator_3.currentFloor < num:
                    Elevator_3.upList.append(num)
                else:
                    Elevator_3.downList.append(num)
            elif Elevator_3.statusDown:
                if Elevator_3.currentFloor > num:
                    Elevator_3.downList.append(num)
                else:
                    Elevator_3.upList.append(num)
            elif Elevator_3.currentFloor > num:
                Elevator_3.downList.append(num)
            elif Elevator_3.currentFloor < num:
                Elevator_3.upList.append(num)
            else:
                Elevator_3.open = True
        elif num in Elevator_3.upList:
            Elevator_3.upList.remove(num)
        else:
            Elevator_3.downList.remove(num)
    elif index == 4:
        if num not in Elevator_4.upList and num not in Elevator_4.downList:
            if Elevator_4.statusUp:
                if Elevator_4.currentFloor < num:
                    Elevator_4.upList.append(num)
                else:
                    Elevator_4.downList.append(num)
            elif Elevator_4.statusDown:
                if Elevator_4.currentFloor > num:
                    Elevator_4.downList.append(num)
                else:
                    Elevator_4.upList.append(num)
            elif Elevator_4.currentFloor > num:
                Elevator_4.downList.append(num)
            elif Elevator_4.currentFloor < num:
                Elevator_4.upList.append(num)
            else:
                Elevator_4.open = True
        elif num in Elevator_4.upList:
            Elevator_4.upList.remove(num)
        else:
            Elevator_4.downList.remove(num)
    elif index == 5:
        if num not in Elevator_5.upList and num not in Elevator_5.downList:
            if Elevator_5.statusUp:
                if Elevator_5.currentFloor < num:
                    Elevator_5.upList.append(num)
                else:
                    Elevator_5.downList.append(num)
            elif Elevator_5.statusDown:
                if Elevator_5.currentFloor > num:
                    Elevator_5.downList.append(num)
                else:
                    Elevator_5.upList.append(num)
            elif Elevator_5.currentFloor > num:
                Elevator_5.downList.append(num)
            elif Elevator_5.currentFloor < num:
                Elevator_5.upList.append(num)
            else:
                Elevator_5.open = True
        elif num in Elevator_5.upList:
            Elevator_5.upList.remove(num)
        else:
            Elevator_5.downList.remove(num)


if __name__ == "__main__":
    Elevator_1 = Elevator()
    Elevator_2 = Elevator()
    Elevator_3 = Elevator()
    Elevator_4 = Elevator()
    Elevator_5 = Elevator()
    upWaiting = []
    downWaiting = []

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
