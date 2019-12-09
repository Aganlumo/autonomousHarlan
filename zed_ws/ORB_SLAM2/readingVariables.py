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
client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=0.1, stopbits=1, bytsize=8, parity='N', baudrate=9600)
#En caso de no estar conectado al PLC, el programa arrojara un error en esta linea debido a que es la encargada de la comunicacion
client.connect()

e = """
Communications Failed
"""

emergency_button = 0
green_button = 0
brk_lin = 0
dir_lin = 0

#client.read_discrete_inputs(n,1,unit=5)
#client.read_input_registers(address,number_of_registers_to_read, unit=5)

def readVariables():
    while not rospy.core.is_shutdown():
        emergency_button = client.read_coils(102,1,unit=5)#8
        green_button = client.read_coils(105,1,unit=5)#49
        brk_lin = client.read_input_registers(7,1,unit=5)
        dir_lin = client.read_input_registers(3,1,unit=5)

        print 'emergency_button:    ', emergency_button.bits[0]
        print 'green_button:        ', green_button.bits[0]
        print 'brk_lin:             ', brk_lin.registers[0]
        print 'dir_lin:             ', dir_lin.registers[0]
        print ''

if __name__ == '__main__': #metodo main que arroja un exception en caso de un error en la comunicacion
    if os.name != 'nt':
        try:
            settings = termios.tcgetattr(sys.stdin)
            readVariables()
        except:
            print e
    if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
