from multiprocessing.connection import Listener


# receive data
def receive_data(conn):
    print("server receive_data")
    result = -1
    while True:
        try:
            msg = conn.recv()  # received result
            print(msg)
            if msg == 'passed':
                result = 1
            elif msg == 'not_passed':
                result = 0
            # conn.close()
        except:
            print("receiving is completed")
            break

    return result


# start server
def result_receiver(address):
    print("server result_receiver")
    serv = Listener(address)
    rslt = -1
    while True:
        client = serv.accept()
        rslt = receive_data(client)
        print(rslt)
        if rslt != -1:
            break

    return rslt
