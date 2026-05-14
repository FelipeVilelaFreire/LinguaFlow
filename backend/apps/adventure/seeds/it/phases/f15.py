SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Quintal de Pietro junto a lenha"}, {"kind": "narrative", "text": "Pietro admite que viu outro estrangeiro anos antes, com outra palavra impossivel."}, {"kind": "npc", "npc": "Pietro", "line": "Sono testimone. E vero. Non era piccolo.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Pietro", "question": "Escolha em italiano: testemunha", "options": [{"id": "a", "text": "Testimone"}, {"id": "b", "text": "Vero"}, {"id": "c", "text": "Piccolo"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_testimone", "target": "Testimone", "native": "testemunha", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Pietro"], "story": "Pietro admite que viu outro estrangeiro anos antes, com outra palavra impossivel.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Pietro", "line": "Ancora: Testimone. Poi Vero.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Pietro", "question": "Volte para: testemunha", "options": [{"id": "a", "text": "Testimone"}, {"id": "b", "text": "Vero"}, {"id": "c", "text": "Piccolo"}], "correct": "a", "word_id": "it_testimone", "target": "Testimone", "native": "testemunha", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Pietro", "question": "Agora: verdadeiro", "options": [{"id": "a", "text": "Vero"}, {"id": "b", "text": "Testimone"}, {"id": "c", "text": "Piccolo"}], "correct": "a", "word_id": "it_vero", "target": "Vero", "native": "verdadeiro", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Pietro", "line": "Adesso: Vero.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Pietro", "question": "Use: verdadeiro", "options": [{"id": "a", "text": "Vero"}, {"id": "b", "text": "Testimone"}, {"id": "c", "text": "Piccolo"}], "correct": "a", "word_id": "it_vero", "target": "Vero", "native": "verdadeiro", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Testimone", "Vero", "Piccolo"]}, "steps": [{"kind": "npc_speak", "npc": "Pietro", "line": "Ascolta: Piccolo.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Pietro", "question": "Qual carrega: pequeno", "options": [{"id": "a", "text": "Piccolo"}, {"id": "b", "text": "Testimone"}, {"id": "c", "text": "Vero"}], "correct": "a", "word_id": "it_piccolo", "target": "Piccolo", "native": "pequeno", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Pietro", "question": "testemunha", "options": [{"id": "a", "text": "Testimone"}, {"id": "b", "text": "Vero"}, {"id": "c", "text": "Piccolo"}], "correct": "a", "word_id": "it_testimone", "target": "Testimone", "native": "testemunha", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Pietro", "question": "pequeno", "options": [{"id": "a", "text": "Piccolo"}, {"id": "b", "text": "Testimone"}, {"id": "c", "text": "Vero"}], "correct": "a", "word_id": "it_piccolo", "target": "Piccolo", "native": "pequeno", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Pietro"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Pietro", "line": "Se vuoi continuare: Testimone. Vero. Piccolo.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Pietro", "question": "Obstaculo final: pequeno", "options": [{"id": "a", "text": "Piccolo"}, {"id": "b", "text": "Testimone"}, {"id": "c", "text": "Vero"}], "correct": "a", "word_id": "it_piccolo", "target": "Piccolo", "native": "pequeno", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

