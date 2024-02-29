
import socket


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
        print()

        #print(LeapIndicator
        
        
        LeapIndicator = ("no warning",
                         "last minute has 61 sec",
                         "last minute has 59 sec",
                         "not synchronized")[response[0] >> 6]
        
        Version = response[0] >> 3 & 0b1111

        Mode = ("reserved",
                "symmetric active",
                "symmetric passive",
                "client",
                "server",
                "broadcast",
                "reserved for NTP control message",
                "reserved for private use")[response[0]& 0b111]
        
        Stratum = response[1]
        if Stratum == 0:
           Stratum = "kiss-o'-death message (see below)"
        elif Stratum == 1:
            Stratum = "primary reference (e.g., synchronized by radio clock)"
        elif Stratum < 16:
           Stratum = "secondary reference (synchronized by NTP or SNTP)"
        else:
           Stratum = "reserved"
    
        Presision = response[3]

        RootDelay = int.from_bytes(response[4:8])
        RootDispersion = int.from_bytes(response[8:12])
        ReferenceIdentifier = int.from_bytes(response[12:16])
        ReferenceTimestamp = int.from_bytes(response[16:24])
        OriginateTimestamp = int.from_bytes(response[24:32])
        
        print(f'{LeapIndicator=}\n{Version=}\n{Mode=}\n{Stratum=}\n{Presision=}')

    except TimeoutError:
       print("Can't conect: timeout")
    finally:
        print("finaly")












if __name__ == "__main__":
    get_ntp_time()