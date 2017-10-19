from makeSlotsForBuildingNames import make_slots_for_blding_names
from makeSlotsForRoomNames import make_slots_for_room_names
from Lambda import ROOM_NAME_SLOT_KEY, BUILDING_NAME_SLOT_KEY
from alexa_synonyms import union_room_synonyms
from external_building_synonyms import external_building_synonyms
import json


def makeAlexaInteractionModelSlotTypesArray(map_of_slot_name_to_synonyms):
    return [
        {
            "name": slot_name,
            "values": map_of_slot_name_to_synonyms[slot_name]
        }
        for slot_name in map_of_slot_name_to_synonyms
    ]


if __name__ == '__main__':
    print(json.dumps(makeAlexaInteractionModelSlotTypesArray(
        {
            ROOM_NAME_SLOT_KEY: make_slots_for_room_names(union_room_synonyms),
            BUILDING_NAME_SLOT_KEY: make_slots_for_blding_names(external_building_synonyms)
        }
    )))
