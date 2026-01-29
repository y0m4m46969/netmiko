from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}


def mentes(ssh):
    ssh.save_config()


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


except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")