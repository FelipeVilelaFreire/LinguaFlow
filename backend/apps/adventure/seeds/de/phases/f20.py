SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The road where the inspector arrives"},
                {"kind": "narrative", "text": "Der Inspektor enters the village in a clean coat, with three uniformed men and no patience for village superstition."},
                {"kind": "npc", "npc": "Der Inspektor", "line": "Ich muss fragen. Sie muessen antworten. Danach sehen wir weiter.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "In this moment, you need the German for 'I must'.", "options": [{"id": "a", "text": "Ich muss"}, {"id": "b", "text": "gehen"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_ich_muss", "target": "Ich muss", "native": "I must", "npc_reaction": "The word lands: Ich muss."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Inspektor"], "story": "Must becomes a chain. Everyone suddenly has obligations.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Inspektor", "line": "Noch einmal: Ich muss. Dann gehen.", "translation": "Again: Ich muss. Then gehen.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Choose 'I must' before the conversation moves on.", "options": [{"id": "a", "text": "Ich muss"}, {"id": "b", "text": "gehen"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_ich_muss", "target": "Ich muss", "native": "I must", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Now answer with 'go'.", "options": [{"id": "a", "text": "gehen"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_gehen", "target": "gehen", "native": "go", "npc_reaction": "Yes. gehen belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You answer what you must do, where you must go, and who the inspector is."},
                {"kind": "npc_speak", "npc": "Der Inspektor", "line": "Jetzt brauchst du: gehen.", "translation": "Now you need: gehen.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "The scene waits for 'go'.", "options": [{"id": "a", "text": "gehen"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_gehen", "target": "gehen", "native": "go", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Muessen pushes the infinitive to the end: Ich muss gehen. The pressure waits at the end too.", "explanation": "Muessen pushes the infinitive to the end: Ich muss gehen. The pressure waits at the end too.", "examples": ["Ich muss", "gehen", "Inspektor"]},
            "steps": [
                {"kind": "narrative", "text": "Muessen pushes the infinitive to the end: Ich muss gehen. The pressure waits at the end too."},
                {"kind": "npc_speak", "npc": "Der Inspektor", "line": "Hoer zu: Inspektor.", "translation": "Listen: Inspektor.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Which option carries 'inspector'?", "options": [{"id": "a", "text": "Inspektor"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "gehen"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_inspektor", "target": "Inspektor", "native": "inspector", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Otto whispers answers until the inspector tells him to be silent."},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Return to 'I must'.", "options": [{"id": "a", "text": "Ich muss"}, {"id": "b", "text": "gehen"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_ich_muss", "target": "Ich muss", "native": "I must", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Return to 'go'.", "options": [{"id": "a", "text": "gehen"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "Inspektor"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_gehen", "target": "gehen", "native": "go", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Return to 'inspector'.", "options": [{"id": "a", "text": "Inspektor"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "gehen"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_inspektor", "target": "Inspektor", "native": "inspector", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Inspektor"], "story": "The inspector asks for the letter. Elias says no.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Inspektor", "line": "Wenn du weitergehen willst: Ich muss. gehen. Inspektor.", "translation": "If you want to move on: Ich muss. gehen. Inspektor.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Inspektor", "question": "Final obstacle: choose 'inspector'.", "options": [{"id": "a", "text": "Inspektor"}, {"id": "b", "text": "Ich muss"}, {"id": "c", "text": "gehen"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_inspektor", "target": "Inspektor", "native": "inspector", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Marta closes her door that night and asks you to come alone."},
            ],
        },
    },
]
