# instafwrnback
This repository cointains a useful tool by which you can see the the peoples on instagram whom you follow but they don't follow you back
# How to setup and Run

#### Clone the project
```
git clone https://github.com/lsnnt/instafwrnback && cd instafwrnback
```
#### Installing the dependencies
```
pip3 install -r requirements.txt
```

1) open instagram on web browser and open developer's tools by pressing (F12) or (fn+F12).
2) There in storage type you will find cookies and then in that you will find `ds_user_id` and `sessionid`
3) In networks tab filter it with `api` and then there you find a request in which in request headers you will find `X-IG-App-ID`.
<img width="499" alt="Screenshot 2025-06-05 at 10 19 43" src="https://github.com/user-attachments/assets/3764454f-463d-4b5b-935f-1ac64143f756" />
<img width="499" alt="Screenshot 2025-06-05 at 10 21 51" src="https://github.com/user-attachments/assets/6a9a3676-e5b9-4040-8e1f-37c70071221d" />

You will have to write all the above things in here

https://github.com/lsnnt/instafwrnback/blob/359e1afcbea23a9b65953166c6b476d20d6553e7/main.py#L3-L5



#### Running the program
```
python3 main.py
```

# Using Docker 🐳
#### Clone the repo and get into it
```
git clone https://github.com/lsnnt/instafwrnback && cd instafwrnback
```
#### Set variables in line 3-5

https://github.com/lsnnt/instafwrnback/blob/359e1afcbea23a9b65953166c6b476d20d6553e7/main.py#L3-L5

#### Build the Docker image
```
docker build -t instafwrnback .
```
#### Run the builded image
```
docker run --rm instafwrnback
```

