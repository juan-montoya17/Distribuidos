import json
import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 3000  # (1024, 65535]
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.listen(5)
print(f'Main server listening on {TCP_IP}:{TCP_PORT}')

while 1:
  conn, addr = server.accept()  
  datos = conn.recv(BUFFER_SIZE).decode("UTF-8")
  if not datos: break
  print("Datos recibidos: ")
  mensaje = json.loads(datos)
  operation = mensaje["Operation"]
  a = int(mensaje["Termino a"])
  b = int(mensaje["Termino b"])
  def operacion (operation, a, b):
      if operation == 'sum': return a + b 
      elif operation == 'subtraction': return a - b
      elif operation == "multiplication": return a * b
      elif operation == "division": return a / b
      elif operation == "power": return a ** b
      elif operation == "logarithm": return math.log(a, b)
  resultado = operacion(operation, a, b)
  mensaje = {"resultado": resultado}
  conn.send(json.dumps(mensaje).encode("UTF-8"))  
  conn.close()



          
        




