
#Name: Alec Burnworth
#ID: 010822093
import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

proceed = True
while proceed:
    if sys.argv.__len__() != 3:
        serverName = 'localhost'
        serverPort = 4372
    else:
        serverName = sys.argv[1]
        serverPort = int(sys.argv[2])
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    while proceed:
        print("Please choose from the following actions:")
        print("1 Deposit\n2 Withdraw\n3 Check balance\n4 Exit")

        choice = input('Choice: ')

        if choice == '4':
            proceed = False
            print("Goodbye")
            break;

        elif choice == '1':
            print("How much would you like to deposit?")
            amount = input('Amount: ')
            try:
                if int(amount) > 0:
                    clientSocket.send(str.encode("\n".join([choice, amount])))

                else:
                    print("Cannot deposit negative amount")

            except ValueError:
                print("Invalid input, inputs cannot be float or string")

        elif choice == '2':
            print("How much would you like to withdraw?")
            amount = input('Amount: ')

            try:
                if int(amount) > 0:
                    clientSocket.send(str.encode("\n".join([choice, amount])))
                    message = format(clientSocket.recv(1024, 0).decode('utf-8'))
                    if message == "Cannot withdraw more money than what is available":
                        print("Cannot withdraw more money than what is available")

                if int(amount) < 0:
                    print("Cannot Withdraw Negative amount")

            except ValueError:
                print("Invalid input, inputs cannot be float or string")

        elif choice == '3':
            amount = ""
            balance = ""
            clientSocket.send(str.encode("\n".join([choice,amount])))
            balance = clientSocket.recv(1024, 0)
            decoded_balance = format(balance.decode('utf-8'))
            print("Your balance is: " + decoded_balance)

    clientSocket.close()
