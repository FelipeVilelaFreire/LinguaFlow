SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "A stone wall behind the chapel"},
                {"kind": "narrative", "text": "The mark is carved behind the chapel where rain cannot reach it: a split sun, old and deliberate."},
                {"kind": "npc", "npc": "Lina", "line": "Schon hier. Nicht neu. Noch nicht verstanden.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Lina", "question": "In this moment, you need the German for 'mark'.", "options": [{"id": "a", "text": "Zeichen"}, {"id": "b", "text": "schon"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_zeichen", "target": "Zeichen", "native": "mark", "npc_reaction": "The word lands: Zeichen."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Lina"], "story": "Already and not yet become the shape of the investigation.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Noch einmal: Zeichen. Dann schon.", "translation": "Again: Zeichen. Then schon.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Choose 'mark' before the conversation moves on.", "options": [{"id": "a", "text": "Zeichen"}, {"id": "b", "text": "schon"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_zeichen", "target": "Zeichen", "native": "mark", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Now answer with 'already'.", "options": [{"id": "a", "text": "schon"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_schon", "target": "schon", "native": "already", "npc_reaction": "Yes. schon belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You compare the coin, the window mark, and the wall carving."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Jetzt brauchst du: schon.", "translation": "Now you need: schon.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "The scene waits for 'already'.", "options": [{"id": "a", "text": "schon"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_schon", "target": "schon", "native": "already", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Schon says the thing has happened. Noch nicht says the story is still holding back.", "explanation": "Schon says the thing has happened. Noch nicht says the story is still holding back.", "examples": ["Zeichen", "schon", "noch nicht"]},
            "steps": [
                {"kind": "narrative", "text": "Schon says the thing has happened. Noch nicht says the story is still holding back."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Hoer zu: noch nicht.", "translation": "Listen: noch nicht.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Which option carries 'not yet'?", "options": [{"id": "a", "text": "noch nicht"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "schon"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_noch_nicht", "target": "noch nicht", "native": "not yet", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Lina repeats both until you can feel the difference without translating."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'mark'.", "options": [{"id": "a", "text": "Zeichen"}, {"id": "b", "text": "schon"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_zeichen", "target": "Zeichen", "native": "mark", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'already'.", "options": [{"id": "a", "text": "schon"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "noch nicht"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_schon", "target": "schon", "native": "already", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'not yet'.", "options": [{"id": "a", "text": "noch nicht"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "schon"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_noch_nicht", "target": "noch nicht", "native": "not yet", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Lina"], "story": "The wall warms under your hand when you say Zeichen.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Wenn du weitergehen willst: Zeichen. schon. noch nicht.", "translation": "If you want to move on: Zeichen. schon. noch nicht.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Final obstacle: choose 'not yet'.", "options": [{"id": "a", "text": "noch nicht"}, {"id": "b", "text": "Zeichen"}, {"id": "c", "text": "schon"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_noch_nicht", "target": "noch nicht", "native": "not yet", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Elias finally opens the locked box and takes out the letter."},
            ],
        },
    },
]
