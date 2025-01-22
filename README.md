
<body>
    <h1>Script em Python para Automação e Backup de Configurações de Rede</h1>
    <h3>
        Este projeto apresenta um script em Python desenvolvido para automatizar o processo de salvamento e backup de configurações 
        em equipamentos de rede. A iniciativa busca aumentar a segurança, reduzir erros humanos e garantir que as configurações críticas 
        estejam sempre atualizadas e armazenadas de forma segura.
        Funcionalidades Principais
    <h3>Automatização e Backup Diário</h3>
    <ul>
        <li><strong>Salvamento Automático:</strong> Executa o comando <code>save</code> no equipamento diariamente, garantindo que todas as alterações realizadas sejam armazenadas permanentemente.</li>
        <li><strong>Backup Organizado:</strong> Captura as configurações completas via <code>display current-configuration</code> e as armazena em arquivos organizados por data no servidor.</li>
    </ul>
    <h3>Execução e Agendamento com Systemd</h3>
    <ul>
        <li><strong>Agendamento Automático:</strong> Substituímos o uso do cron pelo <strong>Systemd Timer</strong>, uma ferramenta moderna e robusta para agendamento no Ubuntu Server.</li>
        <li><strong>Geração de Logs:</strong> Logs detalhados são criados durante a execução para monitoramento e solução de falhas.</li>
    </ul>
    <h2>Tecnologias e Ferramentas Utilizadas</h2>
    <ul>
        <li><strong>Python:</strong> Linguagem principal pela sua versatilidade e eficiência para automação.</li>
        <li><strong>Paramiko:</strong> Biblioteca para conexões SSH e execução de comandos remotos.</li>
        <li><strong>Datetime/OS:</strong> Para manipulação de arquivos e organização por data.</li>
        <li><strong>Ubuntu Server:</strong> Ambiente utilizado para executar o script e armazenar backups.</li>
        <li><strong>VMware ESXi:</strong> Plataforma de virtualização usada para criar e gerenciar a máquina virtual.</li>
    </ul>
    <h2>Benefícios do Script</h2>
    <ul>
        <li>Reduz erros humanos automatizando tarefas repetitivas.</li>
        <li>Garante a segurança e o armazenamento atualizado das configurações da rede.</li>
        <li>Facilita a recuperação de configurações em emergências.</li>
    </ul>
    <h2>Como Funciona o Script?</h2>
    <ol>
        <li>Conecta-se ao equipamento via SSH usando o Paramiko.</li>
        <li>Executa o comando <code>save</code> para salvar alterações.</li>
        <li>Captura as configurações com o comando <code>display current-configuration</code>.</li>
        <li>Armazena os backups em diretórios separados por data.</li>
        <li>Registra logs detalhados de cada execução.</li>
    </ol>
    <h2>Como Implementar no Linux com Systemd Timers</h2>
    <h3>1. Estrutura de Diretórios</h3>
    <pre>
mkdir -p /home/rotina/{scripts,logs,backups}
    </pre>
    <h3>2. Instale Dependências</h3>
    <pre>
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install paramiko
    </pre>
    <h3>3. Coloque o Script no Diretório</h3>
    <p>Salve o script Python em <code>/home/rotina/scripts/huawei_backup.py</code>.</p>
    <h3>4. Crie o Arquivo Systemd Service</h3>
    <pre>
sudo nano /etc/systemd/system/huawei_backup.service
    </pre>
    <div class="highlight">
        <pre>
[Unit]
Description=Execução do Script de Backup Huawei
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/rotina/scripts/huawei_backup.py
WorkingDirectory=/home/rotina/scripts
StandardOutput=append:/home/rotina/logs/huawei_backup.log
StandardError=append:/home/rotina/logs/huawei_backup_error.log

[Install]
WantedBy=multi-user.target
        </pre>
    </div>
    <h3>5. Crie o Arquivo Systemd Timer</h3>
    <pre>
sudo nano /etc/systemd/system/huawei_backup.timer
    </pre>
    <div class="highlight">
        <pre>
[Unit]
Description=Agendamento Diário para Backup Huawei

[Timer]
OnCalendar=*-*-* 00:00:00
Persistent=true
Unit=huawei_backup.service

[Install]
WantedBy=timers.target
        </pre>
    </div>
    <h3>6. Habilite e Inicie o Timer</h3>
    <pre>
sudo systemctl daemon-reload
sudo systemctl enable huawei_backup.timer
sudo systemctl start huawei_backup.timer
    </pre>
    <h3>7. Faça o mesmo para os outros </h3>
    <br>
    <h3>8. Verifique o Status do Timer</h3>
    <pre>
systemctl list-timers
    </pre>
    <h2>Contribuições</h2>
    <p>
        Contribuições e sugestões são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
    </p>
</body>
</html>
