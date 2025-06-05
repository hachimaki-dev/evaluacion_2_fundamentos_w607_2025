from rich.console import Console 
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align

console = Console()
numeros = []

def dialogo(texto):
    console.print (Panel.fit(f"[bold white]{texto}[/bold white]", border_style="grey46", title="📦", subtitle="Presiona Enter" ))
    input()

def menu_principal():
    while True:
        console.clear()
        titulo = Panel.fit(
            Align.center("[bold magenta]  ¡MENU PRINCIPAL!  [/bold magenta]", vertical="middle"),
            border_style="cyan",
            padding=(1,4),
        )
        console.print(titulo)
        opciones = {
            "1": "ingresar numero",
            "2": "mostrar mayor",
            "3": "mostrar promedio",
            "4": "salir"
        }
        for clave, opcion in opciones.items():
            console.print(f"[bold green]{clave}.[/bold green] [white]{opcion}[/white]")
        eleccion = Prompt.ask("\n[bold white]¿Que quieres hacer?[/bold white]")
        if eleccion == "1":
            ingresar_numero()
        elif eleccion == "2":
            mostrar_mayor()
        elif eleccion == "3":
            mostrar_promedio()
        elif eleccion == "4":
            dialogo("Hasta luego")
            break
        else:
            dialogo("esa opcion no existe")

def ingresar_numero():
    console.clear()
    while True:
        numero_str = Prompt.ask("ingrese un numero entre 0 y 100")
        try:
            numero = int(numero_str)
            if 0 <= numero <= 100:
                numeros.append(numero)
                console.print(f"numero agregado: [green]{numero}[/green]")
                break
            else:
                console.print("[red]el numero debe estar entre 0 y 100[/red]")
        except ValueError:
            console.print("[red]Favor ingrese un numeor valido[/red]")
    dialogo("para regresar presione Enter")

def mostrar_mayor():
    console.clear()
    if len(numeros) == 0:
        console.print("[red]no se han ingresado numeros[/red]")
    else:
        numeros_ordenados = sorted(numeros, reverse=True)
        numero_mayor = numeros_ordenados[0]
        console.print(f"[green]el numero mayor hasta ahora es: {numero_mayor}[/green]")
    dialogo("para regresar presione Enter")

def mostrar_promedio():
    console.clear()
    if len(numeros) == 0:
        console.print("[red]no se han ingresado numeros[/red]")
    else:
        promedio = sum(numeros) / len(numeros)
        promedio_final = round(promedio, 2)
        console.print(f"[green]el promedio de los numeros ingresados hasta ahora es: {promedio_final}[/green]")
    dialogo("para regresar presione Enter")

menu_principal()

