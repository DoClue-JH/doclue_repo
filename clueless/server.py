#Server Module
import socket
from _thread import *
import pickle
import sys

HOST_ADDR = "192.168.1.24"
HOST_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST_ADDR, HOST_PORT))
except socket.error as err:
        str(err)

sock.listen(2)
print("Waiting for a connection, server started")

players = []
connected = set()

def threaded_client(conn, player, game):
    conn.send(str.encode(str(player)))
    reply = ""
    while True:
        try:
            player_data = conn.recv(4096).decode()

            if not player_data:
                print("Disconnected")
                break
            else:
                if player_data == "reset":
                    game.reset_round()
                elif player_data != "get":
                    print("Player taking turn")
                    print("Player mouse position: ", player_data)

                conn.sendall(pickle.dumps(game))
        except:
            break

    print("Lost connection")
    try:
        print("Closing Game")
    except:
        pass

    conn.close()

    sys.exit("Server Closed")


while True:
    conn, addr = sock.accept()
    print("Connected to:", addr)

    player = 0
    game = 1

    start_new_thread(threaded_client, (conn, player, game))