import requests
import time
url = "https://labs.vocareum.com/util/vcput.php?a=startaws&stepid=1117042&version=0&mode=s&type=1&vockey=2jSYD0pkJTWSVJS6KXHdww=="
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Cookie": "vocsbmt=1; vocmsg=Submitted+successfully; vocLabAccess_15524=rc56b44c61404a1116444u2253319__centos__terminal; vocLabAccess_59817=r3173b8c61404a1116459u2253319__centos__terminal; vocLabAccess_15525=r6a184fc61404a1116412u2253319__centos__terminal; vocLabAccess_15526=r6f8ddcc61404a1116428u2253319__centos__terminal; vocLabAccess_1=c61404a1116680u2253319__rdp_client_rdp_client; vocLabAccess_0=c61404a1116703u2253319__rdp_client_rdp_client; domain_latestWebProxy=https://vproxy.vocareum.com/hostip//vocproxy/; vocareum_entry_link=../main/main.php?m=editor&asnid=1117039&stepid=1117040&hideNavBar=1; _ga=GA1.2.1476861862.1676565370; _gid=GA1.2.1743759879.1676565370; PHPSESSID=5squu27cmfdt7gngol4rnkkcsu; logintoken=9c43f01224d984677cbece9f8a6bbdd7; tokenExpire=1676652159; usertoken=9c43f01224d984677cbece9f8a6bbdd7; userid=2253319; t2fausers=9c43f01224d984677cbece9f8a6bbdd7; usingLTI=1; myfolder=09734a0c524b613972471ff255edda70; currentcourse=vc_2_0_08302022org270_240; currentassignment=1117041; userassignment=1117041",
    "Referer": "https://labs.vocareum.com/main/main.php?m=editor&asnid=1117041&stepid=1117042&hideNavBar=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
while True:
    time.sleep(1200)
    response = requests.get(url, headers=headers)
    print("enviado peticion a :", url)
    print("respuesta:", response.text)
