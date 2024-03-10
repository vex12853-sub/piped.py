import time

import requests

from . import exceptions

BASE_URL = "https://pipedapi.kavin.rocks/"

def measure_latency() -> float:

    try:
        start_time = time.time()

        res = requests.get(BASE_URL + "cdn-cgi/trace")

        if res.status_code == 504:
            raise exceptions.FetchingTimeoutError
        
        end_time = time.time()

        return end_time - start_time

    except requests.ConnectionError as e:
        raise e

def video_json(id: str) -> dict:

    url = BASE_URL + "streams/" + str(id)
    
    try:
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            return data
        
        elif res.status_code == 500:
            msg = res.json()["message"]
            raise exceptions.UnexpectedError(f"An unexpected error occurred: {msg}")
        
        elif res.status_code == 504:
            raise exceptions.FetchingTimeoutError
        
        else:
            raise exceptions.InvalidVideoIdError(f"The given video id '{id}' is invalid")

    except requests.HTTPError as e:
        raise e

def channel_json(id: str) -> dict:

    url = BASE_URL + "channel/" + str(id)

    try:
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            return data
        
        elif res.status_code == 504:
            raise exceptions.FetchingTimeoutError
        
        else:
            raise exceptions.InvalidChannelIdError(f"The given channel id '{id}' is invalid")
        
    except requests.HTTPError as e:
        raise e

def playlist_json(id: str) -> dict:

    url = BASE_URL + "playlist/" + str(id)

    try:
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            return data
        
        elif res.status_code == 504:
            raise exceptions.FetchingTimeoutError
        
        else:
            raise exceptions.InvalidPlaylistIdError(f"The given playlist id '{id}' is invalid")
        
    except requests.HTTPError as e:
        raise e
