#!/usr/bin/env python
import minimalmodbus
import time

minimalmodbus.BAUDRATE = 9600

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

while True:
    # Register number, number of decimals, function code
    meter = instrument.read_register(03, 03, 4)
    instrument.read_register(17,1,9006)
    print (meter)
    time.sleep(1)