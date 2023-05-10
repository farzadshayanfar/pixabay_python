import enum

__all__ = ["QueryType", "ImageType", "VideoType", "Lang", "ImageOrientation", "Category", "ImageColor", "SortOrder"]


class QueryType(enum.Enum):
    IMAGE = ""
    VIDEO = "videos/"


class ImageType(enum.Enum):
    ALL = "all"
    PHOTO = "photo"
    ILLUSTRATION = "illustration"
    VECTOR = "vector"


class VideoType(enum.Enum):
    ALL = "all"
    FILM = "film"
    ANIMATION = "animation"


class Lang(enum.Enum):
    CZECH = "cs"
    DANISH = "da"
    German = "de"
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    INDONESIAN = "id"
    ITALIAN = "it"
    HUNGARIAN = "hu"
    DUTCH = "nl"
    NORWEGIAN = "no"
    POLISH = "pl"
    PORTUGUESE = "pt"
    ROMANIAN_MOLDAVIAN_MOLDOVAN = "ro"
    SLOVAK = "sk"
    FINNISH = "fi"
    SWEDISH = "sv"
    TURKISH = "tr"
    VIETNAMESE = "vi"
    THAI = "th"
    BULGARIAN = "bg"
    RUSSIAN = "ru"
    GREEK = "el"
    JAPANESE = "ja"
    KOREAN = "ko"
    CHINESE = "zh"


class ImageOrientation(enum.Enum):
    ALL = "all"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class Category(enum.Enum):
    BACKGROUNDS = "backgrounds"
    FASHION = "fashion"
    NATURE = "nature"
    SCIENCE = "science"
    EDUCATION = "education"
    FEELINGS = "feelings"
    HEALTH = "health"
    PEOPLE = "people"
    RELIGION = "religion"
    PLACES = "places"
    ANIMALS = "animals"
    INDUSTRY = "industry"
    COMPUTER = "computer"
    FOOD = "food"
    SPORTS = "sports"
    TRANSPORTATION = "transportation"
    TRAVEL = "travel"
    BUILDINGS = "buildings"
    BUSINESS = "business"
    MUSIC = "music"


class ImageColor(enum.Enum):
    GRAYSCALE = "grayscale"
    TRANSPARENT = "transparent"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    TURQUOISE = "turquoise"
    BLUE = "blue"
    LILAC = "lilac"
    PINK = "pink"
    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"
    BROWN = "brown"


class SortOrder(enum.Enum):
    POPULAR = "popular"
    LATEST = "latest"
