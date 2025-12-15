#!/usr/bin/env python3
import serial
import time

# Adjust the device path to match your setup (e.g., /dev/ttyACM0 or /dev/ttyUSB0)
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600
TIMEOUT = 1  # seconds

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
    time.sleep(2)  # wait for the serial connection to initialize
    print("Pi: Serial connection established on", SERIAL_PORT)
except serial.SerialException as e:
    print("Pi: Could not open serial port:", e)
    exit(1)

try:
    # Example loop: send a message, then read any response
    while True:
        # Send a message to Arduino
        msg = "Hello from Raspberry Pi"
        ser.write((msg + '\n').encode('utf-8'))
        print("Pi -> Arduino:", msg)

        # Read any incoming data from Arduino
        if ser.in_waiting:
            line = ser.readline().decode('utf-8', errors='replace').strip()
            if line:
                print("Arduino -> Pi:", line)

        time.sleep(2)  # adjust as needed

except KeyboardInterrupt:
    print("Pi: Interrupted by user")

finally:
    if ser.is_open:
        ser.close()
    print("Pi: Serial port closed")

