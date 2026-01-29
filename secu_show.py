from netmiko import ConnectHandler

def netmiko_show_version(kapcsolo):
    try:
        with ConnectHandler(**kapcsolo) as kapcsolat:
            output = kapcsolat.send_command("show version")
            
    except Exception as ex:
        print(f"Hiba: {ex}")

def fajl_beolvas():
    try:
        with open("show_version.txt", encoding="utf-8") as fajl:
            szoveg = fajl.read()
        
    except IOError as ex:
        print(f"IO error: {ex}")
        
    return szoveg



# Milyen IOS verzió fut a kapcsolón?
def ios_versio(version_info):
    elso_sor = version_info.split("\n")[0]
    
    r = elso_sor.split(",")
    
    versio = r[1].strip().split(" ")[2].lstrip("(").rstrip(")")
    versio += " " + r[2].strip().lstrip("Version ")

    return versio



# Hány Ethernet interface van a kapcsolón?
def ethernet_interfacek_szama():
    pass



#########################
#        PROGRAM        #
#########################

output = ""

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.133",
    "username": "binkslik",
    "password": "netmiko2026",
}

#netmiko_show_version(kapcsolo)
#print(output)

version_info = fajl_beolvas()



print(f"IOS verzió: {ios_versio(version_info)} \n")
print(f"{ethernet_interfacek_szama()} Ethernet interface van a kapcsolón \n")