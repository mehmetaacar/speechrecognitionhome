import RPi.GPIO as GPIO
import time
import speech_recognition as sr

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)


r = sr.Recognizer()
m = sr.Microphone()    


def listen():
    try:
        print("Sessizlik, lutfen...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        # print("Set minimum energy threshold to {}".format(r.energy_threshold))
        
        while True:
            with m as source:
                audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                print("Bir sey soyle!")
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                    return value
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(value))
                    if value == "can you open bedroom":
                        print("Yes, i can ;)")
                        GPIO.output(11,True)
                    if value == "can you close bedroom":
                        print("Yes, i can ;)")
                        GPIO.output(11,False)
                    if value == "can you open restroom":
                        print("Yes, i can ;)")
                        GPIO.output(13,True)
                    if value == "can you close restroom":
                        print("Yes, i can ;)")
                        GPIO.output(13,False)
                    if value == "can you open black":
                        print("Yes, i can ;)")
                        GPIO.output(19,True)
                    if value == "can you close black":
                        print("Yes, i can ;)")
                        GPIO.output(19,False)
                    if value == "can you open everything":
                        print("Yes, i can ;)")
                        GPIO.output((11,13,19),True)
                    if value == "can you close everything":
                        print("Yes, i can ;)")
                        GPIO.output((11,13,19),False)
                            
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
listen()
"""
while True :
            print("Seni dinliyorum...")
            if listen() == "bedroom":
                while True:
                    print("Yatak odasindasin, ne yapacaksin ?")
                    #if listen() == "go back":
                     #   print("Returning...")
                       # break
                    if listen() == "open":
                        print("Lights opened")
                        GPIO.output(11,True)
                        GPIO.output(13,True)
                        GPIO.output(15,True)
                        break
                    if listen() == "close":
                        print("Lights closed")
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)
                        break
                    print("Yatak odasindasin, ne yapacaksin ?")
            if listen() == "restroom":
                while True:
                    print("Salondasin, ne yapacaksin ?")
                    #if listen() == "go back":
                     #   print("Returning...")
                      #  break
                    if listen() == "open it":
                        print("Lights opened")
                        GPIO.output(13,True)
                        break
                    if listen() == "close":
                        print("Lights closed")
                        GPIO.output(13,False)
                        break
                    print("Salondasin, ne yapacaksin ?")
            if listen() == "door":
                while True:
                    
                    print("What can i do for you ?")
                    #if listen() == "go back":
                     #   print("Returning...")
                      #  break
                    if listen() == "open it":
                    
                        print("Fan opened")
                        GPIO.output(15,True)
                        break
                    if listen() =="close":
                        print("Fan closed")
                        GPIO.output(15,False)
                        break
                    print("Fandasin, ne yapacaksin ?")
            else:
                print("Seni dinliyorum...2")

"""



""" blinking function
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        return
 to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
 blink GPIO17 50 times

            if (value) == "hey":
                blink(11)
                GPIO.cleanup()

for i in range(0,2):
        blink(11)
        
    """

