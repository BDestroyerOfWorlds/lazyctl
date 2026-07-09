lazyradio 1.0.0-beta                                              
-


lazyradio (former lazyctl) is a tool designed to run your nmcli, systemctl and rfkill commands through the simple GUI or the
terminal via legacy mode.

standalone executable located in

`dist/lazyradio`

you have to have the "-internal" folder in the same directory as the executable.
does not need anything else to work.


---

  lazyradio - quick and easy Wi-Fi/bluetooth control 

to access the legacy mode,
```bash
cd ~/Your/Directory
./lazyradio --legacy
```
then you will receive the list of commands in your terminal

note: without the --legacy argument it will start in the GUI mode, invalid arguments will result in an "Invalid Argument"
message and you will have to launch it again.

    Commands:
        bluetooth -r    Restart bluetooth
        bluetooth -on   Turn bluetooth on
        bluetooth -off  Turn bluetooth off
        wifi -r         Restart wifi
        wifi -on        Turn wifi on
        wifi -off       Turn wifi off
        exit            exit application

not a radio, deals with radio signal services hence called lazyradio. will not play music. will not recieve FM signals.
sorry.

---

currently a public beta

built with Python 3.14.6

linux only, as you can tell by the commands it runs
