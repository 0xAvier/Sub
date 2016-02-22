#-*- coding: utf-8 -*-


import socket
import pickle
from confiture import Confiture
from src.socket.code import ACK, SOCK_DISCONNECT, SOCK_GIVE_CARDS, SOCK_BIDDED, SOCK_PLAYED


class Client(object):

    def __init__(self, config_file):
        conf = Confiture("config/templates/client.yaml")
        self.__config = conf.check_and_get(config_file)
        self.__svr_addr = self.__config["addr"]
        self.__svr_port = int(self.__config["port"])
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.__svr_addr, self.__svr_port))
        # TODO
        # Send player id to server
        self.__sock.send(str(1))
        self.__syn()


    def __ack(self):
        self.__sock.send(ACK)


    def __syn(self):
        assert self.__sock.recv(2048) == ACK


    def idle(self):
        recv = self.__sock.recv(2048)
        while recv != SOCK_DISCONNECT and recv != "":
            if recv == SOCK_GIVE_CARDS:
                self.__ack()
                cards = pickle.loads(self.__sock.recv(2048))
                self.__ack()
                print "GIVE CARDS: " + str(cards)
            elif recv == SOCK_BIDDED:
                self.__ack()
                bid = pickle.loads(self.__sock.recv(2048))
                self.__ack()
                print "BIDDED: " + str(bid)
            elif recv == SOCK_PLAYED:
                self.__ack()
                pid = pickle.loads(self.__sock.recv(2048))
                self.__ack()
                card = pickle.loads(self.__sock.recv(2048))
                self.__ack()
                print "PLAYED: {0} | {1}".format(pid, card)
            else:
                print "UNKONWN: #" + recv + "#"
            recv = self.__sock.recv(2048)

