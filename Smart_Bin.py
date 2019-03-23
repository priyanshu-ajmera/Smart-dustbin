import RPi.GPIO as sb
import time
sb.setmode(sb.BOARD)
sb.setwarnings(False)
sb.setup(3,sb.OUT)                          #Ultrasonic Rx
sb.setup(5,sb.IN)                           #Ultrasonic Tx        
sb.setup(7,OUT)                             #Buzzer
sb.setup(11,OUT)                            #Motor
sb.setup(12,OUT)                            #Motor 
sb.setup(13,IN)                             #IR Sensor
echo=5
trig=3
buzz=7
motor1=11
motor2=12
ir=13
while 1:
    if(sb.input(ir)==1):
        sb.input(echo,1)                    #switch on the trigger pulse
        time.sleep(0.00001)
        sb.input(echo,0)                    #triggered for 10 microsec
        time_start=time.time()              #note the start time duration

        while (sb.output(trig,1)):
            time_end=time.time()            #note the end time

        duration=time_end - time_start      #note the distance

        dist=(duration*17050)               #distance=time*speed(=341m/sec)
        print("distance= ",dist)
        if(dist>5):
            sb.output(motor1,1)             #Lid OPEN
            sb.output(motor2,0)
            time.sleep(5)
            sb.output(motor1,0)             #Motor OFF
            sb.output(motor2,0)
            sb.output(buzz,0)               #Buzzer OFF
            time.sleep(10)
            sb.output(motor1,0)             #Lid CLOSE
            sb.output(motor2,1)
            time.sleep(5)
            sb.output(motor1,0)             #Motor OFF
            sb.output(motor2,0)
        else:
            sb.output(motor1,0)             #Motor OFF
            sb.output(motor2,0)
            sb.output(buzz,1)               #Buzzer ON
            time.sleep(5)
            sb.output(buzz,0)
    else:
        sb.output(motor1,0)                 #Motor OFF
        sb.output(motor2,0)
        

        
