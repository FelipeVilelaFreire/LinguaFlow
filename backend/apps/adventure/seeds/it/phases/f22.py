SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Porta de Bianca depois do por do sol"}, {"kind": "narrative", "text": "Bianca confessa que o borgo escolheu silencio porque justica custava caro."}, {"kind": "npc", "npc": "Bianca", "line": "Verita pesa. Bugia vola. La busta era da me.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Bianca", "question": "Escolha em italiano: verdade", "options": [{"id": "a", "text": "Verita"}, {"id": "b", "text": "Bugia"}, {"id": "c", "text": "Busta"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_verita", "target": "Verita", "native": "verdade", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Bianca"], "story": "Bianca confessa que o borgo escolheu silencio porque justica custava caro.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Ancora: Verita. Poi Bugia.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Volte para: verdade", "options": [{"id": "a", "text": "Verita"}, {"id": "b", "text": "Bugia"}, {"id": "c", "text": "Busta"}], "correct": "a", "word_id": "it_verita", "target": "Verita", "native": "verdade", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Agora: mentira", "options": [{"id": "a", "text": "Bugia"}, {"id": "b", "text": "Verita"}, {"id": "c", "text": "Busta"}], "correct": "a", "word_id": "it_bugia", "target": "Bugia", "native": "mentira", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Bianca", "line": "Adesso: Bugia.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Use: mentira", "options": [{"id": "a", "text": "Bugia"}, {"id": "b", "text": "Verita"}, {"id": "c", "text": "Busta"}], "correct": "a", "word_id": "it_bugia", "target": "Bugia", "native": "mentira", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Verita", "Bugia", "Busta"]}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Ascolta: Busta.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Qual carrega: envelope", "options": [{"id": "a", "text": "Busta"}, {"id": "b", "text": "Verita"}, {"id": "c", "text": "Bugia"}], "correct": "a", "word_id": "it_busta", "target": "Busta", "native": "envelope", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "verdade", "options": [{"id": "a", "text": "Verita"}, {"id": "b", "text": "Bugia"}, {"id": "c", "text": "Busta"}], "correct": "a", "word_id": "it_verita", "target": "Verita", "native": "verdade", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "envelope", "options": [{"id": "a", "text": "Busta"}, {"id": "b", "text": "Verita"}, {"id": "c", "text": "Bugia"}], "correct": "a", "word_id": "it_busta", "target": "Busta", "native": "envelope", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Bianca"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Se vuoi continuare: Verita. Bugia. Busta.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Obstaculo final: envelope", "options": [{"id": "a", "text": "Busta"}, {"id": "b", "text": "Verita"}, {"id": "c", "text": "Bugia"}], "correct": "a", "word_id": "it_busta", "target": "Busta", "native": "envelope", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

