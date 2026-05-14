SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "Frost on a rye field outside the village"},
                {"kind": "narrative", "text": "You wake between stiff stalks of rye with mud on your coat and no memory of your name. An older farmer watches from the road, but it is his son who dares to come closer."},
                {"kind": "npc", "npc": "Otto", "line": "Hallo, Fremder. You okay? My English small, but I help.", "pace": "slow"},
                {"kind": "player", "text": "You catch only pieces at first. The scene gives the words weight before it gives them comfort."},
            ],
            "exercises": [
                {"kind": "multiple_choice", "npc": "Otto", "question": "In this moment, you need the German for 'hello'.", "options": [{"id": "a", "text": "Hallo"}, {"id": "b", "text": "Ich heisse"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_hallo", "target": "Hallo", "native": "hello", "npc_reaction": "The word lands: Hallo."},
            ],
        },
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Otto"], "story": "Otto kneels in the dirt and points first to himself, then to you, making names feel like shelter.", "now": "Old words return inside the scene, not as a separate quiz."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Noch einmal: Hallo. Dann Ich heisse.", "translation": "Again: Hallo. Then Ich heisse.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Choose 'hello' before the conversation moves on.", "options": [{"id": "a", "text": "Hallo"}, {"id": "b", "text": "Ich heisse"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Nein"}], "correct": "a", "word_id": "de_hallo", "target": "Hallo", "native": "hello", "npc_reaction": "Good. The first word holds."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Now answer with 'my name is'.", "options": [{"id": "a", "text": "Ich heisse"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Bitte"}], "correct": "a", "word_id": "de_ich_heisse", "target": "Ich heisse", "native": "my name is", "npc_reaction": "Yes. Ich heisse belongs here."},
            ],
        },
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "Elias will not lead you to the village until you can answer like a person and not a ghost."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Jetzt brauchst du: Ich heisse.", "translation": "Now you need: Ich heisse.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "The scene waits for 'my name is'.", "options": [{"id": "a", "text": "Ich heisse"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Guten Morgen"}], "correct": "a", "word_id": "de_ich_heisse", "target": "Ich heisse", "native": "my name is", "npc_reaction": "The answer changes how the room treats you.", "gated": True},
            ],
        },
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "grammar": {"title": "The first pattern is identity: Ich heisse. German begins by giving you a name to stand on.", "explanation": "The first pattern is identity: Ich heisse. German begins by giving you a name to stand on.", "examples": ["Hallo", "Ich heisse", "Fremder"]},
            "steps": [
                {"kind": "narrative", "text": "The first pattern is identity: Ich heisse. German begins by giving you a name to stand on."},
                {"kind": "npc_speak", "npc": "Otto", "line": "Hoer zu: Fremder.", "translation": "Listen: Fremder.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Which option carries 'stranger'?", "options": [{"id": "a", "text": "Fremder"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Ich heisse"}, {"id": "d", "text": "Danke"}], "correct": "a", "word_id": "de_fremder", "target": "Fremder", "native": "stranger", "npc_reaction": "That pattern is enough for now. Keep moving."},
            ],
        },
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "steps": [
                {"kind": "narrative", "text": "The rye bends in the wind. Each repeated word makes the field less strange."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'hello'.", "options": [{"id": "a", "text": "Hallo"}, {"id": "b", "text": "Ich heisse"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Wo ist es?"}], "correct": "a", "word_id": "de_hallo", "target": "Hallo", "native": "hello", "npc_reaction": "Still there."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'my name is'.", "options": [{"id": "a", "text": "Ich heisse"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Fremder"}, {"id": "d", "text": "Ich komme"}], "correct": "a", "word_id": "de_ich_heisse", "target": "Ich heisse", "native": "my name is", "npc_reaction": "Good memory."},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Return to 'stranger'.", "options": [{"id": "a", "text": "Fremder"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Ich heisse"}, {"id": "d", "text": "Auf Wiedersehen"}], "correct": "a", "word_id": "de_fremder", "target": "Fremder", "native": "stranger", "npc_reaction": "Now use it."},
            ],
        },
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Otto"], "story": "At the village path, Elias stops. If you cannot greet the gatekeeper, you stay outside.", "now": "A wrong answer stalls the scene; the right word moves the plot forward."},
            "steps": [
                {"kind": "npc_speak", "npc": "Otto", "line": "Wenn du weitergehen willst: Hallo. Ich heisse. Fremder.", "translation": "If you want to move on: Hallo. Ich heisse. Fremder.", "pace": "normal"},
                {"kind": "multiple_choice", "npc": "Otto", "question": "Final obstacle: choose 'stranger'.", "options": [{"id": "a", "text": "Fremder"}, {"id": "b", "text": "Hallo"}, {"id": "c", "text": "Ich heisse"}, {"id": "d", "text": "Ich weiss nicht"}], "correct": "a", "word_id": "de_fremder", "target": "Fremder", "native": "stranger", "npc_reaction": "The word lands. The scene changes.", "gated": True},
                {"kind": "narrative", "text": "Otto walks beside you toward smoke, bells, and the smell of bread."},
            ],
        },
    },
]
