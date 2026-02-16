from pathlib import Path
import cmd
import typer
import pyfiglet
from rich import print
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
import sys
import time
import os
import files
import shutil
from rich.progress import track
app = typer.Typer()
# app.add_typer(files.app, name="files")
console = Console()

CYAN = "\033[96m"
BOLD_CYAN = "\033[1;96m"
RESET = "\033[0m"

def startup_animation():
    terminal_width = shutil.get_terminal_size().columns
    sys.stdout.write(CYAN)
    for _ in range(terminal_width):
        sys.stdout.write("━")
        sys.stdout.flush()        
        time.sleep(0.001)        
    sys.stdout.write(RESET + "\n")
    result = pyfiglet.figlet_format("Polar CLI")
    print(f"[cyan] {result} [/cyan]")   
    sys.stdout.write(CYAN)
    for _ in range(terminal_width):
        sys.stdout.write("━")
        sys.stdout.flush()
        time.sleep(0.001)
    sys.stdout.write(RESET + "\n\n")

POLAR_COMMANDS = [
    ("help",            "Display this help table"),
    ("fb <int> <type>",       "Find files above a size threshold (-b fb 10 mb)"),
    ("del <file>",      "Deletes a file"),
    ("",    "Search for files by name pattern"),
    ("exit",            "Exit Polar CLI"),
]

def shutdown_animation():
    terminal_width = shutil.get_terminal_size().columns
    sys.stdout.write(CYAN)
    for _ in range(terminal_width):
        sys.stdout.write("━")
        sys.stdout.flush()        
        time.sleep(0.001)        
    sys.stdout.write(RESET + "\n")
    result = pyfiglet.figlet_format("Exiting Polar CLI")
    print(f"[cyan] {result} [/cyan]")   
    sys.stdout.write(CYAN)
    for _ in range(terminal_width):
        sys.stdout.write("━")
        sys.stdout.flush()
        time.sleep(0.001)
    sys.stdout.write(RESET + "\n\n")
class Polar(cmd.Cmd):
    
    @property
    def prompt(self):
        current_working_directory = os.getcwd()
        return f"{current_working_directory} > "

    def do_help(self, arg):
        table = Table(
            title="Polar CLI Commands",
            title_style="bold cyan",
            border_style="cyan",
            header_style="bold cyan",
            show_lines=True,
            padding=(0, 2),
        )
        table.add_column("Command", style="bold white", min_width=20)
        table.add_column("Description", style="white")
        for command, description in POLAR_COMMANDS:
            table.add_row(f"[cyan]{command}[/cyan]", description)
        console.print()
        console.print(table)

    def do_cd(self, arg):
        try:
            if not arg:
                target_dir = os.path.expanduser("~")
            else:
                target_dir = os.path.expanduser(arg)
            os.chdir(target_dir)
            print(f"[cyan]Changed directory to:[/cyan] {os.getcwd()}")
        except FileNotFoundError:
            print(f"[red]Error: Directory '{arg}' not found.[/red]")
        except PermissionError:
            print(f"[red]Error: Permission denied accessing '{arg}'.[/red]")
        except Exception as e:
            print(f"[red]Error: {e}[/red]")
            
    def do_fb(self, arg):
        arguments = arg.lower().split(" ")
        if not arg or len(arguments) != 2:
            print("Please input a number (-b fb <int> <type>)")
            return
        #expected input -p fb 10 mb
        multiplier = 1
        try:
            val_str = float(arguments[0])
            unit = arguments[1]
            if unit in  ["gb", "g"]:
                multiplier = 1024 * 1024 * 1024
            elif unit in ["mb", "m"]:
                multiplier = 1024 * 1024
            elif unit in ["kb", "k"]:
                multiplier = 1024
            size = val_str * multiplier
            found_any = False 
            
            print(f"[cyan]Searching for files larger than {val_str} {unit.upper()}...[/cyan]")
            for root, dirs, files in os.walk("."):
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        file_size = os.path.getsize(filepath)
                        # 5. The Actual Comparison
                        if file_size > size:
                            # Convert to readable string
                            readable_size = f"{file_size / (1024*1024):.2f} MB"
                            print(f"  - {filepath} [bold cyan]({readable_size})[/bold cyan]")
                            found_any = True
                    except Exception as e:
                        print(e)
            if not found_any:
                print("[yellow]No files found.[/yellow]")
        except Exception as e:
            print(e)    
        return  

    def do_del(self, arg):
        file = arg.strip()
        if not arg:
            print(f"[red]Error: Please provide 1 argument '{arg}'.[/red]")
            return
        try:
            full_path = os.path.expanduser(file)
            if not os.path.exists(full_path):
                print(f"[red]Error: File does not exist '{arg}'.[/red]")
                return 
            elif os.path.isdir(full_path):
                print(f"[red]Error: Cannot delete a directory'{arg}'.[/red]")
                return 
            delete_confirmation = input(f"[cyan] Are you sure you want to delete (y/n) [/cyan] '{arg}' > ").lower()
            if delete_confirmation == "y":
                try:
                    os.remove(full_path)
                    print(f"{arg} [cyan] has been deleted! [/cyan]")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        
    
    def do_exit(self, arg):
        """Exit the Polar Bot."""
        shutdown_animation()
        return True

    
    def default(self, line):
        try:
            os.system(line)
        except Exception as e:
            print(f"[red]Error executing system command: {e}[/red]")



if __name__ == "__main__":
    try:
        startup_animation()
        Polar().cmdloop()
    except KeyboardInterrupt:
        print("\n[yellow]Force exiting...[/yellow]")
