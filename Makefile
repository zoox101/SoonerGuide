all: project.zip slots

project.zip: src/*.py
	zip -u $@ -j $^

slots: roomNameSlots.json buildingNameSlots.json slotTypesArray.json

slotTypesArray.json: makeSlotTypesArray.py roomNameSlots.json buildingNameSlots.json
	python $^ > $@

roomNameSlots.json: makeSlotsForRoomNames.py alexa_synonyms.py
	python $^ > $@

buildingNameSlots.json: makeSlotsForBuildingNames.py external_building_synonyms.py
	python $^ > $@