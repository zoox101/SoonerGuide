union_room_synonyms = {
    "kxou": ["the radio station", "radio station", "k. x. o. u."],

    "post_office": ["post office", "the post office"],

    "sooner_card": ["sooner card office", "sooner card", "sun card", "sun card office"], # some times it thinks "sooner" is pronounced "sun"

    "ou_passport": ["o. u. passport"],

    "student_art_gallery": ["student art gallery", "art gallery", "art shop"],

    "starbucks": ["star bucks", "Starbucks"],

    "credit_union": ["bank", "credit union", "o. u. f. c. u.", "o. u. bank"],

    "crossroads": ["cross roads", "24 hour restaurant"],

    "lgbtq_lounge": ["queer lounge", "l. g. b. t. q. lounge", "l. g. b. t. lounge", "gay lounge"],

    "sooner_room": ["sooner room", "sun room"], #sometimes Alexa hears "Sooner" as "sun"

    "student_government_association": ["s. g. a.", "student government", "student government association", "student government office", "s. g. a. office"],

    "one_university_store": ["one u. store", "o. u. store", "computer store", "one university store"],

    "union_market": ["union market"],

    "will_rogers_room": ["will rogers room", "will rogers"],

    "food_court": ["food court", "food", "chick fill a.", "chic fil a", "quizno's", "laughing tomato"], # TODO: taco shop

    "clarke_anderson_room": ["clarke anderson room", "clarke anderson"],

    "stuart_landing": ["stuart landing"],

    "alma_wilson_room": ["alma wilson room", "alma wilson"],

    "pioneer_room": ["pioneer", "pioneer room"],

    "david_f_schrage_traditions_room": ["david f. schrage traditions room", "david schrage", "traditions room", "traditions"],

    "john_houchin_room": ["john houchin room"],

    "louise_houchin_room": ["louise houchin room"],

    "david_l_boren_lounge": ["david l. boren lounge", "boren lounge", "boren room"],

    "presidents_room": ["president's room", "president room"],

    "meacham_auditorium": ["meacham auditorium", "meacham", "auditorium", "movie theatre", "movie theatre"],

    "volunteer_office": ["volunteer office"],

    "student_affairs": ["student affairs", "student affairs office", "student affairs room"],

    "conoco_student_leadership_wing": ["conoco student leadership wing", "conoco", "student leadership", "student leadership wing"],

    "beaird_lounge": ["beaird lounge", "beard lounge"],

    "flint_study_center_computer_lab": ["computer lab", "computers", "study center", "flint study center computer lab"],

    "crimson_meeting_room": ["crimson room", "crimson meeting room"],

    "bartlet_study_room": ["bartlet study room", "bartlet room", "study room"],

    "frontier_room": ["frontier room"],

    "weitzenhoffer_dining_room": ["weitzenhoffer dining room", "dining room", "weitzenhoffer room", "white zen hoffer room", "white zen four", "white zen fer"],

    "heritage_room": ["heritage room"],

    "crawford_university_club": ["crawford", "university club", "fancy restaurant"],

    "career_services": ["career services", "career service"],

    "molly_shi_boren_ballroom": ["molly shi boren ballroom", "ballroom", "molly boren room", "molly shi boren room"],

    "governors_room": ["governors' room", "governor's room", "governor room"],

    "regents_room": ["regents' room", "regent's room", "regent room"],

    "associates_room": ["associates' room", "associate's room", "associate room"],

    "scholars_room": ["scholar's room", "scholar's room", "scholars room", "scholar room"],

    "meacham_balcony": ["meacham balcony", "auditorium balcony", "movie theatre balcony", "movie theater balcony", "theatre balcony", "theater balcony"],

    "student_life": ["student life", "student life office"],

    "union_administration_and_programming_board": ["u. p. b.", "u. p. b. office", "union administration and programming board"],

    "alumni_association": ["alumni association", "alumni office"],

    "paul_massad_conference_room": ["paul massad conference room", "conference room", "massad conference room"]
}


def get_pronounceable_synonyms(canonical_name, synonyms):
    return ["the " + canonical_name.replace("_", " ")] + \
           ["the " + syn for syn in synonyms[canonical_name]] + \
           synonyms[canonical_name]