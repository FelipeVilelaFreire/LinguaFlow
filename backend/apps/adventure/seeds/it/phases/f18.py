SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Caixa antiga de Antonio aberta"}, {"kind": "narrative", "text": "Antonio tira uma carta que deveria ter queimado e finalmente escolhe culpa em vez de silencio."}, {"kind": "npc", "npc": "Antonio", "line": "Non posso dire tutto. Ma devo cominciare.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Antonio", "question": "Escolha em italiano: lembrar", "options": [{"id": "a", "text": "Ricordare"}, {"id": "b", "text": "Passato"}, {"id": "c", "text": "Segreto"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_ricordare", "target": "Ricordare", "native": "lembrar", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Antonio"], "story": "Antonio tira uma carta que deveria ter queimado e finalmente escolhe culpa em vez de silencio.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Ancora: Ricordare. Poi Passato.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Volte para: lembrar", "options": [{"id": "a", "text": "Ricordare"}, {"id": "b", "text": "Passato"}, {"id": "c", "text": "Segreto"}], "correct": "a", "word_id": "it_ricordare", "target": "Ricordare", "native": "lembrar", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Agora: passado", "options": [{"id": "a", "text": "Passato"}, {"id": "b", "text": "Ricordare"}, {"id": "c", "text": "Segreto"}], "correct": "a", "word_id": "it_passato", "target": "Passato", "native": "passado", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Antonio", "line": "Adesso: Passato.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Use: passado", "options": [{"id": "a", "text": "Passato"}, {"id": "b", "text": "Ricordare"}, {"id": "c", "text": "Segreto"}], "correct": "a", "word_id": "it_passato", "target": "Passato", "native": "passado", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Ricordare", "Passato", "Segreto"]}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Ascolta: Segreto.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Qual carrega: segredo", "options": [{"id": "a", "text": "Segreto"}, {"id": "b", "text": "Ricordare"}, {"id": "c", "text": "Passato"}], "correct": "a", "word_id": "it_segreto", "target": "Segreto", "native": "segredo", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "lembrar", "options": [{"id": "a", "text": "Ricordare"}, {"id": "b", "text": "Passato"}, {"id": "c", "text": "Segreto"}], "correct": "a", "word_id": "it_ricordare", "target": "Ricordare", "native": "lembrar", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Antonio", "question": "segredo", "options": [{"id": "a", "text": "Segreto"}, {"id": "b", "text": "Ricordare"}, {"id": "c", "text": "Passato"}], "correct": "a", "word_id": "it_segreto", "target": "Segreto", "native": "segredo", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Antonio"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Antonio", "line": "Se vuoi continuare: Ricordare. Passato. Segreto.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Antonio", "question": "Obstaculo final: segredo", "options": [{"id": "a", "text": "Segreto"}, {"id": "b", "text": "Ricordare"}, {"id": "c", "text": "Passato"}], "correct": "a", "word_id": "it_segreto", "target": "Segreto", "native": "segredo", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

