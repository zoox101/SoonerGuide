import unittest
from external_building_directions import external_building_directions_relative_to_landmarks
from external_building_synonyms import external_building_synonyms
from Lambda import on_intent, BUILDING_NAME_SLOT_KEY, BUILDING_DIRECTIONS_INTENT_NAME


def createIntentForLookingUpBuilding(user_provided_building_name):
    return {'intent': {'name': BUILDING_DIRECTIONS_INTENT_NAME, 'slots': {BUILDING_NAME_SLOT_KEY: {'value': user_provided_building_name}}},
            'requestId': ""}


class BuildingDirectionsTestCase(unittest.TestCase):
    def test_allCanonicalBuildingNamesHaveDirections(self):
        for canonical_building_name in external_building_synonyms:
            self.assertTrue(canonical_building_name in external_building_directions_relative_to_landmarks.keys(),
                            "Building " + canonical_building_name + " is missing directions")

    def test_allBuildingsWithDirectionsHaveCanonicalNames(self):
        for canonical_building_name in external_building_directions_relative_to_landmarks:
            self.assertTrue(canonical_building_name in external_building_synonyms.keys(),
                            "Building " + canonical_building_name + " has directions but no canonical name")

    def test_firingIntentForBuildingReturnsExpectedDirections(self):
        for canonical_building_name in external_building_directions_relative_to_landmarks:
            response = on_intent(createIntentForLookingUpBuilding(canonical_building_name), {"sessionId": ""})
            self.assertEqual(external_building_directions_relative_to_landmarks[canonical_building_name],
                             response['response']['outputSpeech']['text'],
                             "Building  " + canonical_building_name + " gave the wrong directions")

    def test_firingIntentForBuildingSynonymsReturnsExpectedDirections(self):
        for canonical_building_name in external_building_synonyms:
            for room_synonym in external_building_synonyms[canonical_building_name]:
                response = on_intent(createIntentForLookingUpBuilding(room_synonym), {"sessionId": ""})
                self.assertEqual(external_building_directions_relative_to_landmarks[canonical_building_name],
                                 response['response']['outputSpeech']['text'],
                                 "Building " + canonical_building_name + " gave the wrong directions using the synonym " + room_synonym)


if __name__ == '__main__':
    unittest.main()
