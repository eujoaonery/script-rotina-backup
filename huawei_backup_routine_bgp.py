#!/usr/bin/env python3


# Feito por João Pedro Nery
# Email de contato: joaonnery@outlook.com
# Telefone: (18) 99796-7526
# Assis - SP


import paramiko
import logging
import time
from datetime import datetime

class HuaweiBackupRoutine:
    def __init__(self):
         
        log_filename = f"huawei_backup_routine_{datetime.now().strftime('%Y%m%d')}.log"
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        self.router_details = {
            'ip': ' ',  
            'port': 22 ,
            'user': ' ',
            'password': ' '
        }

    def log_message(self, message):
        print(message)
        logging.info(message)

    def execute_backup(self):
        self.log_message("Iniciando rotina de backup no Huawei NE8000 BGP...")

        try:
            self.log_message("Conectando ao equipamento...")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.router_details['ip'], 
                port=self.router_details['port'], 
                username=self.router_details['user'], 
                password=self.router_details['password']
            )
            self.log_message("Login efetuado com sucesso!")

             
            channel = ssh.invoke_shell()
            self.log_message("Canal interativo aberto.")

            
            disable_pagination_command = "screen-length 0 temporary\n"
            self.log_message(f"Enviando comando: {disable_pagination_command.strip()}")
            channel.send(disable_pagination_command)
            time.sleep(1)

             
            command = "display current-configuration\n"
            self.log_message(f"Enviando comando: {command.strip()}")
            channel.send(command)
            time.sleep(5)   

             
            output = ""
            while True:
                if channel.recv_ready():
                    chunk = channel.recv(4096).decode()
                    output += chunk
                    time.sleep(1)   
                else:
                    break

            self.log_message("Comando executado e saída capturada.")

             
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f"bkp_ne_bgp_{timestamp}.txt"  
            with open(backup_filename, 'w') as backup_file:
                backup_file.write(output)

            self.log_message(f"Backup salvo com sucesso no arquivo: {backup_filename}")

            channel.close()
            ssh.close()

        except Exception as e:
            self.log_message(f"Erro ao executar a rotina de backup: {e}")

if __name__ == "__main__":
    routine = HuaweiBackupRoutine()
    routine.execute_backup()
