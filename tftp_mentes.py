from netmiko import ConnectHandler


login = {
    "device_type": "cisco_ios",
    "host": "192.168.40.210",
    "username": "binkslik",
    "password": "netmiko2026"
}


try:
    with ConnectHandler(**login) as connect:
        
        tftp_ip = input(f"Add meg a szerver IP-címét: ")
        filename = input(f"Mentendő konfig filename: ")

        output = connect.send_multiline_timing(["copy run tftp:", tftp_ip, filename])
    
        print(output)

except Exception as ex:
    print(f"Error: {ex}")