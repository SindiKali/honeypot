import socket
import logging
from datetime import datetime

logging.basicConfig(filename='capturas_honeypot.txt', level=logging.INFO, format='%(message)s')

def iniciar_honeypot(porta=2222):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind(('0.0.0.0', porta))
    servidor.listen(5)

    print(f"Terminal de defesa ativo. Honeypot escutando silencionamente na porta {porta} ...")

    while True:
        try:
            conexao, endereco = servidor.accept()
            ip_atacante = endereco[0]
            hora_ataque = datetime.now().strtime("%Y-%m-%d %H:%M:%S")