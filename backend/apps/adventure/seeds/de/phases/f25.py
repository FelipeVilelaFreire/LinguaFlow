SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The gate under the whole village s eyes"},
                {"kind": "narrative", "text": "The whole village gathers at the gate. Otto stands behind the crowd, forbidden to help. Greta holds the envelope. Der Vogt holds the seal."},
                {"kind": "npc", "npc": "Der Vogt", "line": "Letztes Wort, Fremder. Siegel, Urteil, Dorf. Sprich.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "In this moment, you need the German for 'seal'.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Bruder"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "The word lands: Siegel."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "Every word you learned returns under pressure: name, bread, fire, truth, proof, respect.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Noch einmal: Siegel. Dann Bruder.", "translation": "Again: Siegel. Then Bruder.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Choose 'seal' before the conversation moves on.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Bruder"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Now answer with 'brother'.", "options": [{"id": "a", "text": "Bruder"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_bruder", "target": "Bruder", "native": "brother", "npc_reaction": "Yes. Bruder belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You answer in German because the village must hear you without a bridge."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Jetzt brauchst du: Bruder.", "translation": "Now you need: Bruder.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "The scene waits for 'brother'.", "options": [{"id": "a", "text": "Bruder"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_bruder", "target": "Bruder", "native": "brother", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "The boss phase is synthesis. Articles, modals, wenn, perfect, and memory all appear as action.", "explanation": "The boss phase is synthesis. Articles, modals, wenn, perfect, and memory all appear as action.", "examples": ["Siegel", "Bruder", "Willkommen"]},
            "steps": [
                {"kind": "narrative", "text": "The boss phase is synthesis. Articles, modals, wenn, perfect, and memory all appear as action."},
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Hoer zu: Willkommen.", "translation": "Listen: Willkommen.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Which option carries 'welcome'?", "options": [{"id": "a", "text": "Willkommen"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Bruder"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_willkommen", "target": "Willkommen", "native": "welcome", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The seal waits. The envelope opens. The old lie loses its shape."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'seal'.", "options": [{"id": "a", "text": "Siegel"}, {"id": "b", "text": "Bruder"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_siegel", "target": "Siegel", "native": "seal", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'brother'.", "options": [{"id": "a", "text": "Bruder"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Willkommen"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_bruder", "target": "Bruder", "native": "brother", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Return to 'welcome'.", "options": [{"id": "a", "text": "Willkommen"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Bruder"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_willkommen", "target": "Willkommen", "native": "welcome", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Der Vogt"], "story": "When you say Bruder, the second word on the letter burns clear.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Der Vogt", "line": "Wenn du weitergehen willst: Siegel. Bruder. Willkommen.", "translation": "If you want to move on: Siegel. Bruder. Willkommen.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Der Vogt", "question": "Final obstacle: choose 'welcome'.", "options": [{"id": "a", "text": "Willkommen"}, {"id": "b", "text": "Siegel"}, {"id": "c", "text": "Bruder"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_willkommen", "target": "Willkommen", "native": "welcome", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "You win the seal, but the road north becomes more important than staying safe."},
            ],
        },
    },
]
