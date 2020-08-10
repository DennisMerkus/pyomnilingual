import re
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel


class Animacy(Enum):
    Anim = "Anim"
    Hum = "Hum"
    Inan = "Inan"
    Nhum = "Nhum"


class Aspect(Enum):
    Hab = "Hab"
    Imp = "Imp"
    Iter = "Iter"
    Perf = "Perf"
    Prog = "Prog"
    Prosp = "Prosp"


class Case(Enum):
    Abl = "Abl"
    Abs = "Abs"
    Acc = "Acc"
    Dat = "Dat"
    Erg = "Erg"
    Gen = "Gen"
    Loc = "Loc"
    Nom = "Nom"
    Voc = "Voc"


class Clusivity(Enum):
    Ex = "Ex"
    In = "In"


class Definite(Enum):
    Com = "Com"
    Cons = "Cons"
    Def = "Def"
    Ind = "Ind"
    Spec = "Spec"


class Gender(Enum):
    Com = "Com"
    Fem = "Fem"
    Masc = "Masc"
    Neut = "Neut"
    Both = "Both"


class Mood(Enum):
    Adm = "Adm"
    Cnd = "Cnd"
    Des = "Des"
    Imp = "Imp"
    Ind = "Ind"
    Jus = "Jus"
    Nec = "Nec"
    Opt = "Opt"
    Pot = "Pot"
    Prp = "Prp"
    Qot = "Qot"
    Sub = "Sub"


class Number(Enum):
    Coll = "Coll"
    Count = "Count"
    Dual = "Dual"
    Grpa = "Grpa"
    Grpl = "Grpl"
    Inv = "Inv"
    Pauc = "Pauc"
    Plur = "Plur"
    Ptan = "Ptan"
    Sing = "Sing"
    Tri = "Tri"


class NumForm(Enum):
    Word = "Word"
    Digit = "Digit"
    Roman = "Roman"
    Kanji = "Kanji"  # Not in UD


class NumType(Enum):
    Card = "Card"
    Dist = "Dist"
    Frac = "Frac"
    Mult = "Mult"
    Ord = "Ord"
    Range = "Range"
    Sets = "Sets"


class Person(Enum):
    Zero = "0"
    First = "1"
    Second = "2"
    Third = "3"
    Fourth = "4"


class Polarity(Enum):
    Neg = "Neg"
    Pos = "Pos"


class Poss(Enum):
    Yes = "Yes"


class PronType(Enum):
    Art = "Art"
    Dem = "Dem"
    Emp = "Emp"
    Exc = "Exc"
    Ind = "Ind"
    Int = "Int"
    Neg = "Neg"
    Prs = "Prs"
    Rcp = "Rcp"
    Rel = "Rel"
    Tot = "Tot"


class Tense(Enum):
    Fut = "Fut"
    Imp = "Imp"
    Past = "Past"
    Pqp = "Pqp"
    Pres = "Pres"


class VerbForm(Enum):
    Conv = "Conv"
    Fin = "Fin"
    Gdv = "Gdv"
    Ger = "Ger"
    Inf = "Inf"
    Part = "Part"
    Sup = "Sup"
    Vnoun = "Vnoun"


class Voice(Enum):
    Act = "Act"
    Antip = "Antip"
    Bfoc = "Bfoc"
    Cau = "Cau"
    Dir = "Dir"
    Inv = "Inv"
    Lfoc = "Lfoc"
    Mid = "Mid"
    Pass = "Pass"
    Rcp = "Rcp"


class Features(BaseModel):
    Animacy: Optional[Animacy]
    Aspect: Optional[Aspect]
    Case: Optional[Case]
    Definite: Optional[Definite]
    Gender: Optional[Gender]
    Mood: Optional[Mood]
    Number: Optional[Number]
    Person: Optional[Person]
    Polarity: Optional[Polarity]
    Poss: Optional[Poss]
    PronType: Optional[PronType]
    Tense: Optional[Tense]
    VerbForm: Optional[VerbForm]
    Voice: Optional[Voice]


FEATURE_REGEX = r"^(?P<pos>\w+)(__(?P<features>(\w+=\w+\|?)+))?$"


def parse_features(tag: str) -> Features:
    tag = tag.strip()

    if len(tag) == 0:
        return Features()

    match = re.match(FEATURE_REGEX, tag)

    if match is None:
        raise ValueError("Unexpected tag format %s" % (tag))

    if match.group("features") is None:
        return Features()

    pairs: List[str] = match.group("features").split("|")

    features: Dict[str, str] = {}

    for pair in pairs:
        feature, value = pair.split("=")

        features[feature] = value

    return Features(**features)
