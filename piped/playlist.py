from typing import Union
from datetime import datetime

from .channel import Channel
from .stream import AudioStream, VideoStream, RelatedVideo
from . import fetcher
from . import exceptions


class Playlist:

    def __init__(self, id: str) -> None:

        try:
            data = fetcher.playlist_json(id)
        except Exception:
            raise exceptions.InvalidPlaylistIdError(f"The given playlist id '{id}' is invalid")
        
        self._json: dict = data
        self._id: str = id
        self._name: str = ""
        self._banner: str = ""
        self._nextpage: str = ""
        self._relatedStreams: list[RelatedVideo] = []
        self._thumbnail: str = ""
        self._uploader: str = ""
        self._uploaderAvatar: str = ""
        self._uploaderId: str = ""
        self._length: int = 0

    @property
    def json(self) -> dict:
        return self._json
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._json["name"]
    
    @property
    def banner(self) -> str:
        return self._json["bannerUrl"]
    
    @property
    def nextpage(self) -> str:
        return self._json["nextpage"]
    
    @property
    def related_videos(self) -> list[RelatedVideo]:
        r = []
        for i in self._json["relatedStreams"]:
            r.append(RelatedVideo(id=i["url"][9:],
                                  type=i["type"],
                                  title=i["title"],
                                  thumbnail=i["thumbnail"],
                                  uploaderName=i["uploaderName"],
                                  uploaderId=i["uploaderUrl"][9:],
                                  uploaderAvatar=i["uploaderAvatar"],
                                  uploadedDate=i["uploadedDate"],
                                  shortDescription=i["shortDescription"],
                                  duration=i["duration"],
                                  views=i["views"],
                                  uploaded=i["uploaded"],
                                  uploaderVerified=i["uploaderVerified"],
                                  isShort=i["isShort"]))
        return r
    
    @property
    def thumbnail(self) -> str:
        return self._json["thumbnailUrl"]
    
    @property
    def uploader_name(self) -> str:
        return self._json["uploader"]
    
    @property
    def uploader_id(self) -> str:
        return self._json["uploaderUrl"][9:]
    
    @property
    def uploader_avatar(self) -> str:
        return self._json["uploaderAvatar"]
    
    @property
    def length(self) -> int:
        return self._json["videos"]
