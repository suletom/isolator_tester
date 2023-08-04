const { SerialPort } = require('serialport')

// Create a port
const port = new SerialPort({
  path: 'COM3',
  baudRate: 9600,
  stopBits: 2,
  parity: "none",
  dataBits: 8
});

let commands=[];

commands.push({"cmd": "OUTP OFF"});
commands.push({"cmd": "CURR 0.5"});
commands.push({"cmd": "VOLT:RANG P20V"});
commands.push({"cmd": "VOLT 12"});
commands.push({"cmd": function(){
    for(let i=12;i<=14;i++){
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

port.write("MEAS:CURR?\n", function(err) {
    if (err) {
      return console.log('Error on write: ', err.message)
    }
    console.log('message written')
});
  
  // Open errors will be emitted as an error event
port.on('error', function(err) {
    console.log('Error: ', err.message)
});

port.on('data', function (data) {
    let floatstr=data.toString();
    let floatnum=Number.parseFloat(floatstr);



    console.log('Data:', data.toString())
    console.log('Float:',floatnum);
});
