import paramiko
import webbrowser

# Credenciales de acceso
hostname = '172.26.1.194'
port = 22
username = 'usuario'
password = 'usuario'

# Conexión al servidor SFTP
transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)

# Creación del cliente SFTP
sftp = paramiko.SFTPClient.from_transport(transport)

# Descarga del archivo
remote_path = '/var/log/nginx/access.log'
local_path = './access.log'
sftp.get(remote_path, local_path)

# Cierre de la conexión SFTP
sftp.close()
transport.close()
archivo = ""
a = open('access.log', 'r')
for line in a:
    archivo += line

f = open('serverLog.html','w')
f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>"""+archivo+"""</div>
</body>
</html>
""")
webbrowser.open_new_tab('serverLog.html')
a.close()
f.close()