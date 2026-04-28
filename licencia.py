#!/usr/bin/env python3
"""
mensaje.py
Muestra un único mensaje motivador para emprendedores
con título, contenido separado y formato a color en la terminal.
El marco se ajusta automáticamente al contenido.
"""

import textwrap

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


TITULO = "Persistencia"
CONTENIDO = "El éxito es la suma de pequeños esfuerzos repetidos día tras día."

# Ancho máximo en caracteres del texto interior. El marco se ajusta a este
# ancho (más el padding y los bordes). Mensajes cortos producen marcos más
# pequeños; mensajes largos forman varias líneas pero nunca pasan de aquí.
ANCHO_TEXTO = 44


def main() -> None:
    console = Console()
    check = "\u2713"  # ✓

    contenido_envuelto = textwrap.fill(CONTENIDO, width=ANCHO_TEXTO)

    cuerpo = Text(justify="center")
    cuerpo.append(f"{check}  ", style="bold bright_green")
    cuerpo.append(TITULO.upper(), style="bold bright_yellow")
    cuerpo.append("\n\n")
    cuerpo.append(contenido_envuelto, style="italic bright_white")

    panel = Panel(
        cuerpo,
        border_style="bright_magenta",
        padding=(1, 2),
        expand=False,
        title="[bold bright_cyan]\u2728 Emprendedores \u2728[/]",
        subtitle="[dim italic]Hazlo posible hoy[/]",
    )

    console.print()
    console.print(panel, justify="center")
    console.print()


if __name__ == "__main__":
    main()