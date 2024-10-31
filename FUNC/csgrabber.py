import traceback
import requests , base64 , json , time

# ALL IN ONE CS - PK - EMAIL - AMOUNT - CURRENCY - SITE NAME GRABBER . CODED BY @Rocketbd


def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return "None"
    
def getcslive(checkout_url):
    try:
        cs_live = checkout_url.split("#")[0].split("/c/pay/")[1]
        return cs_live
    except:
        return "None"
    
def get_formatted_url(checkout_url):
    try:
        url = checkout_url.split('#')[1]
        return url
    except:
        return "None"

def decode_base64_url(encoded_url):
    try:
        encoded_url += '=' * (len(encoded_url) % 4)
        decoded_bytes = base64.urlsafe_b64decode(encoded_url)
        decoded_url = decoded_bytes.decode('utf-8')
        return decoded_url
    except:
        return "None"
    
def decrypt_url(url):
    try:
        encoded_url = url.replace('%2B', '+').replace('%2F', '/')
        decoded_url = decode_base64_url(encoded_url)
        key = 5
        binary_key = bin(key)[2:].zfill(8)
        plaintext = ""
        for i in range(len(decoded_url)):
            binary_char = bin(ord(decoded_url[i]))[2:].zfill(8)
            xor_result = ""
            for j in range(8):
                xor_result += str(int(binary_char[j]) ^ int(binary_key[j]))
            plaintext += chr(int(xor_result, 2))
        return plaintext
    except:
        return "None"

def get_pk(url):
    try:
        plaintext = decrypt_url(url)
        try:
            pk_live = plaintext.split('{"apiKey":"')[1].split('"')[0]
        except:
            pk_live = "None"
        return pk_live
    except:
        return "None"
    
def getraw(cs , pk):
    try:
        url = f"https://api.stripe.com/v1/payment_pages/{cs}/init"
        post_data = f"key={pk}&eid=NA&browser_locale=en-US&redirect_type=stripe_js"
        req = requests.post(url=url, data=post_data).text
        return req
    except:
        return "None"
    
def get_stripe_data(checkout_url):
    try:
        cs = getcslive(checkout_url)
        url = get_formatted_url(checkout_url)   
        pk = get_pk(url)
        raw = getraw(cs , pk)
        data = json.loads(raw)
        try:
            email = data['customer_email']
        except:
            email = "None"
        try:
            currency = data['currency']
        except:
            currency = "None"
        amount = find_between(raw, '"total": ', ',')
        site_name = find_between(raw, '"statement_descriptor": "', '",')
        return cs , pk , email , amount , currency , site_name
    except:
        return "None" , "None" , "None" , "None" , "None" , "None"


