from modulos.gestor_clientes import GestorClientes
from modulos.archivos import (
    exportar_clientes,
    importar_clientes,
    generar_reporte
)


def main():
    gestor = GestorClientes()

    clientes_importados = importar_clientes()
    for c in clientes_importados:
        gestor.agregar_cliente(c)

    gestor.listar_clientes()

    exportar_clientes(gestor._clientes)
    generar_reporte(gestor._clientes)


if __name__ == "__main__":
    main()
