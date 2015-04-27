#-*- coding: utf-8 -*-

from abc import ABCMeta

class IEventAdapter(object):

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    @abstractmethod
    def coinche(self, pid):
        raise NotImplemented


    @abstractmethod
    def belote(self, pid):
        raise NotImplemented

