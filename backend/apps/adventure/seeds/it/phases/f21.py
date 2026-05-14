SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Sala fechada de Lucia"}, {"kind": "narrative", "text": "Lucia revela que a avó conhecia o sinal e tinha medo do mesmo fogo."}, {"kind": "npc", "npc": "Lucia", "line": "Quando resti, arriva pericolo. Quando parti, ti segue.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Lucia", "question": "Escolha em italiano: quando", "options": [{"id": "a", "text": "Quando"}, {"id": "b", "text": "Erba"}, {"id": "c", "text": "Aiutare"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_quando", "target": "Quando", "native": "quando", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Lucia"], "story": "Lucia revela que a avó conhecia o sinal e tinha medo do mesmo fogo.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ancora: Quando. Poi Erba.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Volte para: quando", "options": [{"id": "a", "text": "Quando"}, {"id": "b", "text": "Erba"}, {"id": "c", "text": "Aiutare"}], "correct": "a", "word_id": "it_quando", "target": "Quando", "native": "quando", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Agora: erva", "options": [{"id": "a", "text": "Erba"}, {"id": "b", "text": "Quando"}, {"id": "c", "text": "Aiutare"}], "correct": "a", "word_id": "it_erba", "target": "Erba", "native": "erva", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Lucia", "line": "Adesso: Erba.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Use: erva", "options": [{"id": "a", "text": "Erba"}, {"id": "b", "text": "Quando"}, {"id": "c", "text": "Aiutare"}], "correct": "a", "word_id": "it_erba", "target": "Erba", "native": "erva", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Quando", "Erba", "Aiutare"]}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ascolta: Aiutare.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Qual carrega: ajudar", "options": [{"id": "a", "text": "Aiutare"}, {"id": "b", "text": "Quando"}, {"id": "c", "text": "Erba"}], "correct": "a", "word_id": "it_aiutare", "target": "Aiutare", "native": "ajudar", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "quando", "options": [{"id": "a", "text": "Quando"}, {"id": "b", "text": "Erba"}, {"id": "c", "text": "Aiutare"}], "correct": "a", "word_id": "it_quando", "target": "Quando", "native": "quando", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "ajudar", "options": [{"id": "a", "text": "Aiutare"}, {"id": "b", "text": "Quando"}, {"id": "c", "text": "Erba"}], "correct": "a", "word_id": "it_aiutare", "target": "Aiutare", "native": "ajudar", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Lucia"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Se vuoi continuare: Quando. Erba. Aiutare.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Obstaculo final: ajudar", "options": [{"id": "a", "text": "Aiutare"}, {"id": "b", "text": "Quando"}, {"id": "c", "text": "Erba"}], "correct": "a", "word_id": "it_aiutare", "target": "Aiutare", "native": "ajudar", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

