import urllib3, discord

http = urllib3.PoolManager()
list = http.request("GET", "https://pomelo-check.onrender.com/list?stringify=y")

predecoded = list.data
usernames = predecoded.decode('UTF-8')

def handle_response(message) -> str:
    p_message = str(message.lower())

    if p_message[0] == '$':
        if p_message.find(" ") > 0:
            return "Spaces disallowed. Learn more: https://discord.com/blog/usernames"
        if p_message.isascii() != True:
            return "Non ASCII characters disallowed. Learn more: https://discord.com/blog/usernames"
        if len(p_message) >= 32:
            return "Exceeds 32 character limit. Learn more: https://discord.com/blog/usernames"
        if usernames.find(p_message.lstrip('$')) > 0:
            return "Your username has been taken!"
        else:
            return "Your username has not been taken!"