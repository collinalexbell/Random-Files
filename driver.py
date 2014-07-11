import serial
import time


class driver:
    def __init__(self, broadcast = False):
        self.broadcast = broadcast
        self.has_ser = True
        try:
            self.ser = serial.Serial("/dev/ttyACM0")
            self.ser.baudrate = 9600
        except:
            print("Serial not found. Entering simulated mode")
            self.has_ser = False

    def stop(self):
        message = "Stop"
        if self.has_ser:
            self.ser.write('4')
            time.sleep(.5)
        else:
            message = message + '(simulated)'
            print("Stop(simulated)")
        if self.broadcast:
            self.broadcast_command(message)
    def forward(self):
        message = "forward"
        if self.has_ser:
            self.ser.write(('3'))
        else:
            message = message + '(simulated)'
            print("Forward(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def backward(self):
        message = "backward"
        if self.has_ser:
            self.ser.write('2')
        else:
            message = message + '(simulated)'
            print("Backward(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def left(self):
        message = "left"
        if self.has_ser:
            self.ser.write('3')
            time.sleep(.2)
            self.ser.write('0')
        else:
            message = message + '(simulated)'
            print("Left(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def backLeft(self):
        message = "BackLeft"
        if self.has_ser:
            self.ser.write('2')
            time.sleep(.2)
            self.ser.write('0')
        else:
            message = message + '(simulated)'
            print("BackLeft(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def right(self):
        message = "Right"
        if self.has_ser:
            self.ser.write('3')	
            time.sleep(.2)
            self.ser.write('1')
        else:
            message = message + '(simulated)'
            print("Right(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def backRight(self):
        message = "BackRight"
        if self.has_ser:
            self.ser.write('2')
            time.sleep(.2)
            self.ser.write('1')	
        else: 
            message = message + '(simulated)'
            print("BackRight(simulated)")
        if self.broadcast:
            self.broadcast_command(message)

    def broadcast_command(self,message):
        print(message)



        


