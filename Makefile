project.zip: *.py
	zip -u $@ $^

roomNameSlots.json: makeSlotsForRoomNames.py alexa_synonyms.py
	python $^ > $@