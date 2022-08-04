import socket
from Test.Ip_key_test import *

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = local
        self.port = port
        self.address = (self.server, self.port)
        self.pos = self.conect()

    def get_pos(self):
        print(self.pos)
        return self.pos

    def conect(self):
        try: 
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
           pass
    

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket as e:
            print(e)


