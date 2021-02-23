from multiprocessing.connection import Listener

# receive data
def receive_data(conn):
    print("server receive_data")
    result = False
    while True:
        try: 
            msg = conn.recv()   # received result
            print(msg)
            if msg == 'passed':
                print("passed")
                result = True
            # conn.close()
        except:
            print("receiving is completed")
            break

    return result

# start server
def result_receiver(address):
    print("server result_receiver")
    serv = Listener(address)
    result = None
    while True:
        client = serv.accept()
        result = receive_data(client)
        print(result)
        if result is not None:
            break

    return result

# result_receiver(('', 5000))         # start receiving result