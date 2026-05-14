SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Three tense days across the village"},
                {"kind": "narrative", "text": "The village changes when a deadline enters it. Doors close earlier. Conversations stop when you approach."},
                {"kind": "npc", "npc": "Lina", "line": "Gestern hast du Feuer gesagt. Heute fragt jeder. Morgen entscheidet der Vogt.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Lina", "question": "In this moment, you need the German for 'yesterday'.", "options": [{"id": "a", "text": "gestern"}, {"id": "b", "text": "heute"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_gestern", "target": "gestern", "native": "yesterday", "npc_reaction": "The word lands: gestern."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Lina"], "story": "Time words become a cage: yesterday, today, tomorrow.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Noch einmal: gestern. Dann heute.", "translation": "Again: gestern. Then heute.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Choose 'yesterday' before the conversation moves on.", "options": [{"id": "a", "text": "gestern"}, {"id": "b", "text": "heute"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_gestern", "target": "gestern", "native": "yesterday", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Now answer with 'today'.", "options": [{"id": "a", "text": "heute"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_heute", "target": "heute", "native": "today", "npc_reaction": "Yes. heute belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Lina makes you report what you heard, because rumors are now evidence."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Jetzt brauchst du: heute.", "translation": "Now you need: heute.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "The scene waits for 'today'.", "options": [{"id": "a", "text": "heute"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_heute", "target": "heute", "native": "today", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "The perfect tense appears as testimony: ich habe es gehoert. You do not master the past; you survive it.", "explanation": "The perfect tense appears as testimony: ich habe es gehoert. You do not master the past; you survive it.", "examples": ["gestern", "heute", "ich habe es gehoert"]},
            "steps": [
                {"kind": "narrative", "text": "The perfect tense appears as testimony: ich habe es gehoert. You do not master the past; you survive it."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Hoer zu: ich habe es gehoert.", "translation": "Listen: ich habe es gehoert.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Which option carries 'I heard'?", "options": [{"id": "a", "text": "ich habe es gehoert"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "heute"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_ich_habe_es_gehoert", "target": "ich habe es gehoert", "native": "I heard", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Every repeated phrase becomes part of the record Lina is building."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'yesterday'.", "options": [{"id": "a", "text": "gestern"}, {"id": "b", "text": "heute"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_gestern", "target": "gestern", "native": "yesterday", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'today'.", "options": [{"id": "a", "text": "heute"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "ich habe es gehoert"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_heute", "target": "heute", "native": "today", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'I heard'.", "options": [{"id": "a", "text": "ich habe es gehoert"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "heute"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_ich_habe_es_gehoert", "target": "ich habe es gehoert", "native": "I heard", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Lina"], "story": "Someone claims you threatened the guard before the fire. That is a lie.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Wenn du weitergehen willst: gestern. heute. ich habe es gehoert.", "translation": "If you want to move on: gestern. heute. ich habe es gehoert.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Final obstacle: choose 'I heard'.", "options": [{"id": "a", "text": "ich habe es gehoert"}, {"id": "b", "text": "gestern"}, {"id": "c", "text": "heute"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_ich_habe_es_gehoert", "target": "ich habe es gehoert", "native": "I heard", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Otto says his family will speak for you, even if it costs them."},
            ],
        },
    },
]
