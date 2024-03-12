import mimetypes
from io import BytesIO, FileIO
from typing import Union

import requests

from .exceptions import DownloadFailedError
from .video import Video


class Stream:

    def __init__(self,
                 bitrate: int,
                 codec: str,
                 format: str,
                 indexStart: int,
                 indexEnd: int,
                 initStart: int,
                 initEnd: int,
                 mimeType: str,
                 quality: str,
                 url: str,
                 videoOnly: bool,
                 itag: int,
                 contentLength: int) -> None:
        self.bitrate: int = bitrate
        self.codec: str = codec
        self.format: str = format
        self.indexStart: int = indexStart
        self.indexEnd: int = indexEnd
        self.initStart: int = initStart
        self.initEnd: int = initEnd
        self.mimeType: str = mimeType
        self.quality: str = quality
        self.url: str = url
        self.vidoOnly: bool = videoOnly
        self.itag: int = itag
        self.contentLength: int = contentLength

    @classmethod
    def fetch_bytes(self) -> BytesIO:
        try:
            r = requests.get(self.url)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            raise requests.exceptions.RequestException(f"Error fetching file from URL: {self.url}")
        return BytesIO(r.content)
    
    @classmethod
    def fetch_file(self) -> FileIO:
        try:
            r = requests.get(self.url)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            raise requests.exceptions.RequestException(f"Error fetching file from URL: {self.url}")
        return FileIO(BytesIO(r.content), mode='rb')
    
    @classmethod
    def download(self, path: str = "", extension: str | None = None) -> None:
        try:
            r = requests.head(self.url)
            r.raise_for_status()
            content_type = r.headers.get('content-type')
            ext = mimetypes.guess_extension(content_type, strict=False) or '.txt' if not extension else extension
            with open(f"{path if path else self.url.split('/')[-1]}", 'wb') as f:
                f.write(r.content)
        except Exception as e:
            raise DownloadFailedError(f"Failed to download file: {e}")


class AudioStream(Stream):

    def __init__(self,
                 bitrate: int,
                 codec: str,
                 format: str,
                 indexStart: int,
                 indexEnd: int,
                 initStart: int,
                 initEnd: int,
                 mimeType: str,
                 quality: str,
                 url: str,
                 videoOnly: bool,
                 itag: int,
                 contentLength: int) -> None:
        
        super().__init__(bitrate,
                         codec,
                         format,
                         indexStart,
                         indexEnd,
                         initStart,
                         initEnd,
                         mimeType,
                         quality,
                         url,
                         videoOnly,
                         itag,
                         contentLength)


class VideoStream(Stream):

    def __init__(self,
                 bitrate: int,
                 codec: str,
                 format: str,
                 indexStart: int,
                 indexEnd: int,
                 initStart: int,
                 initEnd: int,
                 mimeType: str,
                 quality: str,
                 url: str,
                 videoOnly: bool,
                 itag: int,
                 fps: int,
                 height: int,
                 width: int,
                 contentLength: int) -> None:
        
        super().__init__(bitrate,
                         codec,
                         format,
                         indexStart,
                         indexEnd,
                         initStart,
                         initEnd,
                         mimeType,
                         quality,
                         url,
                         videoOnly,
                         itag,
                         contentLength)

        self.fps: int = fps
        self.height: int = height
        self.width: int = width


class RelatedVideo:

    def __init__(self,
                 id: str,
                 type: str,
                 title: str,
                 thumbnail: str,
                 uploaderName: str,
                 uploaderId: str,
                 uploaderAvatar: str,
                 uploadedDate: str,
                 shortDescription: Union[None, str],
                 duration: int,
                 views: int,
                 uploaded: int,
                 uploaderVerified: bool,
                 isShort: bool) -> None:
        
        self.id: int = id
        self.type: str = type
        self.title: str = title
        self.thumbnail: str = thumbnail
        self.uploaderName: str = uploaderName
        self.uploaderId: str = uploaderId
        self.uploaderAvatar: str = uploaderAvatar
        self.uploadedDate: str = uploadedDate
        self.shortDescription: Union[None, str] = shortDescription
        self.duration: int = duration
        self.views: int = views
        self.uploaded: int = uploaded
        self.uploaderVerified: bool = uploaderVerified
        self.isShort: bool = isShort

    @classmethod
    def convert_video(self) -> Video:
        return Video(self.id)
