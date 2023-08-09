import serial
import time

def swrite(serc):
    print(serc+"\n");
    ser.write(serc+"\n");
    line=ser.readline();
    print(line+"\n");

    return line;

def fget(line):
    return float(line)

def testc(a,f,inc):
    for i in range(a,f):
        swrite("VOLT "+(i/1000));
        swrite("OUTP ON");
        time.sleep(0.1);
        currstr=swrite("MEAS:CURR?");
        currfloat=fget(currstr);
        if currfloat > 0.050 :
            if inc = 10 :
                return currfloat
            return testc(i,i+1,inc/10);
    
    return 0


print("Opening serial connection...");
ser = serial.Serial('COM3', 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=2)

print("waiting...");
time.sleep(1)

print("setting defaults...");
swrite("OUTP OFF");
swrite("CURR 0.5");
swrite("VOLT:RANG P20V");
 
res=testc(12,14,1000);
if res = 0:
    print("TEST FAILED");

print("TEST RESULT: "+res);

ser.close()