import time
from rich.console import Console

console = Console()

class App:

    # Constructor
    def __init__(self):
        self.console = console
        self.ports = None
    
    # Methods
    def get_ports(self):
        self.ports = self.console.input('[bold yellow]Por favor, ingrese los puertos a escanear separados por un espacio: \n >')

    # Main function
    def run(self):
        self.get_ports()
        self.console.print(f'Puertos a escanear: {self.ports}')
        time.sleep(2)
        exit()

# Init app
app = App()
app.run()
