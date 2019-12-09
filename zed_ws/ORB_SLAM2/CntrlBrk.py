#!/usr/bin/env python

# Reemplaza talker.py en beginner_tutorials/scripts

#Importacion de librerias importantes
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import rospy
from std_msgs.msg import Float32, Int16
import time
import numpy as np
import serial
import serial.tools.list_ports
import warnings
import math
import sys, select, os
import itertools

if os.name == 'nt':
    import msvcrt
else:
    import tty, termios

#reemplazar port='/dev/tty' por el puerto al que este conectado el PLC
client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytsize=8, parity='N', baudrate=9600)
#En caso de no estar conectado al PLC, el programa arrojara un error en esta linea debido a que es la encargada de la comunicacion
client.connect()

e = """
Communications Failed
"""

acc_sp = 0
fre_sp = 10

def getKey(): #Input de teclado
#es un metodo ya existente de ros
    if os.name == 'nt':
        return msvcrt.getch()
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return

# def callback_acc(acc_data):
#     global acc_sp
#     acc_sp = acc_data.data
#     print 'done1', acc_sp

def callback(brk_data):
    global fre_sp
    fre_sp = brk_data.data
    print 'done2', fre_sp

def speedControl():
    client.write_coil(65,True,unit=5) # subrutinas y prender el plc
    # client.write_coil(60,True,unit=5) # accelerator
    client.write_coil(57,True,unit=5) # brakes
    print ("Connected")
    print ("K to stop control, Ctrl + C to kill program")
    time.sleep(1)
    rospy.init_node('listener', anonymous=True)###################
    while not rospy.core.is_shutdown():
        key = getKey()
        if (key == 'k'):
            print("Detenido")
            # client.write_register(17,0,unit=5)
            client.write_register(20,9,unit=5)
            while key != 'r' or not rospy.core.is_shutdown():
                key = getKey()
                print 'R to resume or Ctl+C to kill program'
            # time.sleep(2)
            # client.write_coil(102,True,unit=5)
        else:
            # rospy.Subscriber("accelerator", Int16, callback_acc)
            rospy.Subscriber("brakes", Int16, callback)
            print 'done0'
            # client.write_register(17, acc_sp, unit=5) #accelator
            client.write_regsiter(20, fre_sp, unit=5) #brakes

if __name__ == '__main__': #metodo main que arroja un exception en caso de un error en la comunicacion
    if os.name != 'nt':
        try:
            settings = termios.tcgetattr(sys.stdin)
            speedControl()
        except:
            print e
    if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
