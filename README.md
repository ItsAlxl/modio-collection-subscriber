# mod.io Collection Subscriber
A simple python script that batch subscribes to mod.io mods in a given mod collection list.

## Dependencies

You will need [Python 3.5+](https://www.python.org/downloads/) and pip. You also need to install `requests`:
```bash
pip install requests
# or
python -m pip install requests
```
After configuring properly (see below), simply run the script:
```bash
py modio_collection.py
```

## Configuration

Configuration of the script is done near the top of the script file itself. Modify modio_collection.py with any text editor to include your OAuth 2 token (see below), the location of the modlist (which can be a URL), and the mod.io ID of the relevant game (see below).

```py
# Configure

OAuthToken = 'YourTokenHere'
ModListFile = 'Path/To/Mods.txt'
modioGameId = 'GameIdHere'
```

## Getting a mod.io OAuth 2 Token

You will need to create an OAuth 2 token on the mod.io site for this script to work. Sign in, navigate to your profile, and click the "API Access" tab on the left. Under OAuth 2 Management > Generate Access Token, name your token and give it write access (read access is not needed) and click Create Token. Copy the provided token (it's huge) and paste it into the value of OAuthToken at the top of modio_collection.py, like so:
```py
OAuthToken = 'YOUR_TOKEN_HERE'
```

## The Mod List

The modlist file is simply a text file with a mod's ID on each line. You can find a mod's ID at the top of the mod's page.
```
mod_id_one
mod_id_two
mod_id_three
```


## Finding a mod.io Game ID

As far as I can tell, there is no simple way to find a game's ID.

If the game ID has not been supplied to you, you can find the game ID of a given game using mod.io's API (you can [find the full API docs here](https://docs.mod.io/#getting-started)). In order to find the game ID, we will be using the [/games](https://docs.mod.io/#games) endpoint. First, you'll need an API key: in the same place as where you got the OAuth 2 token, you can request an API key. Then, go to the following address in your web browser:
```
https://api.mod.io/v1/games?api_key=YOUR_API_KEY_HERE&_q=
```
Make sure to replace YOUR_API_KEY_HERE with your actual API from your account. The _q argument at the end of the URL is a simple text filter to make it easier to find the relevant information; for example, I used _q=ins to find the Insurgency: Sandstorm ID. You can remove it or leave it blank for the full list of games on mod.io.

The reponse from the /games endpoint is a JSON object containing an array of games. Within each game, there is an "id" field that contains the ID value that we want. You can verify the ID by going to https://mod.io/search/id/games/FOUND_ID_VALUE and ensuring that it leads to the correct game page.