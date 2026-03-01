import requests as req
from delimiter import sc, pd, hs

def auth(token, prefix="Bearer"):
    headers = {
        "Authorization": f"{prefix} {token}",
        "Content-Type": "application/json"
    }
    return headers

def get(BASE_URL, headers):
    send = req.get(url=BASE_URL, headers=headers)
    print(sc)
    print("Status Code:", send.status_code)
    print(pd)
    print(send.json())
    print(hs)
    print(send.headers)
    
def post(BASE_URL, heads, payloads):
    send = req.post(url=BASE_URL, headers=heads, json=payloads)
    print(sc)
    print("Status Code :", send.status_code)
    print(pd)
    print(payloads)
    print(hs)
    print("Headers :", send.headers)

def gets(rBase, heads):
    gets = req.get(url=rBase, headers=heads)
    converts = gets.json()
    sub = len(converts) -1
    print(converts)
    return sub  

def put(rBase, heads, payloads):
    pay = req.put(url=rBase, headers=heads, json=payloads)
    print(payloads)
    print(pay.status_code)

def delete(rBase, heads):
    gets = req.delete(url=rBase, headers=heads)
    print(gets.status_code)