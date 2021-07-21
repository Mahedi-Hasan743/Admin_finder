#!/user/bin/env python

import requests
import threading


def katfish():
    print("""
    !!!      !!!           @@@@@@          ========!!!!========  11111111111111   ###############   $$$$$$$$$$$$$$$   @@@       @@@
    !!!      !!!          @@    @@         ========!!!!========  11111111111111   ###############   $$$$$$$$$$$$$$$   @@@       @@@
    !!!   !!!            @@      @@        ========!!!!========  111                   ####         $$$$              @@@       @@@
    !!!  !!!!           @@        @@               !!!!          111                   ####         $$$$              @@@       @@@  
    !!!!!              @@ ======== @@              !!!!          11111111111111        ####         $$$$$$$$$$$$$$$   @@@@@@@@@@@@@
    !!!!!             @@============@@             !!!!          11111111111111        ####         $$$$$$$$$$$$$$$   @@@@@@@@@@@@@
    !!!  !!!!        @@==============@@            !!!!          111                   ####                    $$$$   @@@       @@@
    !!!  !!!!       @@                @@           !!!!          111                   ####                    $$$$   @@@       @@@
    !!!      !!!   @@                  @@          !!!!          111              ###############   $$$$$$$$$$$$$$$   @@@       @@@
    !!!      !!!  @@                    @@         !!!!          111              ###############   $$$$$$$$$$$$$$$   @@@       @@@

    """)

wordlist = open("/root/admin_finder/admin-page.txt","r")
def admin_panel(url):
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+"/"+words)
        if req.status_code == 200:
            print(req.url)


print(katfish())
url = input("Target url -->> ")
if url !=None:
    for i in range(50):
        time = threading.Thread
        time.start()
else:
    print("[+] Unable to find Admin Panel")

