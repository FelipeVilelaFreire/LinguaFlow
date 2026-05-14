SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Hanna s bakery door at dawn"},
                {"kind": "narrative", "text": "Morning arrives with flour dust and oven heat. Hanna opens the bakery shutters and speaks too quickly for you to catch more than warmth and suspicion."},
                {"kind": "npc", "npc": "Hanna", "line": "Guten Morgen. Brot? Wasser? Otto, warum bringst du mir einen Fremden?", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Hanna", "question": "In this moment, you need the German for 'bread'.", "options": [{"id": "a", "text": "Brot"}, {"id": "b", "text": "Wasser"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_brot", "target": "Brot", "native": "bread", "npc_reaction": "The word lands: Brot."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Hanna"], "story": "Otto translates badly, tapping his stomach, then the water bucket, then the loaf in Hanna s hands.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Hanna", "line": "Noch einmal: Brot. Dann Wasser.", "translation": "Again: Brot. Then Wasser.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Choose 'bread' before the conversation moves on.", "options": [{"id": "a", "text": "Brot"}, {"id": "b", "text": "Wasser"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_brot", "target": "Brot", "native": "bread", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Now answer with 'water'.", "options": [{"id": "a", "text": "Wasser"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_wasser", "target": "Wasser", "native": "water", "npc_reaction": "Yes. Wasser belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You must ask for bread and water before hunger turns the lesson into panic."},
                {"kind": "npc_speak", "npc": "Hanna", "line": "Jetzt brauchst du: Wasser.", "translation": "Now you need: Wasser.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "The scene waits for 'water'.", "options": [{"id": "a", "text": "Wasser"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_wasser", "target": "Wasser", "native": "water", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "German uses haben for hunger and thirst: Ich habe Hunger, Ich habe Durst. Need is something you have.", "explanation": "German uses haben for hunger and thirst: Ich habe Hunger, Ich habe Durst. Need is something you have.", "examples": ["Brot", "Wasser", "Ich habe Hunger"]},
            "steps": [
                {"kind": "narrative", "text": "German uses haben for hunger and thirst: Ich habe Hunger, Ich habe Durst. Need is something you have."},
                {"kind": "npc_speak", "npc": "Hanna", "line": "Hoer zu: Ich habe Hunger.", "translation": "Listen: Ich habe Hunger.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Which option carries 'I am hungry'?", "options": [{"id": "a", "text": "Ich habe Hunger"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Wasser"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_ich_habe_hunger", "target": "Ich habe Hunger", "native": "I am hungry", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Hanna makes you repeat the words before she gives you the heel of the loaf."},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Return to 'bread'.", "options": [{"id": "a", "text": "Brot"}, {"id": "b", "text": "Wasser"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_brot", "target": "Brot", "native": "bread", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Return to 'water'.", "options": [{"id": "a", "text": "Wasser"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Ich habe Hunger"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_wasser", "target": "Wasser", "native": "water", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Return to 'I am hungry'.", "options": [{"id": "a", "text": "Ich habe Hunger"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Wasser"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_ich_habe_hunger", "target": "Ich habe Hunger", "native": "I am hungry", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Hanna"], "story": "A man at the next table hears your accent and starts listening. You need to answer calmly.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Hanna", "line": "Wenn du weitergehen willst: Brot. Wasser. Ich habe Hunger.", "translation": "If you want to move on: Brot. Wasser. Ich habe Hunger.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Hanna", "question": "Final obstacle: choose 'I am hungry'.", "options": [{"id": "a", "text": "Ich habe Hunger"}, {"id": "b", "text": "Brot"}, {"id": "c", "text": "Wasser"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_ich_habe_hunger", "target": "Ich habe Hunger", "native": "I am hungry", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "With bread in your coat and water on your hands, you step into the square."},
            ],
        },
    },
]
