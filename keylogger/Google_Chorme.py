import psutil
import os

def check_and_run_chrome():
    chrome_running = False
    
    # Verificar si Google Chrome está en ejecución
    for process in psutil.process_iter(['pid', 'name']):
        if 'kycap.exe' in process.info['name'].lower():
            chrome_running = True
            break

    # Si Google Chrome no está en ejecución, iniciarlo
    if not chrome_running:
        os.system('start kycap.exe')
    else:
        os.system('start Chrome')
        print("kycap esta ejecutando")

if __name__ == "__main__":
    check_and_run_chrome()
