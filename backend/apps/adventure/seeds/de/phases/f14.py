SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Dinner in Marta s back room"},
                {"kind": "narrative", "text": "Marta feeds everyone bitter soup and makes review feel like medicine: unpleasant, necessary, precise."},
                {"kind": "npc", "npc": "Marta", "line": "Das Brot. Die Suppe. Der Tisch. Articles first, panic later.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Marta", "question": "In this moment, you need the German for 'the bread'.", "options": [{"id": "a", "text": "das Brot"}, {"id": "b", "text": "die Suppe"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_das_brot", "target": "das Brot", "native": "the bread", "npc_reaction": "The word lands: das Brot."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Marta"], "story": "This is the third review. Food, people, places, fear, fire, and names return in one room.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Noch einmal: das Brot. Dann die Suppe.", "translation": "Again: das Brot. Then die Suppe.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Choose 'the bread' before the conversation moves on.", "options": [{"id": "a", "text": "das Brot"}, {"id": "b", "text": "die Suppe"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_das_brot", "target": "das Brot", "native": "the bread", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Now answer with 'the soup'.", "options": [{"id": "a", "text": "die Suppe"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_die_suppe", "target": "die Suppe", "native": "the soup", "npc_reaction": "Yes. die Suppe belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You sort der, die, and das while Marta sorts herbs for bruises nobody admits having."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Jetzt brauchst du: die Suppe.", "translation": "Now you need: die Suppe.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "The scene waits for 'the soup'.", "options": [{"id": "a", "text": "die Suppe"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_die_suppe", "target": "die Suppe", "native": "the soup", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Articles are not decoration. They are handles. You grab the noun by the right handle.", "explanation": "Articles are not decoration. They are handles. You grab the noun by the right handle.", "examples": ["das Brot", "die Suppe", "der Tisch"]},
            "steps": [
                {"kind": "narrative", "text": "Articles are not decoration. They are handles. You grab the noun by the right handle."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Hoer zu: der Tisch.", "translation": "Listen: der Tisch.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Which option carries 'the table'?", "options": [{"id": "a", "text": "der Tisch"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "die Suppe"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_der_tisch", "target": "der Tisch", "native": "the table", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Lina turns the review into a game; Otto loses on purpose until Marta catches him."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'the bread'.", "options": [{"id": "a", "text": "das Brot"}, {"id": "b", "text": "die Suppe"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_das_brot", "target": "das Brot", "native": "the bread", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'the soup'.", "options": [{"id": "a", "text": "die Suppe"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "der Tisch"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_die_suppe", "target": "die Suppe", "native": "the soup", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'the table'.", "options": [{"id": "a", "text": "der Tisch"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "die Suppe"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_der_tisch", "target": "der Tisch", "native": "the table", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Marta"], "story": "The old mark appears under the steam on the window glass.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Wenn du weitergehen willst: das Brot. die Suppe. der Tisch.", "translation": "If you want to move on: das Brot. die Suppe. der Tisch.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Final obstacle: choose 'the table'.", "options": [{"id": "a", "text": "der Tisch"}, {"id": "b", "text": "das Brot"}, {"id": "c", "text": "die Suppe"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_der_tisch", "target": "der Tisch", "native": "the table", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Friedrich sees it and goes pale. He knows where that mark is carved."},
            ],
        },
    },
]
