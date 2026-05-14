SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Noite antes do julgamento"}, {"kind": "narrative", "text": "Ninguem dorme. Antonio ocupa as maos porque medo parado fica maior."}, {"kind": "npc", "npc": "Antonio", "line": "Devi riposare. Devi mangiare. Domani devi parlare.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Antonio", "question": "Escolha em italiano: você deve", "options": [{"id": "a", "text": "Devi"}, {"id": "b", "text": "Pronto"}, {"id": "c", "text": "Domani"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_devi", "target": "Devi", "native": "você deve", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Antonio"], "story": "Ninguem dorme. Antonio ocupa as maos porque medo parado fica maior.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Ancora: Devi. Poi Pronto.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Volte para: você deve", "options": [{"id": "a", "text": "Devi"}, {"id": "b", "text": "Pronto"}, {"id": "c", "text": "Domani"}], "correct": "a", "word_id": "it_devi", "target": "Devi", "native": "você deve", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Agora: pronto", "options": [{"id": "a", "text": "Pronto"}, {"id": "b", "text": "Devi"}, {"id": "c", "text": "Domani"}], "correct": "a", "word_id": "it_pronto", "target": "Pronto", "native": "pronto", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Antonio", "line": "Adesso: Pronto.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Use: pronto", "options": [{"id": "a", "text": "Pronto"}, {"id": "b", "text": "Devi"}, {"id": "c", "text": "Domani"}], "correct": "a", "word_id": "it_pronto", "target": "Pronto", "native": "pronto", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Devi", "Pronto", "Domani"]}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Ascolta: Domani.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Qual carrega: amanhã", "options": [{"id": "a", "text": "Domani"}, {"id": "b", "text": "Devi"}, {"id": "c", "text": "Pronto"}], "correct": "a", "word_id": "it_domani", "target": "Domani", "native": "amanhã", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "você deve", "options": [{"id": "a", "text": "Devi"}, {"id": "b", "text": "Pronto"}, {"id": "c", "text": "Domani"}], "correct": "a", "word_id": "it_devi", "target": "Devi", "native": "você deve", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "amanhã", "options": [{"id": "a", "text": "Domani"}, {"id": "b", "text": "Devi"}, {"id": "c", "text": "Pronto"}], "correct": "a", "word_id": "it_domani", "target": "Domani", "native": "amanhã", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Antonio"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Se vuoi continuare: Devi. Pronto. Domani.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Obstaculo final: amanhã", "options": [{"id": "a", "text": "Domani"}, {"id": "b", "text": "Devi"}, {"id": "c", "text": "Pronto"}], "correct": "a", "word_id": "it_domani", "target": "Domani", "native": "amanhã", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

