from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def menu_bonito():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Opção", style="bright_yellow", justify="center", width=8)
    table.add_column("Descrição", style="white")

    # Adicionando as opções
    opcoes = [
        ("1", "Cadastrar novo usuário"),
        ("2", "Listar usuários"),
        ("3", "Editar usuário"),
        ("4", "Excluir usuário"),
        ("0", "Sair"),
    ]

    for numero, descricao in opcoes:
        table.add_row(numero, descricao)

    # Exibindo o menu
    console.print(table)

    # Solicitando a escolha
    escolha = Prompt.ask(
        "\nDigite sua escolha",
        choices=["0", "1", "2", "3", "4"],
        default="0",
        show_choices=False,
    )

    return escolha


# Usando o menu
if __name__ == "__main__":
    while True:
        console.clear()  # Limpa a tela
        escolha = menu_bonito()

        if escolha == "0":
            console.print("\n[bold green]Até logo! 👋[/bold green]")
            break
        else:
            console.print(f"\n[bold blue]Você escolheu a opção {escolha}[/bold blue]")
            input("\nPressione ENTER para continuar...")
