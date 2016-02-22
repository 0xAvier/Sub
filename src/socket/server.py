#!/usr/bin/python

import socket
import thread
import pickle
from confiture import Confiture

from src.adapter.remote_player_adapter import RemotePlayerAdapter
from src.socket.code import ACK

class Server(object):

    def __init__(self, config_file):
        conf = Confiture("config/templates/server.yaml")
        self.__config = conf.check_and_get(config_file)
        self.__port = int(self.__config["port"])
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind(('', self.__port))
        self.__players = dict()


    def idle(self):
        while True:
            self.__sock.listen(0)
            client, addr = self.__sock.accept()
            pid = int(client.recv(2048))
            self.__players[pid] = (RemotePlayerAdapter(self, pid), client, addr)
            self.__ack(pid)

    
    @property
    def nb_players(self):
        return len(self.__players)

    
    @property
    def player(self):
        return [a for a, b, c in self.__players.values()]


    def __syn(self, pid):
        assert self.__players[pid][1].recv(2048) == ACK


    def __ack(self, pid):
        assert self.__players[pid][1].send(ACK)


    def send_to_player(self, pid, CODE, args):
        self.__players[pid][1].send(str(CODE))
        self.__syn(pid)
        for arg in args:
            self.__players[pid][1].send(pickle.dumps(arg))
            self.__syn(pid)

