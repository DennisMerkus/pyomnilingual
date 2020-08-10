from enum import Enum, unique


@unique
class PartOfSpeech(Enum):
    Nil = "∅"

    # Universal
    #  Open Class
    Adjective = "ADJ"
    Adverb = "ADV"
    Interjection = "INTJ"
    Noun = "NOUN"
    ProperNoun = "PROPN"
    Verb = "VERB"

    #  Closed Class
    Adposition = "ADP"
    Auxiliary = "AUX"
    CoordinatingConjunction = "CCONJ"
    Determiner = "DET"
    Number = "NUM"
    Particle = "PART"
    Pronoun = "PRON"
    SubordinatingConjunction = "SCONJ"

    #  Other
    Phrase = "PHRASE"
    Punctuation = "PUNCT"
    Symbol = "SYM"

    Comparative = "COMP"
    Predicate = "PRED"

    Prefix = "PRFX"
    Suffix = "SFFX"

    #   Other/Uncategorized
    X = "X"

    # Extra Universal
    Conjunction = "CONJ"

    # Xi'an
    XianElemental = "elm"
    XianElementalCompound = "elmcmp"
    XianNominalizer = "nlz"
    XianVerbClarifyingParticle = "vcp"

    # Banu
    BanuClass = "clss"
    BanuClassSpecifier = "clsssp"

    BanuIndefiniteQuantity = "qty"

    BanuQuestion = "q"
    BanuQuestionVerb = "qv"
