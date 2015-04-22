# -*- coding: utf-8 -*-

from abc import ABCMeta

class IConsole(object):

    __metaclass__ = ABCMeta

    def write(self, msg):
        raise NotImplemented

    def clear(self):
        raise NotImplemented
