SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Elias s locked room before sunrise"},
                {"kind": "narrative", "text": "Lina arrives with ink on her fingers and disbelief already sharpened on her face. Elias tells you to repeat the word and not to lie about what happened."},
                {"kind": "npc", "npc": "Lina", "line": "Sag Feuer nicht. Sag Licht. Langsam. Ich will sehen, ob das Wort hoert.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Lina", "question": "In this moment, you need the German for 'light'.", "options": [{"id": "a", "text": "Licht"}, {"id": "b", "text": "Funke"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_licht", "target": "Licht", "native": "light", "npc_reaction": "The word lands: Licht."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Lina"], "story": "A cold lamp sits between you and Lina like a witness.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Noch einmal: Licht. Dann Funke.", "translation": "Again: Licht. Then Funke.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Choose 'light' before the conversation moves on.", "options": [{"id": "a", "text": "Licht"}, {"id": "b", "text": "Funke"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_licht", "target": "Licht", "native": "light", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Now answer with 'spark'.", "options": [{"id": "a", "text": "Funke"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_funke", "target": "Funke", "native": "spark", "npc_reaction": "Yes. Funke belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn light, spark, and lamp while everyone watches your hands instead of your mouth."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Jetzt brauchst du: Funke.", "translation": "Now you need: Funke.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "The scene waits for 'spark'.", "options": [{"id": "a", "text": "Funke"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_funke", "target": "Funke", "native": "spark", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Present tense becomes movement: ich gehe, du kommst, sie sieht. People do things; words do too.", "explanation": "Present tense becomes movement: ich gehe, du kommst, sie sieht. People do things; words do too.", "examples": ["Licht", "Funke", "Lampe"]},
            "steps": [
                {"kind": "narrative", "text": "Present tense becomes movement: ich gehe, du kommst, sie sieht. People do things; words do too."},
                {"kind": "npc_speak", "npc": "Lina", "line": "Hoer zu: Lampe.", "translation": "Listen: Lampe.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Which option carries 'lamp'?", "options": [{"id": "a", "text": "Lampe"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Funke"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_lampe", "target": "Lampe", "native": "lamp", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The lamp wick glows only after you stop performing and start meaning the word."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'light'.", "options": [{"id": "a", "text": "Licht"}, {"id": "b", "text": "Funke"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_licht", "target": "Licht", "native": "light", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'spark'.", "options": [{"id": "a", "text": "Funke"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Lampe"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_funke", "target": "Funke", "native": "spark", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Return to 'lamp'.", "options": [{"id": "a", "text": "Lampe"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Funke"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_lampe", "target": "Lampe", "native": "lamp", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Lina"], "story": "Lina steps back, then forward. She is afraid, but she believes.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lina", "line": "Wenn du weitergehen willst: Licht. Funke. Lampe.", "translation": "If you want to move on: Licht. Funke. Lampe.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Lina", "question": "Final obstacle: choose 'lamp'.", "options": [{"id": "a", "text": "Lampe"}, {"id": "b", "text": "Licht"}, {"id": "c", "text": "Funke"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_lampe", "target": "Lampe", "native": "lamp", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "She joins before breakfast, carrying paper, ink, and too many questions."},
            ],
        },
    },
]
