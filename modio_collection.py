# Configure

OAuthToken = 'YourTokenHere'
ModListFile = 'Path/To/Mods.txt'
modioGameId = 'GameIdHere'

# Script

from urllib.request import urlopen
import requests
import math

try:
    skippedCount = 0
    subbedCount = 0

    listIsUrl = ModListFile.startswith('http://') or ModListFile.startswith('https://')
    if listIsUrl:
        modlist = urlopen(ModListFile)
    else:
        modlist = open(ModListFile)
    
    for line in modlist:
        if listIsUrl:
            modId = line.decode('utf-8').strip()
        else:
            modId = line.strip()
        print('Subscribing to', modId, '...')
        r = requests.post('https://api.mod.io/v1/games/' + modioGameId + '/mods/' + modId + '/subscribe', headers={'Authorization': 'Bearer ' + OAuthToken, 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'})
        if math.floor(r.status_code / 100) == 2:
            subbedCount += 1
            print('done')
        else:
            json = r.json()
            if r.status_code == 400 and json.get('error').get('error_ref') == 15004:
                skippedCount += 1
                print('Already subscribed, skipping...')
            else:
                if r.status_code == 401:
                    print('Create an OAuth2 token on the mod.io site')
                    print('Sign in, navigate to your profile, and click the "API Access" tab')
                    print('Under OAuth 2 Management > Generate Access Token, name your token and give it write access (read access is not needed) and click Create Token.')
                    print('Copy the provided token (it\'s huge) and paste it into the value of OAuthToken at the top of modio_collection.py, like so:')
                    print("OAuthToken = 'YOUR_TOKEN_HERE'")
                elif r.status_code == 404:
                    print('Either the mod or the game does not exist')
                    print('game:', modioGameId, '| mod:', modId)
                    print('You can check their pages with the following links:')
                    print('https://mod.io/search/id/games/' + modioGameId)
                    print('https://mod.io/search/id/mods/' + modId)
                else:
                    print(json)
                modlist.close()
                quit()
    
    print(' ')
    print('Success! Out of', subbedCount + skippedCount, 'mods: subbed to', subbedCount, 'new, skipped', skippedCount, 'old')
    modlist.close()
except FileNotFoundError:
    print('Could not find file: ' + ModListFile)
    print('Update modio_collection.py so that the value of ModListFile is the path to your mod list file, like so:')
    print("ModListFile = 'Path/To/Mods.txt'")