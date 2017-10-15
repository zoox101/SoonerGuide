# Sooner Guide
This is an Alexa Skill to guide students and guests around the [OU](https://ou.edu) campus.

## Goals
- Give directions to each building on campus relative to major landmarks, such as well-known buildings.
- Give directions to each room within each of those buildings, even if that's just telling us what floor it's on.
- For special rooms and locations, such as "Crossroads", try to give directions even without knowing which building it's in.
- If Alexa doesn't understand what the user said, help them refine their input.

## Getting set up
This is an Alexa Skill with a Python 2.7 backend, running on AWS.
If you'd like to work on this, you're gonna at least need a text editor like Notepad++.
JJ recommends installing python 3.6, and installing PyCharm Community Edition by JetBeans.

### Making your own test Skill and AWS backend
If you'd like to maintain your own version of this project for testing, you can set up your own copy of it!
Make your own AWS backend, in the N. Virginia region. Then, set it up to receive Alexa events as the trigger.
Then, run `make project.zip` to get a bundled copy of the code. Just upload that to the AWS project you made, and
you're done there! From that, make an Alexa skill, hook it up to the ARN (Amazon Resource Number) at the top of the AWS page,
and you're good to go.

### Testing
If you have your own device, make sure that you've enabled the skill for the account associated with your device.
If you need to use Alexa on a different account than the one that made the skill, just have the developer of that skill
add you as a beta tester. (The developer will need to complete the Publishing Info to do this.) 

### Slots
Amazon's Alexa voice model gives us a way for us to understand when users say
       <center>"Where is &lt;room&gt; in &lt;building&gt;?"</center>
and then store what they said in `room` and `building` variables, for example.
This part works great.

They provide a way to list 'synonyms' for a slot, so you can say two things (like "OU" and "University of Oklahoma") and
Alexa will understand they mean the same thing.
This is broken and does not work; it will always send back the thing they said, and not the canonical synonym.
However, it doesn improve the interaction model, so Alexa can better match it to the right thing.

See [alexa_synonyms.py](alexa_synonyms.py) for a list of these synonyms.
To build a list of slots for use in the interaction model, see [makeSlotsForRoomNames.py](makeSlotsForRoomNames.py), or run `make roomNameSlots.json`.
This will create a JSON file that can be used to define the values of the `RoomName` slot. 

## Contributing
The production version of this is [managed by Will on GitHub](https://github.com/zoox101/SoonerGuide.git).
The easiest way to contribute would be to clone the project to your machine, edit it, pull and merge into the master branch locally, and then push it back to the github repo.
You can also fork it on GitHub and make a pull request into his repo.

### What we need to do
Short-term goals include:

- Writing directions for all of the buildings on campus
- Defining spoken synonyms for all of the buildings on campus
- Hooking up Alexa to the directions for each building in the same way as the rooms.
- Refining descriptions for all for the rooms in the union
- Prompting the user to repeat what they said when Alexa can't understand what room they said.

