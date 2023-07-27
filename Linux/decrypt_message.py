import cryptography.fernet as fernet
import os
############################################3
#--------CONSOLE COMMANDS FOR LINUX----------
clear_c="clear"
exit_c="exit"
############################################3
print("[+] Welcome to Message decryption tool by F1DEL ")
print("[+] If you close the application on any sequence of application you should use (CTRL^C)")



while True:
    try:
        print("\n\tWhich option do you choose ?\n1-Decyrpt Messages from file \n2-Decrypt messages from text")
        inp=int(input(">>>"))
        os.system(clear_c)
        break
    except KeyboardInterrupt:
        print("\n[-]Program is Closing ...")
        os.system(exit_c)
        exit()
    except Exception:
        print("\n[-]Invalid Value")
while True:
    try:
        if inp==1:
            os.system(clear_c)
            input("\n\nPress ENTER for continue or CTRL^C for exit")
            encrypted_messages=[]
            while True:
                try:
                    key_file=input("\n\nEnter file path for Key file with key file's name and extension :")
                    message_file=input("Enter file path for Message file with message file's name and extension :")
                    with open(key_file,"r") as key_f:
                        key1=key_f.read()
                    with open(message_file,"r") as msg_f:
                        encrypted_messages  =  msg_f.readlines()
                    print(f"\n\nYour Key : {key1}")
                    a=1
                    for mssg in encrypted_messages:
                        msg11=fernet.Fernet(key1.encode()).decrypt(str(mssg).encode())
                        print(f"Message {a} : {msg11.decode()}")
                        a+=1
                except KeyboardInterrupt:
                    os.system(clear_c)
                    break
                except FileNotFoundError or FileExistsError:
                    print("[-]File not found")
                except Exception as e:
                    print(e)
                    print("[-]Invalid Value")
        else:
            os.system(clear_c)
            input("Press ENTER for continue or CTRL^C for exit")
            while True:
                try:
                    key_t=input("\n\nWhat is Your Key : ")
                    enc_message_t=input("Your Encrypted Message : ")
                    dec_message_t=fernet.Fernet(key_t.encode()).decrypt(enc_message_t.encode())
                    print(f"Decrypted Message : {dec_message_t.decode()}\n\n")
                except KeyboardInterrupt:
                    os.system(clear_c)
                    break
                except Exception:
                    print("[-]Invalid Value")
    except KeyboardInterrupt:
        print("[-]Program is closing ...")
        os.system(exit_c)
        exit()
    except FileNotFoundError or FileExistsError:
        print("[-]File Is Not Found")
    except Exception:
        print("[-]Invalid Value")