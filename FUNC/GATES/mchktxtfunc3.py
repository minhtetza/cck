import traceback , time
from FUNC.GATES.STRIPE_CHARGE3 import *
from TOOLS.RESPONSE.STRIPE_CHARGE_RESPONSE3 import *
def mchktxtfunc(fullcc , user_id , sks , session):
    try:
        # start = time.perf_counter()
        result = create_charge(fullcc , sks , session)
        getresp = charge_resp(result , user_id , fullcc)
        # end = time.perf_counter()
        # print(f"{fullcc} - {getresp[1]} - {end - start:0.2f} seconds")
        return getresp
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return "Dead 🔴" , "Card Declined 🚫" , "NO" , fullcc