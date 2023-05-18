import requests
import re
import csv

url = "https://github.com/elastic/examples/raw/master/Machine%20Learning/Security%20Analytics%20Recipes/suspicious_login_activity/data/auth.log"
response = requests.get(url)

if response.status_code == 200:
    with open("auth.log", "wb") as file:
        file.write(response.content)
else:
    print("Nie udało się pobrać pliku logu.")
    exit()

date_pattern = r"(\w{3} \d{1,2} \d{2}:\d{2}:\d{2})"
ip_pattern = r"(\d+\.\d+\.\d+\.\d+)"
regex_pattern = r"(?<=\[)(.*?)(?=\]).*?:(.*)"

with open("auth.log", "r") as file:
    log_content = file.readlines()

with open("parsed_log.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["Data", "Adres IP", "Użytkownik/Usługa", "Komunikat"])

    for line in log_content:
        find_date = re.findall(date_pattern, line)
        find_ip = re.findall(ip_pattern, line)
        find_other = re.findall(regex_pattern, line)
        if find_date and find_ip and find_other:
            date = find_date[0]
            ip_address = find_ip[0]
            user_service = find_other[0][0]
            message = find_other[0][1]
            writer.writerow([date, ip_address, user_service, message])
