import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import base64
import uuid
import json
import time

file_path = 'access-key.json'

with open(file_path, 'r') as file:
    access_key = json.load(file)

key = access_key["key"]
publicKey = access_key["publicKey"]
name = access_key["name"]

host = "https://api-testnet.bitscrunch.com"

path = "/api/v1/market/metrics?currency=usd&blockchain=1&metrics=holders&metrics=marketcap&time_range=24h&include_washtrade=true"
body = ""

num_requests = 50000

for _ in range(num_requests):
    try:
        request_id = uuid.uuid1().hex
        message = request_id + ':GET:' + path + ':' + body + ':'

        def sign_message(key, message):
            c_key = ECC.import_key(
                '-----BEGIN EC PRIVATE KEY-----\n' + key + '\n-----END EC PRIVATE KEY-----')
            h = SHA256.new(message.encode('utf-8'))
            signer = DSS.new(c_key, 'fips-186-3', encoding="der")
            signature = signer.sign(h)
            return base64.b64encode(signature)
        signature = sign_message(key, message)

        headers = {
            'rid': request_id,
            'name': name,
            'sign': signature,
            'pubkey': publicKey,
            'message': message
        }

        response = requests.get(host + path, headers=headers, timeout=10)
        response.raise_for_status()
        print(response.json())

        # Tunggu beberapa detik sebelum permintaan berikutnya
        time.sleep(3)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
