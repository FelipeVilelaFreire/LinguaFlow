SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Elias s room with the old box open"},
                {"kind": "narrative", "text": "Inside the box are a dry flower, a rusted key, and a letter Elias says he should have burned years ago."},
                {"kind": "npc", "npc": "Elias", "line": "Ich kann nicht alles sagen. Ich muss aber anfangen.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Elias", "question": "In this moment, you need the German for 'remember'.", "options": [{"id": "a", "text": "erinnern"}, {"id": "b", "text": "Vergangenheit"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_erinnern", "target": "erinnern", "native": "remember", "npc_reaction": "The word lands: erinnern."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Elias"], "story": "Can and must arrive as confession. Elias is not teaching grammar; he is choosing guilt.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Elias", "line": "Noch einmal: erinnern. Dann Vergangenheit.", "translation": "Again: erinnern. Then Vergangenheit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Choose 'remember' before the conversation moves on.", "options": [{"id": "a", "text": "erinnern"}, {"id": "b", "text": "Vergangenheit"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_erinnern", "target": "erinnern", "native": "remember", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Now answer with 'past'.", "options": [{"id": "a", "text": "Vergangenheit"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_vergangenheit", "target": "Vergangenheit", "native": "past", "npc_reaction": "Yes. Vergangenheit belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You ask what he remembers, what he can say, and what he must still hide."},
                {"kind": "npc_speak", "npc": "Elias", "line": "Jetzt brauchst du: Vergangenheit.", "translation": "Now you need: Vergangenheit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "The scene waits for 'past'.", "options": [{"id": "a", "text": "Vergangenheit"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_vergangenheit", "target": "Vergangenheit", "native": "past", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Koennen and muessen carry power and obligation. They explain why people delay the truth.", "explanation": "Koennen and muessen carry power and obligation. They explain why people delay the truth.", "examples": ["erinnern", "Vergangenheit", "Geheimnis"]},
            "steps": [
                {"kind": "narrative", "text": "Koennen and muessen carry power and obligation. They explain why people delay the truth."},
                {"kind": "npc_speak", "npc": "Elias", "line": "Hoer zu: Geheimnis.", "translation": "Listen: Geheimnis.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Which option carries 'secret'?", "options": [{"id": "a", "text": "Geheimnis"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Vergangenheit"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_geheimnis", "target": "Geheimnis", "native": "secret", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The old farmer repeats Vergangenheit like it hurts his mouth."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'remember'.", "options": [{"id": "a", "text": "erinnern"}, {"id": "b", "text": "Vergangenheit"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_erinnern", "target": "erinnern", "native": "remember", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'past'.", "options": [{"id": "a", "text": "Vergangenheit"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Geheimnis"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_vergangenheit", "target": "Vergangenheit", "native": "past", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'secret'.", "options": [{"id": "a", "text": "Geheimnis"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Vergangenheit"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_geheimnis", "target": "Geheimnis", "native": "secret", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Elias"], "story": "The first word on the letter appears only when you read it aloud.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Elias", "line": "Wenn du weitergehen willst: erinnern. Vergangenheit. Geheimnis.", "translation": "If you want to move on: erinnern. Vergangenheit. Geheimnis.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Final obstacle: choose 'secret'.", "options": [{"id": "a", "text": "Geheimnis"}, {"id": "b", "text": "erinnern"}, {"id": "c", "text": "Vergangenheit"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_geheimnis", "target": "Geheimnis", "native": "secret", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Lina sees the word VUELVES in old ink and says it is not German."},
            ],
        },
    },
]
