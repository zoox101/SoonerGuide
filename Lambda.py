"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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
                    "Please ask me for directions by asking me something like, "\
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


def get_directions_for_intent(intent, session):
    """Creates an appropriate response, given intent and session information directly from Alexa"""

    room_name = intent['slots']['RoomName']['value']
    speech_output = get_directions_for_room(room_name)

    responses = {}
    responses['kxou'] = 'Its the glass room in front of you to the left!'
    responses['post_office'] = 'Its on the right side of the hallway to your left. '
    responses['sooner_card'] = 'Its on the left side of the hallway to your left.'
    responses['ou_passport'] = 'Its on the left side of the hallway to your left.'
    responses['student_art_gallery'] = 'Its on the left side of the hallway to your left. '
    responses['starbucks'] = 'Its on the left side of the hallway to your left.'
    responses['credit_union'] = 'Go down the hall to your left. It will be on your left after the ramp.'
    responses['crossroads'] = 'Go down the hall to your left. It will be on your right after the ramp.'
    responses['lgbtq_lounge'] = 'Go down the hall to your left. Turn right after going down the ramp. Its on the right side just past Crossroads. '
    responses['sooner_room'] = 'Go down the hall to your left. Turn right after going down the ramp. Its at the end of the hallway on the left.'
    responses['student_government_association'] = 'Go down the hall to your left. Turn right after going down the ramp. Its at the end of the hallway on the right.'
    responses['one_university_store'] = 'Its the glass room to your right!'
    responses['union_market'] = 'Its on the left side of the hallway to your right.'
    responses['will_rogers_room'] = 'Its on the left side of the of the hallway to your right.'
    responses['food_court'] = 'Its on the right side of the hallway to your right.'
    responses['clarke_anderson_room'] = 'Go down the hallway to your right. It will be on the left just past the room with all the chairs.'
    responses['stuart_landing'] = 'Turn around and use the stairs to go up to the second floor. Its immediately in front of the staircase.'
    responses['alma_wilson_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the first room on your left.'
    responses['pioneer_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the first room on your right.'
    responses['david_f_schrage_traditions_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the second room on your right.'
    responses['john_houchin_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the second room on your left.'
    responses['louise_houchin_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the third room on your left.'
    responses['david_l_boren_lounge'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the third room on your right.'
    responses['presidents_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. It will be the fourth room on your left.'
    responses['meacham_auditorium'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. Its on the right side of the atrium at the end of the hall.'
    responses['volunteer_office'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. Its at the end of the hallway down the short flight of stairs.'
    responses['student_affairs'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. Go all the way down the hallway and down the short flight of stairs. It will be at the end of the hallway on your right.'
    responses['conoco_student_leadership_wing'] = 'Turn around and use the stairs to go up to the second floor. Then turn left. Go all the way down the hallway and down the short flight of stairs. It will be on the right side of the hallway on your right.'
    responses['beaird_lounge'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. It will be the room on your right after the double doors.'
    responses['flint_study_center_computer_lab'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its on your left after the double doors. '
    responses['crimson_meeting_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its on your left after the double doors. '
    responses['bartlet_study_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its on your left after the double doors. '
    responses['frontier_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its the first room on your left after the short flight of stairs. '
    responses['weitzenhoffer_dining_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its the second room on your left after the short flight of stairs. '
    responses['heritage_room'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its the third room on your left after the short flight of stairs. '
    responses['crawford_university_club'] = 'Turn around and use the stairs to go up to the second floor. Then turn right. Its the big room on your right after the short flight of stairs. '
    responses['career_services'] = 'Turn around and use the stairs to go up to the third floor. It will be the room on your left.'
    responses['molly_shi_boren_ballroom'] = 'Turn around and use the stairs to go up to the third floor. Then turn right. It will be the room on your right. '
    responses['governors_room'] = 'Turn around and use the stairs to go up to the third floor. Then turn right. It will be the first room on your right after the ballroom. '
    responses['regents_room'] = 'Turn around and use the stairs to go up to the third floor. Then turn right. It will be the second room on your right after the ballroom. '
    responses['associates_room'] = 'Turn around and use the stairs to go up to the third floor. Then turn right. It will be the third room on your right after the ballroom. '
    responses['scholars_room'] = 'Turn around and use the stairs to go up to the third floor. Then turn right. It will be the room in the corner on your left after the ballroom. '
    responses['meacham_balcony'] = 'Go down the hallway to your left then turn right after the ramp. Use the stairs on your left to get to the third floor. It will be at the end of the hallway to your right after a short flight of stairs. '
    responses['student_life'] = 'Go down the hallway to your left then turn right after the ramp. Use the stairs on your left to get to the third floor. It will be on your left.'
    responses['student_leadership_wing'] = 'Go down the hallway to your left then turn right after the ramp. Use the stairs on your left to get to the third floor. Go through the student life hallway on your left. '
    responses['union_administration_and_programming_board'] = 'Turn around and use the stairs to go up to the fourth floor. Then turn left. It will be the first room on your right.'
    responses['alumni_association'] = 'Turn around and use the stairs to go up to the fourth floor. Then turn left. It will be the first room on your left.'
    responses['paul_massad_conference_room'] = 'Turn around and use the stairs to go up to the fourth floor. It will be the room in front of you to the right. '

    # establish control settings for the response object
    card_title = intent['name']
    key = intent['slots']['RoomName']['value']

    key = key.replace(' ', '_');
    key = key.lower()

    speech_output = responses[key]
    reprompt_text = 'Wat?'
    should_end_session = False

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

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
