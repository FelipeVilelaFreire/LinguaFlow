SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The hall before the trial"},
                {"kind": "narrative", "text": "Der Vogt agrees to a public hearing because refusing would make him look afraid. He smiles like law is a knife he owns."},
                {"kind": "npc", "npc": "Der Vogt", "line": "Wenn du Respekt willst, zeig Beweise. Sonst schweig.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "In this moment, you need the German for 'show'.", "options": [{"id": "a", "text": "zeigen"}, {"id": "b", "text": "Respekt"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_zeigen", "target": "zeigen", "native": "show", "npc_reaction": "The word lands: zeigen."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "Every ally carries one word into the hall: Elias remembers, Lina records, Marta watches, Greta holds the envelope.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Noch einmal: zeigen. Dann Respekt.", "translation": "Again: zeigen. Then Respekt.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Choose 'show' before the conversation moves on.", "options": [{"id": "a", "text": "zeigen"}, {"id": "b", "text": "Respekt"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_zeigen", "target": "zeigen", "native": "show", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Now answer with 'respect'.", "options": [{"id": "a", "text": "Respekt"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_respekt", "target": "Respekt", "native": "respect", "npc_reaction": "Yes. Respekt belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn to show respect without surrendering the truth."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Jetzt brauchst du: Respekt.", "translation": "Now you need: Respekt.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "The scene waits for 'respect'.", "options": [{"id": "a", "text": "Respekt"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_respekt", "target": "Respekt", "native": "respect", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Wenn returns as condition: if you show proof, the village must answer.", "explanation": "Wenn returns as condition: if you show proof, the village must answer.", "examples": ["zeigen", "Respekt", "wenn"]},
            "steps": [
                {"kind": "narrative", "text": "Wenn returns as condition: if you show proof, the village must answer."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Hoer zu: wenn.", "translation": "Listen: wenn.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Which option carries 'if'?", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "Respekt"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "if", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The Vogt repeats zeigen as if proof were a trick. You repeat it as if proof were a door."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'show'.", "options": [{"id": "a", "text": "zeigen"}, {"id": "b", "text": "Respekt"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_zeigen", "target": "zeigen", "native": "show", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'respect'.", "options": [{"id": "a", "text": "Respekt"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "wenn"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_respekt", "target": "Respekt", "native": "respect", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'if'.", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "Respekt"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "if", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "He forbids Otto from translating for you.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Wenn du weitergehen willst: zeigen. Respekt. wenn.", "translation": "If you want to move on: zeigen. Respekt. wenn.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Final obstacle: choose 'if'.", "options": [{"id": "a", "text": "wenn"}, {"id": "b", "text": "zeigen"}, {"id": "c", "text": "Respekt"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_wenn", "target": "wenn", "native": "if", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "For the first time, you must stand without the bridge character."},
            ],
        },
    },
]
