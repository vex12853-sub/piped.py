from typing import Union


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
