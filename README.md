# vbi-music-app

Simple music player to manage the playlists 

### Setup

Create virtual environment
python3 -m venv venv

Activate virtual environment
source venv/bin/act	ivate

to deactivate:  ~deactivate

### Install dependencies

pip3 install -r requirements.txt

### To run locally

python3 main.py

### To Deploy to heroku

git push heroku branch-name
commit before deploying to heroku

### API list

Signup: **/signup** (method=POST) \
Login: **/login**   (method=POST) \
Logout: **/logout** (method=POST) \
Save playlist: **/api/playlists**  (method=POST) \
Fetch playlist: **/api/playlists** (method=GET) \
Delete Playlist:**/api/playlists** (method=PUT) \
Add Song To Playlist : **/api/playlists/song** (method=POST) \
Delete Song To Playlist: **/api/playlists/song** (method=PUT) \
fetch songs: **/api/songs** (method=GET)
