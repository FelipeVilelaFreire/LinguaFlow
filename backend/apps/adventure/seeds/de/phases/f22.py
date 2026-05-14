SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Greta s doorway after sunset"},
                {"kind": "narrative", "text": "Greta admits the village did not simply forget Joao. They chose silence because silence was cheaper than justice."},
                {"kind": "npc", "npc": "Greta", "line": "Wahrheit ist schwer. Luege ist leicht. Der Umschlag war bei mir.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Greta", "question": "In this moment, you need the German for 'truth'.", "options": [{"id": "a", "text": "Wahrheit"}, {"id": "b", "text": "Luege"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_wahrheit", "target": "Wahrheit", "native": "truth", "npc_reaction": "The word lands: Wahrheit."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Greta"], "story": "Truth and lie stop being abstract. They have names, dates, and a hidden envelope.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Greta", "line": "Noch einmal: Wahrheit. Dann Luege.", "translation": "Again: Wahrheit. Then Luege.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Choose 'truth' before the conversation moves on.", "options": [{"id": "a", "text": "Wahrheit"}, {"id": "b", "text": "Luege"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_wahrheit", "target": "Wahrheit", "native": "truth", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Now answer with 'lie'.", "options": [{"id": "a", "text": "Luege"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_luege", "target": "Luege", "native": "lie", "npc_reaction": "Yes. Luege belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn Wahrheit, Luege, and Umschlag while Greta opens the floorboard under her bed."},
                {"kind": "npc_speak", "npc": "Greta", "line": "Jetzt brauchst du: Luege.", "translation": "Now you need: Luege.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "The scene waits for 'lie'.", "options": [{"id": "a", "text": "Luege"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_luege", "target": "Luege", "native": "lie", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "German nouns make secrets feel solid. You can hold an Umschlag. You can be crushed by Wahrheit.", "explanation": "German nouns make secrets feel solid. You can hold an Umschlag. You can be crushed by Wahrheit.", "examples": ["Wahrheit", "Luege", "Umschlag"]},
            "steps": [
                {"kind": "narrative", "text": "German nouns make secrets feel solid. You can hold an Umschlag. You can be crushed by Wahrheit."},
                {"kind": "npc_speak", "npc": "Greta", "line": "Hoer zu: Umschlag.", "translation": "Listen: Umschlag.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Which option carries 'envelope'?", "options": [{"id": "a", "text": "Umschlag"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Luege"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_umschlag", "target": "Umschlag", "native": "envelope", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Greta makes you say truth before she gives you the envelope."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'truth'.", "options": [{"id": "a", "text": "Wahrheit"}, {"id": "b", "text": "Luege"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_wahrheit", "target": "Wahrheit", "native": "truth", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'lie'.", "options": [{"id": "a", "text": "Luege"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Umschlag"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_luege", "target": "Luege", "native": "lie", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'envelope'.", "options": [{"id": "a", "text": "Umschlag"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Luege"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_umschlag", "target": "Umschlag", "native": "envelope", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Greta"], "story": "Inside is a witness note signed by the old Vogt s hand.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Greta", "line": "Wenn du weitergehen willst: Wahrheit. Luege. Umschlag.", "translation": "If you want to move on: Wahrheit. Luege. Umschlag.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Final obstacle: choose 'envelope'.", "options": [{"id": "a", "text": "Umschlag"}, {"id": "b", "text": "Wahrheit"}, {"id": "c", "text": "Luege"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_umschlag", "target": "Umschlag", "native": "envelope", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Tomorrow, the current Vogt must hear it in front of everyone."},
            ],
        },
    },
]
