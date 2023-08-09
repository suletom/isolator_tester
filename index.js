const { SerialPort } = require('serialport')

// Create a port
const port = new SerialPort({
  path: 'COM3',
  baudRate: 9600,
  stopBits: 2,
  parity: "none",
  dataBits: 8
});

class serialsync{

    constructor(port){
        this.port=port;
        this.commands=[];
        this.error="";

        this.port.on('data', function (data) {

            let floatstr=data.toString();
            let floatnum=Number.parseFloat(floatstr);
        
            console.log('Data:', data.toString())
            console.log('Float:',floatnum);
        
            this.commands[this.commands.length-1]["ret"]={"str":floatstr,"float":floatnum};
            
        });

    }

    write(cmd){
        console.log("writing command: ",cmd);
        commands.push({"cmd": cmd});

        this.port.write(cmd+"\n", function(err) {
            if (err) {
                console.log('Error on write: ', err.message)
                this.error='Error on write: ', err.message;
            }
        });

    }

    read(timeout=1){
        
    }

}


let commands=[];

write_ser("OUTP OFF");
write_ser("CURR 0.5");
write_ser("OLT:RANG P20V");

commands.push({"cmd": function(j=12){
    for(let i=j;i<=14;i++){
        //commands.push({"cmd": "OUTP ON"});
        //cmd: VOLT $i
        //wait
        //MEAS:CURR?
        //CURR>0.050 => 
    }
});
commands.push({"cmd": "OUTP OFF"});
//wait

commands.push({"cmd": function(){  //tizedre ,majd századra is ->az előző egész érétktől ahol még nem teljesült
    for(let i=12;i<=14;i++){
        //commands.push({"cmd": "OUTP ON"});
        //cmd: VOLT $i
        //wait
        //MEAS:CURR?
        //CURR>0.050 => 
    }
});

commands.push({"cmd": "MEAS:CURR?"});
commands.push({"cmd": "MEAS:VOLT?"});
commands.push({"cmd": "OUTP OFF"});

function write_ser(port,cmd) {

    
    
}


  
  // Open errors will be emitted as an error event
port.on('error', function(err) {
    console.log('Error: ', err.message)
});


