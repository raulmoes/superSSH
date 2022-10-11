import os
import paramiko
sel = input ("Seleccione 1 para ejecutar un comando o 2 para copiar fichero del remotehost: ")

if (sel == "1"):
  pkey = paramiko.RSAKey.from_private_key_file('/home/frodo/.ssh/frodo', password='bolson')
  trans = paramiko.Transport(('192.168.58.191', 22))
  trans.connect(username='frodo', pkey=pkey)
  ssh = paramiko.SSHClient()
  ssh._transport = trans
  comando = input ("Indica el comando a ejecutar: ")
  stdin, stdout, stderr = ssh.exec_command(comando)
  print(stdout.read().decode())
  del stdin, stdout, stderr
  trans.close()

elif (sel == "2"):
    pkey = paramiko.RSAKey.from_private_key_file('/home/frodo/.ssh/frodo', password='bolson')
    trans = paramiko.Transport(('192.168.58.191', 22))
    trans.connect(username='frodo', password='bolson')
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    sftp = paramiko.SFTPClient.from_transport(trans)
    local = input("Indique el fichero / carpeta local a copiar: ")
    remoto = input("Indique la carpeta remota: ")
    sftp.put(localpath=local, remotepath=remoto)
    trans.close()