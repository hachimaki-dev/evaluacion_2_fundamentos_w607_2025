from rich.console import Console 
from rich.panel import Panel
from rich.prompt import Prompt

console = Console ()

contador_dosisCompleta = 0
contador_dosisIncompleta = 0

console.print(Panel.fit("[bold cyan]Registro de esquema de vacuancion[/bold cyan]", title="💉"))

while True:
    console.print("\n[bold]¿Cuantas personas se van a vacunar?[/bold]")
    cantidad_str = Prompt.ask("N° de personas : ")
    try:
        cantidad_personas = int(cantidad_str)
        if cantidad_personas <=0:
            console.print("[red]Favor ingrese un numero mayor a 0[/red]")
            continue
        break
    except ValueError:
        console.print("[red]Favor ingrese un numero entero positivo[/red]")

for i in range(1, cantidad_personas + 1):
    console.clear()
    console.print(Panel.fit(f"[bold green]Registro de la persona N°: {i}[/bold green]"))
    while True:
        dosis_str = Prompt.ask ("Cuantas dosis ha recibido: ")
        try:
            dosis = int(dosis_str)
            if dosis < 0:
                console.print("[red]Favor ingrese un numero mayor o igual a 0")
                continue
            elif dosis >= 3:
                console.print("[green]Esquema completo[/green]")
                contador_dosisCompleta += 1
            else:
                console.print("[yellow]Esquema incompleto[/yellow]")
                contador_dosisIncompleta += 1
            break    
        except ValueError:
            console.print("[red]Favor ingrese un numero entero positivo[/red]")

console.print("\n[bold underline cyan]Resumen del registro:[/bold underline cyan]")
console.print(f"[green]Esquemas completos:[/green] {contador_dosisCompleta}")
console.print(f"[yellow]Esquemas incompletos:[/yellow] {contador_dosisIncompleta}")           

