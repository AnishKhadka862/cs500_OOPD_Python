from enum import Enum

class CoverType(Enum):
    HARDCOVER = "HARDCOVER"
    PAPERBACK = "PAPERBACK"
    CLOTHCOVER = "CLOTHCOVER"

class FormatType(Enum):
    DVD = "DVD"
    BLU_RAY = "BLU_RAY"
    VCD = "VCD"

class PeriodicalType(Enum):
    JOURNAL = "JOURNAL"
    MAGAZINE = "MAGAZINE"
    NEWSPAPER = "NEWSPAPER"