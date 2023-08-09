import serial
import time

def swrite(serc):
    wt=serc+"\n"
    print(wt);
    ser.write(wt.encode());
    line=ser.readline();
    if line.decode('ascii') == "":
        print('')
    else:     
        print(line);

    line = line.decode('ascii')
    line2 = str(line)
    line2 = line2.strip()
    return (line2)

def fget(line):
    return float(line)

def testc(a,f,inc):

    print(" ");
    print("Check: From: "+str(a)+" To: "+str(f)+"     inc:"+str(inc));
    
    for i in range(a,f,inc):
        
        cv=(i/1000)
        swrite("VOLT "+str(cv));
        swrite("OUTP ON");

        time.sleep(0.5);
        currstr=swrite("MEAS:CURR?");
        currfloat=fget(currstr);
        if currfloat > 1.2 :
            if inc == 1 :
                print("Current: "+str(currfloat));
                return cv;
            
            at = i-inc;

            swrite("OUTP OFF");
            time.sleep(0.5);
            
            return testc(at,i,int(inc/10));
    
    return 0


print("Opening serial connection...");
ser = serial.Serial('COM3', 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=2)

print("waiting...");
time.sleep(1)

print("setting defaults...");
swrite("VOLT:RANG P20V");
#swrite("OUTP OFF");
swrite("CURR 3");
swrite("VOLT 10");

swrite("OUTP ON");

currstr=swrite("MEAS:CURR?");
currfloat=fget(currstr);
if currfloat > 2:
    print("OverCurrent!");
    print("TEST FAILED");
    swrite("OUTP OFF");
    quit()
 
res=testc(12000,14000,1000);

swrite("OUTP OFF");

if res == 0:
    print("TEST FAILED");

print("TEST RESULT: "+str(res)+" Volt");

ser.close()