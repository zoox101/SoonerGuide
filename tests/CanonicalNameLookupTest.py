import unittest
from Lambda import get_canonical_union_room_name, remove_prefix, get_key_from_multimap, get_canonical_name, \
    get_canonical_building_name
from alexa_synonyms import union_room_synonyms
from external_building_synonyms import external_building_synonyms


class MultimapLookupWorksTestCase(unittest.TestCase):
    def test_getMultimapWorksOkay(self):
        test_multimap = {"my_key": ["value 1", "value 2"], "my_other_key": ["value 4", "value 5"]}
        self.assertEqual("my_key", get_key_from_multimap("my_key", test_multimap))
        self.assertEqual("my_key", get_key_from_multimap("my key", test_multimap))
        self.assertEqual("my_key", get_key_from_multimap("value 1", test_multimap))
        self.assertEqual("my_key", get_key_from_multimap("value 2", test_multimap))

        self.assertFalse(get_key_from_multimap("value 3", test_multimap))

        self.assertEqual("my_other_key", get_key_from_multimap("my_other_key", test_multimap))
        self.assertEqual("my_other_key", get_key_from_multimap("my other key", test_multimap))
        self.assertEqual("my_other_key", get_key_from_multimap("value 4", test_multimap))
        self.assertEqual("my_other_key", get_key_from_multimap("value 5", test_multimap))

    def test_canFindAllUnionRoomNamesWithMultimapLookup(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertEqual(canonical_union_room_name,
                             get_key_from_multimap(canonical_union_room_name, union_room_synonyms),
                             "Lookup of key " + canonical_union_room_name + " in multimap did not return itself")
            for room_synonym in union_room_synonyms[canonical_union_room_name]:
                self.assertEqual(canonical_union_room_name, get_key_from_multimap(room_synonym, union_room_synonyms),
                                 "Lookup of multimap vaue " + room_synonym + " did not return key " + canonical_union_room_name)


class PrefixRemovalWorksTest(unittest.TestCase):
    def test_prefixRemovalRemovesFromFrontOfLiteral(self):
        self.assertEqual("room", remove_prefix("the room", "the "))

    def test_prefixRemovalDoesntAffectStringsWithoutPrefix(self):
        self.assertEqual("room", remove_prefix("room", "the "))

    def test_prefixRemovalCanRemoveOptionalTheAtFrontOfRoomName(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertEqual(canonical_union_room_name, remove_prefix("the " + canonical_union_room_name, "the "),
                             "prefix removal not working")
            self.assertEqual(canonical_union_room_name, remove_prefix(canonical_union_room_name, "the "),
                             "prefix removal affecting strings without prefix")


class RoomCanonicalNameLookupTestCase(unittest.TestCase):
    def test_allCanonicalRoomNamesReturnCanonicalRoomName(self):
        for canonical_room_name in union_room_synonyms:
            self.assertEqual(canonical_room_name, get_canonical_name(canonical_room_name, union_room_synonyms),
                             "canonical union room name should return itself")  # idempotency
            self.assertEqual(canonical_room_name,
                             get_canonical_name(canonical_room_name.replace("_", " "), union_room_synonyms),
                             "should be able to say canonical room name (with spaces) and get the canonical part back")  # fine if we do the key with space separations

    def test_allUnionRoomSynonymsReturnCorrectCanonicalRoomName(self):
        for canonical_union_room_name in union_room_synonyms:
            for room_synonym in union_room_synonyms[canonical_union_room_name]:
                self.assertEqual(canonical_union_room_name, get_canonical_name(room_synonym, union_room_synonyms),
                                 "a room's synonym (" + room_synonym + ") didn't identify its key")

    def test_missingRoomReturnsFalse(self):
        self.assertFalse(get_canonical_name('missing room', union_room_synonyms),
                         "Found room that shouldn't have been there!")
        for canonical_union_room_name in union_room_synonyms:
            self.assertFalse(get_canonical_name(canonical_union_room_name + " FAIL", union_room_synonyms),
                             "Found room that shouldn't have been there!")

    def test_canAddTheToAnyRoomNameAndItStillMatches(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertEqual(canonical_union_room_name,
                             get_canonical_name("the " + canonical_union_room_name.replace("_", " "),
                                                union_room_synonyms),
                             "Can't add \"the \" to the front of any canonical room name")
            for room_synonym in union_room_synonyms[canonical_union_room_name]:
                self.assertEqual(canonical_union_room_name,
                                 get_canonical_name("the " + room_synonym, union_room_synonyms),
                                 "Can't add \"the \" to the front of any room name")


class UnionRoomCanonicalNameLookupTestCase(unittest.TestCase):
    def test_noEmptyStringSynonyms(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertFalse("" in union_room_synonyms[canonical_union_room_name],
                             canonical_union_room_name + " has an empty string as a synonym")

    def test_allCanonicalRoomNamesReturnCanonicalRoomName(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertEqual(canonical_union_room_name, get_canonical_union_room_name(canonical_union_room_name),
                             "canonical union room name should return itself")  # idempotency
            self.assertEqual(canonical_union_room_name,
                             get_canonical_union_room_name(canonical_union_room_name.replace("_", " ")),
                             "should be able to say canonical room name (with spaces) and get the canonical part back")  # fine if we do the key with space separations

    def test_allUnionRoomSynonymsReturnCorrectCanonicalRoomName(self):
        for canonical_union_room_name in union_room_synonyms:
            for room_synonym in union_room_synonyms[canonical_union_room_name]:
                self.assertEqual(canonical_union_room_name, get_canonical_union_room_name(room_synonym),
                                 "a room's synonym (" + room_synonym + ") didn't identify its key")

    def test_missingRoomReturnsFalse(self):
        self.assertFalse(get_canonical_union_room_name('missing room'), "Found room that shouldn't have been there!")
        for canonical_union_room_name in union_room_synonyms:
            self.assertFalse(get_canonical_union_room_name(canonical_union_room_name + " FAIL"),
                             "Found room that shouldn't have been there!")

    def test_canAddTheToAnyRoomNameAndItStillMatches(self):
        for canonical_union_room_name in union_room_synonyms:
            self.assertEqual(canonical_union_room_name,
                             get_canonical_union_room_name("the " + canonical_union_room_name.replace("_", " ")),
                             "Can't add \"the \" to the front of any canonical room name")
            for room_synonym in union_room_synonyms[canonical_union_room_name]:
                self.assertEqual(canonical_union_room_name, get_canonical_union_room_name("the " + room_synonym),
                                 "Can't add \"the \" to the front of any room name")


class BuildingCanonicalNameLookupTestCase(unittest.TestCase):
    def test_noEmptyStringSynonyms(self):
        for canonical_building_name in external_building_synonyms:
            self.assertFalse("" in external_building_synonyms[canonical_building_name],
                             canonical_building_name + " has an empty string as a synonym")

    def test_allCanonicalBuildingNamesReturnCanonicalBuildingName(self):
        for canonical_building_name in external_building_synonyms:
            self.assertEqual(canonical_building_name, get_canonical_building_name(canonical_building_name),
                             "canonical building name should return itself")  # idempotency
            self.assertEqual(canonical_building_name,
                             get_canonical_building_name(canonical_building_name.replace("_", " ")),
                             "should be able to say canonical building name (with spaces) and get the canonical part back")  # fine if we do the key with space separations

    def test_allBuildingSynonymsReturnCorrectCanonicalBuildingName(self):
        for canonical_building_name in external_building_synonyms:
            for building_synonym in external_building_synonyms[canonical_building_name]:
                self.assertEqual(canonical_building_name, get_canonical_building_name(building_synonym),
                                 "a building's synonym (" + building_synonym + ") didn't identify its key")

    def test_missingBuildingReturnsFalse(self):
        self.assertFalse(get_canonical_building_name('missing building'),
                         "Found building that shouldn't have been there!")
        for canonical_building_name in external_building_synonyms:
            self.assertFalse(get_canonical_building_name(canonical_building_name + " FAIL"),
                             "Found building that shouldn't have been there!")

    def test_canAddTheToAnyBuildingNameAndItStillMatches(self):
        for canonical_building_name in external_building_synonyms:
            self.assertEqual(canonical_building_name,
                             get_canonical_building_name("the " + canonical_building_name.replace("_", " ")),
                             "Can't add \"the \" to the front of any canonical building name")
            for building_synonym in external_building_synonyms[canonical_building_name]:
                self.assertEqual(canonical_building_name, get_canonical_building_name("the " + building_synonym),
                                 "Can't add \"the \" to the front of any building name")


if __name__ == '__main__':
    unittest.main()
