hotserver
===========

This is an implementation of Erlang's awesome hot-code-reloading
in python.It is very simple and highly readable(duhhh it's python).

### Example
First start the server:

    python hotserver.py 127.0.0.1 8080


Then a client:

    telnet 127.0.0.1 8080
    oi
You should get back an 'OI'.


Then open hotserver.py, and comment the following line(in the callback function):

    client.send(buff.upper())

Reconnect to the server and send the reload:

    telnet 127.0.0.1 8080
    reload

Reconnect(again) and send another request:

    telnet 127.0.0.1 8080
    oi

You wont get any answer.
Basically when you changed the hotserver.py and
sent the 'reload', the server updated the
callback function he was using.

