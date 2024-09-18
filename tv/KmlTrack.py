import json
from pathlib import Path
import numpy as np
import pandas as pd
import xmltodict

def save_dict(d, fn):
    p = Path(f'{fn}.json')
    with p.open(mode= "w", encoding='utf-8') as json_file:
        json.dump(d, json_file, indent=2)


# copy from https://laurentperrinet.github.io/sciblog/posts/2014-11-22-reading-kml-my-tracks-files-in-ipython.html
class KmlTrack():
    def __init__(self, data):
        kml_dict = xmltodict.parse(data)
        save_dict(kml_dict,'kml_dict')
        doc = kml_dict['kml']['Document']
        #keypoint_folder = doc['Folder']
        self.name = doc['name']
        self.author = doc['atom:author']['atom:name']
        Placemark = doc['Placemark']
        save_dict(Placemark,'Placemark')

        #self.tracks_type =  Placemark[1]['ExtendedData']['Data']['value']
        track = Placemark['gx:MultiTrack']['gx:Track']
        self.lon, self.lat, self.alt = [], [], []
        for when, where in zip(track['when'], track['gx:coord']):
            self.whens = pd.to_datetime(track['when'])
            for coord in track['gx:coord']:
                lon, lat, alt = coord.split(' ')
                self.lon.append(np.float64(lon))
                self.lat.append(np.float64(lat))
                self.alt.append(np.float64(alt))

#filename = '/tmp/test.kml'
#track =  KmlReader(filename)
