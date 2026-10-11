import requests

def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    dat = response.json()

    if dat["success"] and "data" in dat:
        user_data = dat["data"]
        user_name = user_data["login"]["username"]
        user_loc = user_data["location"]["country"]
        return user_name, user_loc
    else:
        raise Exception("failed to fetch user data")

def main():
    try:
        user_name, country = fetch_api()
        print(f"Username:{user_name},Country:{country}")
    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    main()