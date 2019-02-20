"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/2/20
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛'hello server'.encode('utf8'),
"""
from socket import *
# tcp
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 6000))
while True:
    senddata = input("输入要发送的数据")
    client.send(senddata.encode('utf-8'))
    result = client.recv(1024).decode('utf8')
    if result == 'exit':
        break
client.close()



# sc = socket(AF_INET, SOCK_STREAM)
# saddr = ('192.168.15.12', 60000)
# sc.connect(saddr)
# while True:
#     senddata = input("输入要发送的数据")
#     if senddata.__eq__("exit"):
#         sc.close()
#         break
#     sendbytes = senddata.encode("utf-8")
#     sc.send(sendbytes)
#     receivebytes = sc.recv(1024)
#     receivedata = receivebytes.decode("utf-8")
#     print(receivedata)
