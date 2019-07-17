cookies = []

def cookie_offer(user):
    print("caught cookie_offer")
    if user not in cookies:
        cookies.append(user)
        return user + " has a cookie to give away!"
    else:
        return user + "! You already told me you have a cookie to give away!"

def cookie_query(user):
    print("caught cookie_query")
    return "There are " + len(cookies) + " cookies posted!"

def cookie_beg(user):
    print("caught cookie_beg")
    return user + "is begging for your cookie!"

commands = {
    "cookie offer": cookie_offer,
    "cookie query": cookie_query,
    "cookie beg": cookie_beg,
}
