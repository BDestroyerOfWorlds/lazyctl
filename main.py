import funcs
import time
while True:
    print("""
    lazyctl - quick and easy wifi/bluetooth control
    
    Commands:
        bluetooth -r    Restart bluetooth
        bluetooth -on   Turn bluetooth on
        bluetooth -off  Turn bluetooth off
        wifi -r         Restart wifi
        wifi -on        Turn wifi on
        wifi -off       Turn wifi off
        exit            exit application
    """)
    choice = input(">")

    if choice == "bluetooth -r":
        funcs.bt_restart()

    elif choice == "bluetooth -on":
        funcs.bt_on()

    elif choice == "bluetooth -off":
        funcs.bt_off()

    elif choice == "wifi -r":
        funcs.wifi_restart()

    elif choice == "wifi -on":
        funcs.wifi_on()

    elif choice == "wifi -off":
        funcs.wifi_off()

    elif choice == "exit":
        break

    else:
        print("Invalid command")
        time.sleep(1)





"""
CONSIDER ARGPARSE, TYPER, CLICK, DYKES
Typer and dykes require type annotations to work. Argparse and click do not.
Look at the docs. Click is very well known and supported, very mature.
Argparse is part of the standard library.

I don't want to be that guy because Ik you're doing it to learn, but...
```bash

alias btoff="systemctl bluetooth stop"```
add audio stuff to unfuck audio
"""