<<<<<<< HEAD
python hot-server
===========

This is an implementation of Erlang's awesome hot-code-reloading
in python.
It is very simple and highly readable(duhhh it's written in python).

Example
=============
First start the server:
  python hotserver.py 127.0.0.1 8080


Then a client:
  telnet 127.0.0.1 8080
  oi
You should get back an upper 'OI'.


Then open hotserver.py, and comment the following line(in the callback function):
  client.send(buff.upper())

Reconnect to the server and send the reload:
  telnet 127.0.0.1 8080
  reload

You wont get any answer.

=======
hotserver
=========

Erlang's awesome hot-code-reloading in python
>>>>>>> b53d53bf91a354457962ab886aafd037de7c264c
