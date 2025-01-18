

import socket
import datetime


def parse_ntp_response(response, verbouse = True):

    raw = {
        'Leap Indicator':response[0] >> 6,
        'Version Number':response[0] >> 3 & 0b1111,
        'Mode':response[0]& 0b111,
        'Stratum':response[1],
        'Poll':response[2],
        'Percicion':int.from_bytes(response[3:4], signed=True),
        'Root Delay':int.from_bytes(response[4:8], signed=True),
        'Root Dispersion':int.from_bytes(response[8:12]),
        'Referenve Identifier':int.from_bytes(response[12:16]),
        'Reference Timestamp':int.from_bytes(response[16:24]),
        'Originate Timestamp':int.from_bytes(response[24:32]),
        'Receive Timestamp':int.from_bytes(response[32:40]),
        'Transmit Timestamp':int.from_bytes(response[40:48]),
    }
    if not verbouse:
        return raw

    fancy = {
    'Leap Indicator':('no warning' ,'last minute has 61 seconds','last minute has 59 seconds','alarm condition')[raw['Leap Indicator']],
    'Version Number':raw['Version Number'],
    'Mode':('reserved' ,'symmetric active' ,'symmetric passive' ,'client' ,'server' ,'broadcast' ,'reserved for NTP control message' ,'reserved for private use')[raw['Mode']],
    'Stratum':("kiss-o'-death message" if raw['Mode'] == 0 else 'primary reference' if raw['Mode'] == 1 else 'secondary reference' if raw['Mode']  < 16 else 'reserved'),
    'Poll':f'{datetime.timedelta(seconds = 2 ** raw["Poll"])}',
    'Percision':2 ** raw['Percicion'],
    'Root Delay':raw['Root Delay'] / 2 **16,
    'Root Dispersion':raw['Root Dispersion'] / 2 ** 16,
    



    }
    

    return fancy


def get_ntp_time():
    server_url = "ntp0.ntp-servers.net"
    port = 123
    waiting_timeout = 5
    MySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MySocket.settimeout(waiting_timeout)
    try:
        MySocket.connect((server_url, port))
        packet = bytearray(48)
        packet[0]=0x1B
        MySocket.sendall(packet)
        response = MySocket.recv(48)
        parsed = parse_ntp_response(response, True)
        
        '''
        for row in range(12):
            print('\n',response[row*4:row*4 + 4], end=' ')
            for i in range(row*4, row*4 + 4):
                print(response[i], end=' ')
        '''
        [print(f'{i[0]}: {i[1]}') for i in parsed.items()]
        
        #print(f'{LeapIndicator=}\n{Version=}\n{Mode=}\n{Stratum=}\n{Presision=}')


    except TimeoutError:
       print("Can't conect: timeout")
    finally:
        print("finaly")













if __name__ == "__main__":
   print("\033c")
   get_ntp_time()