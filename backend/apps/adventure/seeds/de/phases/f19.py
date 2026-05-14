SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "The letter under candlelight"},
                {"kind": "narrative", "text": "The record names another foreigner: Joao. Portuguese, not English, not German. He came before you and left a warning nobody understood."},
                {"kind": "npc", "npc": "Joao der Andere", "line": "Some strangers arrive before you. Some leave messages. Norden matters.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "In this moment, you need the German for 'letter'.", "options": [{"id": "a", "text": "Brief"}, {"id": "b", "text": "du kommst zurueck"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_brief", "target": "Brief", "native": "letter", "npc_reaction": "The word lands: Brief."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Joao der Andere"], "story": "The fourth review pulls every old word into the letter: name, fire, truth, mark, north.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Joao der Andere", "line": "Noch einmal: Brief. Dann du kommst zurueck.", "translation": "Again: Brief. Then du kommst zurueck.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Choose 'letter' before the conversation moves on.", "options": [{"id": "a", "text": "Brief"}, {"id": "b", "text": "du kommst zurueck"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_brief", "target": "Brief", "native": "letter", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Now answer with 'you return'.", "options": [{"id": "a", "text": "du kommst zurueck"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_du_kommst_zurueck", "target": "du kommst zurueck", "native": "you return", "npc_reaction": "Yes. du kommst zurueck belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "You learn Brief and Norden while the ink darkens by itself."},
                {"kind": "npc_speak", "npc": "Joao der Andere", "line": "Jetzt brauchst du: du kommst zurueck.", "translation": "Now you need: du kommst zurueck.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "The scene waits for 'you return'.", "options": [{"id": "a", "text": "du kommst zurueck"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_du_kommst_zurueck", "target": "du kommst zurueck", "native": "you return", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "Zurueckkommen appears as a door in the sentence: du kommst zurueck. Return is built from motion and direction.", "explanation": "Zurueckkommen appears as a door in the sentence: du kommst zurueck. Return is built from motion and direction.", "examples": ["Brief", "du kommst zurueck", "Norden"]},
            "steps": [
                {"kind": "narrative", "text": "Zurueckkommen appears as a door in the sentence: du kommst zurueck. Return is built from motion and direction."},
                {"kind": "npc_speak", "npc": "Joao der Andere", "line": "Hoer zu: Norden.", "translation": "Listen: Norden.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Which option carries 'north'?", "options": [{"id": "a", "text": "Norden"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "du kommst zurueck"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_norden", "target": "Norden", "native": "north", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Lina copies the letter. Greta refuses to touch it."},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Return to 'letter'.", "options": [{"id": "a", "text": "Brief"}, {"id": "b", "text": "du kommst zurueck"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_brief", "target": "Brief", "native": "letter", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Return to 'you return'.", "options": [{"id": "a", "text": "du kommst zurueck"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "Norden"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_du_kommst_zurueck", "target": "du kommst zurueck", "native": "you return", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Return to 'north'.", "options": [{"id": "a", "text": "Norden"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "du kommst zurueck"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_norden", "target": "Norden", "native": "north", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Joao der Andere"], "story": "A second line almost appears, then fades before anyone can read it.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Joao der Andere", "line": "Wenn du weitergehen willst: Brief. du kommst zurueck. Norden.", "translation": "If you want to move on: Brief. du kommst zurueck. Norden.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Joao der Andere", "question": "Final obstacle: choose 'north'.", "options": [{"id": "a", "text": "Norden"}, {"id": "b", "text": "Brief"}, {"id": "c", "text": "du kommst zurueck"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_norden", "target": "Norden", "native": "north", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "The inspector arrives the next morning with men who do not answer to Der Vogt."},
            ],
        },
    },
]
