SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Portao diante de todo o borgo"}, {"kind": "narrative", "text": "Todo o borgo se junta. Nico nao pode traduzir. Chiara segura as anotacoes. O selo espera."}, {"kind": "npc", "npc": "Il Podesta", "line": "Ultima parola, straniero. Sigillo, giudizio, borgo.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Il Podesta", "question": "Escolha em italiano: selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Fratello"}, {"id": "c", "text": "Benvenuto"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "Todo o borgo se junta. Nico nao pode traduzir. Chiara segura as anotacoes. O selo espera.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ancora: Sigillo. Poi Fratello.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Volte para: selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Fratello"}, {"id": "c", "text": "Benvenuto"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Agora: irmão", "options": [{"id": "a", "text": "Fratello"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Benvenuto"}], "correct": "a", "word_id": "it_fratello", "target": "Fratello", "native": "irmão", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Il Podesta", "line": "Adesso: Fratello.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Use: irmão", "options": [{"id": "a", "text": "Fratello"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Benvenuto"}], "correct": "a", "word_id": "it_fratello", "target": "Fratello", "native": "irmão", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Sigillo", "Fratello", "Benvenuto"]}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Ascolta: Benvenuto.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Qual carrega: bem-vindo", "options": [{"id": "a", "text": "Benvenuto"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Fratello"}], "correct": "a", "word_id": "it_benvenuto", "target": "Benvenuto", "native": "bem-vindo", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "selo", "options": [{"id": "a", "text": "Sigillo"}, {"id": "b", "text": "Fratello"}, {"id": "c", "text": "Benvenuto"}], "correct": "a", "word_id": "it_sigillo", "target": "Sigillo", "native": "selo", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "bem-vindo", "options": [{"id": "a", "text": "Benvenuto"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Fratello"}], "correct": "a", "word_id": "it_benvenuto", "target": "Benvenuto", "native": "bem-vindo", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Il Podesta"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Il Podesta", "line": "Se vuoi continuare: Sigillo. Fratello. Benvenuto.", "pace": "urgent"}, {"kind": "multiple_choice", "npc": "Il Podesta", "question": "Obstaculo final: bem-vindo", "options": [{"id": "a", "text": "Benvenuto"}, {"id": "b", "text": "Sigillo"}, {"id": "c", "text": "Fratello"}], "correct": "a", "word_id": "it_benvenuto", "target": "Benvenuto", "native": "bem-vindo", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

