SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Friedrich s yard by the woodpile"},
                {"kind": "narrative", "text": "Friedrich finally admits he saw something years ago: another stranger, another word, another impossible light."},
                {"kind": "npc", "npc": "Friedrich", "line": "Ich war Zeuge. Es ist wahr. Klein war das Feuer nicht.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "In this moment, you need the German for 'witness'.", "options": [{"id": "a", "text": "Zeuge"}, {"id": "b", "text": "wahr"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_zeuge", "target": "Zeuge", "native": "witness", "npc_reaction": "The word lands: Zeuge."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Friedrich"], "story": "Witness words make the mystery older than you.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Noch einmal: Zeuge. Dann wahr.", "translation": "Again: Zeuge. Then wahr.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Choose 'witness' before the conversation moves on.", "options": [{"id": "a", "text": "Zeuge"}, {"id": "b", "text": "wahr"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_zeuge", "target": "Zeuge", "native": "witness", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Now answer with 'true'.", "options": [{"id": "a", "text": "wahr"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_wahr", "target": "wahr", "native": "true", "npc_reaction": "Yes. wahr belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn to describe size and truth while Friedrich decides how much courage he has left."},
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Jetzt brauchst du: wahr.", "translation": "Now you need: wahr.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "The scene waits for 'true'.", "options": [{"id": "a", "text": "wahr"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_wahr", "target": "wahr", "native": "true", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Adjectives stay simple for now: klein, wahr, hoch. Enough to identify what happened.", "explanation": "Adjectives stay simple for now: klein, wahr, hoch. Enough to identify what happened.", "examples": ["Zeuge", "wahr", "klein"]},
            "steps": [
                {"kind": "narrative", "text": "Adjectives stay simple for now: klein, wahr, hoch. Enough to identify what happened."},
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Hoer zu: klein.", "translation": "Listen: klein.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Which option carries 'small'?", "options": [{"id": "a", "text": "klein"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "wahr"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_klein", "target": "klein", "native": "small", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "He makes you repeat Zeuge because testimony matters only if the word holds."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'witness'.", "options": [{"id": "a", "text": "Zeuge"}, {"id": "b", "text": "wahr"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_zeuge", "target": "Zeuge", "native": "witness", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'true'.", "options": [{"id": "a", "text": "wahr"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "klein"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_wahr", "target": "wahr", "native": "true", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Return to 'small'.", "options": [{"id": "a", "text": "klein"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "wahr"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_klein", "target": "klein", "native": "small", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Friedrich"], "story": "The guard arrives before Friedrich can finish the story.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Friedrich", "line": "Wenn du weitergehen willst: Zeuge. wahr. klein.", "translation": "If you want to move on: Zeuge. wahr. klein.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Friedrich", "question": "Final obstacle: choose 'small'.", "options": [{"id": "a", "text": "klein"}, {"id": "b", "text": "Zeuge"}, {"id": "c", "text": "wahr"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_klein", "target": "klein", "native": "small", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Friedrich lies for you, badly but bravely. That makes him your first witness."},
            ],
        },
    },
]
