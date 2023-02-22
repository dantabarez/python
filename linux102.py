import psutil

# Itera sobre todos los procesos en ejecución
for proceso in psutil.process_iter():

    try:
        # Obtiene la información del proceso
        info = proceso.as_dict(attrs=['pid', 'name', 'cmdline'])

        # Verifica si el proceso es de Java
        if 'java' in info['name'] or ('java' in info['cmdline'] and 'jar' in info['cmdline']):
            print('Proceso de Java en ejecución: PID={}, Nombre={}, Comando={}'.format(info['pid'], info['name'], info['cmdline']))
    
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


