SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Greta s market stall after closing"},
                {"kind": "narrative", "text": "Greta waits until the stalls are covered and the square is empty. Then she tells you the village has two kinds of prices: coin and silence."},
                {"kind": "npc", "npc": "Greta", "line": "Geld kauft Brot. Muenzen kaufen Zeit. Wahrheit kostet mehr.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Greta", "question": "In this moment, you need the German for 'money'.", "options": [{"id": "a", "text": "Geld"}, {"id": "b", "text": "Muenze"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_geld", "target": "Geld", "native": "money", "npc_reaction": "The word lands: Geld."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Greta"], "story": "Market words return darker now. Buying is no longer about apples.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Greta", "line": "Noch einmal: Geld. Dann Muenze.", "translation": "Again: Geld. Then Muenze.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Choose 'money' before the conversation moves on.", "options": [{"id": "a", "text": "Geld"}, {"id": "b", "text": "Muenze"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_geld", "target": "Geld", "native": "money", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Now answer with 'coin'.", "options": [{"id": "a", "text": "Muenze"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_muenze", "target": "Muenze", "native": "coin", "npc_reaction": "Yes. Muenze belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn money, coin, and want while Greta decides whether to trust you with a route."},
                {"kind": "npc_speak", "npc": "Greta", "line": "Jetzt brauchst du: Muenze.", "translation": "Now you need: Muenze.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "The scene waits for 'coin'.", "options": [{"id": "a", "text": "Muenze"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_muenze", "target": "Muenze", "native": "coin", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Wollen is dangerous because it reveals desire: Ich will wissen, ich will gehen.", "explanation": "Wollen is dangerous because it reveals desire: Ich will wissen, ich will gehen.", "examples": ["Geld", "Muenze", "Ich will"]},
            "steps": [
                {"kind": "narrative", "text": "Wollen is dangerous because it reveals desire: Ich will wissen, ich will gehen."},
                {"kind": "npc_speak", "npc": "Greta", "line": "Hoer zu: Ich will.", "translation": "Listen: Ich will.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Which option carries 'I want'?", "options": [{"id": "a", "text": "Ich will"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Muenze"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_ich_will", "target": "Ich will", "native": "I want", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Greta makes you say what you want without hiding behind Otto."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'money'.", "options": [{"id": "a", "text": "Geld"}, {"id": "b", "text": "Muenze"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_geld", "target": "Geld", "native": "money", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'coin'.", "options": [{"id": "a", "text": "Muenze"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Ich will"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_muenze", "target": "Muenze", "native": "coin", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Return to 'I want'.", "options": [{"id": "a", "text": "Ich will"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Muenze"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_ich_will", "target": "Ich will", "native": "I want", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Greta"], "story": "She gives you a coin marked with the same old sign.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Greta", "line": "Wenn du weitergehen willst: Geld. Muenze. Ich will.", "translation": "If you want to move on: Geld. Muenze. Ich will.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Greta", "question": "Final obstacle: choose 'I want'.", "options": [{"id": "a", "text": "Ich will"}, {"id": "b", "text": "Geld"}, {"id": "c", "text": "Muenze"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_ich_will", "target": "Ich will", "native": "I want", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Lina recognizes the mark from the window. Elias recognizes it from the locked box."},
            ],
        },
    },
]
