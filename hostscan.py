from scapy.all import ARP, Ether, srp

# Define la dirección de red a escanear
direccion_red = "172.17.8.0/24"

# Crea una solicitud ARP para buscar los hosts en la red
arp = ARP(pdst=direccion_red)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
paquete = ether/arp

# Envía el paquete y espera la respuesta
resultados, _ = srp(paquete, timeout=2, verbose=0)

# Imprime los resultados
print("Direcciones IP encontradas en la red:")
for resultado in resultados:
    print(resultado[1].psrc)
