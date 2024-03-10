from typing import Union
from datetime import datetime

from .channel import Channel
from .stream import AudioStream, VideoStream, RelatedVideo
from . import fetcher
from . import exceptions


class Subtitle:

    def __init__(self,
                 url: str,
                 mimeType: str,
                 name: str,
                 code: str,
                 autoGenerated: bool) -> None:
        
        self.url: str = url
        self.mimeType: str = mimeType
        self.name: str = name
        self.code: str = code
        self.autoGenerated: bool = autoGenerated


class Chapter:

    def __init__(self,
                 title: str,
                 image: str,
                 start: int) -> None:
        
        self.title: str = title
        self.image: str = image
        self.start: int = start


class PreviewFrame:

    def __init__(self,
                 urls: list[str],
                 frameHeight: int,
                 frameWidth: int,
                 totalCount: int,
                 durationPerFrame: int,
                 framesPerPageX: int,
                 framesPerPageY: int) -> None:
        
        self.urls: list[str] = urls
        self.frameHeight: int = frameHeight
        self.frameWidth: int = frameWidth
        self.totalCount: int = totalCount
        self.durationPerFrame: int = durationPerFrame
        self.framesPerPageX: int = framesPerPageX
        self.framesPerPageY: int = framesPerPageY


class Video:

    def __init__(self, id: str) -> None:

        try:
            data = fetcher.video_json(id)
        except Exception:
            raise exceptions.InvalidVideoIdError(f"The given video id '{id}' is invalid")
        
        self._json: dict = data
        self._id: str = id
        self._title: str = ""
        self._description: str = ""
        self._uploadDate: str = ""
        self._uploader: str = ""
        self._uploaderId: str = ""
        self._uploaderAvatar: str = ""
        self._thumbnail: str = ""
        self._hls: str = ""
        self._dash: Union[None, str] = None
        self._lbryId: str = ""
        self._category: str = ""
        self._license: str =  ""
        self._visibility: str = ""
        self._tags: list[str] = []
        self._metaInfo: list = []
        self._uploaderVerified: bool = True
        self._duration: int = 0
        self._views: int = 0
        self._likes: int = 0
        self._dislikes: int = 0
        self._uploaderSubscriberCount: int = 0
        self._isLivestream: bool = False
        self._audioStreams: list[AudioStream] = []
        self._videoStreams: list[VideoStream] = []
        self._relatedVideos: list[RelatedVideo] = []
        self._subtitles: list[Subtitle] = []
        self._chapters: list[Chapter] = []
        self._previewFrames: list[PreviewFrame] = []

    @property
    def json(self) -> dict:
        return self._json

    @property
    def id(self) -> str:
        return self._id
        
    @property
    def title(self) -> str:
        return self._json["title"]
    
    @property
    def description(self) -> str:
        return self._json["description"]
    
    @property
    def upload_date(self) -> datetime:
        self._uploadDate = self._json["uploadDate"]
        return datetime.fromisoformat(self._uploadDate)
    
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
    def thumbnail(self) -> str:
        return self._json["thumbnail"]
    
    @property
    def hls(self) -> Union[None, str]:
        return self.json["hls"]
    
    @property
    def dash(self) -> Union[None, str]:
        return self._json["dash"]
    
    @property
    def lbry_id(self) -> Union[None, str]:
        return self._json["lbryId"]
    
    @property
    def category(self) -> str:
        return self._json["category"]
    
    @property
    def license(self) -> str:
        return self._json["license"]
    
    @property
    def visibility(self) -> str:
        return self._json["visibility"]
    
    @property
    def tags(self) -> list[str]:
        return self._json["tags"]
    
    @property
    def meta_info(self) -> list[str]:
        return self._json["metaInfo"]
    
    @property
    def uploader_verified(self) -> bool:
        return self._json["uploaderVerified"]
    
    @property
    def duration(self) -> int:
        return self._json["duration"]
    
    @property
    def views(self) -> int:
        return self._json["views"]
    
    @property
    def likes(self) -> int:
        return self._json["likes"]
    
    @property
    def dislikes(self) -> int:
        return self._json["dislikes"]
    
    @property
    def uploader_subscriber_count(self) -> int:
        return self._json["uploaderSubscriberCount"]
    
    @property
    def is_livestream(self) -> bool:
        return self._json["livestream"]
    
    @property
    def audio_streams(self) -> list[AudioStream]:
        r = []
        for i in self._json["audioStreams"]:
            r.append(AudioStream(bitrate=i["bitrate"],
                                codec=i["codec"],
                                format=i["format"],
                                indexStart=i["indexStart"],
                                indexEnd=i["indexEnd"],
                                initStart=i["initStart"],
                                initEnd=i["initEnd"],
                                mimeType=i["mimeType"],
                                quality=i["quality"],
                                url=i["url"],
                                videoOnly=i["videoOnly"],
                                itag=i["itag"],
                                contentLength=i["contentLength"]))
        return r
    
    @property
    def video_streams(self) -> list[VideoStream]:
        r = []
        for i in self._json["videoStreams"]:
            r.append(VideoStream(bitrate=i["bitrate"],
                                codec=i["codec"],
                                format=i["format"],
                                indexStart=i["indexStart"],
                                indexEnd=i["indexEnd"],
                                initStart=i["initStart"],
                                initEnd=i["initEnd"],
                                mimeType=i["mimeType"],
                                quality=i["quality"],
                                url=i["url"],
                                videoOnly=i["videoOnly"],
                                itag=i["itag"],
                                contentLength=i["contentLength"],
                                height=i["height"],
                                width=i["width"],
                                fps=i["fps"]))
        return r
    
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
    def subtitles(self) -> list[Subtitle]:
        r = []
        for i in self._json["subtitles"]:
            r.append(Subtitle(url=i["url"],
                              mimeType=i["mimeType"],
                              name=i["name"],
                              code=i["code"],
                              autoGenerated=i["autoGenerated"]))
        return r
    
    @property
    def chapters(self) -> list[Chapter]:
        r = []
        for i in self._json["chapters"]:
            r.append(Chapter(title=i["title"],
                             image=i["image"],
                             start=i["start"]))
        return r
    
    @property
    def prewiew_frames(self) -> list[PreviewFrame]:
        r = []
        for i in self._json["previewFrames"]:
            r.append(PreviewFrame(urls=i["urls"],
                                  frameHeight=i["frameHeight"],
                                  frameWidth=i["frameWidth"],
                                  totalCount=i["totalCount"],
                                  durationPerFrame=i["durationPerFrame"],
                                  framesPerPageX=i["framesPerPageX"],
                                  framesPerPageY=i["framesPerPageY"]))
        return r
    
    def fetch_author(self) -> Channel:
        id = str(self._json["uploaderUrl"][9:])
        return Channel(id=id)
