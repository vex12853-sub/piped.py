class UnexpectedError(Exception):
    def __init__(self, message="An unexpected error occurred") -> None:
        self.message = message
        super().__init__(self.message)


class FetchingTimeoutError(Exception):
    def __init__(self, message="The connection has timed out") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidIdError(Exception):
    def __init__(self, message="The given id is invalid") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidVideoIdError(InvalidIdError):
    def __init__(self, message="The given video id is invalid") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidChannelIdError(InvalidIdError):
    def __init__(self, message="The given channel id is invalid") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidPlaylistIdError(InvalidIdError):
    def __init__(self, message="The given playlist id is invalid") -> None:
        self.message = message
        super().__init__(self.message)


class DownloadFailedError(Exception):
    def __init__(self, message="Failed to download file") -> None:
        self.message = message
        super().__init__(self.message)
