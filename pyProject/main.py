import pyfiglet
from rich.console import Console
from os import walk 

print("")


con = Console()

banner = pyfiglet.figlet_format("BabuRao",font="banner3-D")
con.print(banner,"v9.0",style="bold green")

print("")
print("")
input("Enter victim's IP address - ")