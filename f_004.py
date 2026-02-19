from netmiko import ConnectHandler

login = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}


def zarolas(ssh):
    ssh.send_config_set(["login block-for 60 attempts 3 within 600"])
    
"""def pass_check(ssh):
    
    vty_pass = ssh.send_command("sh run | section line vty")
    vty_pass = vty_pass.split("\n")
    
    con_pass = ssh.send_command("sh run | section line con")
    con_pass = con_pass.split("\n")
    
    
    
    print(f"{vty_pass} \n {con_pass} \n {user_pass}")
    
    # username pass
    if len(user_pass[-1]) < 8:
        csere = input("Túl rövid a username jelszó, minimum 8 karaktereset kérek: ")
        user_pass[-1] = csere
    
    print(user_pass[-1])

"""

def enapass_check_kozos(ssh):
    ena_pass = connect.send_command("sh run | include enable password").split(' ')[-1]
    
    if len(ena_pass) < 8:
        uj_enable = input("Túl rövid az enable jelszó, kérek egy újat (minimum 8 karakteres): ")
        
        while len(uj_enable) < 8:
            uj_enable = input("Túl rövid az enable jelszó, kérek egy újat (minimum 8 karakteres): ")
            
        connect.send_config_set(f"enable pass {uj_enable}")
        print("Beállitva")

def conpass_check_kozos(ssh):
    con_pass = connect.send_command("sh run | section line con").split("\n")
    
    for i in con_pass:
        if i.strip().startswith("password"):
            
            if len(i.split(' ')[-1]) < 8:
                uj_con = input("Túl rövid a konzól jelszó, kérek egy újat (minimum 8 karakteres): ")
                
                while len(uj_con) < 8:
                    uj_con = input("Túl rövid a konzól jelszó, kérek egy újat (minimum 8 karakteres): ")
                
                connect.send_config_set(["line con 0" , f"password {uj_con}"])
                print("Beállitva")  
                
def vtypass_check_kozos(ssh):
    vty_pass = connect.send_command("sh run | section line vty 0-4").split("\n")
    
    for i in vty_pass:
        if i.strip().startswith("password"):
            
            if len(i.split(' ')[-1]) < 8:
                uj_vty = input("Túl rövid a vty jelszó, kérek egy újat (minimum 8 karakteres): ")
                
                while len(uj_vty) < 8:
                    uj_vty = input("Túl rövid a vty jelszó, kérek egy újat (minimum 8 karakteres): ")
                
                connect.send_config_set(["line vty 0 15" , f"password {uj_vty}"])
                print("Beállitva")  

def userpass_check_solo(ssh):
    user_pass = ssh.send_command("sh run | include user")
    user_pass = user_pass.split("\n")
    print(user_pass)
    
    """for i in user_pass:
        if len(user_pass[-1]) < 8:
            
            uj_user_pass = input(f"Túl rövid a {user_pass(1)} user jelszava, kérek egy újat (minimum 8 karakteres): ")
                    
            while len(uj_user_pass) < 8:
                uj_user_pass = input(f"Túl rövid a {user_pass(1)} user jelszava, kérek egy újat (minimum 8 karakteres): ")
                    
            connect.send_config_set(["line con 0" , f"password {uj_user_pass}"])
            print("Beállitva")  """

    for i in user_pass:
        print(user_pass.rstrip()[i])

    """for i in user_pass:
        if user_pass.rstrip()[i] < 8:
            uj_user_pass = input(f"Túl rövid a {user_pass(1)} user jelszava, kérek egy újat (minimum 8 karakteres): ")
                    
            while len(uj_user_pass) < 8:
                uj_user_pass = input(f"Túl rövid a {user_pass(1)} user jelszava, kérek egy újat (minimum 8 karakteres): ")
                    
            connect.send_config_set(["line con 0" , f"password {uj_user_pass}"])
            print("Beállitva")"""




#########################
#        PROGRAM        #
#########################

try:
    with ConnectHandler (**login) as connect:
        #B feladat
        zarolas(connect)
        
        #2. feladat
        # pass_check(connect)

        #2.2 feladat
        """enapass_check_kozos(connect)
        
        conpass_check_kozos(connect)
        
        vtypass_check_kozos(connect)"""
        
        userpass_check_solo(connect)
        
except Exception as ex:
    print(f"Hiba: {ex}")