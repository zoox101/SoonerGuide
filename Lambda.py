"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
from alexa_synonyms import union_room_synonyms
from room_directions import union_room_directions
import json


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Sooner Guide test. " \
                    "Please ask me for directions by asking me something like, " \
                    "Where is KXOU?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask me for directions by saying something like, " \
                    "Where is Crossroads?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Sooner Guide. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_canonical_union_room_name(intent_value):
    return get_canonical_room_name(intent_value, union_room_synonyms)


def remove_prefix(str, prefix):
    if str.startswith(prefix):
        return str[len(prefix):]
    return str


def get_canonical_room_name(intent_value, room_synonyms):
    return get_key_from_multimap(remove_prefix(intent_value, prefix="the "), map=room_synonyms)


def get_key_from_multimap(value, map):
    """
    Returns the key in map that includes value in its values, or matches the value with spaces instead of underscores.
    It returns false if nothing is matched.

    For example,
    get_key_from_multimap(<value>, {"my_key": ["value 1", "value 2"]})

    would return "my_key" if value was "my key", "my_key", "value 1", or "value 2", and would return False if value was "value 3"
    """
    for key in map:
        if (value.replace(" ", "_") == key) or (value == key.replace("_", " ")) or (value in map[key]):
            return key
    return False


def get_directions_for_intent(intent, session):
    """Creates an appropriate response, given intent and session information directly from Alexa"""

    room_name = get_canonical_union_room_name(intent['slots']['RoomName']['value'])

    if room_name is False:  # meaning we can't find what room they're talking about
        # TODO: reprompt them for the room name they meant to say
        return build_response(session_attributes={},
                              speechlet_response=build_speechlet_response(
                                  title="Directions to \"" + intent['slots']['RoomName']['value'] + "\"",
                                  output=("I don't know where the room called " + intent['slots']['RoomName'][
                                      'value'] + " is."),
                                  reprompt_text=None,
                                  should_end_session=True))
    else:  # if we COULD get a canonical room_name
        speech_output = union_room_directions[room_name]
        card_title = "Directions to " + room_name.replace('_', ' ')
        reprompt_text = None
        should_end_session = True

        session_attributes = {}
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))


def get_directions_for_room(room_name):
    responses = {'kxou': 'It\'s the glass room in front of you to the left!',
                 'crossroads': 'Go down the hall to your left. It will be on your right after the ramp.'}
    return responses[room_name]


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    print("on_intent intentInfo=" + json.dumps(intent_request['intent']))

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhereIsMyRoom":
        return get_directions_for_intent(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    print('onHandle event_request=' + json.dumps(event['request']))

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
