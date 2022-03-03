import json
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 3000
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))
operations = ['sum', 'subtraction', 'multiplication', 'division', 'power', 'logarithm']
print('\nAVAILABLE OPERATIONS:')
print('\n'.join(operations))

print('\nEnter de operation: ')
operation = input()
if operation not in operations:
    client.close()
    raise Exception('Invalid operation')

print('Enter the operator a: ')
a = input()
print('Enter the operator b: ')
b = input()

mensaje = {
  "Operation": operation, "Termino a" : a, "Termino b": b
}

client.send(json.dumps(mensaje).encode('UTF-8'))
resultado = client.recv(BUFFER_SIZE).decode('UTF-8')
result = json.loads(resultado)
print("El resultado es: ", result["resultado"])
client.close()

