from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}


def mentes(ssh):
    ssh.save_config()
    
    
def set_enable_pass(ssh):
    jelszo = input("Adj egy enable jelszót NOW: ")
    ssh.send_config_set(f"enable password {jelszo}")
    
def pass_titkos(ssh):
    ssh.send_config_set("service password-encryption")
    print(kapcsolat.send_command("show run | include enable"))
    
def banner(ssh):
    ssh.send_config_set("banner motd -Jogosulatlanul bejelentkezni tilos!-")
    print(kapcsolat.send_command("show run | include banner"))
    print(kapcsolat.send_command("show run | include password"))
    print(kapcsolat.send_command("show run | include secret"))
    
def pvst(ssh):
    ssh.send_config_set("spanning-tree mode rapid-pvst")
    print(kapcsolat.send_command("show run | include rapid"))


#########################
#        PROGRAM        #
#########################



try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #2. feladat
        print(kapcsolat.find_prompt())

        #3. feladat
        mentes(kapcsolat)
        
        valasz = kapcsolat.send_command("show star")
        if "not present" not in valasz:
            print("A mentés sikerült! Yay!!")
        else:
            print("A mentés nem sikerült.")
        
        #4. feladat
        set_enable_pass(kapcsolat)
        
        print(kapcsolat.send_command("show run | include enable"))

        #5. feladat
        pass_titkos(kapcsolat)
        
        #6. feladat
        banner(kapcsolat)
        
        #7. feladat
        pvst(kapcsolat)
        
        #8. feladat
        try:
            with open ("config-save.txt", "w", encoding="utf-8") as save:
                save.write(kapcsolat.send_command("sh run"))
        except Exception as ex:
            print(f"Error: {ex}")


except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")