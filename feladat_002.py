from netmiko import ConnectHandler

login = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}



def vlan(ssh):
    parancsok=["vlan 10",
                "name Tanulo",
                "vlan 20",
                "name Oktato",
                "vlan 30",
                "name Pedagogus",
                "vlan 100",
                "name Ugyvitel"
              ]
    ssh.send_config_set(parancsok)


def console_pass(ssh):
    ssh.save_config()
    
    parancsok=["password", "login"]
    con_pass = connect.send_command("sh run | section line con")
    if ("password" and "login" in con_pass):
        print("Konzol jelszó és hitelesítés beállítása OK!")
        con_pass = con_pass.split("\n")
        print(con_pass)
    else:
        for i in range (len(parancsok)):
            if ("login local" in con_pass):
                print("Login local van megadva sima login helyett!")
            elif (parancsok[i] not in con_pass):
                print(f"Szar, mert: {parancsok[i]} nincs megadva")
            



#########################
#        PROGRAM        #
#########################



try:
    with ConnectHandler(**login) as connect:
        #1. feladat
        vlan(connect)
        
        print(connect.send_command("sh vl br"))
        
        
        #2. feladat
        console_pass(connect)
    
except Exception as ex:
    print(f"Error: {ex}")