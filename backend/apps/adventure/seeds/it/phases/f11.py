SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Sala do palazzo"}, {"kind": "narrative", "text": "Il Podesta repousa a mao perto do selo como se fosse arma."}, {"kind": "npc", "npc": "Il Podesta", "line": "Un borgo ha regole. Uno straniero le impara o parte.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Il Podesta", "question": "Escolha em italiano: selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Giudizio"}, {"id": "c", "text": "Autorita"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "Il Podesta repousa a mao perto do selo como se fosse arma.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ancora: Sigillo. Poi Giudizio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Volte para: selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Giudizio"}, {"id": "c", "text": "Autorita"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Agora: julgamento", "options": [{"id": "a", "text": "Giudizio"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Autorita"}], "correct": "a", "word_id": "it_giudizio", "target": "Giudizio", "native": "julgamento", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Il Podesta", "line": "Adesso: Giudizio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Use: julgamento", "options": [{"id": "a", "text": "Giudizio"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Autorita"}], "correct": "a", "word_id": "it_giudizio", "target": "Giudizio", "native": "julgamento", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Sigillo", "Giudizio", "Autorita"]}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ascolta: Autorita.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Qual carrega: autoridade", "options": [{"id": "a", "text": "Autorita"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Giudizio"}], "correct": "a", "word_id": "it_autorita", "target": "Autorita", "native": "autoridade", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Giudizio"}, {"id": "c", "text": "Autorita"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "autoridade", "options": [{"id": "a", "text": "Autorita"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Giudizio"}], "correct": "a", "word_id": "it_autorita", "target": "Autorita", "native": "autoridade", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Se vuoi continuare: Sigillo. Giudizio. Autorita.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Obstaculo final: autoridade", "options": [{"id": "a", "text": "Autorita"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Giudizio"}], "correct": "a", "word_id": "it_autorita", "target": "Autorita", "native": "autoridade", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

