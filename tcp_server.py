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
                  ┗┻┛  ┗┻┛
"""
# from socket import *
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 9999))
# server.listen(100)
# while True:
#     sc, caddr = server.accept()
#     receivebytes = sc.recv(1024)
#     receivedata = receivebytes.decode("utf-8")
#     print("收到：%s" % receivedata)
#     sendenbytes = receivebytes
#     sc.send(sendenbytes)
#     # sc.close()
# with open('a.txt', 'w') as f:
#     f.read
# print('abc'.center(21, '*'))
# *********
# ********

from socket import *
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 6000))
server.listen()
sock, addr = server.accept()
# print(sock, addr)
while True:
    result = sock.recv(1024).decode('utf8')
    print(result)
    if result == 'exit':
        sock.send('exit'.encode('utf8'))
        break
    sock.send(input('imput data').encode('utf8'))

