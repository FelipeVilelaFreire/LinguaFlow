SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The town hall chamber"},
                {"kind": "narrative", "text": "Der Vogt sits beneath a carved beam blackened by age. His seal lies on the desk like a small red eye."},
                {"kind": "npc", "npc": "Der Vogt", "line": "Ein Dorf hat Regeln. Ein Fremder lernt sie, oder er geht.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "In this moment, you need the German for 'seal'.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Urteil"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "The word lands: Siegel."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "He speaks slowly because he wants every word to land as law.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Noch einmal: Siegel. Dann Urteil.", "translation": "Again: Siegel. Then Urteil.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Choose 'seal' before the conversation moves on.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Urteil"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Now answer with 'judgment'.", "options": [{"id": "a", "text": "Urteil"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_urteil", "target": "Urteil", "native": "judgment", "npc_reaction": "Yes. Urteil belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn seal, judgment, and authority while he decides whether you are a person or a problem."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Jetzt brauchst du: Urteil.", "translation": "Now you need: Urteil.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "The scene waits for 'judgment'.", "options": [{"id": "a", "text": "Urteil"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_urteil", "target": "Urteil", "native": "judgment", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Future intent appears as threat and promise: ich werde fragen, du wirst antworten.", "explanation": "Future intent appears as threat and promise: ich werde fragen, du wirst antworten.", "examples": ["Siegel", "Urteil", "Macht"]},
            "steps": [
                {"kind": "narrative", "text": "Future intent appears as threat and promise: ich werde fragen, du wirst antworten."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Hoer zu: Macht.", "translation": "Listen: Macht.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Which option carries 'authority'?", "options": [{"id": "a", "text": "Macht"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Urteil"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_macht", "target": "Macht", "native": "authority", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Greta stands in the back, saying nothing, but she watches the seal."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'seal'.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Urteil"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'judgment'.", "options": [{"id": "a", "text": "Urteil"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Macht"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_urteil", "target": "Urteil", "native": "judgment", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'authority'.", "options": [{"id": "a", "text": "Macht"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Urteil"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_macht", "target": "Macht", "native": "authority", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "Der Vogt gives you three days to prove you are not dangerous.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Wenn du weitergehen willst: Siegel. Urteil. Macht.", "translation": "If you want to move on: Siegel. Urteil. Macht.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Final obstacle: choose 'authority'.", "options": [{"id": "a", "text": "Macht"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Urteil"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_macht", "target": "Macht", "native": "authority", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Outside, Lina writes the deadline at the top of a clean page."},
            ],
        },
    },
]
