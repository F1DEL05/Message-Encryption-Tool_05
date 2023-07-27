import cryptography.fernet as fernet
import os

############################################3
#--------CONSOLE COMMANDS FOR LINUX----------
clear_c="cls"
exit_c="exit"
############################################3
#------------------Default Encription Key----------------------
key_def="1L4kYfLzy0b-SZzw3zwqaYJv6mT9j3F5nkxzWsjJH00=".encode()
#--------------------------------------------------------------


print("[+] Welcome to Message encryption tool by F1DEL ")
print("[+] If you close the application on any sequence of application you should use (CTRL^C)")



while True:
    try:
        print("\tWhich key do you use ?\n1-Generate New Key \n2-Use Default Key")
        inp=int(input(">>>"))
        os.system(clear_c)
        break
    except KeyboardInterrupt:
        print("\n[-]Program is Closing ...")
        os.system(exit_c)
        exit()
    except Exception:
        print("\n[-]Invalid Value")
if inp==2:
    print(f"\nYour encription key is : {key_def.decode()} ")
else:
    new_key=fernet.Fernet.generate_key().decode()
    print(f"\nYour encryption key is {new_key}")
print("\nPlease Don' Lost This Key...")
all_message=[]
while True:
    try:
        if inp==2:
            message=input("\nYour Message : ")
            enc_message=fernet.Fernet(key_def).encrypt(message.encode()).decode()
            all_message.append(enc_message)
            print(f"Encrypted Message : {enc_message}")
        else:
            message_n=input("\nYour Message : ")
            enc_message_n=fernet.Fernet(new_key).encrypt(message_n.encode()).decode()
            all_message.append(enc_message_n)
            print(f"Encrypted Message : {enc_message_n}")
    except KeyboardInterrupt:
        print("[-]Program is Closing ...")
        break
    except Exception:
        print("[-]Exception Found")
while True:
    try:
        inp1=input("[?]Do you want to save all your messages ? (Y/N)")
        if inp1=="y" or inp1=="Y":
            print("your key is saving to key.txt file\nyour all encrypted messages is saving to enc_message.txt file\nthis files is in same directory with this python file")
            if inp==1:
                with open("key.txt","w") as keyfile:
                    keyfile.write(new_key)
                    keyfile.close()
            else:
                with open("key.txt","w") as key_file:
                    key_file.write(key_def)
                    key_file.close()
            with open("enc_message.txt","w") as message_file:
                message_file.write(all_message[0]+"\n")
                message_file.close()
            with open("enc_message.txt","a") as message_file1:
                for i in all_message:
                    message_file1.write(i+"\n")
                message_file1.close()
            break
        elif inp1=="n" or inp1=="N":
            break
        else:
            print("\n[-]Invalid Value")
    except KeyboardInterrupt:
        print("\n[-]Program is closing ...")
        os.system(exit_c)
        exit()
    except Exception:
        print("\n[-]Invalid Value")