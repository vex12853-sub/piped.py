import json
from typing import Union
from datetime import datetime

from .stream import RelatedVideo
from . import fetcher
from . import exceptions


class Tab:

    def __init__(self, name: str, data: Union[str, dict]) -> None:
        self.name = name
        self.data = json.loads(data)


class Channel:

    def __init__(self, id: str) -> None:

        try:
            data = fetcher.channel_json(id)
        except Exception:
            raise exceptions.InvalidVideoIdError(f"The given channel id '{id}' is invalid")
        
        self._json: dict = data
        self._id: str = ""
        self._avatarUrl: str = ""
        self._bannerUrl: str = ""
        self._description: str = ""
        self._name: str = ""
        self._nextpage: dict = ""
        self._relatedStreams: list[RelatedVideo] = []
        self._subscriberCount: int = 0
        self._verified: bool = False
        self._tabs: list[Tab] = []

    @property
    def json(self) -> dict:
        return self._json
    
    @property
    def id(self) -> str:
        return self._json["id"]
    
    @property
    def avatar(self) -> str:
        return self._json["avatarUrl"]
    
    @property
    def banner(self) -> str:
        return self._json["bannerUrl"]
    
    @property
    def description(self) -> str:
        return self._json["description"]
    
    @property
    def name(self) -> str:
        return self._json["name"]
    
    @property
    def nextpage(self) -> dict:
        return json.loads(self._json["nextpage"])
    
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
    def subscriber_count(self) -> int:
        return self._json["subscriberCount"]
    
    @property
    def verified(self) -> bool:
        return self._json["verified"]
    
    @property
    def tabs(self) -> list[Tab]:
        r = []
        for i in self._json["tabs"]:
            r.append(Tab(name=i["name"],
                         data=i["data"]))
        return r
