
import serial.tools.list_ports

def retserial() :

    # this lines lists all the serial port components connected to the device
    ports = serial.tools.list_ports.comports()

    serialIns = serial.Serial()

    portlist = []

    for onePort in ports:
        portlist.append(str(onePort))
        print(str(portlist))

    serialIns.baudrate = 115200
    serialIns.port = 'COM7'
    serialIns.open()
    bp = []
    f = 62
    while f:
        if serialIns.in_waiting:
            packet = serialIns.readline()
            # print(packet.decode('utf-8'))
            vals = str(packet.decode('utf-8', errors='ignore'))
            lval = vals.split('x')
            lval = lval[0].strip('\r\n')
            print(lval)
            bp.append(lval)
            f -= 1

    return bp

def takeinput(att):

    bp = retserial()
    i = -6
    while i:
        if int(float(bp[i])) < 40 :
            i = i-3
        else :
            att[0][1] = int(float(bp[i]))  # bpm
            break

    i = -5
    while i:
        if int(float(bp[i])) < 80:
            i = i - 3
        else:
            att[0][5] = int(float(bp[i]))  # sp02
            break

    i = -4
    while i:
        if int(float(bp[i])) < 70:
            i = i - 3
        else:
            att[0][0] = int(float(bp[i]))  # sp02
            break

    return att

