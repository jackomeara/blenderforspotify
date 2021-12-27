import requests
from base64 import b64encode

from spotiblend.settings import CLIENT_ID, CLIENT_SECRET

class User_Request():
    def authenticate(self, authcode):
        auth_header = b64encode(str('%s:%s' % (CLIENT_ID, CLIENT_SECRET)).encode('ascii'))
        headers = {'Authorization': 'Basic %s' % auth_header.decode('ascii'), 'Content-Type':'application/x-www-form-urlencoded'}
        response = requests.post('https://accounts.spotify.com/api/token?grant_type=authorization_code&code=%s&redirect_uri=http://localhost:8000/callback' % authcode, headers=headers)
        authtoken = response.json()['access_token']
        return authtoken
        
    def getsongid(self, track):
        params={'limit':'1'}
        response = requests.get('https://api.spotify.com/v1/search?q=%s&type=track' % track, headers=self._headers, params=params)
        return response.json()['tracks']['items'][0]['id']

    def getids(self, list, type, headers):
        id_list = [self.getid(type, track, headers) for track in list]
        return id_list

    def getid(self, type, name, headers):
        '''
        return spotify track ID of top result of query name. type should be 'track' or 'artist', headers are http req headers
        '''
        params={'limit':'1'}
        response = requests.get('https://api.spotify.com/v1/search?q=%s&type=%s' % (name,type), headers=headers, params=params)
        rj = response.json()
        return response.json()['%ss' % type]['items'][0]['id']

    def getrecommendations(self, artists, tracks, genres, limit, headers):
        '''
        get track recommendations (given as a list of track ids), from seed artists, tracks and genres (as string if len=1 or list if len>2). 
        Max total seeds=5. limit = quant of recs, headers are http req headers -> authorization token + content type 
        '''

        #Convert Artists and Tracks from text to IDs
        if type(artists) == list:
            artistids = [self.getid('artist', artist, headers) if type(artists)==list else self.getid('artist', artist, headers) for artist in artists]
        else:
            artistids = self.getid('artist', artists, headers)
        if type(tracks) == list:
            trackids = [self.getids('track', track, headers) for track in tracks]
        else:
            trackids = self.getid('track', tracks, headers)

        #Convert Lists to comma-separated strings for url
        params = list([artistids, trackids, genres])
        for i, category in enumerate(params):
            if type(params[i]) == list:
                params[i] = str(params[i])
                params[i] = params[i].replace("'", "")
                params[i] = params[i].replace("[", "")
                params[i] = params[i].replace("]", "")
                params[i] = params[i].replace(" ", "")

        #Send GET request to retrieve recommendations
        url = 'https://api.spotify.com/v1/recommendations?limit=%s&seed_artists=%s&seed_genre=%s&seed_tracks=%s'% (str(limit), artistids, genres, trackids)
        response = requests.get('https://api.spotify.com/v1/recommendations?limit=%s&seed_artists=%s&seed_genre=%s&seed_tracks=%s'
                                 % (str(limit), params[0], params[2], params[1]), headers=headers)
        
        #Extract just IDs from response and return them
        rawtracks = response.json()['tracks']
        tracks = []
        for track in rawtracks:
            tracks.append(track['id'])
        return tracks

        #NEED TO DEAL WITH LIMIT > 100 

    def createplaylist(self, songs, desc, name, headers):
        '''
        create playlist in authorised user's library given name, description and songs [list of ids], headers=http req headers.
        '''

        #Get basic data for request and make it
        data = '{"name":"'+name+'","description":"'+desc+'","public":false}'
        userid = requests.get('https://api.spotify.com/v1/me', headers=headers).json()['id']
        response = requests.post('https://api.spotify.com/v1/users/%s/playlists' % userid, headers=headers, data=data)
        playlistid  = response.json()['id']
        
        #Convert Song IDs to URIs
        urisongs =''
        for song in songs:
            urisongs += 'spotify:track:'+song+','
        urisongs=urisongs[:-1]

        #Send POST request to add songs
        response = requests.post('https://api.spotify.com/v1/playlists/%s/tracks?uris=%s' % (playlistid, urisongs), headers=headers)


        #NEED TO DEAL WITH len(songs) > 100
