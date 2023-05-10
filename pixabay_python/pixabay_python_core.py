import datetime
import json
import time
from pathlib import Path
from typing import Union, List, Iterator

import requests

from .pixabay_python_enums import *

__all__ = ["PixabayClient"]


class ImageQueryResult:
    def __init__(self, dataDict: dict):
        self._dataDict: dict = dataDict
        self._total: int = self._dataDict["total"]
        self._totalHits: int = self._dataDict["totalHits"]
        self._hits: Iterator[ImageHit] = (ImageHit(x) for x in self._dataDict["hits"])

    @property
    def data(self):
        return self._dataDict

    @property
    def total(self):
        return self._total

    @property
    def totalHits(self):
        return self._totalHits

    @property
    def hits(self):
        return self._hits


class ImageHit:
    def __init__(self, hitDict: dict):
        self._id: int = hitDict["id"]
        self._pageURL: str = hitDict["pageURL"]
        self._imageType: str = hitDict["type"]
        self._tags: List[str] = hitDict["tags"].split(", ")
        self._previewURL: str = hitDict["previewURL"]
        self._previewWidth: int = hitDict["previewWidth"]
        self._previewHeight: int = hitDict["previewHeight"]
        self._webformatURL: str = hitDict["webformatURL"]
        self._webformatWidth: int = hitDict["webformatWidth"]
        self._webformatHeight: int = hitDict["webformatHeight"]
        self._largeImageURL: str = hitDict["largeImageURL"]
        self._imageWidth: int = hitDict["imageWidth"]
        self._imageHeight: int = hitDict["imageHeight"]
        self._imageSize: int = hitDict["imageSize"]
        self._views: int = hitDict["views"]
        self._downloads: int = hitDict["downloads"]
        self._collections: int = hitDict["collections"]
        self._likes: int = hitDict["likes"]
        self._comments: int = hitDict["comments"]
        self._user_id: int = hitDict["user_id"]
        self._user: str = hitDict["user"]
        self._userImageURL: str = hitDict["userImageURL"]

    @property
    def id(self):
        return self._id

    @property
    def pageURL(self):
        return self._pageURL

    @property
    def imageType(self):
        return self._imageType

    @property
    def tags(self):
        return self._tags

    @property
    def previewURL(self):
        return self._previewURL

    @property
    def previewWidth(self):
        return self._previewWidth

    @property
    def previewHeight(self):
        return self._previewHeight

    @property
    def webformatURL(self):
        return self._webformatURL

    @property
    def webformatWidth(self):
        return self._webformatWidth

    @property
    def webformatHeight(self):
        return self._webformatHeight

    @property
    def largeImageURL(self):
        return self._largeImageURL

    @property
    def imageWidth(self):
        return self._imageWidth

    @property
    def imageHeight(self):
        return self._imageHeight

    @property
    def imageSize(self):
        return self._imageSize

    @property
    def views(self):
        return self._views

    @property
    def downloads(self):
        return self._downloads

    @property
    def collections(self):
        return self._collections

    @property
    def likes(self):
        return self._likes

    @property
    def comments(self):
        return self._comments

    @property
    def user_id(self):
        return self._user_id

    @property
    def user(self):
        return self._user

    @property
    def userImageURL(self):
        return self._userImageURL


class VideoQueryResult:
    def __init__(self, dataDict: dict):
        self._dataDict: dict = dataDict
        self._total: int = self._dataDict["total"]
        self._totalHits: int = self._dataDict["totalHits"]
        self._hits: Iterator[VideoHit] = (VideoHit(x) for x in self._dataDict["hits"])

    @property
    def data(self):
        return self._dataDict

    @property
    def total(self):
        return self._total

    @property
    def totalHits(self):
        return self._totalHits

    @property
    def hits(self):
        return self._hits


class VideoHit:
    def __init__(self, hitDict):
        self._id: int = hitDict["id"]
        self._pageURL: str = hitDict["pageURL"]
        self._videoType: str = hitDict["type"]
        self._tags: List[str] = hitDict["tags"].split(", ")
        self._duration: float = hitDict["duration"]
        self._picture_id: str = hitDict["picture_id"]
        self._videos: dict = hitDict["videos"]
        self._large: VideoSizeVariant = VideoSizeVariant(self._videos["large"])
        self._medium: VideoSizeVariant = VideoSizeVariant(self._videos["medium"])
        self._small: VideoSizeVariant = VideoSizeVariant(self._videos["small"])
        self._tiny: VideoSizeVariant = VideoSizeVariant(self._videos["tiny"])
        self._views: int = hitDict["views"]
        self._downloads: int = hitDict["downloads"]
        self._likes: int = hitDict["likes"]
        self._comments: int = hitDict["comments"]
        self._user_id: int = hitDict["user_id"]
        self._user: str = hitDict["user"]
        self._userImageURL: str = hitDict["userImageURL"]

    @property
    def id(self):
        return self._id

    @property
    def pageURL(self):
        return self._pageURL

    @property
    def videoType(self):
        return self._videoType

    @property
    def tags(self):
        return self._tags

    @property
    def duration(self):
        return self._duration

    @property
    def picture_id(self):
        return self._picture_id

    @property
    def videos(self):
        return self._videos

    @property
    def large(self):
        return self._large

    @property
    def medium(self):
        return self._medium

    @property
    def small(self):
        return self._small

    @property
    def tiny(self):
        return self._tiny

    @property
    def views(self):
        return self._views

    @property
    def downloads(self):
        return self._downloads

    @property
    def likes(self):
        return self._likes

    @property
    def comments(self):
        return self._comments

    @property
    def user_id(self):
        return self._user_id

    @property
    def user(self):
        return self._user

    @property
    def userImageURL(self):
        return self._userImageURL


class VideoSizeVariant:
    def __init__(self, aDict: dict):
        self._url: str = aDict["url"]
        self._width: int = aDict["width"]
        self._height: int = aDict["height"]
        self._size: int = aDict["size"]

    @property
    def url(self):
        return self._url

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return self._size


class PixabayClient:
    """
    
    """
    url: str = "https://pixabay.com/api/"
    defaultRequestPerMinLimit: int = 100
    defaultCacheDirPath: Path = Path.home().joinpath(".cache/pixabaypy")
    defaultCacheFileName: str = "pixabayRequestCache.json"

    def __init__(self,
                 apiKey: Union[None, str] = None,
                 requestLimitPerMin: int = defaultRequestPerMinLimit,
                 cacheDirPath: Union[str, Path] = defaultCacheDirPath,
                 cacheFileName: str = defaultCacheFileName):

        self._requestLimitPerMin: int = requestLimitPerMin
        self._remainingRequests: int = self._requestLimitPerMin
        self._remainingTimeToReset: float = 1

        # setting up or retriveing of the cache directory and cache history
        self._cacheDirPath: Path = Path(cacheDirPath)
        if not cacheFileName.endswith(".json"):
            cacheFileName += ".json"
        self._cacheFilePath = self._cacheDirPath.joinpath(cacheFileName)
        self._cacheDirPath.mkdir(parents=True, exist_ok=True)
        self._cacheFilePath.touch(exist_ok=True)
        contents = self._cacheFilePath.read_text(encoding="utf-8")
        self._requestCache: dict = dict() if contents == str() else json.loads(contents)

        # setting and/or retrieving apikey
        apiKeyFileName: str = "pixabayKey.txt"
        apiKeyFilePath: Path = self._cacheDirPath.joinpath(apiKeyFileName)
        if apiKey is not None:
            self._key = apiKey
            apiKeyFilePath.write_text(apiKey, encoding="utf-8")
        else:
            if apiKeyFilePath.exists():
                self._key: str = apiKeyFilePath.read_text(encoding="utf-8")
            else:
                raise FileNotFoundError("Couldn't find the file for pixabay api key in cache directory!\n" + \
                                        "Please make sure set your api key by inputting it to PixelClient\n" + \
                                        "(you only need to do this once)")

    def saveRequestCache(self):
        jstring = json.dumps(self._requestCache, ensure_ascii=False, indent=4)
        self._cacheFilePath.write_text(data=jstring, encoding="utf-8")

    def createQueryString(self,
                          q: str,
                          qtype: QueryType = QueryType.IMAGE,
                          imageType: ImageType = ImageType.ALL,
                          videoType: VideoType = VideoType.ALL,
                          lang: Lang = Lang.ENGLISH,
                          orientation: ImageOrientation = ImageOrientation.ALL,
                          category: Union[Category, None] = None,
                          minWidth: int = 0,
                          minHeight: int = 0,
                          colors: Union[ImageColor, List[ImageColor], None] = None,
                          editorsChoice: bool = False,
                          safeSearch: bool = False,
                          order: Union[str, SortOrder] = SortOrder.POPULAR,
                          page: int = 1,
                          perPage: int = 20,
                          pretty: bool = False) -> str:

        assert page > 0 and 3 <= perPage <= 200

        q = q.replace(" ", "+")

        qstring = f"{PixabayClient.url}{qtype.value}?key={self._key}" \
                  f"&q={q}&lang={lang.value}" \
                  f"&min_width={minWidth}&min_height={minHeight}" \
                  f"&editors_choice={editorsChoice}&safe_search={safeSearch}" \
                  f"&order={order.value}&pretty={pretty}&page={page}&per_page={perPage}"

        if category:
            qstring += f"&category={category.value}"

        if qtype == QueryType.IMAGE:
            qstring += f"&image_type={imageType.value}"
            if colors:
                qstring += f"&colors={','.join([str(color.value) for color in colors])}"
            if orientation:
                qstring += f"&orientation={orientation.value}"
        else:
            qstring += f"&video_type={videoType.value}"

        return qstring

    def makeQuery(self, query: str, connectTimeout: float, readTimeout: float) -> requests.Response:
        try:
            if self._remainingRequests > 0:
                res = requests.get(url=query,
                                   verify=True,
                                   timeout=(connectTimeout, readTimeout))
                res.raise_for_status()
                return res
            else:
                self.waitToReset()
                self.makeQuery(query=query,
                               connectTimeout=connectTimeout,
                               readTimeout=readTimeout)
        except requests.ConnectTimeout as err:
            print(err)
        except requests.ReadTimeout as err:
            print(err)
        except requests.HTTPError as err:
            print(err)
        except Exception as err:
            print(err)
        finally:
            self._remainingRequests -= 1

    def searchImage(self,
                    q: str,
                    imageType: ImageType = ImageType.ALL,
                    lang: Lang = Lang.ENGLISH,
                    orientation: ImageOrientation = ImageOrientation.ALL,
                    category: Union[Category, None] = None,
                    minWidth: Union[int, None] = None,
                    minHeight: Union[int, None] = None,
                    colors: Union[ImageColor, List[ImageColor], None] = None,
                    editorsChoice: bool = False,
                    safeSearch: bool = False,
                    order: Union[str, SortOrder] = SortOrder.POPULAR,
                    page: int = 1,
                    perPage: int = 20,
                    pretty: bool = False,
                    connectTimeout: float = 10,
                    readTimeout: float = 20) -> ImageQueryResult:

        qstring = self.createQueryString(q=q, qtype=QueryType.IMAGE, imageType=imageType, lang=lang,
                                         orientation=orientation, category=category, minWidth=minWidth,
                                         minHeight=minHeight, colors=colors, editorsChoice=editorsChoice,
                                         safeSearch=safeSearch, order=order, page=page, perPage=perPage,
                                         pretty=pretty)

        if qstring in self._requestCache.keys():
            thenString = self._requestCache[qstring]["t"]
            then = datetime.datetime.strptime(thenString, "%Y-%m-%d %H:%M:%S")
            now = datetime.datetime.now()
            delta = now - then
            if delta.days >= 1:
                del self._requestCache[qstring]
            dataDict = self._requestCache[qstring]["dataDict"]
            print(f"used cached result for this image query: \"{q}\"")
            return ImageQueryResult(dataDict=dataDict)

        resp = self.makeQuery(query=qstring, connectTimeout=connectTimeout, readTimeout=readTimeout)
        res = ImageQueryResult(dataDict=resp.json())
        now = datetime.datetime.now()
        now = now.replace(microsecond=0)
        self._requestCache[qstring] = dict(q=q, qtype="Image", t=str(now), dataDict=resp.json())
        self.saveRequestCache()

        return res

    def searchVideo(self,
                    q: str,
                    videoType: VideoType = VideoType.ALL,
                    lang: Lang = Lang.ENGLISH,
                    category: Union[Category, None] = None,
                    minWidth: Union[int, None] = None,
                    minHeight: Union[int, None] = None,
                    editorsChoice: bool = False,
                    safeSearch: bool = False,
                    order: Union[str, SortOrder] = SortOrder.POPULAR,
                    page: int = 1,
                    perPage: int = 20,
                    pretty: bool = False,
                    connectTimeout: float = 10,
                    readTimeout: float = 20) -> VideoQueryResult:

        qstring = self.createQueryString(q=q, qtype=QueryType.VIDEO, videoType=videoType, lang=lang,
                                         category=category, minWidth=minWidth, minHeight=minHeight,
                                         editorsChoice=editorsChoice, safeSearch=safeSearch, order=order,
                                         page=page, perPage=perPage, pretty=pretty)

        if qstring in self._requestCache.keys():
            thenString = self._requestCache[qstring]["t"]
            then = datetime.datetime.strptime(thenString, "%Y-%m-%d %H:%M:%S")
            now = datetime.datetime.now()
            delta = now - then
            if delta.days >= 1:
                del self._requestCache[qstring]
            dataDict = self._requestCache[qstring]["dataDict"]
            print(f"used cached result for this video query: \"{q}\"")
            return VideoQueryResult(dataDict=dataDict)

        resp = self.makeQuery(query=qstring, connectTimeout=connectTimeout, readTimeout=readTimeout)
        res = VideoQueryResult(dataDict=resp.json())
        now = datetime.datetime.now()
        now = now.replace(microsecond=0)
        self._requestCache[qstring] = dict(q=q, qtype="Video", t=str(now), dataDict=resp.json())
        self.saveRequestCache()

        return res

    def waitToReset(self):
        t = 0
        while t < 60:
            print(f"\rwaiting for 60 secs:\t{t}", end='')
            time.sleep(1)
            t += 1
        self._remainingRequests = self._requestLimitPerMin
