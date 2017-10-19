import json

from alexa_synonyms import get_pronounceable_synonyms
from external_building_synonyms import external_building_synonyms


def make_slots_for_blding_names(blding_synonyms):
    return [{'id': canonical_blding_name,
             'name': {'value': canonical_blding_name.replace('_', ' '),
                      'synonyms': get_pronounceable_synonyms(canonical_blding_name, blding_synonyms)}}
            for canonical_blding_name in external_building_synonyms]


if __name__ == '__main__':
    print(json.dumps(make_slots_for_blding_names(external_building_synonyms)))
