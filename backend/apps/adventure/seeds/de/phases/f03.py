SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The dirt road beyond the north gate"},
                {"kind": "narrative", "text": "Friedrich the woodcutter waits by the ditch with an axe over one shoulder. He says the village teaches walls, but the forest teaches warnings."},
                {"kind": "npc", "npc": "Friedrich", "line": "Der Wald ist alt. Der Stein auch. Hier hoert man besser.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "In this moment, you need the German for 'the forest'.", "options": [{"id": "a", "text": "der Wald"}, {"id": "b", "text": "der Stein"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_der_wald", "target": "der Wald", "native": "the forest", "npc_reaction": "The word lands: der Wald."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Friedrich"], "story": "He points to the forest, a stone, and the ground under your boots, forcing the articles to attach to real things.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Noch einmal: der Wald. Dann der Stein.", "translation": "Again: der Wald. Then der Stein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Choose 'the forest' before the conversation moves on.", "options": [{"id": "a", "text": "der Wald"}, {"id": "b", "text": "der Stein"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_der_wald", "target": "der Wald", "native": "the forest", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Now answer with 'the stone'.", "options": [{"id": "a", "text": "der Stein"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_der_stein", "target": "der Stein", "native": "the stone", "npc_reaction": "Yes. der Stein belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "A mark carved into bark matches the half-burned sign you saw in a dream."},
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Jetzt brauchst du: der Stein.", "translation": "Now you need: der Stein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "The scene waits for 'the stone'.", "options": [{"id": "a", "text": "der Stein"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_der_stein", "target": "der Stein", "native": "the stone", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Articles arrive as names with weight: der Wald, der Stein, das Tor. Do not master all gender today; notice it.", "explanation": "Articles arrive as names with weight: der Wald, der Stein, das Tor. Do not master all gender today; notice it.", "examples": ["der Wald", "der Stein", "hier"]},
            "steps": [
                {"kind": "narrative", "text": "Articles arrive as names with weight: der Wald, der Stein, das Tor. Do not master all gender today; notice it."},
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Hoer zu: hier.", "translation": "Listen: hier.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Which option carries 'here'?", "options": [{"id": "a", "text": "hier"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "der Stein"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_hier", "target": "hier", "native": "here", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Friedrich asks again and again until Wald no longer sounds like noise."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'the forest'.", "options": [{"id": "a", "text": "der Wald"}, {"id": "b", "text": "der Stein"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_der_wald", "target": "der Wald", "native": "the forest", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'the stone'.", "options": [{"id": "a", "text": "der Stein"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "hier"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_der_stein", "target": "der Stein", "native": "the stone", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'here'.", "options": [{"id": "a", "text": "hier"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "der Stein"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_hier", "target": "hier", "native": "here", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Friedrich"], "story": "On the way back, hoofprints cross the path. Someone followed you out.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Wenn du weitergehen willst: der Wald. der Stein. hier.", "translation": "If you want to move on: der Wald. der Stein. hier.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Final obstacle: choose 'here'.", "options": [{"id": "a", "text": "hier"}, {"id": "b", "text": "der Wald"}, {"id": "c", "text": "der Stein"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_hier", "target": "hier", "native": "here", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Friedrich gives you a river stone and says Elias should see it."},
            ],
        },
    },
]
