SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "A dark corridor behind the inn"},
                {"kind": "narrative", "text": "Night presses against the inn windows. The market guard follows you into the corridor where the lamps have gone out one by one."},
                {"kind": "npc", "npc": "Der Waechter", "line": "Halt. Kein Schritt weiter. Wer bist du wirklich?", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "In this moment, you need the German for 'fire'.", "options": [{"id": "a", "text": "Feuer"}, {"id": "b", "text": "Angst"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_feuer", "target": "Feuer", "native": "fire", "npc_reaction": "The word lands: Feuer."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Waechter"], "story": "Fear makes every German word harder to hold. Otto is not here. Elias is too far away.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Noch einmal: Feuer. Dann Angst.", "translation": "Again: Feuer. Then Angst.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Choose 'fire' before the conversation moves on.", "options": [{"id": "a", "text": "Feuer"}, {"id": "b", "text": "Angst"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_feuer", "target": "Feuer", "native": "fire", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Now answer with 'fear'.", "options": [{"id": "a", "text": "Angst"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_angst", "target": "Angst", "native": "fear", "npc_reaction": "Yes. Angst belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The guard reaches for your coat. The word for fire rises before thought can stop it."},
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Jetzt brauchst du: Angst.", "translation": "Now you need: Angst.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "The scene waits for 'fear'.", "options": [{"id": "a", "text": "Angst"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_angst", "target": "Angst", "native": "fear", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Imperatives cut through panic: Halt. Lauf. Komm. Short words become commands.", "explanation": "Imperatives cut through panic: Halt. Lauf. Komm. Short words become commands.", "examples": ["Feuer", "Angst", "Lauf!"]},
            "steps": [
                {"kind": "narrative", "text": "Imperatives cut through panic: Halt. Lauf. Komm. Short words become commands."},
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Hoer zu: Lauf!.", "translation": "Listen: Lauf!.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Which option carries 'run'?", "options": [{"id": "a", "text": "Lauf!"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Angst"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_lauf", "target": "Lauf!", "native": "run", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You say Feuer once as vocabulary, once as warning, and once as something alive."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'fire'.", "options": [{"id": "a", "text": "Feuer"}, {"id": "b", "text": "Angst"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_feuer", "target": "Feuer", "native": "fire", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'fear'.", "options": [{"id": "a", "text": "Angst"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Lauf!"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_angst", "target": "Angst", "native": "fear", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'run'.", "options": [{"id": "a", "text": "Lauf!"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Angst"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_lauf", "target": "Lauf!", "native": "run", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Waechter"], "story": "The lamp flame leaps sideways into your open hand and does not burn you.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Wenn du weitergehen willst: Feuer. Angst. Lauf!.", "translation": "If you want to move on: Feuer. Angst. Lauf!.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Final obstacle: choose 'run'.", "options": [{"id": "a", "text": "Lauf!"}, {"id": "b", "text": "Feuer"}, {"id": "c", "text": "Angst"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_lauf", "target": "Lauf!", "native": "run", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Elias pulls you into his room and bolts the door. Tomorrow, Lina must see this."},
            ],
        },
    },
]
