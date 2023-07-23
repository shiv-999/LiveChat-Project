import os, socket, threading


os.system("clear")
os.system("systemctl stop firewalld")
os.system("figlet -c -f bubble.flf UDP CHAT APP | lolcat -a -d 3")
os.system("espeak-ng 'Your welcome to my udp chat application'")
os.system("tput setaf 3")
ip = input("\n\n\t\t\t Enter Your ip: ")
print("\n")
sender_ip = input("\t\t\t Enter the server  ip: ")
print("\n\n")
os.system("tput setaf 6")
print("\t\t  <--------------------------- Start Chatting ---------------------------->")
os.system("tput setaf 7")

def reciver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 1234

    s.bind((ip, port))

    while True:
        os.system("tput setaf 5")
        x = s.recvfrom(1024)

        data = x[0].decode()
        if (("exit" in data)or ("Exit" in data) or ("EXIT" in data)):
            os.system("tput setaf 1")
            print("\t\t\t Your friend has gone  offline... !!!\n\n")
            os.system("tput setaf 5")
            ex = input("\t Do you want to exit ?? (y/n): ")
            if "y" in ex :
                os.system("tput setaf 5")
                print("\n\n\t\t\t Thanks for using my Chat Application ..... !!!\n")
                os.system("tput setaf 7")
                os._exit(1)
        client_ip = x[1][0]
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t     |",end="")
        os.system("tput setaf 2")
        print("\t   ","   from--> ",client_ip," : ",data)
        os.system("tput setaf 7")

def sender():
    os.system("tput setaf 5")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 1234
    print("\n")
    while True:
        os.system("tput setaf 5")
        message = input().encode()
        s.sendto(message, (sender_ip,port))
        if (("exit" in message.decode())or ("Exit" in message.decode()) or ("EXIT" in message.decode())):
            os.system("tput setaf 3")
            print("\t\t\t Thanks for using my Chat Application ..... !!!\n")
            os.system("tput setaf 7")
            os._exit(1)


t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=reciver)

t1.start()
t2.start()
