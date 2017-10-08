#!bin/python


class MissingTranslationException(Exception):
    pass

translations = {
    "en_US": [
        [
            'The space',
            'Bytespeicher'
        ],
        [
            'is',
        ],
        [
            'open',
            'allowing access',
        ],
        [
            'closed',
            'not open anymore'
        ],
        [
            'magnificent',
            'imposing',
            'impressive',
            'awe-inspiring',
            'grand',
            'splendid',
            'majestic',
            'monumental',
            'glorious',
            'sumptuous',
            'resplendent',
            'lavish',
            'beautiful',
            'delightful',
            'lovely',
        ],
        [
            'Too bad',
            'ignoble',
            'inglorious',
            'dishonorable',
            'atrocious',
            'flagitious',
            'lowly',
            'mean',
            'poor',
        ]
    ],
	"de_DE": [
        [
            'Der Raum',
            'Bytespeicher'
        ],
        [
            'ist',
        ],
        [
            'offen',
            'Zutritt möglich',
        ],
        [
            'geschlossen',
            'nicht mehr geöffnet'
        ],
        [
            'Großartig',
            'Imposant',
            'Beeindruckend',
            'Ehrfurcht einflößend',
            'Grandios',
            'Herrlich',
            'Majestätisch',
            'Monumental',
            'Glorreich',
            'Prächtig',
            'Prachtvoll',
            'Nobel',
            'Wunderschön',
            'Reizend',
            'Lieblich',
        ],
        [
            'Schade',
            'Unwürdig',
            'Schmählich',
            'Unehrenhaft',
            'Scheußlich',
            'Sündhaft',
            'Bescheiden',
            'Gemein',
            'Schwach',
        ]
    ]
}


def wordlist(language="en_US"):
    """
    Returns a list of lists containing words to be used in a status update
    The word list is a list with seperate lists for

        * Space
        * is
        * open
        * closed
        * fill words - good
        * fill words - bad
    """
    try:
        wordlist = translations[language]
        return wordlist
    except:
        raise MissingTranslationException("No translation for %s found" %
                                          language)
