"""from netmiko import ConnectHandler

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
"""

def console_pass():
    #ssh.save_config()
    
    parancsok = []
    con_pass = "line con 0\n password Jelszo123\n logging synchronous\n login local"
    #con_pass = connect.send_command("sh run | section line con")
    con_pass = con_pass.split("\n")
    
    for szo in con_pass:
        szo = szo.strip()
        if "password" in szo or szo == "login":
            parancsok.append(szo)

    print(parancsok)
    
    
    
    if len(parancsok) == 2:
        print("Konzol jelszó és hitelesítés beállítása OK!")
        
    elif len(parancsok) < 2:
        
        #ezt a reszt aznezni
        if "password" in parancsok:
            print("Van jelszó, de nincs login")
        
        else:
            print("Van login, de nincs jelszó")
        #eddig
    else:
        print("Semmilyen beállítás nincs (jelszó, login)")
    
    
"""    if ("password" in con_pass):
        
        if con_pass.count("login") == 1:
                print("Konzol jelszó és hitelesítés beállítása OK!")
            
        else:
            print("Nincs login")
            
    else:
        print(f"Nincs jelszó")
            
    for i in range (len(con_pass)):
        
        if ("password" in con_pass[i]):
            if ("login" == con_pass[i+1]):
                print("Konzol jelszó és hitelesítés beállítása OK!")
                break
            else:
                print("Nincs login")
                break
        else:
            print(f"Nincs jelszó")
            break
            
      """      
            
"""def interface_db(ssh):
    interfaces = ssh.send_command("sh run | include int")
    interfaces = interfaces.split("\n")
    int = ["Ethernet", "FastEthernet", "GigabitEthernet"]
    print(interfaces)
    
    EtDB=0
    FEtDB=0
    GEtDB=0
    Et=[]
    FE=[]
    GE=[]
    
    for i in range (len(int)):
        for j in range (len(interfaces)):
            
            if (int[i] in interfaces and "Ethernet" in interfaces[j]):
                EtDB+=1
                Et.append(interfaces[i])
            elif (int[i] in interfaces and interfaces[i] == "FastEthernet"):
                FEtDB+=1
                FE.append(interfaces[i])
            elif (int[i] in interfaces and interfaces[i] == "GigabitEthernet"):
                GEtDB+=1
                GE.append(interfaces[i])
    
    
    
    for i in range (len(interfaces)):
            
        if ("FastEthernet" in interfaces[i]):
            FEtDB+=1
            FE.append(interfaces[i])
        elif ("GigabitEthernet" in interfaces[i]):
            GEtDB+=1
            GE.append(interfaces[i])
    
    print(f"{EtDB}, {FEtDB}, {GEtDB}")
    print(f"{Et}, {FE}, {GE}")"""
                
            



#########################
#        PROGRAM        #
#########################


console_pass()


"""try:
    with ConnectHandler(**login) as connect:
        #1. feladat
        vlan(connect)
        
        #print(f"{connect.send_command("sh vl br")} \n")
        
        
        #2. feladat
        console_pass(connect)
        
        
        #4. feladat
        #interface_db(connect)
        
    
except Exception as ex:
    print(f"Error: {ex}")"""