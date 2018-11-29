import socket, os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 12346))
sock.listen(5)

print('Esperando um novo cliente')
conn, address = sock.accept()
print('Cliente aceito.')

while True:
    buffer = conn.recv(1024)
    print('Recebido', buffer.decode('utf-8'))
    # Interpretação da mensagem que chegou  
    # [HADAMARD;1]
    # Realizar os comandos conforme pedido
    # Devolver a resposta

    mensagem = 'Olá, tudo bem?'
    print('Enviado', mensagem)
    conn.send(mensagem.encode('utf-8'))
    conn.close()
    print('Conexão com encerrada.')


