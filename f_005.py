from netmiko import ConnectHandler

login = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}
"""
def ospf_lekerdezes(ssh):
    global ospf
    
    print(connect.send_command("sh ip ospf neighbor"))
    ospf =  connect.send_command("sh run | include router ospf").split(" ")
    hal_cim = input("Adj meg egy hálózat címet amit szeretnél hirdetni:")
    print(connect.send_config_set([f"router ospf {ospf[-1]}", f"network {hal_cim} area 0"] ))
    
def savszelesseg_beallitas(ssh):
    savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
    while savszelesseg != 100 and savszelesseg != 1000 and savszelesseg != 10000: 
        savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
    print(connect.send_config_set([f"router ospf {ospf[-1]}", f"auto-cost reference-bandwidth {savszelesseg}"]))
    """
def router_id_beallitasa(ssh):
    router_id = input("Kérek egy router azonositőt: ")
    router_id = router_id.split(".")
    norm = True

    while len(router_id) != 4:
        router_id = input("Négy számból álhat: ")
        router_id = router_id.split(".")
        
    for i in router_id:
        if not(i.isnumeric()):
            norm = False
            router_id = input("Csak számokból állhat: ")
        else:
            norm =  True
            
        if int(i) >= 255:
            norm = False
            router_id = input("255 vagy az alatti számok lehetnek csak: ")
        else:
            norm = True
    
    if norm == True:
        print("Jó a router id (❁´◡`❁)")


    print(router_id)



#########################
#        PROGRAM        #
#########################

try:
    with ConnectHandler (**login) as connect:
        """#1. feladat
        ospf_lekerdezes(connect)
        
        #2. feladat
        savszelesseg_beallitas(connect)"""
        
        #3. feladat
        router_id_beallitasa(connect)
        
except Exception as ex:
    print(f"Hiba: {ex}")