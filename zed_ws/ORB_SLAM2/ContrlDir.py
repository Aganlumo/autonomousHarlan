#!/usr/bin/env python

# Reemplaza talker.py en beginner_tutorials/scripts
#98 izq , 99der
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
count=0
check=0
t=0
sp = 4
k = 1
e = """
Communications Failed
"""
direction = 1

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

def callback_gamma(twist_dir):
    global direction
    direction = twist_dir.data

def listener():
    global direction
    global check
    client.write_coil(65,True,unit=5) # subrutinas y prender el plc
    client.write_coil(58,True,unit=5) #Energizar
    print ("Conectado")
    time.sleep(1)
    #client.write_coil(106,True,unit=5)
    print ("Aprieta Ctrl+C 2 veces para parar")
    rospy.init_node('listener', anonymous=True)
    while not rospy.core.is_shutdown():
        key = getKey()
        if (key == '\x03'):
            print("Detenido")
            client.write_register(17,0,unit=5)
            client.write_register(20,9,unit=5)
            time.sleep(2)
            client.write_coil(102,True,unit=5)
            break
        else:
            rospy.Subscriber("control_gamma", Int16, callback_gamma)
            if direction == 0:
                client.write_coil(98, True, unit=5)
                client.write_coil(99, False, unit=5)
            elif direction == 2:
                client.write_coil(99, True, unit=5)
                client.write_coil(98, False, unit=5)
            elif direction == 1:
                client.write_coil(98, False, unit=5)
                client.write_coil(99, False, unit=5)

if __name__ == '__main__': #metodo main que arroja un exception en caso de un error en la comunicacion
    if os.name != 'nt':
        try:
            settings = termios.tcgetattr(sys.stdin)
            listener()
        except:
            print e
    if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
