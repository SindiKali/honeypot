import socket
import logging
from datetime import datetime

logging.basicConfig(filename='capturas_honeypot.txt', level=logging.INFO, format='%(message)s')

def iniciar_honeypot(porta=2222):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    servidor.bind(('0.0.0.0', porta))
    servidor.listen(5)
    
    print(f"[+] Terminal de Defesa Ativo. Honeypot escutando silenciosamente na porta {porta}...")
    
    while True:
        try:
            conexao, endereco = servidor.accept()
            ip_atacante = endereco[0]
            hora_ataque = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[!] Alerta: Conexão detectada de: {ip_atacante}")

            conexao.send(b"SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8\n")
            
            dados = conexao.recv(1024)
            payload = dados.decode('utf-8', errors='ignore').strip()
            
            registro = f"[{hora_ataque}] Invasor: {ip_atacante} | Payload Tentado: {payload}"
            logging.info(registro)
            print(f"[*] Dados capturados e gravados no log de segurança.")
            
            conexao.close()
            
        except Exception as erro:
            print(f"Erro no módulo de defesa: {erro}")

if __name__ == "__main__":
    iniciar_honeypot()