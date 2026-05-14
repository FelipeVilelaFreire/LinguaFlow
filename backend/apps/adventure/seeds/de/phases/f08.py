SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Marta s herb room"},
                {"kind": "narrative", "text": "Marta s room smells of dried leaves, vinegar, and old smoke. She does not ask whether the fire hurt. She asks where it answered from."},
                {"kind": "npc", "npc": "Marta", "line": "Du bist krank? Nein. Nicht krank. Anders. Gib mir die Hand.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Marta", "question": "In this moment, you need the German for 'sick'.", "options": [{"id": "a", "text": "krank"}, {"id": "b", "text": "Medizin"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_krank", "target": "krank", "native": "sick", "npc_reaction": "The word lands: krank."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Marta"], "story": "She teaches body words like she is checking a wound under the language.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Noch einmal: krank. Dann Medizin.", "translation": "Again: krank. Then Medizin.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Choose 'sick' before the conversation moves on.", "options": [{"id": "a", "text": "krank"}, {"id": "b", "text": "Medizin"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_krank", "target": "krank", "native": "sick", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Now answer with 'remedy'.", "options": [{"id": "a", "text": "Medizin"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_medizin", "target": "Medizin", "native": "remedy", "npc_reaction": "Yes. Medizin belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You must tell her what hurts, what does not, and what you fear touching."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Jetzt brauchst du: Medizin.", "translation": "Now you need: Medizin.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "The scene waits for 'remedy'.", "options": [{"id": "a", "text": "Medizin"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_medizin", "target": "Medizin", "native": "remedy", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Accusative appears softly: die Hand sehen, den Kopf halten. The scene needs objects, not tables.", "explanation": "Accusative appears softly: die Hand sehen, den Kopf halten. The scene needs objects, not tables.", "examples": ["krank", "Medizin", "Hand"]},
            "steps": [
                {"kind": "narrative", "text": "Accusative appears softly: die Hand sehen, den Kopf halten. The scene needs objects, not tables."},
                {"kind": "npc_speak", "npc": "Marta", "line": "Hoer zu: Hand.", "translation": "Listen: Hand.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Which option carries 'hand'?", "options": [{"id": "a", "text": "Hand"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Medizin"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_hand", "target": "Hand", "native": "hand", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Marta repeats krank, Medizin, Hand until Otto stops joking."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'sick'.", "options": [{"id": "a", "text": "krank"}, {"id": "b", "text": "Medizin"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_krank", "target": "krank", "native": "sick", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'remedy'.", "options": [{"id": "a", "text": "Medizin"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Hand"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_medizin", "target": "Medizin", "native": "remedy", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Return to 'hand'.", "options": [{"id": "a", "text": "Hand"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Medizin"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_hand", "target": "Hand", "native": "hand", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Marta"], "story": "When you say Hand, the dried herbs tremble toward your palm.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Marta", "line": "Wenn du weitergehen willst: krank. Medizin. Hand.", "translation": "If you want to move on: krank. Medizin. Hand.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Marta", "question": "Final obstacle: choose 'hand'.", "options": [{"id": "a", "text": "Hand"}, {"id": "b", "text": "krank"}, {"id": "c", "text": "Medizin"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_hand", "target": "Hand", "native": "hand", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Marta packs a pouch and joins because she has seen this before in old notes."},
            ],
        },
    },
]
