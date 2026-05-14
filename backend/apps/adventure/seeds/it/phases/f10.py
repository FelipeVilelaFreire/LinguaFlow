SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Portao do mercado sob chuva"}, {"kind": "narrative", "text": "A Guardia agora tem livro de nomes e dois homens atras dele."}, {"kind": "npc", "npc": "La Guardia", "line": "Lavoro? Permesso? Senza nome, niente posto.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "La Guardia", "question": "Escolha em italiano: guarda", "options": [{"id": "a", "text": "Guardia"}, {"id": "b", "text": "Lavoro"}, {"id": "c", "text": "Permesso"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_guardia", "target": "Guardia", "native": "guarda", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["La Guardia"], "story": "A Guardia agora tem livro de nomes e dois homens atras dele.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "La Guardia", "line": "Ancora: Guardia. Poi Lavoro.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "Volte para: guarda", "options": [{"id": "a", "text": "Guardia"}, {"id": "b", "text": "Lavoro"}, {"id": "c", "text": "Permesso"}], "correct": "a", "word_id": "it_guardia", "target": "Guardia", "native": "guarda", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "Agora: trabalho", "options": [{"id": "a", "text": "Lavoro"}, {"id": "b", "text": "Guardia"}, {"id": "c", "text": "Permesso"}], "correct": "a", "word_id": "it_lavoro", "target": "Lavoro", "native": "trabalho", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "La Guardia", "line": "Adesso: Lavoro.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "Use: trabalho", "options": [{"id": "a", "text": "Lavoro"}, {"id": "b", "text": "Guardia"}, {"id": "c", "text": "Permesso"}], "correct": "a", "word_id": "it_lavoro", "target": "Lavoro", "native": "trabalho", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Guardia", "Lavoro", "Permesso"]}, "steps": [{"kind": "npc_speak", "npc": "La Guardia", "line": "Ascolta: Permesso.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "Qual carrega: permissão", "options": [{"id": "a", "text": "Permesso"}, {"id": "b", "text": "Guardia"}, {"id": "c", "text": "Lavoro"}], "correct": "a", "word_id": "it_permesso", "target": "Permesso", "native": "permissão", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "guarda", "options": [{"id": "a", "text": "Guardia"}, {"id": "b", "text": "Lavoro"}, {"id": "c", "text": "Permesso"}], "correct": "a", "word_id": "it_guardia", "target": "Guardia", "native": "guarda", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "permissão", "options": [{"id": "a", "text": "Permesso"}, {"id": "b", "text": "Guardia"}, {"id": "c", "text": "Lavoro"}], "correct": "a", "word_id": "it_permesso", "target": "Permesso", "native": "permissão", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["La Guardia"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "La Guardia", "line": "Se vuoi continuare: Guardia. Lavoro. Permesso.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "La Guardia", "question": "Obstaculo final: permissão", "options": [{"id": "a", "text": "Permesso"}, {"id": "b", "text": "Guardia"}, {"id": "c", "text": "Lavoro"}], "correct": "a", "word_id": "it_permesso", "target": "Permesso", "native": "permissão", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

