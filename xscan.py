import os

def ejecutar_comando(comando):
    return os.system(comando)

def mostrar_arte_ascii():
    arte = """
 __  _____  ___   _   _  _ 
 \ \/ / __|/ __| /_\ | \| |
  >  <\__ \ (__ / _ \| .` |
 /_/\_\___/\___/_/ \_\_|\_|
                           
    """
    print("\033[1;32;40m" + arte + "\033[0m")

def main():
    mostrar_arte_ascii()

    # Crear archivo de registro
    archivo_log = open("xscan.log", "w")

    # Verificar e instalar rkhunter
    archivo_log.write("Verificando rkhunter...\n")
    ejecutar_comando("sudo apt-get update")
    ejecutar_comando("sudo apt-get install rkhunter -y")

    # Actualizar bases de datos de rkhunter
    archivo_log.write("Actualizando bases de datos de rkhunter...\n")
    ejecutar_comando("sudo rkhunter --update")

    # Escanear con rkhunter
    archivo_log.write("Escanendo con rkhunter...\n")
    ejecutar_comando("sudo rkhunter -c --sk")

    # Verificar e instalar chkrootkit
    archivo_log.write("Verificando chkrootkit...\n")
    ejecutar_comando("sudo apt-get install chkrootkit -y")

    # Escanear con chkrootkit
    archivo_log.write("Escanendo con chkrootkit...\n")
    ejecutar_comando("sudo chkrootkit")

    archivo_log.write("Escaneo completo. Revisa los resultados en los archivos de log.\n")
    archivo_log.close()

if __name__ == "__main__":
    main()

