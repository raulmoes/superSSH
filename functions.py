import paramiko
from paramiko import SSHClient, AutoAddPolicy, RSAKey


def connectpassword(ssh, remotehost, user, defaultpassword):
    try:
        ssh.connect(remotehost, username=user, password=defaultpassword)
        return 1
    except Exception as e:
        print("Cannot connect to the remote host error :")
        print(e)
        return 0


def connectkey(ssh, remotehost, user, key):
    ssh.connect(remotehost, username=user, pkey=key)
    return 1


def tryconnect(ssh, remotehost, user, key, password):
    try:
        i = connectkey(ssh, remotehost, user, key)
    except paramiko.AuthenticationException as error:
        print("You cannot connect to this server with key will try default password")
        i = connectpassword(ssh, remotehost, user, password)
    except paramiko.SSHException as error:
        print("You cannot connect to this host")
        print(error)
        i = 0
    return i
