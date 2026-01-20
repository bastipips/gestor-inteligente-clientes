#  Gestor Inteligente de Clientes (GIC)

Proyecto desarrollado en **Python 3** que implementa un sistema de gestión de clientes por consola, aplicando **Programación Orientada a Objetos (POO)**, validaciones, manejo de errores, manejo de archivos y registro de actividad.
Este proyecto fue realizado como evaluación académica del módulo **Full Stack Python**, cumpliendo estrictamente todos los requerimientos solicitados.

---

##  Objetivo del proyecto

Desarrollar un sistema que permita:

- Gestionar clientes (crear, listar y eliminar)
- Diferenciar tipos de clientes usando herencia y polimorfismo
- Validar datos de entrada y manejar errores con excepciones personalizadas
- Exportar e importar información mediante archivos CSV
- Generar reportes en archivos TXT
- Registrar acciones del sistema en archivos LOG
- Interactuar mediante un menú por consola

---

## Conceptos aplicados

- Programación Orientada a Objetos (POO)
  - Encapsulación
  - Herencia
  - Polimorfismo
- Excepciones personalizadas
- Validaciones de datos (email, teléfono, duplicados)
- Manejo de archivos (CSV, TXT, LOG)
- Modularización del código
- Interfaz por consola

---

## Estructura del proyecto

GIC/
├── main.py
├── modulos/
│ ├── cliente.py
│ ├── cliente_regular.py
│ ├── cliente_premium.py
│ ├── cliente_corporativo.py
│ ├── gestor_clientes.py
│ ├── validaciones.py
│ ├── excepciones.py
│ └── archivos.py
├── datos/
│ ├── clientes.csv
│ └── clientes_entrada.csv
├── reportes/
│ └── resumen.txt
├── logs/
│ └── app.log
├── cmd/
│ └── diagrama_clases_gic.jpg
└── README.md


## Tipos de clientes

- **ClienteRegular**
- **ClientePremium**
- **ClienteCorporativo**

Todos heredan de la clase base `Cliente` y redefinen métodos utilizando **polimorfismo**.

## Validaciones implementadas

- Email válido con dominio `@gmail.com`
- Teléfono de 9 dígitos comenzando en `9`
- Prevención de clientes duplicados
- Manejo de errores mediante excepciones personalizadas

## Manejo de archivos

- Exportación de clientes a `datos/clientes.csv`
- Importación desde `datos/clientes_entrada.csv`
- Generación de reporte `reportes/resumen.txt`
- Registro de actividad en `logs/app.log`

##  Ejecución del sistema

Desde la carpeta `GIC`, ejecutar:

bash
python main.py

El sistema mostrará un menú por consola para interactuar con la aplicación.

Diagrama UML
El proyecto incluye un diagrama de clases UML, ubicado en:
cmd/diagrama_clases_gic.jpg

Este diagrama representa:
Clases del sistema
Atributos y métodos
Relaciones de herencia
Relación de composición entre GestorClientes y Cliente

Evidencia de funcionamiento

La funcionalidad del sistema se valida mediante:

Ejecución por consola

Archivos generados (CSV, TXT, LOG)

Casos de prueba manuales

Salidas visibles del sistema

🚀 Tecnologías utilizadas
Python 3
Visual Studio Code
Git & GitHub
diagrams.net (UML)

👤 Autor
Bastián Bachmann
Proyecto académico – Portafolio profesional

