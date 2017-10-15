import unittest
from room_directions import union_room_directions
from alexa_synonyms import union_room_synonyms
from Lambda import on_intent


def createIntentForLookingUpRoom(user_provided_room_name):
    return {'intent': {'name': 'WhereIsMyRoom', 'slots': {'RoomName': {'value': user_provided_room_name}}},
            'requestId': ""}


class RoomDirectionsTestCase(unittest.TestCase):
    def test_allCanonicalRoomNamesHaveDirections(self):
        for canonicalRoomName in union_room_synonyms:
            self.assertTrue(canonicalRoomName in union_room_directions.keys(),
                            "Room " + canonicalRoomName + " is missing directions")

    def test_allRoomsWithDirectionsHaveCanonicalNames(self):
        for canonicalRoomName in union_room_directions:
            self.assertTrue(canonicalRoomName in union_room_synonyms.keys(),
                            "Room " + canonicalRoomName + " has directions but no canonical name")

    def test_firingIntentForRoomReturnsExpectedDirections(self):
        for canonicalRoomName in union_room_directions:
            self.assertEqual(union_room_directions[canonicalRoomName],
                             on_intent(createIntentForLookingUpRoom(canonicalRoomName),
                                       {"sessionId": ""})['response']['outputSpeech']['text'],
                             "Room " + canonicalRoomName + " gave the wrong directions")

    def test_firingIntentForRoomSynonymsReturnsExpectedDirections(self):
        for canonicalRoomName in union_room_synonyms:
            for room_synonym in union_room_synonyms[canonicalRoomName]:
                self.assertEqual(union_room_directions[canonicalRoomName],
                                 on_intent(createIntentForLookingUpRoom(room_synonym),
                                           {"sessionId": ""})['response']['outputSpeech']['text'],
                                 "Room " + canonicalRoomName + "gave the wrong directions using the synonym " + room_synonym)


if __name__ == '__main__':
    unittest.main()
