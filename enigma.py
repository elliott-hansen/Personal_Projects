import random
from collections import deque
import os

class Rotor():

    def __init__(self, id, disk, next=None,):
        self.id = id
        self.disk = disk
        self.rotated = 0
        self.next = next
        self.prev = None

    def __len__(self):
        return len(self.disk)
    
    def rotate(self, times = 1, nospin=False, spinself=True):
        for i in range(times):
            self.rotated += 1
            values_deque = deque(self.disk.values())
            if spinself:
                values_deque.rotate(-1)
            self.disk = dict(zip(self.disk.keys(), values_deque))
            if self.rotated >= len(self.disk):
                self.rotated = 0
                if self.next is not None and not nospin:
                    self.next.rotate(1)


    def set(self, pos):
        print("SETTING DISK",self.id," TO POS:",pos)
        while self.rotated != 0:
            self.rotate(1,nospin=True)
        self.rotate(pos, nospin=True)

    def endisk(self, character, ref=False):
        if not ref:
            ret = list(self.disk.values())[list(self.disk.keys()).index(character)]
        else:
            ret = list(self.disk.keys())[list(self.disk.values()).index(character)]
        return ret

    
def encrypt(rotorset, char, ref=False):
    for disk in rotorset:
        if not ref:
            char = disk.endisk(char)
        else:
            char = disk.endisk(char, ref=True)
    return char

def print_setting(rotorset):
    for disk in rotorset:
        print(" - ",disk.rotated," - ", end=" | ")
    print('\n')

def print_disks(rotorset):
    print_setting(rotorset)
    print("")
    for i in range(0,len(rotorset[0].disk.keys())):
        for disk in rotorset:
            print('[ ',list(disk.disk.keys())[i],' : ',list(disk.disk.values())[i],' ]' + ' '*2, end="")
        print("")

def reflect(i):
    reg_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ref = list("EJMZALYXVBWFCRQUONTSPIKHGD")
    ref = dict(zip(reg_alphabet, ref))
    return ref[i]

def encrypt_message(rotorset, message, ref=True):
    encrypted = ""
    for i in [i for i in message.upper() if i.isalnum()]:
        char = encrypt(rotorset, i)
        if ref:
            char = encrypt(rotorset[::-1], reflect(char), ref=True)
        encrypted += char
        rotorset[0].rotate(1)
    return encrypted

def display(message):
    print(" - - ENCRYPTED MESSAGE - - \n\n")
    m = [message[i:i+5] for i in range(0,len(message),5)]
    for i in m:
        print(i)
    print('\n\n')

def build_disk(a1, a2):
    returndisk = {}
    for i in range(0,len(a1)):
        returndisk[a1[i]] = a2[i]
    return returndisk

def configure_enigma():
    reg_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    disk1 = build_disk(reg_alphabet, list("JGDQOXUSCAMIFRVTPNEWKBLZYH"))
    disk2 = build_disk(reg_alphabet, list("NTZPSFBOKMWRCJDIVLAEYUXHGQ"))
    disk3 = build_disk(reg_alphabet, list("JVIUBHTCDYAKEQZPOSGXNRMWFL"))
    rotor6 = Rotor(6, disk3)
    rotor5 = Rotor(5, disk2, next=rotor6)
    rotor4 = Rotor(4, disk1, next=rotor5)
    rotor3 = Rotor(3, disk3, next=rotor4)
    rotor2 = Rotor(2, disk2, next=rotor3)
    rotor1 = Rotor(1, disk1, next=rotor2)
    os.system('cls')
    disknum = 0

    #configure number of rotors to use (3 <= disks <= 6). More = harder to crack
    # while type(disknum) != 'int' or int(disknum) > 6 or int(disknum) < 3:
        
    disknum = int(input("Enter a number of rotors to use (between 3 and 6): "))

    if disknum == 3:
        print("SETTING ",disknum,"ROTORS")
        rotor3.next = None
        rotorset = [rotor1, rotor2, rotor3,]
    elif disknum == 4:
        print("SETTING ",disknum,"ROTORS")
        rotor4.next = None
        rotorset = [rotor1, rotor2, rotor3, rotor4]
    elif disknum == 5:
        print("SETTING ",disknum,"ROTORS")
        rotor5.next = None
        rotorset = [rotor1, rotor2, rotor3, rotor4, rotor5]
    elif disknum == 6:
        print("SETTING ",disknum,"ROTORS")
        rotorset = [rotor1, rotor2, rotor3, rotor4, rotor5, rotor6]

    for i in range(0, disknum):
        pos = int(input("ENTER A STARTING POS: "))
        rotorset[i].set(pos)
        print("SUCCESS")
    return rotorset



if __name__ == "__main__":
    rotorset = configure_enigma()
    print_setting(rotorset)
    while True:
        pre = input("Enter a message to encrypt (without any non-alpha characters). \n - Type '!' to quit\n - Type '@' to configure\n - Type '#' to view the current rotor configuration \n\n")
        if pre == '!':
            print("Thanks for hacking!")
            quit()
        elif pre == '@':
            rotorset = configure_enigma()
            continue
        elif pre == '#':
            os.system('cls')
            print_disks(rotorset)
            continue;
        enc = encrypt_message(rotorset, pre, ref=True)
        display(enc)
