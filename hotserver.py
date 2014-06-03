import imp
import socket
import sys

# Called foreach
# new connection
def callback(client, buff):
  sbuff = buff.strip()
  peer = client.getpeername()
  print "Received '%s' from %s:%d" % (sbuff, peer[0], peer[1])
  print "Echoing '%s' back" % sbuff
  client.send(buff.upper())
  client.close()


def spawn_server(host, port):
  global callback

  BUFSIZE = 1024

  sock = socket.socket()
  sock.bind((host, port))
  sock.listen(port)

  print "Server ready at %s:%d" % (host, port)
  while True:
    client,_ = sock.accept()
    buff = client.recv(BUFSIZE)
    
    if buff.strip().lower() == 'reload':
      import hotserver
      mod = imp.reload(hotserver)
      callback = mod.callback

    callback(client,buff)


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print "Usage python hotserver.py <host> <port>"
    sys.exit(1)

  host = sys.argv[1]
  port = int(sys.argv[2])

  spawn_server(host, port)


