import requests

SESSIONID='<Your sessionid>'
XIGAPPID='<Your X-IG-App-ID>'
DSUSERID='<Your ds_user_id>'
follower_users=[]
following_but_not_follower_users=[]
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-IG-App-ID': XIGAPPID,
    'Cookie': 'sessionid='+SESSIONID+';ds_user_id='+DSUSERID+';',
    }
def getfollowers(next_max_id=""):
    url = "https://www.instagram.com/api/v1/friendships/"+DSUSERID+"/followers/?count=25&max_id="+next_max_id+"&search_surface=follow_list_page"
    # remove DsuerID on both sides and enter friends id to get the not following back
    

    response = requests.request("GET", url, headers=headers)

    for id in response.json()["users"]:
        follower_users.append(id["id"])
    if "next_max_id" in response.json():
        return getfollowers(response.json()["next_max_id"])
    else:
        print("Completed getting followers")
def getfollowings(next_max_id=""):
    url = "https://www.instagram.com/api/v1/friendships/"+DSUSERID+"/following/?count=25&max_id="+next_max_id+"&search_surface=follow_list_page"


    response = requests.request("GET", url, headers=headers)

    for id in response.json()["users"]:
        if id["id"] not in follower_users:
            following_but_not_follower_users.append(id["username"])
    if "next_max_id" in response.json():
        return getfollowings(response.json()["next_max_id"])
    else:
        print("Completed getting followings")
if __name__=='__main__':
    try:
        getfollowers()
        getfollowings()
        nnt = list(set(following_but_not_follower_users))
        for i in nnt:
            print(i)
        print(f"Found {len(nnt)} users not following you")
    except:
        print("Set the variables on line 3-5 correctly")
        exit(0)