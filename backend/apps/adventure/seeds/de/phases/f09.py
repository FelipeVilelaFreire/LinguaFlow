SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "A crowded table in Elias s kitchen"},
                {"kind": "narrative", "text": "For the first time, the group sits together: Elias silent, Otto restless, Lina writing, Marta watching what everyone refuses to say."},
                {"kind": "npc", "npc": "Marta", "line": "Suppe zuerst. Fragen danach. Wer nicht isst, denkt schlecht.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Marta", "question": "In this moment, you need the German for 'soup'.", "options": [{"id": "a", "text": "Suppe"}, {"id": "b", "text": "Tisch"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_suppe", "target": "Suppe", "native": "soup", "npc_reaction": "The word lands: Suppe."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Marta"], "story": "Food words become group words. You ask, receive, thank, and survive being looked at.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Noch einmal: Suppe. Dann Tisch.", "translation": "Again: Suppe. Then Tisch.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Choose 'soup' before the conversation moves on.", "options": [{"id": "a", "text": "Suppe"}, {"id": "b", "text": "Tisch"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_suppe", "target": "Suppe", "native": "soup", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Now answer with 'table'.", "options": [{"id": "a", "text": "Tisch"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_tisch", "target": "Tisch", "native": "table", "npc_reaction": "Yes. Tisch belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You ask for soup without sounding like a child and for the table without pointing."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Jetzt brauchst du: Tisch.", "translation": "Now you need: Tisch.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "The scene waits for 'table'.", "options": [{"id": "a", "text": "Tisch"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_tisch", "target": "Tisch", "native": "table", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Ich moechte lets need become polite. It is softer than want and safer than silence.", "explanation": "Ich moechte lets need become polite. It is softer than want and safer than silence.", "examples": ["Suppe", "Tisch", "Ich moechte"]},
            "steps": [
                {"kind": "narrative", "text": "Ich moechte lets need become polite. It is softer than want and safer than silence."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Hoer zu: Ich moechte.", "translation": "Listen: Ich moechte.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Which option carries 'I would like'?", "options": [{"id": "a", "text": "Ich moechte"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Tisch"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_ich_moechte", "target": "Ich moechte", "native": "I would like", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Each person at the table makes you ask again in a different tone."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'soup'.", "options": [{"id": "a", "text": "Suppe"}, {"id": "b", "text": "Tisch"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_suppe", "target": "Suppe", "native": "soup", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'table'.", "options": [{"id": "a", "text": "Tisch"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Ich moechte"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_tisch", "target": "Tisch", "native": "table", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'I would like'.", "options": [{"id": "a", "text": "Ich moechte"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Tisch"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_ich_moechte", "target": "Ich moechte", "native": "I would like", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Marta"], "story": "A knock hits the door. Everyone stops eating at once.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Wenn du weitergehen willst: Suppe. Tisch. Ich moechte.", "translation": "If you want to move on: Suppe. Tisch. Ich moechte.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Final obstacle: choose 'I would like'.", "options": [{"id": "a", "text": "Ich moechte"}, {"id": "b", "text": "Suppe"}, {"id": "c", "text": "Tisch"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_ich_moechte", "target": "Ich moechte", "native": "I would like", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "It is only Friedrich, but he brings news: the guard reported the fire."},
            ],
        },
    },
]
