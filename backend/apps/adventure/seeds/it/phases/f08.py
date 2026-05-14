SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Sala de ervas de Lucia"}, {"kind": "narrative", "text": "Lucia nao pergunta se o fogo queimou. Ela pergunta de onde a palavra respondeu."}, {"kind": "npc", "npc": "Lucia", "line": "Non sei malato. Sei altro. Dammi la mano.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Lucia", "question": "Escolha em italiano: doente", "options": [{"id": "a", "text": "Malato"}, {"id": "b", "text": "Medicina"}, {"id": "c", "text": "Mano"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_malato", "target": "Malato", "native": "doente", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Lucia"], "story": "Lucia nao pergunta se o fogo queimou. Ela pergunta de onde a palavra respondeu.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ancora: Malato. Poi Medicina.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Volte para: doente", "options": [{"id": "a", "text": "Malato"}, {"id": "b", "text": "Medicina"}, {"id": "c", "text": "Mano"}], "correct": "a", "word_id": "it_malato", "target": "Malato", "native": "doente", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Agora: remédio", "options": [{"id": "a", "text": "Medicina"}, {"id": "b", "text": "Malato"}, {"id": "c", "text": "Mano"}], "correct": "a", "word_id": "it_medicina", "target": "Medicina", "native": "remédio", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Lucia", "line": "Adesso: Medicina.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Use: remédio", "options": [{"id": "a", "text": "Medicina"}, {"id": "b", "text": "Malato"}, {"id": "c", "text": "Mano"}], "correct": "a", "word_id": "it_medicina", "target": "Medicina", "native": "remédio", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Malato", "Medicina", "Mano"]}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ascolta: Mano.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Qual carrega: mão", "options": [{"id": "a", "text": "Mano"}, {"id": "b", "text": "Malato"}, {"id": "c", "text": "Medicina"}], "correct": "a", "word_id": "it_mano", "target": "Mano", "native": "mão", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "doente", "options": [{"id": "a", "text": "Malato"}, {"id": "b", "text": "Medicina"}, {"id": "c", "text": "Mano"}], "correct": "a", "word_id": "it_malato", "target": "Malato", "native": "doente", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "mão", "options": [{"id": "a", "text": "Mano"}, {"id": "b", "text": "Malato"}, {"id": "c", "text": "Medicina"}], "correct": "a", "word_id": "it_mano", "target": "Mano", "native": "mão", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Lucia"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Se vuoi continuare: Malato. Medicina. Mano.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Obstaculo final: mão", "options": [{"id": "a", "text": "Mano"}, {"id": "b", "text": "Malato"}, {"id": "c", "text": "Medicina"}], "correct": "a", "word_id": "it_mano", "target": "Mano", "native": "mão", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

