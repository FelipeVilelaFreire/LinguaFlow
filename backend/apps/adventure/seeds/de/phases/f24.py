SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The night before judgment"},
                {"kind": "narrative", "text": "Nobody sleeps. Elias sharpens nothing, fixes nothing, and still keeps his hands busy because fear needs work."},
                {"kind": "npc", "npc": "Elias", "line": "Du sollst ruhen. Du sollst essen. Morgen sollst du sprechen.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Elias", "question": "In this moment, you need the German for 'should'.", "options": [{"id": "a", "text": "soll"}, {"id": "b", "text": "bereit"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_soll", "target": "soll", "native": "should", "npc_reaction": "The word lands: soll."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Elias"], "story": "Should is gentler than must, but tonight it feels heavier.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Elias", "line": "Noch einmal: soll. Dann bereit.", "translation": "Again: soll. Then bereit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Choose 'should' before the conversation moves on.", "options": [{"id": "a", "text": "soll"}, {"id": "b", "text": "bereit"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_soll", "target": "soll", "native": "should", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Now answer with 'ready'.", "options": [{"id": "a", "text": "bereit"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_bereit", "target": "bereit", "native": "ready", "npc_reaction": "Yes. bereit belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You prepare the words you will need when Otto cannot help."},
                {"kind": "npc_speak", "npc": "Elias", "line": "Jetzt brauchst du: bereit.", "translation": "Now you need: bereit.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "The scene waits for 'ready'.", "options": [{"id": "a", "text": "bereit"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_bereit", "target": "bereit", "native": "ready", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Sollen gives advice, duty, and expectation. It is the village voice before judgment.", "explanation": "Sollen gives advice, duty, and expectation. It is the village voice before judgment.", "examples": ["soll", "bereit", "morgen"]},
            "steps": [
                {"kind": "narrative", "text": "Sollen gives advice, duty, and expectation. It is the village voice before judgment."},
                {"kind": "npc_speak", "npc": "Elias", "line": "Hoer zu: morgen.", "translation": "Listen: morgen.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Which option carries 'tomorrow'?", "options": [{"id": "a", "text": "morgen"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "bereit"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_morgen", "target": "morgen", "native": "tomorrow", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Elias makes you say bereit until you almost believe it."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'should'.", "options": [{"id": "a", "text": "soll"}, {"id": "b", "text": "bereit"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_soll", "target": "soll", "native": "should", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'ready'.", "options": [{"id": "a", "text": "bereit"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "morgen"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_bereit", "target": "bereit", "native": "ready", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Return to 'tomorrow'.", "options": [{"id": "a", "text": "morgen"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "bereit"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_morgen", "target": "morgen", "native": "tomorrow", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Elias"], "story": "The old letter shows a pale second word, then hides it again.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Elias", "line": "Wenn du weitergehen willst: soll. bereit. morgen.", "translation": "If you want to move on: soll. bereit. morgen.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Elias", "question": "Final obstacle: choose 'tomorrow'.", "options": [{"id": "a", "text": "morgen"}, {"id": "b", "text": "soll"}, {"id": "c", "text": "bereit"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_morgen", "target": "morgen", "native": "tomorrow", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "At sunrise, bells call the whole village to the gate."},
            ],
        },
    },
]
