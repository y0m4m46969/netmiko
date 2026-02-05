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
    con_pass = con_pass.split("\n")
    
    for szo in con_pass:
        elem = szo
        if "password" in elem or "login" in elem:
            elem = elem.strip()
            con_pass.append(elem)
        con_pass.remove(szo)
        # csinalok meg egy listat es abba teszem at az elem-et
        
    print(con_pass)
    
    
    
    if ("password" in con_pass):
        
        if con_pass.count("login") == 1:
                print("Konzol jelszó és hitelesítés beállítása OK!")
            
        else:
            print("Nincs login")
            
    else:
        print(f"Nincs jelszó")
            
    
    """for i in range (len(con_pass)):
        
        if ("password" in con_pass[i]):
            if ("login" == con_pass[i+1]):
                print("Konzol jelszó és hitelesítés beállítása OK!")
                break
            else:
                print("Nincs login")
                break
        else:
            print(f"Nincs jelszó")
            break"""
            

            
                
            



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