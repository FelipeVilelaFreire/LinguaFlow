SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Sala antes da audiencia"}, {"kind": "narrative", "text": "Il Podesta aceita audiencia publica porque recusar pareceria medo."}, {"kind": "npc", "npc": "Il Podesta", "line": "Se vuoi rispetto, mostra prove.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Il Podesta", "question": "Escolha em italiano: mostrar", "options": [{"id": "a", "text": "Mostrare"}, {"id": "b", "text": "Rispetto"}, {"id": "c", "text": "Se"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_mostrare", "target": "Mostrare", "native": "mostrar", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "Il Podesta aceita audiencia publica porque recusar pareceria medo.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ancora: Mostrare. Poi Rispetto.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Volte para: mostrar", "options": [{"id": "a", "text": "Mostrare"}, {"id": "b", "text": "Rispetto"}, {"id": "c", "text": "Se"}], "correct": "a", "word_id": "it_mostrare", "target": "Mostrare", "native": "mostrar", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Agora: respeito", "options": [{"id": "a", "text": "Rispetto"}, {"id": "b", "text": "Mostrare"}, {"id": "c", "text": "Se"}], "correct": "a", "word_id": "it_rispetto", "target": "Rispetto", "native": "respeito", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Il Podesta", "line": "Adesso: Rispetto.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Use: respeito", "options": [{"id": "a", "text": "Rispetto"}, {"id": "b", "text": "Mostrare"}, {"id": "c", "text": "Se"}], "correct": "a", "word_id": "it_rispetto", "target": "Rispetto", "native": "respeito", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Mostrare", "Rispetto", "Se"]}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ascolta: Se.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Qual carrega: se", "options": [{"id": "a", "text": "Se"}, {"id": "b", "text": "Mostrare"}, {"id": "c", "text": "Rispetto"}], "correct": "a", "word_id": "it_se", "target": "Se", "native": "se", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "mostrar", "options": [{"id": "a", "text": "Mostrare"}, {"id": "b", "text": "Rispetto"}, {"id": "c", "text": "Se"}], "correct": "a", "word_id": "it_mostrare", "target": "Mostrare", "native": "mostrar", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "se", "options": [{"id": "a", "text": "Se"}, {"id": "b", "text": "Mostrare"}, {"id": "c", "text": "Rispetto"}], "correct": "a", "word_id": "it_se", "target": "Se", "native": "se", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Se vuoi continuare: Mostrare. Rispetto. Se.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Obstaculo final: se", "options": [{"id": "a", "text": "Se"}, {"id": "b", "text": "Mostrare"}, {"id": "c", "text": "Rispetto"}], "correct": "a", "word_id": "it_se", "target": "Se", "native": "se", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

