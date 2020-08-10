from enum import Enum, unique


@unique
class XianMood(Enum):
    Imperial = "IMP"
    Reverential = "REV"
    Laudative = "LAUD"
    Neutral = "NEU"
    Familiar = "FAM"
    Pejorative = "PEJ"


@unique
class XianFormality(Enum):
    # Polite=...
    Casual = "Infm"
    SemiFormal = "Semi"  # Not in Universal Dependencies
    Formal = "Form"


@unique
class XianGender(Enum):
    # Gender=...
    Female = "Fem"
    Male = "Masc"


@unique
class XianSlang(Enum):
    # Style=...
    General = "Coll"
    Service = "Serv"  # Not in Universal Dependencies
