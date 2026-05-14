SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Ruas do borgo tentando parecer normais"}, {"kind": "narrative", "text": "Nico insiste em um dia normal: direcoes, entregas e gente olhando demais."}, {"kind": "npc", "npc": "Nico", "line": "Sinistra, destra, cancello. Simples? Nao, nada simples.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Nico", "question": "Escolha em italiano: esquerda", "options": [{"id": "a", "text": "Sinistra"}, {"id": "b", "text": "Destra"}, {"id": "c", "text": "Cancello"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_sinistra", "target": "Sinistra", "native": "esquerda", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Nico"], "story": "Nico insiste em um dia normal: direcoes, entregas e gente olhando demais.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Ancora: Sinistra. Poi Destra.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Volte para: esquerda", "options": [{"id": "a", "text": "Sinistra"}, {"id": "b", "text": "Destra"}, {"id": "c", "text": "Cancello"}], "correct": "a", "word_id": "it_sinistra", "target": "Sinistra", "native": "esquerda", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Nico", "question": "Agora: direita", "options": [{"id": "a", "text": "Destra"}, {"id": "b", "text": "Sinistra"}, {"id": "c", "text": "Cancello"}], "correct": "a", "word_id": "it_destra", "target": "Destra", "native": "direita", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Nico", "line": "Adesso: Destra.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Use: direita", "options": [{"id": "a", "text": "Destra"}, {"id": "b", "text": "Sinistra"}, {"id": "c", "text": "Cancello"}], "correct": "a", "word_id": "it_destra", "target": "Destra", "native": "direita", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Sinistra", "Destra", "Cancello"]}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Ascolta: Cancello.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Qual carrega: portão", "options": [{"id": "a", "text": "Cancello"}, {"id": "b", "text": "Sinistra"}, {"id": "c", "text": "Destra"}], "correct": "a", "word_id": "it_cancello", "target": "Cancello", "native": "portão", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Nico", "question": "esquerda", "options": [{"id": "a", "text": "Sinistra"}, {"id": "b", "text": "Destra"}, {"id": "c", "text": "Cancello"}], "correct": "a", "word_id": "it_sinistra", "target": "Sinistra", "native": "esquerda", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Nico", "question": "portão", "options": [{"id": "a", "text": "Cancello"}, {"id": "b", "text": "Sinistra"}, {"id": "c", "text": "Destra"}], "correct": "a", "word_id": "it_cancello", "target": "Cancello", "native": "portão", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Nico"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Se vuoi continuare: Sinistra. Destra. Cancello.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Obstaculo final: portão", "options": [{"id": "a", "text": "Cancello"}, {"id": "b", "text": "Sinistra"}, {"id": "c", "text": "Destra"}], "correct": "a", "word_id": "it_cancello", "target": "Cancello", "native": "portão", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

