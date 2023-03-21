#Server Module
import socket
import threading
import pickle
import sys

#HOST_ADDR = "192.168.1.24"
HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 8080
PLAYER_MAX = 3
PLAYER_MIN = 3

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST_ADDR, HOST_PORT))
except socket.error as err:
        str(err)


def threaded_client(conn, player_id, game):
    conn.send(pickle.dumps(player_id))
    reply = ""
    #player_data = Package()
    connected = True

    while connected:
        try:
            #print("Server receiving player data")
            player_data = pickle.loads(conn.recv(4096))
            #print(player_data)
            #print("Server received player data")

            if not player_data:
                print("Disconnected")
                connected = False
                break
            else:
                #if player_data == "reset":
                #    game.reset_round()
                #elif player_data != "get":
                #    print("Player status: ", player_data)
                #    #conn.send(pickle.dumps(player_data))

                status = player_data['header']
                player_id = player_data['player_id']
                #print(status)

                if status == "reset":
                    game.reset_round()
                elif status != "get":
                    player_status = player_data['data']
                    if status == "CHOOSING":
                            print("Player taking turn: Player ", player_id)
                            print("Player chooses to move to location ", player_status)
                            print()

                    #conn.send(pickle.dumps(player_data))

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

def start():
    id_count = 0
    server.listen(2)

    while True:
    #this loops runs forever, so any print statements outside of 
    # the if statemennt will print forever

        if (id_count < PLAYER_MAX):
            conn, addr = server.accept()
            print("Connected to:", addr)
            
            game = 1

            thread = threading.Thread(target=threaded_client, args=(conn, id_count+1, game))
            thread.start()
            id_count = threading.active_count()-1
            print("Active Players: ", threading.active_count()-1)
            print()



print("Waiting for a connection, server started")
start()