#!/usr/bin/env python3
"""Sirve las guías HTML del proyecto (raíz de abm-alumnos) en la red local.

Uso:
    python servir-guias-red.py [puerto]

Por defecto usa el puerto 8901. Cualquier dispositivo conectado a la misma
red (Wi-Fi o cable) que esta PC va a poder abrir las guías desde la IP que
imprime el script al arrancar.
"""

import functools
import http.server
import os
import socket
import sys

PUERTO_POR_DEFECTO = 8901

GUIAS = [
    "guia-conceptos.html",
    "guia-github.html",
    "ejercicio-conflicto.html",
]

RAIZ_PROYECTO = os.path.dirname(os.path.abspath(__file__))


def obtener_ip_local():
    """Devuelve la IP de esta PC dentro de la red local (no la usa para conectar)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def main():
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else PUERTO_POR_DEFECTO
    ip = obtener_ip_local()

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=RAIZ_PROYECTO
    )
    servidor = http.server.ThreadingHTTPServer(("0.0.0.0", puerto), handler)

    print(f"Sirviendo '{RAIZ_PROYECTO}' en el puerto {puerto}\n", flush=True)

    print("Desde esta misma PC:", flush=True)
    for guia in GUIAS:
        print(f"  http://127.0.0.1:{puerto}/{guia}", flush=True)

    print("\nDesde otro dispositivo en la MISMA red (Wi-Fi o cable):", flush=True)
    for guia in GUIAS:
        print(f"  http://{ip}:{puerto}/{guia}", flush=True)

    print("\nCtrl+C para detener.", flush=True)
    print("Si no conecta desde otro dispositivo, revisá que el Firewall de", flush=True)
    print("Windows haya permitido el acceso a Python en la ventana que", flush=True)
    print("pudo haber aparecido, o que ambos estén en la misma red.", flush=True)

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        servidor.shutdown()


if __name__ == "__main__":
    main()
