SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Estrada por onde o inspetor chega"}, {"kind": "narrative", "text": "L'Ispettore entra no borgo com homens uniformizados e paciencia nenhuma."}, {"kind": "npc", "npc": "L'Ispettore", "line": "Io devo chiedere. Voi dovete rispondere.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Escolha em italiano: eu devo", "options": [{"id": "a", "text": "Devo"}, {"id": "b", "text": "Andare"}, {"id": "c", "text": "Ispettore"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_devo", "target": "Devo", "native": "eu devo", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["L'Ispettore"], "story": "L'Ispettore entra no borgo com homens uniformizados e paciencia nenhuma.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "L'Ispettore", "line": "Ancora: Devo. Poi Andare.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Volte para: eu devo", "options": [{"id": "a", "text": "Devo"}, {"id": "b", "text": "Andare"}, {"id": "c", "text": "Ispettore"}], "correct": "a", "word_id": "it_devo", "target": "Devo", "native": "eu devo", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Agora: ir", "options": [{"id": "a", "text": "Andare"}, {"id": "b", "text": "Devo"}, {"id": "c", "text": "Ispettore"}], "correct": "a", "word_id": "it_andare", "target": "Andare", "native": "ir", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "L'Ispettore", "line": "Adesso: Andare.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Use: ir", "options": [{"id": "a", "text": "Andare"}, {"id": "b", "text": "Devo"}, {"id": "c", "text": "Ispettore"}], "correct": "a", "word_id": "it_andare", "target": "Andare", "native": "ir", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Devo", "Andare", "Ispettore"]}, "steps": [{"kind": "npc_speak", "npc": "L'Ispettore", "line": "Ascolta: Ispettore.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Qual carrega: inspetor", "options": [{"id": "a", "text": "Ispettore"}, {"id": "b", "text": "Devo"}, {"id": "c", "text": "Andare"}], "correct": "a", "word_id": "it_ispettore", "target": "Ispettore", "native": "inspetor", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "eu devo", "options": [{"id": "a", "text": "Devo"}, {"id": "b", "text": "Andare"}, {"id": "c", "text": "Ispettore"}], "correct": "a", "word_id": "it_devo", "target": "Devo", "native": "eu devo", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "inspetor", "options": [{"id": "a", "text": "Ispettore"}, {"id": "b", "text": "Devo"}, {"id": "c", "text": "Andare"}], "correct": "a", "word_id": "it_ispettore", "target": "Ispettore", "native": "inspetor", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["L'Ispettore"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "L'Ispettore", "line": "Se vuoi continuare: Devo. Andare. Ispettore.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "L'Ispettore", "question": "Obstaculo final: inspetor", "options": [{"id": "a", "text": "Ispettore"}, {"id": "b", "text": "Devo"}, {"id": "c", "text": "Andare"}], "correct": "a", "word_id": "it_ispettore", "target": "Ispettore", "native": "inspetor", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

