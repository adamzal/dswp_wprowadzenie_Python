import re

with open("strings.txt", "r") as file:
    content = file.read()

numbers = re.findall(r"\d+", content)

numbers_3_digits = re.findall(r"\d{3,}", content)

ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)

capitalized_words = re.findall(r"\b[A-Z]\w*\b", content)

lines_with_4_words = re.findall(r"^(?:\w+\s+){3,}\w+$", content, re.MULTILINE)

urls = re.findall(r"\bhttps?://\S+\b", content)

print("Wszystkie liczby:", numbers)
print("Liczby co najmniej 3 cyfrowe:", numbers_3_digits)
print("Adresy IPv4:", ip_addresses)
print("Wyrazy rozpoczynające się od wielkiej litery:", capitalized_words)
print("Linie z co najmniej 4 wyrazami:", lines_with_4_words)
print("Adresy URL:", urls)
