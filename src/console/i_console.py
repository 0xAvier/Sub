# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IConsole(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, msg):
        """
            Write a log message into console

        """
        raise NotImplemented

    @abstractmethod
    def clear(self):
        """
            Clear the console, ie remove all previously displayed 
            messages

        """
        raise NotImplemented
