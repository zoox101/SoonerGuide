project.zip: *.py
	zip -u $@ $^

slots: roomNameSlots.json buildingNameSlots.json

roomNameSlots.json: makeSlotsForRoomNames.py alexa_synonyms.py
	python $^ > $@

buildingNameSlots.json: makeSlotsForBuildingNames.py alexa_synonyms.py
	python $^ > $@