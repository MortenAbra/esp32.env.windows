import serial, time, sys

port = ''
baudrate = 115200

def read():

    # open serial connection
    connection = serial.Serial(port, baudrate)

    # open raw log file
    file = open('logs/raw_log.txt', 'a')

    try:
        while True:

            # read value, should be 4 bytes long
            # decode to utf-8
            value = connection.read(4).decode('utf-8')

            # write timestamp and value to raw log file
            file.write('%s,%s\n'%(str(round(time.time())), str(value)))

            # print to console
            print(round(time.time()), 'received value =', value)
            
    except KeyboardInterrupt:
        file.close()
        exit('Finished.')


if __name__ == '__main__':
    port = sys.argv[2]
    print('Starting read from serial:')
    read()
        

