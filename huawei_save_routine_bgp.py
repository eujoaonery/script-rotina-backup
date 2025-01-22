#!/usr/bin/env python3


# Feito por João Pedro Nery
# Email de contato: joaonnery@outlook.com
# Telefone: (18) 99796-7526
# Assis - SP


import paramiko
import logging
import time
from datetime import datetime

class HuaweiSaveRoutine:
    def __init__(self):
         
        log_filename = f"huawei_save_routine_bgp_{datetime.now().strftime('%Y%m%d')}.log"
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

    def execute_save(self):
        self.log_message("Iniciando rotina de save no Huawei NE8000 BRAS...")

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

             
            commands = ["save\n", "y\n"]
            for cmd in commands:
                self.log_message(f"Enviando comando: {cmd.strip()}")
                channel.send(cmd)
                time.sleep(2)   

                while channel.recv_ready():
                    output = channel.recv(1024).decode()
                    self.log_message(output.strip())

            self.log_message("Processo de save concluído com sucesso!")
            channel.close()
            ssh.close()

        except Exception as e:
            self.log_message(f"Erro ao executar a rotina de save: {e}")

if __name__ == "__main__":
    routine = HuaweiSaveRoutine()
    routine.execute_save()
