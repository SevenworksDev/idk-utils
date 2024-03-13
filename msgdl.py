import requests, base64, itertools, time, os

accountid = ""
password = ""

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, itertools.cycle(key)))

def base64_decode(string: str) -> str:
    return base64.urlsafe_b64decode(string.encode()).decode()

def gjp_encrypt(data):
    return base64.b64encode(xor(data, "37526").encode()).decode()

def message_decode(data):
    return xor(base64_decode(data), '14251')

def savemsg(user, tsubject, tbody):
    with open('messages.txt', 'a', encoding='utf-8') as file:
        file.write("___________________________________________\n")
        file.write(f"User: {user}\n")
        file.write(f"Subject: {tsubject}\n")
        file.write(f"Body: {tbody}\n")

def msgdl(page=0):
    msgcount = 0
    while True:
        try:
            r = requests.post("http://www.boomlings.com/database/getGJMessages20.php", data={"accountID":accountid,"gjp":gjp_encrypt(password),"getSent":"0","page":str(page),"secret":"Wmfd2893gb7"}, headers={"User-Agent": ""}).text
            if r.startswith('-'):
                input("Done")
            if r.startswith('error code:'):
                print("Waiting for 61 minutes before retrying...")
                time.sleep(61 * 60)
                continue
            time.sleep(0.4)
            msgids = set()
            for msg in r.split('|'):
                msginfo = msg.split(':')
                if len(msginfo) >= 8:
                    messageID = msginfo[7]
                    if messageID not in msgids:
                        msgids.add(messageID)
                        rr = requests.post("http://www.boomlings.com/database/downloadGJMessage20.php", data={"accountID":accountid,"gjp":gjp_encrypt(password),"messageID":messageID,"secret":"Wmfd2893gb7"}, headers={"User-Agent": ""}).text
                        savemsg(rr.split(":")[1], base64_decode(rr.split(":")[9]), message_decode(rr.split(":")[15]))
                        msgcount += 1
                        os.system("cls")
                        print(f"Messages: {msgcount}")
                        print(f"Page: {page}")
                        time.sleep(0.6)
            page += 1
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    msgdl()
