import time
from datetime import datetime as dt

# path of the hosts file for windows --> C:\Windows\System32\drivers\etc\hosts

# host_temp = r"D:\My Programs\Python Projects\Website Blocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com"] # List of website names you want to block

while True:
    # Checking current time with the time we want the sites to be blocked
    if dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working time....")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " +website+ "\n")
    else:
        print("Fun time....")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)

# The file extension should be .pyw so that it can run without terminal just by clicking on it
# You can schedule the file from Task Schedular as per your desired