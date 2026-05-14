SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Marta s closed back room"},
                {"kind": "narrative", "text": "Marta has been holding back more than herbs. Her grandmother knew Joao s name and feared the same split sun."},
                {"kind": "npc", "npc": "Marta", "line": "Wenn du bleibst, kommt Gefahr. Wenn du gehst, folgt sie dir.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Marta", "question": "In this moment, you need the German for 'when/if'.", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "Kraut"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "when/if", "npc_reaction": "The word lands: wenn."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Marta"], "story": "Wenn turns choices into consequences.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Noch einmal: wenn. Dann Kraut.", "translation": "Again: wenn. Then Kraut.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Choose 'when/if' before the conversation moves on.", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "Kraut"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "when/if", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Now answer with 'herb'.", "options": [{"id": "a", "text": "Kraut"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_kraut", "target": "Kraut", "native": "herb", "npc_reaction": "Yes. Kraut belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You ask when to stay, when to go, and whether help is still help if it brings danger."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Jetzt brauchst du: Kraut.", "translation": "Now you need: Kraut.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "The scene waits for 'herb'.", "options": [{"id": "a", "text": "Kraut"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_kraut", "target": "Kraut", "native": "herb", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Wenn clauses are only introduced as story logic: if this, then that. No lecture, only consequence.", "explanation": "Wenn clauses are only introduced as story logic: if this, then that. No lecture, only consequence.", "examples": ["wenn", "Kraut", "helfen"]},
            "steps": [
                {"kind": "narrative", "text": "Wenn clauses are only introduced as story logic: if this, then that. No lecture, only consequence."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Hoer zu: helfen.", "translation": "Listen: helfen.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Which option carries 'help'?", "options": [{"id": "a", "text": "helfen"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "Kraut"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_helfen", "target": "helfen", "native": "help", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Marta gives you bitter Kraut and makes you name it before taking it."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'when/if'.", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "Kraut"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "when/if", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'herb'.", "options": [{"id": "a", "text": "Kraut"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "helfen"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_kraut", "target": "Kraut", "native": "herb", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'help'.", "options": [{"id": "a", "text": "helfen"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "Kraut"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_helfen", "target": "helfen", "native": "help", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Marta"], "story": "The herb pouch reacts to the word helfen and tightens shut.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Wenn du weitergehen willst: wenn. Kraut. helfen.", "translation": "If you want to move on: wenn. Kraut. helfen.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Final obstacle: choose 'help'.", "options": [{"id": "a", "text": "helfen"}, {"id": "b", "text": "wenn"}, {"id": "c", "text": "Kraut"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_helfen", "target": "helfen", "native": "help", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Greta waits outside with the truth Marta did not want to say."},
            ],
        },
    },
]
