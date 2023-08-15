## XSCAN: Script de Escaneo en Busca de Rootkits para Linux

El script XSCAN es una simple herramienta diseñada para llevar a cabo un escaneo exhaustivo en busca de rootkits en sistemas Linux. Esta herramienta utiliza las populares herramientas rkhunter y chkrootkit para detectar posibles amenazas de seguridad que podrían comprometer la integridad del sistema.

### Características:

- Realiza la instalación y actualización de las bases de datos de rkhunter y chkrootkit.
- Escanea el sistema en busca de rootkits utilizando rkhunter y chkrootkit.
- Genera un archivo de registro (xscan.log) donde se registran los resultados de los escaneos.

### Requisitos:

- Sistema operativo Linux.
- Acceso de administrador (sudo).

### Instrucciones de Uso:

1. Clona este repositorio en tu sistema:

```bash
git clone https://github.com/ch4hub/xscan.git
cd xscan
```

2. Asegúrate de que tienes instalado Python en tu sistema.

3. Ejecuta el script usando Python con privilegios de administrador:

```bash
sudo python xscan.py
```

4. Sigue las instrucciones en pantalla para verificar la instalación de rkhunter y chkrootkit, actualizar las bases de datos y realizar el escaneo.

5. Los resultados del escaneo se registrarán en el archivo xscan.log en el mismo directorio.

### Notas Importantes:

- Este script debe ser ejecutado con cuidado, ya que realiza cambios en el sistema y puede generar falsos positivos. Siempre es recomendable revisar los resultados y comprender las implicaciones antes de tomar medidas.

- Asegúrate de que el script tenga los permisos necesarios para ser ejecutado.

by @ceachecuatro 2023
