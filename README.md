#Script em Python para fixar configurações e realizar backup automatico de equipamentos de rede

Este repositório contém um script Python desenvolvido para automatizar o processo de salvamento e backup de configurações em equipamentos de rede. O objetivo é trazer maior segurança, evitar falhas humanas e garantir que as configurações críticas estejam sempre atualizadas e armazenadas de forma segura.

Funcionalidades

Automatização e Backup Diário

Salvamento Automático: Executa o comando save no equipamento diariamente às 00:00, garantindo que todas as alterações realizadas sejam armazenadas permanentemente no equipamento.

Backup Organizado: Realiza o comando display current-configuration para capturar as configurações completas, armazenando-as em arquivos organizados por data em diretórios no servidor. Isso facilita a recuperação em caso de necessidade.

Execução e Agendamento

Agendamento Automático: O script é executado diariamente por meio do cron no Ubuntu Server.

Geração de Logs: Logs detalhados são criados durante cada execução, permitindo a análise de eventuais problemas.

Tecnologias e Ferramentas Utilizadas

Python: Linguagem principal utilizada, conhecida por sua simplicidade e versatilidade em automação.

Paramiko: Biblioteca Python utilizada para conexão SSH e execução de comandos remotamente.

Datetime e OS: Funções para manipulação de arquivos e organização por data.

Ubuntu Server: Ambiente Linux para armazenamento dos arquivos e execução do script.

VMware ESXi: Plataforma utilizada para criar e gerenciar a máquina virtual.

Benefícios

Redução de Erros Humanos: Automatiza tarefas repetitivas e minimiza erros operacionais.

Segurança: Garante que as configurações da rede estejam sempre salvas e atualizadas.

Eficiência: Facilita a recuperação de configurações em casos de emergência.

Como Funciona

O script é agendado no cron para ser executado diariamente às 00:00.

Durante a execução, ele:

Conecta-se ao equipamento de rede via SSH usando a biblioteca Paramiko.

Executa o comando save para salvar alterações no equipamento.

Executa o comando display current-configuration para capturar as configurações completas.

Armazena as configurações em arquivos organizados por data no servidor.

Gera logs detalhados do processo.

Expansão

A ideia é expandir a automação para outros equipamentos e processos dentro da empresa, reduzindo ainda mais o trabalho manual e aumentando a segurança operacional.

Configuração do Cron

Exemplo de configuração do cron para executar o script:

0 0 * * * /usr/bin/python3 /caminho/para/seu/script.py >> /caminho/para/log.txt 2>&1

Contribuições

Contribuições para melhorias são bem-vindas! Por favor, envie um pull request ou abra uma issue.
