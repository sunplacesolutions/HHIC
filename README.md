![hhic Logo](hostheader.webp)
# HHIC
# Host Header Injection Check
es un script en Python diseñado para detectar vulnerabilidades de inyección de cabecera Host en aplicaciones web. Este tipo de ataque puede permitir a un atacante realizar falsificación de solicitudes del lado del servidor (SSRF), envenenamiento de caché, y elusión de controles de acceso. El script utiliza la biblioteca requests para realizar solicitudes HTTP con un encabezado Host malicioso y la biblioteca colorama para mejorar la salida en la terminal.

# Requisitos
Python 3.x

Requests: pip install requests

Colorama: pip install colorama

# Uso
Instalar dependencias:
pip install requests colorama

# Preparar el archivo de dominios:

Crea un archivo llamado Dominios_A_Chequear.txt en el mismo directorio que el script.
Añade las URLs de los dominios que deseas verificar, una por línea.Instalación y Uso:

# Ejecutar el script:
python hhic.py

# Uso de colorama:
La biblioteca colorama permite utilizar colores en la consola de manera portátil.
init(autoreset=True) inicializa colorama y asegura que los colores se reinicien después de cada impresión.
Colores en la Salida:

# Fore.RED
se usa para la salida en rojo cuando el estado es 502 (Bad Gateway).
# Fore.BLUE
se usa para la salida en azul cuando se detecta una posible vulnerabilidad de Host Header Injection.
El resto de los mensajes se imprimen en el color por defecto.
