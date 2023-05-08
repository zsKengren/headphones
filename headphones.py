import json

import requests
from requests.auth import HTTPBasicAuth, _basic_auth_str

from beets.plugins import BeetsPlugin
from beets import config

class Headphones(BeetsPlugin):
    def __init__(self):
        super(Headphones, self).__init__()

        config['headphones'].add({
            'host': 'hattp://localhost',
            'key': None,
            'username': None,
            'password': None
        })

        self.register_listener('import_task_files', self.listen_for_import_complete)
        #self.import_stages = [self.listen_for_import_complete]
    def listen_for_import_complete(self, session, task):
        host = config['headphones']['host'].get() 
        key = config['headphones']['key'].get()
        username = config['headphones']['username'].get() 
        password = config['headphones']['password'].get() 

        if not any({host, key, username, password}): 
            self._log.warning('Provide the Headphone host, api key, username, and password')
            return

        artist = None
        if task.is_album:
            if task.album is not None:
                artist = task.album['albumartist']
        
            url = host + '/api?cmd=getWanted&apikey=' + key 
            r = requests.get(url)
            if (r.status_code != 200):
                self._log.warning('Could not get wanted albums from Headphone')
            else:
                wanteds = json.loads(r.text)
                for wanted in wanteds:
                    if wanted['ArtistName'] == artist:
                        self.start_scan(wanted['ArtistID'], artist)
                        return
                    
            self._log.warning('Could not find artist in Headphones. Plase add the artist to Headphones before importing')

    def start_scan(self, artistid, artist):
        basic = HTTPBasicAuth(config['headphones']['username'].get(), config['headphones']['password'].get())
        url = config['headphones']['host'].get()  + '/scanArtist?ArtistID=' + artistid 
        requests.post(url, auth=basic)
        self._log.info('Notified Headhpones to update artist: ' + artist)
        
