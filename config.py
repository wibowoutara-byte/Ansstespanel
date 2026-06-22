import os
import json

# Heroku vs Local
IS_HEROKU = os.environ.get('DYNO') is not None

if IS_HEROKU:
    # Heroku config
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID', '')
    GROUP_CHAT_ID = os.environ.get('GROUP_CHAT_ID', '')
    
    # Orange Carrier Login Credentials (fallback)
    ORANGE_EMAIL = os.environ.get('ORANGE_EMAIL', '')
    ORANGE_PASSWORD = os.environ.get('ORANGE_PASSWORD', '')
    
    # URLs
    LOGIN_URL = os.environ.get('LOGIN_URL', 'https://www.orangecarrier.com/login')
    CALL_URL = os.environ.get('CALL_URL', 'https://www.orangecarrier.com/live/calls')
    BASE_URL = os.environ.get('BASE_URL', 'https://www.orangecarrier.com')
    
    # Cookies from environment variable (JSON string)
    cookies_env = os.environ.get('ORANGE_COOKIES', '')
    ORANGE_COOKIES = json.loads(cookies_env) if cookies_env else []
    
    # Settings
    MAX_ERRORS = int(os.environ.get('MAX_ERRORS', '10'))
    CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', '5'))
    
else:
    # Local development Configuration
    BOT_TOKEN = '8921418965:AAHVR3FsOrvVi9Mn7ZspV203PAm4dfdRtWw'
    ADMIN_CHAT_ID = '7562559526'
    GROUP_CHAT_ID = 'YOUR_GROUP_CHAT_ID_HERE'
    
    # Orange Carrier Login Credentials
    ORANGE_EMAIL = 'anjaswmara@gmail.com'
    ORANGE_PASSWORD = 'AnjasWibowo122@'
    
    # URLs
    LOGIN_URL = 'https://www.orangecarrier.com/login'
    CALL_URL = 'https://www.orangecarrier.com/live/calls'
    BASE_URL = 'https://www.orangecarrier.com'
    
    # Cookies (paste your cookies here as Python list)
    ORANGE_COOKIES = [
        # Paste your cookies here in the same format
[
  {
    "domain": ".orangecarrier.com",
    "expirationDate": 1816656515.140008,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.894741238.1782096433"
  },
  {
    "domain": ".orangecarrier.com",
    "expirationDate": 1782182915,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_gid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.638929653.1782096433"
  },
  {
    "domain": ".orangecarrier.com",
    "expirationDate": 1789872517,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_fbp",
    "path": "/",
    "sameSite": "lax",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "fb.1.1782096433361.269817212868021665"
  },
  {
    "domain": ".orangecarrier.com",
    "expirationDate": 1782096575,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_gat_gtag_UA_191466370_1",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1"
  },
  {
    "domain": "www.orangecarrier.com",
    "expirationDate": 1782103716.423241,
    "hostOnly": true,
    "httpOnly": false,
    "name": "XSRF-TOKEN",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "eyJpdiI6IndBZXlGWlR1bGg2UWFFeE40TGQxSVE9PSIsInZhbHVlIjoicUtybGJVdGhuQU9QcnlnR2J6dzJwNkNydXE0REVYYVZYaHRxRm9BUktQY202NFBWZlh6SHhBQm9mM2JmeGhmU2JNRDRUQUlIRHhVZXZVcThKVXBocU5IclZwbnpDT2lvcXpqbjdMWGIySzRZTFFQQlh0VGt6NHdJSStzWFQ2NnUiLCJtYWMiOiI4ZmRlNTg4ZTFiYWU2ODRhNmJiM2FjNmY4YzA0MGQ1MWZiNmVlZGJmZTY1ZGI3MjExYzYxYmRkOWZmM2RiMzVlIn0%3D"
  },
  {
    "domain": "www.orangecarrier.com",
    "expirationDate": 1782103716.423353,
    "hostOnly": true,
    "httpOnly": true,
    "name": "orange_carrier_session",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "eyJpdiI6Im51eWJ2R2t1eWZSS0ZWNmREZ0lMYkE9PSIsInZhbHVlIjoiYTJLc2lrVTg3NlNOZlhXUGU3QktzOGZtZEMxY1dHWVdMRzl0cmVQcm5uVHVNdkZoTFE0TW5Vb0I3NGk4TUxuN3MrZWZDRklQclcxSVB5a0VmNHl5UzNiM3dzbk1jcktWTFFublBVd05OZDNpa3d6dXBQXC9rbDdEVnVuRGVBdndTIiwibWFjIjoiZmUyNDBiMTlhMzI1NzhmYmQyMzYwOTA5N2Q3ZTQyNmZkYWRiYThlMGE4YzdmYTY2NzNjNzkyNjgzZjM4MDMyYSJ9"
  },
  {
    "domain": ".orangecarrier.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "_gat_gtag_UA_191466370_1",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "1"
  }
]
    
    # Settings
    MAX_ERRORS = 10
    CHECK_INTERVAL = 5
