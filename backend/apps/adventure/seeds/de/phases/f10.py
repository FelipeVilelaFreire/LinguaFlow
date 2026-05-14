SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The market gate under gray rain"},
                {"kind": "narrative", "text": "The guard stands where the market narrows into the gate. Today he has two men with him and a book of names."},
                {"kind": "npc", "npc": "Der Waechter", "line": "Arbeit? Erlaubnis? Kein Name, kein Platz.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "In this moment, you need the German for 'guard'.", "options": [{"id": "a", "text": "Waechter"}, {"id": "b", "text": "Arbeit"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_waechter", "target": "Waechter", "native": "guard", "npc_reaction": "The word lands: Waechter."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Waechter"], "story": "Negation arrives as a locked door: nicht and kein decide what the village refuses you.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Noch einmal: Waechter. Dann Arbeit.", "translation": "Again: Waechter. Then Arbeit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Choose 'guard' before the conversation moves on.", "options": [{"id": "a", "text": "Waechter"}, {"id": "b", "text": "Arbeit"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_waechter", "target": "Waechter", "native": "guard", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Now answer with 'work'.", "options": [{"id": "a", "text": "Arbeit"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_arbeit", "target": "Arbeit", "native": "work", "npc_reaction": "Yes. Arbeit belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You answer questions about work, permission, and why your name is missing."},
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Jetzt brauchst du: Arbeit.", "translation": "Now you need: Arbeit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "The scene waits for 'work'.", "options": [{"id": "a", "text": "Arbeit"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_arbeit", "target": "Arbeit", "native": "work", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Nicht denies actions; kein denies things. The guard uses both like bars.", "explanation": "Nicht denies actions; kein denies things. The guard uses both like bars.", "examples": ["Waechter", "Arbeit", "Erlaubnis"]},
            "steps": [
                {"kind": "narrative", "text": "Nicht denies actions; kein denies things. The guard uses both like bars."},
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Hoer zu: Erlaubnis.", "translation": "Listen: Erlaubnis.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Which option carries 'permission'?", "options": [{"id": "a", "text": "Erlaubnis"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Arbeit"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_erlaubnis", "target": "Erlaubnis", "native": "permission", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Lina whispers examples while the guard pretends not to hear."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'guard'.", "options": [{"id": "a", "text": "Waechter"}, {"id": "b", "text": "Arbeit"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_waechter", "target": "Waechter", "native": "guard", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'work'.", "options": [{"id": "a", "text": "Arbeit"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Erlaubnis"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_arbeit", "target": "Arbeit", "native": "work", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Return to 'permission'.", "options": [{"id": "a", "text": "Erlaubnis"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Arbeit"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_erlaubnis", "target": "Erlaubnis", "native": "permission", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Waechter"], "story": "He marks a blank line in his book where your name should be.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Waechter", "line": "Wenn du weitergehen willst: Waechter. Arbeit. Erlaubnis.", "translation": "If you want to move on: Waechter. Arbeit. Erlaubnis.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Waechter", "question": "Final obstacle: choose 'permission'.", "options": [{"id": "a", "text": "Erlaubnis"}, {"id": "b", "text": "Waechter"}, {"id": "c", "text": "Arbeit"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_erlaubnis", "target": "Erlaubnis", "native": "permission", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "The next summons comes from the town hall. Der Vogt wants to see you."},
            ],
        },
    },
]
