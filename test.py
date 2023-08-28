import serial
import time
from datetime import datetime

def swrite(serc):
    wt=serc+"\n"
    print(serc);
    ser.write(wt.encode());
    line=ser.readline();
    #if line.decode('ascii') == "":
    #    print('')
    #else:     
    #    print(line);

    line = line.decode('ascii')
    print(line);
    line2 = str(line)
    line2 = line2.strip()
    return (line2)

def fget(line):
    return float(line)

def testc(a,f,inc):

    print(" ");
    print("Check: Tol: "+str(a)+" Ig: "+str(f+inc)+"     inc:"+str(inc));
    
    for i in range(a,f+inc,inc):
        
        cv=(i/1000)
        swrite("VOLT "+str(cv));

        time.sleep(12);
        currstr=swrite("MEAS:CURR?");
        currfloat=fget(currstr);
        if currfloat > 0.05 :
            if inc == 1 :
                print("Current: "+str(currfloat));
                return cv;
            
            at = i-inc;

            swrite("VOLT 0");
            time.sleep(1);
            
            return testc(at,i,int(inc/10));
    
    return 0

def testcback(a,f,inc):

    print(" ");
    print("Check: From: "+str(a-inc)+" To: "+str(f)+"     inc:"+str(inc));
    
    for i in reversed(range(a-inc,f,inc)):
        
        cv=(i/1000)
        swrite("VOLT "+str(cv));

        time.sleep(12);
        currstr=swrite("MEAS:CURR?");
        currfloat=fget(currstr);
        if currfloat < 0.05 :
            if inc == 1 :
                print("Current: "+str(currfloat));
                return cv;
            
            at = i+inc;

            swrite("VOLT 14");
            time.sleep(12);
            
            return testcback(i,at,int(inc/10));
    
    return 0

print("Opening serial connection...");
ser = serial.Serial('COM3', 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=2)

print("waiting...");
time.sleep(0.5)

print("setting defaults...");
swrite("OUTP OFF");
swrite("VOLT:RANG P20V");
swrite("CURR 0.5");
swrite("VOLT 10");

swrite("OUTP ON");

logfile = open("tester_logfile.txt", "a");

currstr=swrite("MEAS:CURR?");
currfloat=fget(currstr);
if currfloat > 0.49 :
    print("OverCurrent!");
    print("TEST FAILED");
    logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": Overcurrent TEST FAILED\n")
    swrite("OUTP OFF");
    quit()
 
swrite("VOLT 14");
time.sleep(20)
currstr=swrite("MEAS:CURR?");
currfloat=fget(currstr);
voltstr=swrite("MEAS:VOLT?")
voltval=fget(voltstr)
ohm=voltval/currfloat
swrite("VOLT 0");


res=testc(12000,15000,1000);

if res == 0:
    print("TEST FAILED");
    logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": TEST FAILED\n")
    quit();

res2=testcback(10000,15000,1000);

swrite("OUTP OFF");

if res2 == 0:
    print("BACKTEST FAILED");
    logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": BACKTEST FAILED\n")
    quit();


print("TEST RESULT: "+str(res)+" Volt");
print("BACKTEST RESULT: "+str(res2)+" Volt");
print("10V resistance measurment: "+str(ohm)+" Ohm");

logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": TEST RESULT: "+str(res)+" Closing Voltage\n")
logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": BACKTEST RESULT: "+str(res2)+" Opening Voltage\n")
logfile.write(datetime.now().strftime('%Y-%m-%d_%H-%M')+": 10V resistance measurment: "+str(ohm)+" Ohm\n")

ser.close()