from random import randint


def create_phrase(phrase_structures, tr):
        gender = randint(0, 2)
        blasphemy = ""
        for x in phrase_structures[randint(0, len(phrase_structures)-1)]:
                blasphemy += tr[x][gender][randint(0, len(tr[x][gender])-1)] + " "
        return blasphemy


def engine():
    articles = [["Il"], ["La"], ["Lo"]]
    connectives = [['e'], ['e'], ['e']]
    subjects = [["dio", "gesu", 'San Faustino', "Santo Stefano", "San Zeno", 'papa', 'San Crispino', 'mosè'],
                ["madonna", "Santa Rita"], ["spirito santo"]]
    qualities = [['porcodione', 'bastardo', 'cane', 'mostro', 'schifoso', 'porco', 'svergolo', 'stronzo', 'assassino',
                  'scimmietta', 'inculato', 'infiammato', 'impestato', 'lebbroso', 'coniglio', 'cancaro', 'ladro',
                  'negro', 'babbuino', 'sborrato', 'cinghiale', 'maiale', 'crotalo', 'polpo', 'infiocinato',
                  'puttaniere', 'pinguino', 'bestiaccia', 'boia', 'merda', 'balena', 'vacca', 'strabico', 'incavalcato',
                  'spastico', 'fulminato', 'can', 'schifo', 'pedofilo', 'inchiodato', 'girarrosto', 'stuprapolli',
                  'fruttolo rancido', 'marmotta che confeziona la cioccolata', 'caterpillar', 'pederasta',
                  'sculacciatopi', 'windows vista', 'ciclista senza sellino', 'crostaceo', 'spiedino', 'contorsionista',
                  'pescivendolo'],
                 ['porcodiona', 'stiticona', 'luridona', 'maialona', 'infiammata', 'inculata', 'stuprata', 'schifosa',
                  'scimmietta', 'stronza', 'porca', 'impestata', 'lebbrosa', 'impiccata', 'sborrata', 'puttana',
                  'puttanella', 'bestiaccia', 'boia', 'merda', 'balena', 'vacca', 'slabbrata', 'maiala', 'sfondata',
                  'pompinara', 'troia', 'cavalcata', 'cavalla', 'ingravida', 'giraffa', 'zebra', 'scartavetrata',
                  'zanzara', 'cimice', 'mosca', 'cagata', 'deflorata', 'pederasta', 'in deltaplano', 'girarrosto',
                  'stuprapolli', 'fruttolo rancido', 'marmotta che confeziona la cioccolata', 'caterpillar',
                  'sculacciatopi', 'windows vista', 'ciclista senza sellino', 'crostaceo', 'spiedino',
                  'contorsionista', 'pescivendola'], []]

    qualities[2] = qualities[0]
    prepositions = [["di", "del", "quel"], ['di', 'della', 'quella'], ["dello", "quello"]]

    phrase_structures = [['s', 'q'], ['a', 's', 'q'], ['a', 's', 'p', 'q'], ['s', 'q', 'q', 'q'],
                         ['a', 'q', 's', 'p', 'q'], ['s', 'q', 'p', 'q'], ['q', 's', 'q'], ['q', 'p', 'q', 'p', 's'],
                         ['s', 'q', 'q', 'q', 'q', 'q', 'p', 's'], ['a', 'q', 'p', 's'], ['s', 'q', 'q', 'q', 'q', 'q', 'q', 'q'],
                         ['q', 'p', 's', 'q'], ['s', 'p', 'q', 'p', 's', 'q'], ['q', 'p', 's', 'q'],
                         ['a', 's', 'q', 'c', 'a', 's', 'q']]

    tr = {
        'a': articles,
        's': subjects,
        'q': qualities,
        'p': prepositions,
        'c': connectives,
    }

    return create_phrase(phrase_structures, tr)
