import time

def ratInterface():
    print("IT'S RATTING TIME")
    print("This tool will deploy a RAT (remote acsess trojan)")
    print("onto any machine (not just computer!) of your choice!!!!!!!!\n\ŋ\n\n\ŋ\n")

    addr = input("Input IP ADDRRES to RAT: ")

    print(f'\nestablishing connection to {addr}........')
    time.sleep(.92)
    print('sending packets........')
    for i in range(1,11):
        time.sleep(.1)
        print(f'[{i}/10]')
    print('done!')
    time.sleep(1)
    print(f'recieving packets from {addr}........')
    for i in range(1,11):
        time.sleep(.5)
        print(f'[{i}/10]')
    print('done!')
    time.sleep(1)
    print(f'succesfully connected to {addr} !!!!')
    time.sleep(.1)
    print('initializing rat tools........')
    time.sleep(.5)
    print('\nRAT TYPES:\n1. Black rat (Impossible to detect, only terminal access)\n2. Brown rat (Can be detected by top level anti malware, full file access)\n3. Fancy rat (Hidden in filesystem, can modify files)\n4. Tanezumi rat (Easily seen by users, full access to everything)\n')
    rat = input('Select rat type to send (1-4): ')
    print("detecting os........")
    time.sleep(.5)
    print("detecting version........")
    time.sleep(.5)
    print("detecting version........")
    print('\n compiling rat objects........')
    for i in range(1,11):
        time.sleep(1.727)
        print(f'[{i}/10]')
    print('Rat compiled!')
    time.sleep(.1)
    print('sending rat files to system........')
    for i in range(1,11):
        time.sleep(.4)
        print(f'[{i}/10]')
    print('done!')
    time.sleep(.1)
    print('activating daemon........')
    time.sleep(1)
    print("done!\n")
    print(f"Rat of type {rat} has been deployed at {addr}")

ratInterface()
