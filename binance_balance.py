11.29 3:21 AM
from binance.client import Client

# Binance API Key और Secret Key दर्ज करें
api_key = "hELY96fratcvHc7YSRtgt54f0PsetZH2S1F4TifuszYuH60Gfkd3SpbgUIFOKMI9"
api_secret = "JClqiok0WXpUh1t1gimzHSfxVFS9kXRwSIE2XFA0MELZyftVQDJlg28pLIVeT5Uh"

# Binance क्लाइंट इनिशियलाइज़ करें
client = Client(api_key, api_secret)

try:
    # अकाउंट बैलेंस प्राप्त करें
    account_info = client.get_account()
    balances = account_info['balances']

    # USDT बैलेंस खोजें
    for balance in balances:
        if balance['asset'] == 'USDT':
            free_usdt = float(balance['free'])
            locked_usdt = float(balance['locked'])
            total_usdt = free_usdt + locked_usdt
            print(f"आपके खाते में कुल USDT: {total_usdt}")
            break
    else:
        print("आपके खाते में USDT नहीं है।")

except Exception as e:
    print(f"कोई त्रुटि हुई: {e}")
