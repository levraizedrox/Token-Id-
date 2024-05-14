# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.RED + """
 ██╗██████╗        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║██╔══██╗        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║██║  ██║           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║██║  ██║           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║██████╔╝           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝╚═════╝            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                                                
     Create by Zedrox  Create by Zedrox Create by Zedrox                                                 
    ===============================================================
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input("┌──<Id Token>─[~]\n└──╼ $ ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] 1er PARTIE : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
