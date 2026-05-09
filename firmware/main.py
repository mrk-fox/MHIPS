# use https://github.com/Longan-Labs/MicroPython_CAN_BUS_MCP2515 for CAN bus support
import sys
import time
from machine import Pin
from canbus import Can, CanError, CanMsg, CanMsgFlag

id = 0x002

id_byte_high = (id >> 8) & 0xFF
id_byte_low  = id & 0xFF 

setup_array = [Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN, Pin.IN]
pin_addr_array = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10]
states_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pin_array = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]


can = Can()
error = can.begin()
if error != CanError.ERROR_OK:
    print("Failed to initialize can!")


p0 = Pin(2, setup_array[0])
p1 = Pin(3, setup_array[1])
p2 = Pin(4, setup_array[2])
p3 = Pin(5, setup_array[3])
p4 = Pin(6, setup_array[4])
p5 = Pin(7, setup_array[5])
p6 = Pin(8, setup_array[6])
p7 = Pin(9, setup_array[7])
p8 = Pin(11, setup_array[8])
p9 = Pin(12, setup_array[9])
p10 = Pin(13, setup_array[10])
p11 = Pin(14, setup_array[11])
p12 = Pin(15, setup_array[12])
p13 = Pin(16, setup_array[13])
p14 = Pin(17, setup_array[14])
p15 = Pin(18, setup_array[15])


for i in range(0, 16):
    read = pin_array[i].value()
    states_array[i] = read

while True:
    for i in range(0, 16):
        read = pin_array[i].value()
        if read != states_array[i]:
            states_array[i] = read
            msg = CanMsg(can_id=id, data=b"\x01\id_byte_high\id_byte_low\x00\x00\x00\x00\pin_addr_array[i]")
            error = can.send(msg)
            if error != CanError.ERROR_OK:
                print("Failed to send!")
    if can.checkReceive():
        error, msg = can.recv()
        if error == CanError.ERROR_OK:
            print("Can id", msg.can_id)
            print("Can data", msg.data)
    time.sleep(0.1)
