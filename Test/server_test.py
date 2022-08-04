"""
This define setting up of the server.

when running  a connection between clients and server will be made to send and recieve 
information to and from other clients from a port with the utilization of sockets and threading.
The script server.py must be running on machine that contains the local ip address.
"""
import socket
from _thread import *
import sys
from Test.Ip_key_test import * 

server = local
port = port

"""
Since we will be using ip b4 address we will set up the sockets utilizing AFNet connections and then bind 
our servers and port to it, encoding and decoding our information. 
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


# opens up the port to 4 people
s.listen()
print("Server started, Wating for connections....")


def read_pos(strs: str):
    """
    takes in  a string inpurt and convert it to tuple of interger.
    Parameters
    ----------
        strs: str
        string input 
    """
    strs = strs.split(",")
    return int(strs[0]), int(strs[1])

def make_pos(tup):
    """
    takes in a tuple and creates a string
    Parameters
    ----------
        tup: tuple
    """
    return str(tup[0]) + "," + str(tup[1])


"keeps track of players position, since its not alot of data we will store in memory"
pos = [(0,0), (100,100)]

def thread_client(conn, player):
    """
    generate multiple thread that encode and decode our info based on the position of our player
    Parameters
    ----------
        conn : str
            connection to port.
            this connection will be passed to the client threading function.
        player: any
            keeps track of our player based on connections
    """
    conn.send(str.encode(make_pos(pos[player])))
    reply= ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            # reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received:", data)
                print("Sending:", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connections")
    conn.close()

current_player =0
while True:
    conn, address = s.accept()
    print("Connected to:", address)

    start_new_thread(thread_client, (conn, current_player))
    current_player += 1
