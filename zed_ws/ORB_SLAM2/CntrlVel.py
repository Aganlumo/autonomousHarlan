#!/usr/bin/env python

# Reemplaza talker.py en beginner_tutorials/scripts

#Importacion de librerias importantes
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import rospy
from std_msgs.msg import Int16, String
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

#client.read_discrete_inputs(n,1,unit=5)
#client.read_input_registers(address,number_of_registers_to_read, unit=5)

acc_sp = 0
brk_sp = 9
direction = 4
stop_data = 0


def callback_acc(acc_data):
    global acc_sp
    acc_sp = acc_data.data

def callback_brk(brk_data):
    global brk_sp
    brk_sp = brk_data.data

def callback_gamma(twist_dir):
    global direction
    direction = twist_dir.data

# def callback_stop(stop_frame):
#     global stop_data
#     stop_data = stop_frame.data

def controlComm():
    print ("Connected")
    print ("K to stop control, Ctrl + C to kill program")
    rospy.init_node('listener', anonymous=True)
    client.write_coil(65,True,unit=5) # subrutinas y prender el plc
    # client.write_coil(60,True,unit=5) # accelerator
    client.write_coil(57,True,unit=5) # brakes
    client.write_coil(58,True,unit=5) # Energizar direccion
    time.sleep(1)
    while not rospy.core.is_shutdown():
        # rospy.Subscriber("accelerator", Int16, callback_acc)
        rospy.Subscriber("control_gamma", Int16, callback_gamma)
        rospy.Subscriber("brakes", Int16, callback_brk)
        # rospy.Subscriber("stopRoutine", Int16, callback_stop)
        emergency = client.read_coils(8,1,unit=5)
        directionPLC = client.read_input_registers(3,1,unit=5)
        if stop_data != 0:
            # client.write_register(17, 0, unit=5) #accelator
            client.write_coil(8, True, unit=5)
            # client.write_coil(58,False,unit=5)
            print 'stop'
            time.sleep(2)
            # pub_gamma.publish(0)
        elif emergency.bits[0] == False:
            # client.write_coil(58,True,unit=5)
            client.write_register(20, brk_sp, unit=5) #brakes
            client.write_register(25, direction, unit=5)
            # pub_gamma.publish(1)
            print 'directionSP: ', direction
            print 'direction:   ', directionPLC.registers[0]
            print 'ok'


if __name__ == '__main__': #metodo main que arroja un exception en caso de un error en la comunicacion
    if os.name != 'nt':
        try:
            settings = termios.tcgetattr(sys.stdin)
            # pubRoutine = rospy.Publisher('motion_state', Int16, queue_size=10)
            controlComm()
        except:
            print e
    if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
