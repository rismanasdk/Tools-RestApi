from methods_func import auth, get, post, put, delete, gets

BASE_URL = input("Input Url :")
DEFAULT_PREFIX = "Bearer"
methods = ['GET', 'POST', 'PUT', 'DELETE', 'Change Prefix', 'Exit']

print()
while True:
    for no,method in enumerate(methods, start=1):
        print(f"{no}.{method}")
    user = input("Choose Method Number:")

    if user == "1":
        token = input("Input Token :")
        heads = auth(token, prefix=DEFAULT_PREFIX)
        get(BASE_URL, heads)
    elif user == "2":
        payloads = {}
        head = input("Input Token :")
        heads = auth(token=head, prefix=DEFAULT_PREFIX)
        print("Input `done` in Key if you finished")
        while True:
            Key = input("Input Key :")
            if Key.lower() == "done":
                break
            Val = input(f"Input Value For {Key}:")
            payloads[Key] = Val
        post(BASE_URL, heads, payloads)
    elif user == "3":
        payloads = {}
        head = input("Input Token :")
        heads = auth(token=head, prefix=DEFAULT_PREFIX)
        id = input("Input Id :")
        rBase = f"{BASE_URL}/{id}"
        remai = gets(rBase, heads)
        while remai > 0:
            print(f"Replace Remaining :{remai}")
            Key = input("Input Key :")
            Val = input("Input Value :")
            payloads[Key] = Val
            remai -= 1
        put(rBase, heads, payloads)
    elif user == "4":
        head = input("Input Token :")
        heads = auth(token=head, prefix=DEFAULT_PREFIX)
        id = input("Input Id :")
        rBase = f"{BASE_URL}/{id}"
        delete(rBase, heads)
    elif user == "5":
        print(">>>By default authorization using Bearer token But you can change the prefix<<<")
        cp = input("Input New Prefix, Input `exit` to go back:").lower()
        if cp != "exit":
            DEFAULT_PREFIX = cp
            print("Prefix Successfully Change")
        elif cp == "":
            print("Cancel")
    elif user == "6":
        break
    else:
        print("Error Number")
        