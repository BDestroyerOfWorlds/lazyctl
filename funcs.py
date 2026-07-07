import subprocess

def bt_restart():
    subprocess.run(["systemctl", "restart", "bluetooth"], check=True)

def bt_on():
    subprocess.run(["systemctl", "enable","--now", "bluetooth"], check=True)

def bt_off():
    subprocess.run(["systemctl", "disable", "--now", "bluetooth"], check=True)




def wifi_restart():
    try:
        subprocess.run(["nmcli", "radio", "wifi", "off"], check=True)
        subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)
        subprocess.run(["systemctl", "restart", "NetworkManager.service"], check=True)
    except:
        print("nmcli and systemctl failed, using rfkill instead.")
        subprocess.run(["rfkill","block","wifi"])
        subprocess.run(["rfkill","unblock","wifi"])
    
#BUG HERE, IF NMCLI WIFI OFF WORKS AND SOMEHOW NMCLI WIFI ON DOESNT USER IS LEFT WITH NO WIFI

def wifi_on():
    subprocess.run(["rfkill", "unblock", "wifi"])
    subprocess.run(["systemctl", "start", "NetworkManager.service"], check=True)
    subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)

#trying starting the service first, doesnt work at the moment, 7/8 1:36

def wifi_off():
    subprocess.run(["rfkill", "block", "wifi"])
    subprocess.run(["nmcli", "radio", "wifi", "off"], check=True)
    subprocess.run(["systemctl", "stop", "NetworkManager.service"], check=True)

