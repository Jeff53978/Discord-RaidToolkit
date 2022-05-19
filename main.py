import requests, os, time

class attacks():
    
    def client_crasher(token):
        pass
    
    def server_leaver(token):
        pass
    
    def message_remover(token):
        pass
    
    def dm_spammer(token):
        pass

os.system("cls")

token = input("[?] Enter discord token: ")

headers = {
    "authorization": token
}

def main():
    print("\n[*] Logged in as: {}".format(requests.get("https://discord.com/api/v10/users/@me", headers=headers).json()["username"]))
    time.sleep(1)
    print("[*] Loaded {} guilds\n".format(len(requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers).json())))

    time.sleep(2)
    print("[0] Client crasher")
    print("[1] Server leaver")
    print("[2] Message remover")
    print("[3] DM Spammer\n")

    time.sleep(1)
    attack = int(input("[?] Select attack: "))

    if attack == 0:
        os.system("cls")
        attacks.client_crasher(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 1:
        os.system("cls")
        attacks.server_leaver(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 2:
        os.system("cls")
        attacks.message_remover(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 3:
        os.system("cls")
        attacks.dm_spammer(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    
main()
    

