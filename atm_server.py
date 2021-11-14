
#Name: Alec Burnworth
#ID: 010822093

import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

balance = 100
while 1:
    if sys.argv.__len__() != 2:
        serverPort = 4372
    else:
        serverPort = int(sys.argv[1])

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    while True:
        user_amount = ""
        user_choice = ""
        user_input = connectionSocket.recv(1024)
        user_input_decoded = user_input.decode('utf-8')
        input_array = user_input_decoded.split("\n")
        user_choice = input_array[0]
        user_amount = input_array[1]

        if user_choice == '1':
            balance = balance + int(user_amount)
            encoded_balance = str(balance).encode('utf-8')
            connectionSocket.send(encoded_balance)

        elif user_choice == '2':
            if int(user_amount) > balance:
                error_message = "Cannot withdraw more money than what is available"
                connectionSocket.send(error_message.encode('utf-8'))
            else:
                balance = balance - int(user_amount)
                encoded_balance = str(balance).encode('utf-8')
                connectionSocket.send(encoded_balance)

        elif user_choice == '3' and user_amount == "":
            current_balance = str(balance).encode('utf-8')
            connectionSocket.send(current_balance)
