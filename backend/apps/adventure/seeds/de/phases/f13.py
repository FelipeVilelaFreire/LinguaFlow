SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Otto s family kitchen"},
                {"kind": "narrative", "text": "Otto s mother sets out bowls without asking who deserves one. His little sister stares at you like you are a story that walked in from the cold."},
                {"kind": "npc", "npc": "Otto", "line": "Meine Familie. Dein Platz, for now. Sein Stuhl, do not sit, father angry.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Otto", "question": "In this moment, you need the German for 'family'.", "options": [{"id": "a", "text": "Familie"}, {"id": "b", "text": "mein"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_familie", "target": "Familie", "native": "family", "npc_reaction": "The word lands: Familie."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Otto"], "story": "Possessives arrive through chairs, bowls, names, and boundaries.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Noch einmal: Familie. Dann mein.", "translation": "Again: Familie. Then mein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Choose 'family' before the conversation moves on.", "options": [{"id": "a", "text": "Familie"}, {"id": "b", "text": "mein"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_familie", "target": "Familie", "native": "family", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Now answer with 'my'.", "options": [{"id": "a", "text": "mein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_mein", "target": "mein", "native": "my", "npc_reaction": "Yes. mein belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You explain what is yours, what is Otto s, and what belongs to nobody anymore."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Jetzt brauchst du: mein.", "translation": "Now you need: mein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "The scene waits for 'my'.", "options": [{"id": "a", "text": "mein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_mein", "target": "mein", "native": "my", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Mein, dein, sein are small claims. German makes belonging visible.", "explanation": "Mein, dein, sein are small claims. German makes belonging visible.", "examples": ["Familie", "mein", "dein"]},
            "steps": [
                {"kind": "narrative", "text": "Mein, dein, sein are small claims. German makes belonging visible."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Hoer zu: dein.", "translation": "Listen: dein.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Which option carries 'your'?", "options": [{"id": "a", "text": "dein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "mein"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_dein", "target": "dein", "native": "your", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The family corrects you gently until the words stop feeling stolen."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'family'.", "options": [{"id": "a", "text": "Familie"}, {"id": "b", "text": "mein"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_familie", "target": "Familie", "native": "family", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'my'.", "options": [{"id": "a", "text": "mein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "dein"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_mein", "target": "mein", "native": "my", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'your'.", "options": [{"id": "a", "text": "dein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "mein"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_dein", "target": "dein", "native": "your", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Otto"], "story": "A stone hits the shutter. Someone outside shouts Fremder.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Wenn du weitergehen willst: Familie. mein. dein.", "translation": "If you want to move on: Familie. mein. dein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Final obstacle: choose 'your'.", "options": [{"id": "a", "text": "dein"}, {"id": "b", "text": "Familie"}, {"id": "c", "text": "mein"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_dein", "target": "dein", "native": "your", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Elias sends everyone away from the windows and takes out the old locked box."},
            ],
        },
    },
]
