# HHIC
Host Header Injection Check

Instalación y Uso:

Guarda el script modificado en un archivo, por ejemplo, hhic.py, y asegúrate de tener tu archivo dominios.txt en el mismo directorio. Luego, ejecuta el script
python3 hhic.py !!


Uso de colorama:
La biblioteca colorama permite utilizar colores en la consola de manera portátil.
init(autoreset=True) inicializa colorama y asegura que los colores se reinicien después de cada impresión.
Colores en la Salida:

Fore.RED se usa para la salida en rojo cuando el estado es 502 (Bad Gateway).
Fore.BLUE se usa para la salida en azul cuando se detecta una posible vulnerabilidad de Host Header Injection.
El resto de los mensajes se imprimen en el color por defecto.
