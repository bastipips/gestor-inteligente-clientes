import csv
import os
from datetime import datetime
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo


RUTA_LOG = "logs/app.log"


def registrar_log(mensaje):
    with open(RUTA_LOG, "a", encoding="utf-8") as log:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{fecha}] {mensaje}\n")


def exportar_clientes(clientes, ruta="datos/clientes.csv"):
    """
    Exporta la lista de clientes a un archivo CSV.
    """
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["tipo", "nombre", "email", "telefono", "direccion", "extra"])

        for c in clientes:
            if isinstance(c, ClientePremium):
                tipo = "Premium"
                extra = c._beneficios
            elif isinstance(c, ClienteCorporativo):
                tipo = "Corporativo"
                extra = c._empresa
            else:
                tipo = "Regular"
                extra = ""

            writer.writerow([
                tipo,
                c._nombre,
                c._email,
                c._telefono,
                c._direccion,
                extra
            ])

    registrar_log("Exportación de clientes a CSV realizada.")


def importar_clientes(ruta="datos/clientes_entrada.csv"):
    clientes = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                tipo = fila["tipo"]
                nombre = fila["nombre"]
                email = fila["email"]
                telefono = fila["telefono"]
                direccion = fila["direccion"]
                extra = fila["extra"]

                if tipo == "Premium":
                    clientes.append(
                        ClientePremium(nombre, email, telefono, direccion, extra)
                    )
                elif tipo == "Corporativo":
                    clientes.append(
                        ClienteCorporativo(nombre, email, telefono, direccion, extra)
                    )
                else:
                    clientes.append(
                        ClienteRegular(nombre, email, telefono, direccion)
                    )

        registrar_log("Importación de clientes desde CSV realizada.")

    except FileNotFoundError:
        registrar_log("ERROR: Archivo CSV de entrada no encontrado.")

    return clientes


def generar_reporte(clientes, ruta="reportes/resumen.txt"):
    total = len(clientes)
    reg = sum(isinstance(c, ClienteRegular) for c in clientes)
    pre = sum(isinstance(c, ClientePremium) for c in clientes)
    corp = sum(isinstance(c, ClienteCorporativo) for c in clientes)

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE GIC\n")
        archivo.write("------------------\n")
        archivo.write(f"Total clientes: {total}\n")
        archivo.write(f"Clientes Regular: {reg}\n")
        archivo.write(f"Clientes Premium: {pre}\n")
        archivo.write(f"Clientes Corporativo: {corp}\n")

    registrar_log("Reporte TXT generado correctamente.")
