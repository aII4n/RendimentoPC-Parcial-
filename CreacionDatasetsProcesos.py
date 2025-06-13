import psutil
import pandas as pd
from datetime import datetime
import time

csv_path = "rendimiento_pc.csv"


try:
    open(csv_path, 'x').write("Fecha,CPU (%),RAM (%),Disco (%),Subida KB/s,Bajada KB/s\n")
except FileExistsError:
    pass

# Medir datos periódicamente (una muestra cada 5 segundos)
while True:
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent

    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    subida_kbps = (net2.bytes_sent - net1.bytes_sent) / 1024
    bajada_kbps = (net2.bytes_recv - net1.bytes_recv) / 1024

    fila = f"{fecha},{cpu},{ram},{disco},{subida_kbps:.2f},{bajada_kbps:.2f}\n"

    with open(csv_path, 'a') as f:
        f.write(fila)

    print(fila.strip())
    time.sleep(4)  
