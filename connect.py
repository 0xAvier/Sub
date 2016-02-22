#-*- coding: utf-8 -*-


from src.socket.client import Client


client = Client("config/client.yaml")
client.idle()
