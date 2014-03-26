# taken from http://sdiehl.github.io/gevent-tutorial/

from gevent.server import StreamServer

def handle(socket, address):
    socket.send("Hello from a telnet!\n")
    for i in range(5):
        socket.send(str(i) + '\n')
    socket.close()

server = StreamServer(('127.0.0.1', 5000), handle)
server.serve_forever()


