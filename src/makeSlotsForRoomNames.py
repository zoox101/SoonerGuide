from alexa_synonyms import union_room_synonyms, get_pronounceable_synonyms
import json


def make_slots_for_room_names(room_synonyms):
    return [{'id': canonical_room_name,
             'name': {'value': canonical_room_name.replace('_', ' '),
                      'synonyms': get_pronounceable_synonyms(canonical_room_name, room_synonyms)}}
            for canonical_room_name in room_synonyms]


if __name__ == '__main__':
    print(json.dumps(make_slots_for_room_names(union_room_synonyms)))
