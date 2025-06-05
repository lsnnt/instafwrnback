import requests

SESSIONID='<Your sessionid>'
XIGAPPID='<Your X-IG-App-ID>'
DSUSERID='<Your ds_user_id>'
hashmap={}
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
        hashmap[id["username"]]=0
    try:
        return response.json()["next_max_id"]
    except:
        return None
def getfollowings(next_max_id=""):
    url = "https://www.instagram.com/api/v1/friendships/"+DSUSERID+"/following/?count=25&max_id="+next_max_id+"&search_surface=follow_list_page"


    response = requests.request("GET", url, headers=headers)

    for id in response.json()["users"]:
        try:
            hashmap[id["username"]]+=1
        except KeyError as e:
            # print(e)
            print(id["username"])
    try:
        return response.json()["next_max_id"]
    except:
        return None
if __name__=='__main__':
    next_max = getfollowers()
    while next_max!=None:
        next_max=getfollowers(next_max_id=next_max)
    next_max = getfollowings()
    while next_max!=None:
        next_max=getfollowings(next_max_id=next_max)
