SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Village streets pretending nothing happened"},
                {"kind": "narrative", "text": "Otto insists on a normal day. Normal means directions, errands, and pretending nobody saw light answer your voice."},
                {"kind": "npc", "npc": "Otto", "line": "Links zur Schmiede, rechts zum Tor. Easy, yes? No, not easy. People watch.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Otto", "question": "In this moment, you need the German for 'left'.", "options": [{"id": "a", "text": "links"}, {"id": "b", "text": "rechts"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_links", "target": "links", "native": "left", "npc_reaction": "The word lands: links."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Otto"], "story": "He makes you choose left and right at every corner until the village map forms in your feet.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Noch einmal: links. Dann rechts.", "translation": "Again: links. Then rechts.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Choose 'left' before the conversation moves on.", "options": [{"id": "a", "text": "links"}, {"id": "b", "text": "rechts"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_links", "target": "links", "native": "left", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Now answer with 'right'.", "options": [{"id": "a", "text": "rechts"}, {"id": "b", "text": "links"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_rechts", "target": "rechts", "native": "right", "npc_reaction": "Yes. rechts belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "At the gate, the guard tests whether you belong enough to know where you are going."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Jetzt brauchst du: rechts.", "translation": "Now you need: rechts.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "The scene waits for 'right'.", "options": [{"id": "a", "text": "rechts"}, {"id": "b", "text": "links"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_rechts", "target": "rechts", "native": "right", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "German keeps the verb in second position: Heute gehe ich. Jetzt gehst du. The sentence walks with order.", "explanation": "German keeps the verb in second position: Heute gehe ich. Jetzt gehst du. The sentence walks with order.", "examples": ["links", "rechts", "Tor"]},
            "steps": [
                {"kind": "narrative", "text": "German keeps the verb in second position: Heute gehe ich. Jetzt gehst du. The sentence walks with order."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Hoer zu: Tor.", "translation": "Listen: Tor.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Which option carries 'gate'?", "options": [{"id": "a", "text": "Tor"}, {"id": "b", "text": "links"}, {"id": "c", "text": "rechts"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_tor", "target": "Tor", "native": "gate", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Otto speeds up. Links. Rechts. Tor. Platz. You keep up."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'left'.", "options": [{"id": "a", "text": "links"}, {"id": "b", "text": "rechts"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_links", "target": "links", "native": "left", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'right'.", "options": [{"id": "a", "text": "rechts"}, {"id": "b", "text": "links"}, {"id": "c", "text": "Tor"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_rechts", "target": "rechts", "native": "right", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'gate'.", "options": [{"id": "a", "text": "Tor"}, {"id": "b", "text": "links"}, {"id": "c", "text": "rechts"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_tor", "target": "Tor", "native": "gate", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Otto"], "story": "A stranger in a dark coat asks Otto your name from across the street.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Wenn du weitergehen willst: links. rechts. Tor.", "translation": "If you want to move on: links. rechts. Tor.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Final obstacle: choose 'gate'.", "options": [{"id": "a", "text": "Tor"}, {"id": "b", "text": "links"}, {"id": "c", "text": "rechts"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_tor", "target": "Tor", "native": "gate", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Otto lies badly. Lina notices the lie and writes down the stranger s coat pin."},
            ],
        },
    },
]
