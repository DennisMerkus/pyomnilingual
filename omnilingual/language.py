from __future__ import annotations

import re
from enum import Enum, auto
from typing import Dict, List, Optional

from pydantic import BaseModel

from .iso.iso_3 import Code as LanguageCode


class LanguageScope(Enum):
    Individual = auto()
    Macro = auto()


class LanguageType(Enum):
    Living = auto()
    Extinct = auto()
    Ancient = auto()
    Historical = auto()
    Constructed = auto()


class LanguageFamily(BaseModel):
    name: str  # ISO language name

    iso_1: Optional[str]  # ISO 639-1 code
    iso_1_deprecated: Optional[str]
    iso_2_T: Optional[str]
    iso_2_B: Optional[str]
    iso_3: Optional[str]  # ISO 639-3 code

    code: LanguageCode

    scope: Optional[LanguageScope]
    type: Optional[LanguageType]


Undetermined = LanguageFamily(
    name="Undetermined", iso_1="un", iso_3="und", code=LanguageCode.Undetermined,
)


languages = [
    LanguageFamily(
        name="Abkhazian", iso_1="ab", iso_3="abk", code=LanguageCode.Abkhazian
    ),
    LanguageFamily(name="Afar", iso_1="aa", iso_3="aar", code=LanguageCode.Afar),
    LanguageFamily(
        name="Afrikaans", iso_1="af", iso_3="afr", code=LanguageCode.Afrikaans
    ),
    LanguageFamily(
        name="Ainu (Japan)",
        iso_3="ain",
        scope=LanguageScope.Individual,
        type=LanguageType.Living,
        code=LanguageCode.Ainu,
    ),
    LanguageFamily(name="Akan", iso_1="ak", iso_3="aka", code=LanguageCode.Akan),
    LanguageFamily(
        name="Albanian",
        iso_1="sq",
        iso_2_B="alb",
        iso_3="sqi",
        code=LanguageCode.Albanian,
    ),
    LanguageFamily(name="Amharic", iso_1="am", iso_3="amh", code=LanguageCode.Amharic),
    LanguageFamily(name="Arabic", iso_1="ar", iso_3="ara", code=LanguageCode.Arabic),
    LanguageFamily(
        name="Aragonese", iso_1="an", iso_3="arg", code=LanguageCode.Aragonese
    ),
    LanguageFamily(
        name="Armenian",
        iso_1="hy",
        iso_2_B="arm",
        iso_3="hye",
        code=LanguageCode.Armenian,
    ),
    LanguageFamily(
        name="Assamese", iso_1="as", iso_3="asm", code=LanguageCode.Assamese
    ),
    LanguageFamily(name="Avaric", iso_1="av", iso_3="ava", code=LanguageCode.Avaric),
    LanguageFamily(name="Aymara", iso_1="ay", iso_3="aym", code=LanguageCode.Aymara),
    LanguageFamily(
        name="Azerbaijani", iso_1="az", iso_3="aze", code=LanguageCode.Azerbaijani,
    ),
    LanguageFamily(name="Bashkir", iso_1="ba", iso_3="bak", code=LanguageCode.Bashkir),
    LanguageFamily(
        name="Basque", iso_1="eu", iso_2_B="baq", iso_3="eus", code=LanguageCode.Basque,
    ),
    LanguageFamily(
        name="Belarusian", iso_1="be", iso_3="bel", code=LanguageCode.Belarusian
    ),
    LanguageFamily(name="Bengali", iso_1="bn", iso_3="ben", code=LanguageCode.Bengali),
    LanguageFamily(name="Bihari", iso_1="bh", iso_3="bih", code=LanguageCode.Bihari),
    LanguageFamily(name="Bislama", iso_1="bi", iso_3="bis", code=LanguageCode.Bislama),
    LanguageFamily(name="Bosnian", iso_1="bs", iso_3="bos", code=LanguageCode.Bosnian),
    LanguageFamily(name="Breton", iso_1="br", iso_3="bre", code=LanguageCode.Breton),
    LanguageFamily(
        name="Bulgarian", iso_1="bg", iso_3="bul", code=LanguageCode.Bulgarian
    ),
    LanguageFamily(
        name="Burmese",
        iso_1="my",
        iso_2_B="bur",
        iso_3="mya",
        code=LanguageCode.Burmese,
    ),
    LanguageFamily(name="Catalan", iso_1="ca", iso_3="cat", code=LanguageCode.Catalan),
    LanguageFamily(name="Cebuano", iso_3="ceb", code=LanguageCode.Cebuano),
    LanguageFamily(name="Cherokee", iso_3="chr", code=LanguageCode.Cherokee),
    LanguageFamily(
        name="Chinese",
        iso_1="zh",
        iso_2_B="chi",
        iso_3="zho",
        code=LanguageCode.Chinese,
    ),
    LanguageFamily(
        name="Corsican", iso_1="co", iso_3="cos", code=LanguageCode.Corsican
    ),
    LanguageFamily(
        name="Croatian", iso_1="hr", iso_3="hrv", code=LanguageCode.Croatian
    ),
    LanguageFamily(
        name="Czech", iso_1="cs", iso_2_B="cze", iso_3="ces", code=LanguageCode.Czech,
    ),
    LanguageFamily(name="Danish", iso_1="da", iso_3="dan", code=LanguageCode.Danish),
    LanguageFamily(name="Dhivehi", iso_1="dv", iso_3="div", code=LanguageCode.Dhivehi),
    LanguageFamily(
        name="Dutch", iso_1="nl", iso_2_B="dut", iso_3="nld", code=LanguageCode.Dutch,
    ),
    LanguageFamily(
        name="Dzongkha", iso_1="dz", iso_3="dzo", code=LanguageCode.Dzongkha
    ),
    LanguageFamily(name="English", iso_1="en", iso_3="eng", code=LanguageCode.English),
    LanguageFamily(
        name="Esperanto",
        iso_1="eo",
        iso_3="epo",
        code=LanguageCode.Esperanto,
        type=LanguageType.Constructed,
    ),
    LanguageFamily(
        name="Estonian", iso_1="et", iso_3="est", code=LanguageCode.Estonian
    ),
    LanguageFamily(name="Ewe", iso_1="ee", iso_3="ewe", code=LanguageCode.Ewe),
    LanguageFamily(name="Faroese", iso_1="fo", iso_3="fao", code=LanguageCode.Faroese),
    LanguageFamily(name="Fijian", iso_1="fj", iso_3="fij", code=LanguageCode.Fijian),
    LanguageFamily(name="Finnish", iso_1="fi", iso_3="fin", code=LanguageCode.Finnish),
    LanguageFamily(
        name="French", iso_1="fr", iso_2_B="fre", iso_3="fra", code=LanguageCode.French,
    ),
    LanguageFamily(
        name="Western Frisian",
        iso_1="fy",
        iso_3="fry",
        code=LanguageCode.WesternFrisian,
    ),
    LanguageFamily(name="Ga", iso_1=None, iso_3="gaa", code=LanguageCode.Ga),
    LanguageFamily(
        name="Galician", iso_1="gl", iso_3="glg", code=LanguageCode.Galician
    ),
    LanguageFamily(name="Ganda", iso_1="lg", iso_3="lug", code=LanguageCode.Ganda),
    LanguageFamily(
        name="Georgian",
        iso_1="ka",
        iso_2_B="geo",
        iso_3="kat",
        code=LanguageCode.Georgian,
    ),
    LanguageFamily(
        name="German", iso_1="de", iso_2_B="ger", iso_3="deu", code=LanguageCode.German,
    ),
    LanguageFamily(
        name="Greenlandic", iso_1="kl", iso_3="kal", code=LanguageCode.Greenlandic,
    ),
    LanguageFamily(name="Guarani", iso_1="gn", iso_3="grn", code=LanguageCode.Guarani),
    LanguageFamily(
        name="Gujarati", iso_1="gu", iso_3="guj", code=LanguageCode.Gujarati
    ),
    LanguageFamily(
        name="Haitian Creole", iso_1="ht", iso_3="hat", code=LanguageCode.HaitianCreole,
    ),
    LanguageFamily(name="Hausa", iso_1="ha", iso_3="hau", code=LanguageCode.Hausa),
    LanguageFamily(
        name="Hawaiian", iso_1=None, iso_3="haw", code=LanguageCode.Hawaiian
    ),
    LanguageFamily(
        name="Hebrew",
        iso_1="he",
        iso_1_deprecated="iw",
        iso_3="heb",
        code=LanguageCode.Hebrew,
    ),
    LanguageFamily(name="Hindi", iso_1="hi", iso_3="hin", code=LanguageCode.Hindi),
    LanguageFamily(name="Hmong", iso_1=None, iso_3="hmn", code=LanguageCode.Hmong),
    LanguageFamily(
        name="Hungarian", iso_1="hu", iso_3="hun", code=LanguageCode.Hungarian
    ),
    LanguageFamily(
        name="Icelandic",
        iso_1="is",
        iso_2_B="ice",
        iso_3="isl",
        code=LanguageCode.Icelandic,
    ),
    LanguageFamily(name="Igbo", iso_1="ig", iso_3="ibo", code=LanguageCode.Igbo),
    LanguageFamily(
        name="Indonesian",
        iso_1="id",
        iso_1_deprecated="in",
        iso_3="ind",
        code=LanguageCode.Indonesian,
    ),
    LanguageFamily(
        name="Interlingua", iso_1="ia", iso_3="ina", code=LanguageCode.Interlingua,
    ),
    LanguageFamily(
        name="Interlingue", iso_1="ie", iso_3="ile", code=LanguageCode.Interlingue,
    ),
    LanguageFamily(
        name="Inuktitut", iso_1="iu", iso_3="iku", code=LanguageCode.Inuktitut
    ),
    LanguageFamily(name="Inupiaq", iso_1="ik", iso_3="ipk", code=LanguageCode.Inupiaq),
    LanguageFamily(name="Irish", iso_1="ga", iso_3="gle", code=LanguageCode.Irish),
    LanguageFamily(name="Italian", iso_1="it", iso_3="ita", code=LanguageCode.Italian),
    LanguageFamily(
        name="Japanese", iso_1="ja", iso_3="jpn", code=LanguageCode.Japanese
    ),
    LanguageFamily(
        name="Javanese",
        iso_1="jv",
        iso_1_deprecated="jw",
        iso_3="jav",
        code=LanguageCode.Javanese,
    ),
    LanguageFamily(name="Kannada", iso_1="kn", iso_3="kan", code=LanguageCode.Kannada),
    LanguageFamily(
        name="Kashmiri", iso_1="ks", iso_3="kas", code=LanguageCode.Kashmiri
    ),
    LanguageFamily(name="Kazakh", iso_1="kk", iso_3="kaz", code=LanguageCode.Kazakh),
    LanguageFamily(name="Khasi", iso_1=None, iso_3="kha", code=LanguageCode.Khasi),
    LanguageFamily(name="Khmer", iso_1="km", iso_3="khm", code=LanguageCode.Khmer),
    LanguageFamily(
        name="Kinyarwanda", iso_1="rw", iso_3="kin", code=LanguageCode.Kinyarwanda,
    ),
    LanguageFamily(name="Klingon", iso_1=None, iso_3="tlh", code=LanguageCode.Klingon),
    LanguageFamily(name="Korean", iso_1="ko", iso_3="kor", code=LanguageCode.Korean),
    LanguageFamily(name="Krio", iso_1=None, iso_3="kri", code=LanguageCode.Krio),
    LanguageFamily(name="Kurdish", iso_1="ku", iso_3="kur", code=LanguageCode.Kurdish),
    LanguageFamily(name="Kyrgyz", iso_1="ky", iso_3="kir", code=LanguageCode.Kyrgyz),
    LanguageFamily(name="Lao", iso_1="lo", iso_3="lao", code=LanguageCode.Lao),
    LanguageFamily(name="Latin", iso_1="la", iso_3="lat", code=LanguageCode.Latin),
    LanguageFamily(name="Latvian", iso_1="lv", iso_3="lav", code=LanguageCode.Latvian),
    LanguageFamily(name="Limbu", iso_1=None, iso_3="lif", code=LanguageCode.Limbu),
    LanguageFamily(name="Lingala", iso_1="ln", iso_3="lin", code=LanguageCode.Lingala),
    LanguageFamily(
        name="Lithuanian", iso_1="lt", iso_3="lit", code=LanguageCode.Lithuanian
    ),
    LanguageFamily(name="Lojban", iso_1=None, iso_3="jbo", code=LanguageCode.Lojban),
    LanguageFamily(name="Lozi", iso_1=None, iso_3="loz", code=LanguageCode.Lozi),
    LanguageFamily(
        name="Luba-Katanga", iso_1="lu", iso_3="lub", code=LanguageCode.LubaKatanga,
    ),
    LanguageFamily(
        name="Luba-Lulua", iso_1=None, iso_3="lua", code=LanguageCode.LubaLulua
    ),
    LanguageFamily(
        name="Luo (Kenya and Tanzania)", iso_1=None, iso_3="luo", code=LanguageCode.Luo,
    ),
    LanguageFamily(
        name="Luxembourgish", iso_1="lb", iso_3="ltz", code=LanguageCode.Luxembourgish,
    ),
    LanguageFamily(
        name="Macedonian",
        iso_1="mk",
        iso_2_B="mac",
        iso_3="mkd",
        code=LanguageCode.Macedonian,
    ),
    LanguageFamily(
        name="Malagasy", iso_1="mg", iso_3="mlg", code=LanguageCode.Malagasy
    ),
    LanguageFamily(
        name="Malay", iso_1="ms", iso_2_B="may", iso_3="msa", code=LanguageCode.Malay,
    ),
    LanguageFamily(
        name="Malayalam", iso_1="ml", iso_3="mal", code=LanguageCode.Malayalam
    ),
    LanguageFamily(name="Maltese", iso_1="mt", iso_3="mlt", code=LanguageCode.Maltese),
    LanguageFamily(name="Manx", iso_1="gv", iso_3="glv", code=LanguageCode.Manx),
    LanguageFamily(
        name="Maori", iso_1="mi", iso_2_B="mao", iso_3="mri", code=LanguageCode.Maori,
    ),
    LanguageFamily(name="Marathi", iso_1="mr", iso_3="mar", code=LanguageCode.Marathi),
    LanguageFamily(
        name="Greek, Modern (1453–)",
        iso_1="el",
        iso_2_B="gre",
        iso_3="ell",
        scope=LanguageScope.Individual,
        type=LanguageType.Living,
        code=LanguageCode.ModernGreek,
    ),
    LanguageFamily(
        name="Morisyen", iso_1=None, iso_3="mfe", code=LanguageCode.Morisyen
    ),
    LanguageFamily(
        name="Moldavian", iso_1="mo", iso_3="mol", code=LanguageCode.Moldavian
    ),
    LanguageFamily(
        name="Mongolian", iso_1="mn", iso_3="mon", code=LanguageCode.Mongolian
    ),
    LanguageFamily(
        name="Montenegrin", iso_1=None, iso_3="cnr", code=LanguageCode.Montenegrin,
    ),
    LanguageFamily(name="Nauru", iso_1="na", iso_3="nau", code=LanguageCode.Nauru),
    LanguageFamily(
        name="South Ndebele", iso_1="nr", iso_3="nbl", code=LanguageCode.SouthNdebele,
    ),
    LanguageFamily(
        name="North Ndebele", iso_1="nd", iso_3="nde", code=LanguageCode.NorthNdebele,
    ),
    LanguageFamily(name="Nepali", iso_1="ne", iso_3="nep", code=LanguageCode.Nepali),
    LanguageFamily(name="Newari", iso_1=None, iso_3="new", code=LanguageCode.Newari),
    LanguageFamily(
        name="Norwegian", iso_1="no", iso_3="nor", code=LanguageCode.Norwegian
    ),
    LanguageFamily(
        name="Norwegian Bokmål",
        iso_1="nb",
        iso_3="nob",
        code=LanguageCode.NorwegianBokmal,
    ),
    LanguageFamily(
        name="Norwegian Nynorsk",
        iso_1="nn",
        iso_3="nno",
        code=LanguageCode.NorwegianNynorsk,
    ),
    LanguageFamily(name="Nyanja", iso_1="ny", iso_3="nya", code=LanguageCode.Nyanja),
    LanguageFamily(name="Occitan", iso_1="oc", iso_3="oci", code=LanguageCode.Occitan),
    LanguageFamily(
        name="Old Dutch",
        iso_3="odt",
        code=LanguageCode.OldDutch,
        type=LanguageType.Historical,
    ),
    LanguageFamily(name="Oriya", iso_1="or", iso_3="ori", code=LanguageCode.Oriya),
    LanguageFamily(name="Oromo", iso_1="om", iso_3="orm", code=LanguageCode.Oromo),
    LanguageFamily(
        name="Ossetian", iso_1="os", iso_3="oss", code=LanguageCode.Ossetian
    ),
    LanguageFamily(
        name="Pampanga", iso_1=None, iso_3="pam", code=LanguageCode.Pampanga
    ),
    LanguageFamily(name="Pashto", iso_1="ps", iso_3="pus", code=LanguageCode.Pashto),
    LanguageFamily(name="Pedi", iso_1=None, iso_3="nso", code=LanguageCode.Pedi),
    LanguageFamily(
        name="Persian",
        iso_1="fa",
        iso_2_B="per",
        iso_3="fas",
        code=LanguageCode.Persian,
    ),
    LanguageFamily(name="Polish", iso_1="pl", iso_3="pol", code=LanguageCode.Polish),
    LanguageFamily(
        name="Portuguese", iso_1="pt", iso_3="por", code=LanguageCode.Portuguese
    ),
    LanguageFamily(name="Punjabi", iso_1="pa", iso_3="pan", code=LanguageCode.Punjabi),
    LanguageFamily(name="Quechua", iso_1="qu", iso_3="que", code=LanguageCode.Quechua),
    LanguageFamily(
        name="Rajasthani", iso_1=None, iso_3="raj", code=LanguageCode.Rajasthani
    ),
    LanguageFamily(
        name="Romanian",
        iso_1="ro",
        iso_1_deprecated="mo",
        iso_2_B="rum",
        iso_3="ron",
        code=LanguageCode.Romanian,
    ),
    LanguageFamily(name="Romansh", iso_1="rm", iso_3="roh", code=LanguageCode.Romansh),
    LanguageFamily(name="Rundi", iso_1="rn", iso_3="run", code=LanguageCode.Rundi),
    LanguageFamily(name="Russian", iso_1="ru", iso_3="rus", code=LanguageCode.Russian),
    LanguageFamily(name="Samoan", iso_1="sm", iso_3="smo", code=LanguageCode.Samoan),
    LanguageFamily(name="Sango", iso_1="sg", iso_3="sag", code=LanguageCode.Sango),
    LanguageFamily(
        name="Sanskrit", iso_1="sa", iso_3="san", code=LanguageCode.Sanskrit
    ),
    LanguageFamily(name="Scots", iso_1=None, iso_3="sco", code=LanguageCode.Scots),
    LanguageFamily(
        name="Scottish Gaelic",
        iso_1="gd",
        iso_3="gla",
        code=LanguageCode.ScottishGaelic,
    ),
    LanguageFamily(name="Serbian", iso_1="sr", iso_3="srp", code=LanguageCode.Serbian),
    LanguageFamily(name="Seselwa", iso_1=None, iso_3="crs", code=LanguageCode.Seselwa),
    LanguageFamily(name="Sesotho", iso_1="st", iso_3="sot", code=LanguageCode.Sesotho),
    LanguageFamily(name="Shona", iso_1="sn", iso_3="sna", code=LanguageCode.Shona),
    LanguageFamily(name="Sindhi", iso_1="sd", iso_3="snd", code=LanguageCode.Sindhi),
    LanguageFamily(
        name="Sinhalese", iso_1="si", iso_3="sin", code=LanguageCode.Sinhalese
    ),
    LanguageFamily(
        name="Slovak", iso_1="sk", iso_2_B="slo", iso_3="slk", code=LanguageCode.Slovak,
    ),
    LanguageFamily(
        name="Slovenian", iso_1="sl", iso_3="slv", code=LanguageCode.Slovenian
    ),
    LanguageFamily(name="Somali", iso_1="so", iso_3="som", code=LanguageCode.Somali),
    LanguageFamily(name="Spanish", iso_1="es", iso_3="spa", code=LanguageCode.Spanish),
    LanguageFamily(
        name="Sundanese", iso_1="su", iso_3="sun", code=LanguageCode.Sundanese
    ),
    LanguageFamily(name="Swahili", iso_1="sw", iso_3="swa", code=LanguageCode.Swahili),
    LanguageFamily(name="Swati", iso_1="ss", iso_3="ssw", code=LanguageCode.Swati),
    LanguageFamily(name="Swedish", iso_1="sv", iso_3="swe", code=LanguageCode.Swedish),
    LanguageFamily(name="Syriac", iso_1=None, iso_3="syr", code=LanguageCode.Syriac),
    LanguageFamily(name="Tagalog", iso_1="tl", iso_3="tgl", code=LanguageCode.Tagalog),
    LanguageFamily(name="Tajik", iso_1="tg", iso_3="tgk", code=LanguageCode.Tajik),
    LanguageFamily(name="Tamil", iso_1="ta", iso_3="tam", code=LanguageCode.Tamil),
    LanguageFamily(name="Tatar", iso_1="tt", iso_3="tat", code=LanguageCode.Tatar),
    LanguageFamily(name="Telugu", iso_1="te", iso_3="tel", code=LanguageCode.Telugu),
    LanguageFamily(name="Thai", iso_1="th", iso_3="tha", code=LanguageCode.Thai),
    LanguageFamily(
        name="Tibetan",
        iso_1="bo",
        iso_2_B="tib",
        iso_3="bod",
        code=LanguageCode.Tibetan,
    ),
    LanguageFamily(
        name="Tigrinya", iso_1="ti", iso_3="tir", code=LanguageCode.Tigrinya
    ),
    LanguageFamily(name="Tonga", iso_1="to", iso_3="ton", code=LanguageCode.Tonga),
    LanguageFamily(name="Tsonga", iso_1="ts", iso_3="tso", code=LanguageCode.Tsonga),
    LanguageFamily(name="Tswana", iso_1="tn", iso_3="tsn", code=LanguageCode.Tswana),
    LanguageFamily(name="Tumbuka", iso_1=None, iso_3="tum", code=LanguageCode.Tumbuka),
    LanguageFamily(name="Turkish", iso_1="tr", iso_3="tur", code=LanguageCode.Turkish),
    LanguageFamily(name="Turkmen", iso_1="tk", iso_3="tuk", code=LanguageCode.Turkmen),
    LanguageFamily(name="Twi", iso_1="tw", iso_3="twi", code=LanguageCode.Twi),
    LanguageFamily(name="Uighur", iso_1="ug", iso_3="uig", code=LanguageCode.Uighur),
    LanguageFamily(
        name="Ukrainian", iso_1="uk", iso_3="ukr", code=LanguageCode.Ukrainian
    ),
    LanguageFamily(name="Urdu", iso_1="ur", iso_3="urd", code=LanguageCode.Urdu),
    LanguageFamily(name="Uzbek", iso_1="uz", iso_3="uzb", code=LanguageCode.Uzbek),
    LanguageFamily(name="Venda", iso_1="ve", iso_3="ven", code=LanguageCode.Venda),
    LanguageFamily(
        name="Vietnamese", iso_1="vi", iso_3="vie", code=LanguageCode.Vietnamese
    ),
    LanguageFamily(name="Volapuk", iso_1="vo", iso_3="vol", code=LanguageCode.Volapuk),
    LanguageFamily(
        name="Waray (Phillipines)", iso_1=None, iso_3="war", code=LanguageCode.Waray,
    ),
    LanguageFamily(
        name="Welsh", iso_1="cy", iso_2_B="wel", iso_3="cym", code=LanguageCode.Welsh,
    ),
    LanguageFamily(name="Wolof", iso_1="wo", iso_3="wol", code=LanguageCode.Wolof),
    LanguageFamily(name="Xhosa", iso_1="xh", iso_3="xho", code=LanguageCode.Xhosa),
    LanguageFamily(
        name="Xi'an",
        iso_1=None,
        iso_3="uxy",
        code=LanguageCode.Xian,
        type=LanguageType.Constructed,
    ),
    LanguageFamily(
        name="Yiddish",
        iso_1="yi",
        iso_1_deprecated="ji",
        iso_3="yid",
        code=LanguageCode.Yiddish,
    ),
    LanguageFamily(name="Yoruba", iso_1="yo", iso_3="yor", code=LanguageCode.Yoruba),
    LanguageFamily(name="Zhuang", iso_1="za", iso_3="zha", code=LanguageCode.Zhuang),
    LanguageFamily(name="Zulu", iso_1="zu", iso_3="zul", code=LanguageCode.Zulu),
    Undetermined,
]


class LanguageDictionary(BaseModel):
    iso_1: Dict[str, LanguageFamily]
    iso_1_deprecated: Dict[str, LanguageFamily]

    iso_2_B: Dict[str, LanguageFamily]

    iso_3: Dict[str, LanguageFamily]


def generate_language_dictionary(
    languages: List[LanguageFamily],
) -> LanguageDictionary:
    dictionary = LanguageDictionary(iso_1={}, iso_3={}, iso_1_deprecated={}, iso_2_B={})

    for language in languages:
        if language.iso_1 is not None:
            dictionary.iso_1[language.iso_1] = language

        if language.iso_1_deprecated is not None:
            dictionary.iso_1_deprecated[language.iso_1_deprecated] = language

        if language.iso_2_B is not None:
            dictionary.iso_2_B[language.iso_2_B] = language

        if language.iso_3 is not None:
            dictionary.iso_3[language.iso_3] = language

    return dictionary


language_dictionary = generate_language_dictionary(languages)


class Script(BaseModel):
    # ISO 15924, Codes for the representation of names of scripts
    # https://en.wikipedia.org/wiki/ISO_15924
    name: str

    code: str
    number: str  # 3 digit number


scripts = [
    Script(name="Latin", code="Latn", number="215"),
    Script(name="Cyrillic", code="Cyrl", number="220"),
    Script(name="Hangul", code="Hang", number="286"),
    Script(name="Korean", code="Kore", number="287"),
    Script(name="Hiragana", code="Hira", number="410"),
    Script(name="Katakana", code="Kana", number="411"),
    Script(name="Japanese syllabaries", code="Hrkt", number="412"),
    Script(name="Japanese", code="Jpan", number="413"),
    Script(name="Han (Hanzi, Kanji, Hanja)", code="Hani", number="500"),
    Script(name="Han (Simplified)", code="Hans", number="501"),
    Script(name="Han (Traditional)", code="Hant", number="502"),
]

script_dictionary = {script.code: script for script in scripts}


def lookup_script(code: str) -> Script:
    if code in script_dictionary:
        return script_dictionary[code]

    raise ValueError("Unrecognized script %s" % (code))


class Region(BaseModel):
    name: str
    code: str


regions = [Region(name="United Kingdom", code="GB")]

region_dictionary = {region.code: region for region in regions}


def lookup_region(code: str) -> Region:
    normalized_code = code.upper()

    if normalized_code in region_dictionary:
        return region_dictionary[normalized_code]

    raise ValueError("Unrecognized script %s" % (code))


class Language(object):
    # Supporting more of the standard:
    # https://www.w3.org/International/articles/language-tags/
    def __init__(self, original_tag: str):
        self.name = None  # ISO language name
        self.original_tag: str = original_tag  # Application-specific code (pycld2, etc)

        self.language: Optional[LanguageFamily] = None

        self.script: Optional[Script] = None
        self.region: Optional[Region] = None

    @staticmethod
    def lookup_iso_1(code: str) -> LanguageFamily:
        if len(code) != 2:
            raise ValueError("Language code %s of incorrect length" % (code))

        if code in language_dictionary.iso_1_deprecated:
            return language_dictionary.iso_1_deprecated[code]
        elif code in language_dictionary.iso_1:
            return language_dictionary.iso_1[code]
        else:
            raise ValueError("Unrecognized ISO 639-1 code %s" % (code))

    @staticmethod
    def lookup_iso_2(code: str) -> LanguageFamily:
        if len(code) != 3:
            raise ValueError("Language code %s of incorrect length" % (code))

        if code in language_dictionary.iso_2_B:
            return language_dictionary.iso_2_B[code]
        elif code in language_dictionary.iso_3:
            return language_dictionary.iso_3[code]
        else:
            raise ValueError("Unrecognized ISO 639-2 code %s" % (code))

    @staticmethod
    def lookup_iso_3(code: str) -> LanguageFamily:
        if len(code) != 3:
            raise ValueError("Language code %s of incorrect length" % (code))

        # Make it undefined, we're not handling Pirate, etc
        if code in ["xxx", "zzb", "zze", "zzh", "zzp"]:
            return Undetermined
        elif code in language_dictionary.iso_3:
            return language_dictionary.iso_3[code]
        else:
            raise ValueError("Unknown ISO 639-3 code %s" % (code))

    @staticmethod
    def lookup(code: str) -> LanguageFamily:
        try:
            return Language.lookup_iso_1(code)
        except ValueError:
            try:
                return Language.lookup_iso_2(code)
            except ValueError:
                return Language.lookup_iso_3(code)

        raise ValueError("Could not find a language with code %s" % (code))

    @staticmethod
    def where(
        tag: Optional[str] = None,  # A complete (IETF) tag
        iso_1: Optional[str] = None,
        iso_2: Optional[str] = None,
        iso_3: Optional[str] = None,
        script: Optional[Script] = None,
        region: Optional[str] = None,
    ) -> Language:
        language: Language

        if tag is not None:
            language = Language(tag)

            # Special case: Montenegrin
            if tag == "sr-ME":
                language.language = language_dictionary.iso_3["cnr"]
                language.original_tag = tag
            else:
                # Parse
                IETF_TAG = r"^(?P<code>\w{2,3})([-_](?P<script>\w{4}))?([-_](?P<region>\w{2}))?$"

                match = re.match(IETF_TAG, tag)

                if match is not None:
                    language.language = Language.lookup(match.group("code"))

                    script_match = match.group("script")
                    if script_match is not None:
                        language.script = lookup_script(script_match)

                    region_match = match.group("region")
                    if region_match is not None:
                        language.region = lookup_region(region_match)
                else:
                    raise ValueError("Could not parse IETF tag %s" % (tag))

            return language
        elif iso_1 is not None:
            language = Language(iso_1)
            language.language = Language.lookup_iso_1(iso_1)
        elif iso_2 is not None:
            language = Language(iso_2)
            language.language = Language.lookup_iso_2(iso_2)
        elif iso_3 is not None:
            language = Language(iso_3)
            language.language = Language.lookup_iso_3(iso_3)
        else:
            language.language = Undetermined

        return language

    def __str__(self):
        return self.alpha_3

    def __repr__(self):
        return "<Language %s%s>" % (
            self.alpha_3,
            ":" + self.specific if self.specific is not None else "",
        )

    def __hash__(self):
        return hash(self.specific)

    def __eq__(self, other):
        if isinstance(other, Language):
            return (
                self.language == other.language
                and self.region == other.region
                and self.script == other.script
            )
        elif isinstance(other, LanguageCode):
            return self.code == other
        elif isinstance(other, str):
            return (
                self.alpha_3 == other or self.alpha_2 == other or self.specific == other
            )

    @property
    def alpha_2(self) -> str:
        if self.language is not None and self.language.iso_1 is not None:
            return self.language.iso_1
        else:
            return "un"

    @property
    def alpha_3(self) -> str:
        if self.language is not None:
            return self.language.code.value
        else:
            return "und"

    @property
    def code(self) -> LanguageCode:
        if self.language is not None:
            return self.language.code
        else:
            return LanguageCode.Undetermined

    @property
    def specific(self) -> str:
        return self.original_tag if self.original_tag is not None else self.alpha_3

    def original_or_alpha_2(self):
        if self.original_tag is not None:
            return self.original_tag
        elif self.alpha_2 != "un":
            return self.alpha_2
        elif self.alpha_3 != "und":
            return self.alpha_3
        else:
            return "un"
