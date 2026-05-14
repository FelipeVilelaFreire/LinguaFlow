SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Tres dias de portas fechando cedo"}, {"kind": "narrative", "text": "O prazo muda o borgo. Conversas morrem quando voce se aproxima."}, {"kind": "npc", "npc": "Chiara", "line": "Ieri fuoco. Oggi domande. Domani giudizio.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Chiara", "question": "Escolha em italiano: ontem", "options": [{"id": "a", "text": "Ieri"}, {"id": "b", "text": "Oggi"}, {"id": "c", "text": "Ho sentito"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_ieri", "target": "Ieri", "native": "ontem", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Chiara"], "story": "O prazo muda o borgo. Conversas morrem quando voce se aproxima.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ancora: Ieri. Poi Oggi.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Volte para: ontem", "options": [{"id": "a", "text": "Ieri"}, {"id": "b", "text": "Oggi"}, {"id": "c", "text": "Ho sentito"}], "correct": "a", "word_id": "it_ieri", "target": "Ieri", "native": "ontem", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Agora: hoje", "options": [{"id": "a", "text": "Oggi"}, {"id": "b", "text": "Ieri"}, {"id": "c", "text": "Ho sentito"}], "correct": "a", "word_id": "it_oggi", "target": "Oggi", "native": "hoje", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Chiara", "line": "Adesso: Oggi.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Use: hoje", "options": [{"id": "a", "text": "Oggi"}, {"id": "b", "text": "Ieri"}, {"id": "c", "text": "Ho sentito"}], "correct": "a", "word_id": "it_oggi", "target": "Oggi", "native": "hoje", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Ieri", "Oggi", "Ho sentito"]}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ascolta: Ho sentito.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Qual carrega: eu ouvi", "options": [{"id": "a", "text": "Ho sentito"}, {"id": "b", "text": "Ieri"}, {"id": "c", "text": "Oggi"}], "correct": "a", "word_id": "it_ho_sentito", "target": "Ho sentito", "native": "eu ouvi", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "ontem", "options": [{"id": "a", "text": "Ieri"}, {"id": "b", "text": "Oggi"}, {"id": "c", "text": "Ho sentito"}], "correct": "a", "word_id": "it_ieri", "target": "Ieri", "native": "ontem", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "eu ouvi", "options": [{"id": "a", "text": "Ho sentito"}, {"id": "b", "text": "Ieri"}, {"id": "c", "text": "Oggi"}], "correct": "a", "word_id": "it_ho_sentito", "target": "Ho sentito", "native": "eu ouvi", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Chiara"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Se vuoi continuare: Ieri. Oggi. Ho sentito.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Obstaculo final: eu ouvi", "options": [{"id": "a", "text": "Ho sentito"}, {"id": "b", "text": "Ieri"}, {"id": "c", "text": "Oggi"}], "correct": "a", "word_id": "it_ho_sentito", "target": "Ho sentito", "native": "eu ouvi", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

