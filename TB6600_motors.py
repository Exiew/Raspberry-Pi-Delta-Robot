from time import sleep
import RPi.GPIO as gpio
import multiprocessing as mp
import math

def motor1(x):
    #x is an angle in degree
    #set pin output for driver motor
    DIR1 = 27
    PUL1 = 17
    
    #set pin at Raspberry Pi
    gpio.setmode(gpio.BCM)
    gpio.setup(DIR1, gpio.OUT)
    gpio.setup(PUL1, gpio.OUT)
    
    t = math.sqrt((math.radians(abs(x))*2)/1)
    f = round((400/360)*(abs(x)/t))
    s = f*(360/400)
    p1 = gpio.PWM(PUL1, f)
    p1.start(0)
       
    # Main body of code
    try:
        # If the motor used gearbox no need for lines 27-28.
        # These lines is just for better accuracy
        if x%.9 != 0:
            x = round(.9*round(x/.9),1)
            
        if x < 0:
            # Direction: ccw
            gpio.output(DIR1, gpio.LOW)
            p1.ChangeDutyCycle(50)
            sleep((-x)/s)
            
        else:
            # Direction: cw
            gpio.output(DIR1, gpio.HIGH)
            p1.ChangeDutyCycle(50)
            sleep(x/s)
            
        p1.stop()
        gpio.cleanup((17,27))
        
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    except KeyboardInterrupt: 
        print("Cleaning up!")
        p1.stop()
        gpio.cleanup()

def motor2(x):
    #x is an angle in degree
    #set pin output for driver motor
    DIR2 = 18
    PUL2 = 23
    
    #set pin at Raspberry Pi
    gpio.setmode(gpio.BCM)
    gpio.setup(DIR2, gpio.OUT)
    gpio.setup(PUL2, gpio.OUT)
    
    t = math.sqrt((math.radians(abs(x))*2)/1)
    f = round((400/360)*(abs(x)/t))
    s = f*(360/400)
    p2 = gpio.PWM(PUL2, f)
    p2.start(0)
         
    # Main body of code
    try:
        # If the motor used gearbox no need for lines 72-73.
        # These lines is just for better accuracy
        if x%.9 != 0:
            x = round(.9*round(x/.9),1)
        if x < 0:
            # Direction: ccw
            gpio.output(DIR2, gpio.LOW)
            p2.ChangeDutyCycle(50)
            sleep((-x)/s)
            
        else:
            # Direction: cw
            gpio.output(DIR2, gpio.HIGH)
            p2.ChangeDutyCycle(50)
            sleep(x/s)
            
        p2.stop()
        gpio.cleanup((18, 23))
        
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup    
    except KeyboardInterrupt: 
        print("Cleaning up!")
        p2.stop()
        gpio.cleanup()

def motor3(x):
    #x is an angle in degree
    #set pin output for driver motor
    DIR3 = 12
    PUL3 = 13
    
    #set pin at Raspberry Pi
    gpio.setmode(gpio.BCM)
    gpio.setup(DIR3, gpio.OUT)
    gpio.setup(PUL3, gpio.OUT)
    
    t = math.sqrt((math.radians(abs(x))*2)/1)
    f = round((400/360)*(abs(x)/t))
    s = f*(360/400)
    p3 = gpio.PWM(PUL3, f)
    p3.start(0)
          
    # Main body of code
    try:
        # If the motor used gearbox no need for lines 116-117.
        # These lines is just for better accuracy
        if x%.9 != 0:
            x = round(.9*round(x/.9),1)
        if x < 0:
            # Direction: ccw
            gpio.output(DIR3, gpio.LOW)
            p3.ChangeDutyCycle(50)
            sleep((-x)/s)

        else:
            # Direction: cw
            gpio.output(DIR3, gpio.HIGH)
            p3.ChangeDutyCycle(50)
            sleep(x/s)
        
        p3.stop()
        gpio.cleanup((12, 13))
    
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    except KeyboardInterrupt: 
        print("Cleaning up!")
        p3.stop()
        gpio.cleanup()

def motors(x, y, z):
    #x = teta 1
    #y = teta 2
    #z = teta 3
    #parallel processing
    pool1 = mp.Process(target=motor1, args=(x,))
    pool1.start()
    pool2 = mp.Process(target=motor2, args=(y,))
    pool2.start()
    pool3 = mp.Process(target=motor3, args=(z,))
    pool3.start()
    pool1.join()
    pool2.join()
    pool3.join()

    