import traceback
def gcgenfunc(len=4):
    try:
        import string
        import random
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(chars) for _ in range(len))
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def insert_pm(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        info = {"gc": f"{gc}", "status": "ACTIVE", "type": "PREMIUM"}
        insert = gcdb.insert_one(info)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def insert_plan1(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        info = {"gc": f"{gc}", "status": "ACTIVE", "type": "PLAN1"}
        insert = gcdb.insert_one(info)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def insert_plan2(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        info = {"gc": f"{gc}", "status": "ACTIVE", "type": "PLAN2"}
        insert = gcdb.insert_one(info)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def insert_plan3(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        info = {"gc": f"{gc}", "status": "ACTIVE", "type": "PLAN3"}
        insert = gcdb.insert_one(info)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def getgc(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        find = gcdb.find_one({"gc": f"{gc}"}, {"_id": 0})
        return find
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def getallgc():
    try:
        import pymongo
        from mongodb import client, gcdb
        find = gcdb.find({}, {"_id": 0})
        return find
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def updategc(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        prev = {"gc": f"{gc}"}
        nextt = {"$set": {"status": "USED"}}
        update = gcdb.update_one(prev, nextt)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def plan1gc(user_id):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        credit = int(getuser["credit"])
        getkey = int(getuser["totalkey"])
        plan_value = "Starter Plan 0.99$"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"plan": f"{plan_value}"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=7)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
        setkey = getkey + 1
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"totalkey": f"{setkey}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def plan2gc(user_id):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        credit = int(getuser["credit"])
        getkey = int(getuser["totalkey"])
        plan_value = "Silver Plan 1.99$ ∞"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"plan": f"{plan_value}"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=15)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
        setkey = getkey + 1
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"totalkey": f"{setkey}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def plan3gc(user_id):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        credit = int(getuser["credit"])
        getkey = int(getuser["totalkey"])
        plan_value = "Gold Plan 4.99$ ∞"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"plan": f"{plan_value}"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=30)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
        setkey = getkey + 1
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"totalkey": f"{setkey}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def onlycredits(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        credit = int(getuser["credit"])
        getkey = int(getuser["totalkey"])
        setcredit = credit + 1000
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"credit": f"{setcredit}"}}
        update = usersdb.update_one(prev, nextt)
        setkey = getkey + 1
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"totalkey": f"{setkey}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
