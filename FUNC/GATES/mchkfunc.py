import traceback
from FUNC.GATES.STRIPE_CHARGE import *
from TOOLS.RESPONSE.STRIPE_CHARGE_RESPONSE import *
def mchkfunc(fullcc , user_id , sks , session):
    try:
        result = create_charge(fullcc , sks , session)
        getresp = charge_resp(result , user_id , fullcc)
        return (f"<code>{fullcc}</code>\n<b>Result - {getresp[1]}</b>\n")
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return (f"<code>{fullcc}</code>\n<b>Result - Card Declined 🚫</b>\n")