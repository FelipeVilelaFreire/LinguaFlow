SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The crowded market square"},
                {"kind": "narrative", "text": "The square becomes a maze of apples, cloth, tin cups, and coins. Otto says the market is friendly only to people who can count."},
                {"kind": "npc", "npc": "Der Markthaendler", "line": "Eins, zwei, drei. Nicht vier. Drei Aepfel, zwei Muenzen.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "In this moment, you need the German for 'one'.", "options": [{"id": "a", "text": "eins"}, {"id": "b", "text": "zwei"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_eins", "target": "eins", "native": "one", "npc_reaction": "The word lands: eins."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Markthaendler"], "story": "The seller smiles with all his teeth and waits to see whether you know the difference between a price and a trap.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Markthaendler", "line": "Noch einmal: eins. Dann zwei.", "translation": "Again: eins. Then zwei.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Choose 'one' before the conversation moves on.", "options": [{"id": "a", "text": "eins"}, {"id": "b", "text": "zwei"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_eins", "target": "eins", "native": "one", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Now answer with 'two'.", "options": [{"id": "a", "text": "zwei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_zwei", "target": "zwei", "native": "two", "npc_reaction": "Yes. zwei belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You count apples out loud while Greta watches from her doorway."},
                {"kind": "npc_speak", "npc": "Der Markthaendler", "line": "Jetzt brauchst du: zwei.", "translation": "Now you need: zwei.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "The scene waits for 'two'.", "options": [{"id": "a", "text": "zwei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_zwei", "target": "zwei", "native": "two", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Numbers are survival grammar here. Eins, zwei, drei are small words, but they decide what you owe.", "explanation": "Numbers are survival grammar here. Eins, zwei, drei are small words, but they decide what you owe.", "examples": ["eins", "zwei", "drei"]},
            "steps": [
                {"kind": "narrative", "text": "Numbers are survival grammar here. Eins, zwei, drei are small words, but they decide what you owe."},
                {"kind": "npc_speak", "npc": "Der Markthaendler", "line": "Hoer zu: drei.", "translation": "Listen: drei.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Which option carries 'three'?", "options": [{"id": "a", "text": "drei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "zwei"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_drei", "target": "drei", "native": "three", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The seller changes the order, then the objects, then the speed."},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Return to 'one'.", "options": [{"id": "a", "text": "eins"}, {"id": "b", "text": "zwei"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_eins", "target": "eins", "native": "one", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Return to 'two'.", "options": [{"id": "a", "text": "zwei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "drei"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_zwei", "target": "zwei", "native": "two", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Return to 'three'.", "options": [{"id": "a", "text": "drei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "zwei"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_drei", "target": "drei", "native": "three", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Markthaendler"], "story": "A guard asks why Otto is buying food for a stranger.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Markthaendler", "line": "Wenn du weitergehen willst: eins. zwei. drei.", "translation": "If you want to move on: eins. zwei. drei.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Markthaendler", "question": "Final obstacle: choose 'three'.", "options": [{"id": "a", "text": "drei"}, {"id": "b", "text": "eins"}, {"id": "c", "text": "zwei"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_drei", "target": "drei", "native": "three", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Greta warns Elias in a low voice: someone is asking about the newcomer."},
            ],
        },
    },
]
