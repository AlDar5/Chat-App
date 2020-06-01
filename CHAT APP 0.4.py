import socket
import threading
from datetime import datetime
import time



def SERVER(): # Wont have any "input" command # THREAD 1
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_SOCKET)
    server.listen()
    print(f"[LISTENING] Server started in socket: {SERVER_SOCKET}\n")


    # Looks for connections and accepts them
    global conn, addr
    conn, addr = server.accept()
    print(f"[CONNECTION] {addr} connected.")
    # print(conn, addr)


    # Reverse communication (message sending)
    global CONNECTED
    CONNECTED = True
    CLIENT_THREAD = threading.Thread(target=CLIENT)
    CLIENT_THREAD.start()

    # Client handling (message receiving)
    HANDLE_CLIENT()
    # print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")

def HANDLE_CLIENT():
    global CONNECTED
    while CONNECTED:
        # Msg handling
        msg = message_reciever()
        timestamp = str(datetime.now())


        # Command portion
        if msg == DISCONNECT_MESSAGE:
            print(f"[DISCONNECTION] {addr} has been disconnected at {timestamp}")
            print("[ATTENTION] You can no longer receive messages!")
            CONNECTED = False
            break
        else:
            # Just message printing
            msg = f"\r[{addr}|{timestamp}]\n::{msg}\n\n>" # Put \r at the start to delete previus line
            print(msg, end="") # put 'end=""' to avoid new line

def message_reciever():
    message_length = conn.recv(HEADER).decode(FORMAT)
    if message_length: # If the message length header has something is going to decode
        message_length = int(message_length)
        msg = conn.recv(message_length).decode(FORMAT)
        return msg






def CLIENT(): # Any "input" command will be here
    global CONNECTED, conn, addr
    if not CONNECTED:
        CONNECTED = True
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(CLIENT_SOCKET)
        SERVER_THREAD = threading.Thread(target=HANDLE_CLIENT)
        SERVER_THREAD.start()

        addr = CLIENT_SOCKET

    while CONNECTED:
        msg = input("\n>")

        if msg == DISCONNECT_MESSAGE:
            inx = input("[ATTENTION] Are you sure you want to disconnect? YES(Y)/NO(N)")
            if inx.lower() == "y":
                send_message(msg)
                CONNECTED = False
                exit("You /disconnected")
                break

        else:
            send_message(msg)


def send_message(msg):
    message = msg.encode(FORMAT) # Encodes the message itself
    message_length = str(len(message)) # Converts the length of the encoded message to a string
    send_length = message_length.encode(FORMAT) # Formats the length o the encoded message
    send_length += b" " * (HEADER - len(send_length)) # Padds the message

    # print(msg, message, send_length)

    conn.send(send_length)
    conn.send(message)



#--------------------------------------------------------------------------------------------
# UNIVERSAL VARIABLES
HEADER = 5
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "/disconnect"



# Who you want to connect
CONNECTED = False
CLIENT_PORT = 0
# SERVER_IP_ADDRESS = ""
CLIENT_IP_ADDRESS = socket.gethostbyname(socket.gethostname())


# Who are you?
# SERVER_PORT = 55554 # this instance port
SERVER_IP_ADDRESS = socket.gethostbyname(socket.gethostname()) # Gets you local ip address
# SERVER_SOCKET = (SERVER_IP_ADDRESS, SERVER_PORT)  # it MUST be in a tuple as "socket.bind" only accepts a tuple





# Thread 0
# CHAT APP # [ALSO] Dont foret to start the thread
inx = input("Do you want to connect so someone or do you want to wait? CONNECT(c)/WAIT(w)")
if inx.lower() == "c": # Connects you to a server
    CLIENT_IP_ADDRESS = input("IP ADDRESS:")
    CLIENT_PORT = int(input("PORT:"))
    CLIENT_SOCKET = (CLIENT_IP_ADDRESS, CLIENT_PORT)


    CLIENT_THREAD = threading.Thread(target=CLIENT)
    CLIENT_THREAD.start()


elif inx.lower() == "w": # Starts the server and waits for a connection
    SERVER_PORT = int(input(f"What port do you want to open?:"))
    SERVER_SOCKET = (SERVER_IP_ADDRESS, SERVER_PORT)

    SERVER_THREAD = threading.Thread(target=SERVER)
    SERVER_THREAD.start()