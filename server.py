"""
This define setting up of the server.

when running  a connection between clients and server will be made to send and recieve 
information to and from other clients from a port with the utilization of sockets and threading.
The script server.py must be running on machine that contains the local ip address.
"""
import socket
from _thread import *
from game import Game
from player import Player
import pickle 
import sys
from Ip_key import * 

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
s.listen(2)
print("Server started, Wating for connections....")

connected = set()
games = {}
idCount = 0

def thread_client(conn, player, gameId):
    global idCount
    conn.send(str.encode(str(player)))
    pass

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(player, data)
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("lost connections")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -=1
    conn.close()
    

while True:
    conn, address = s.accept()
    print("Connected to:", address)
    idCount +=1
    player = 0
    gameId = (idCount - 1)//2
    if  idCount %2 ==1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        player = 1
    start_new_thread(thread_client, (conn, player, gameId))
    
