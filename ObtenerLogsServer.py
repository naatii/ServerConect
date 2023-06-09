import paramiko
import webbrowser
# '172.26.1.194'
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
webbrowser.open_new_tab('serverLog.html')

while True:
    sftp.get(remote_path, local_path)

    # Cierre de la conexión SFTP

    a = open('access.log', 'r')
    f = open('serverLog.html','w')
    for line in a.readlines()[-10:]:
        f.write("""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="refresh" content="2">
                <title>Document</title>
            </head>
            <body>
                <div>"""+line+"""</div>
            </body>
            </html>
            """)
