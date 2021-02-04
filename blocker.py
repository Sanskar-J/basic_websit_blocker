import time
from datetime import datetime as dt
hosts_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
web_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,2) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Working Hours")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()

        print("Fun hours")
    time.sleep(5)