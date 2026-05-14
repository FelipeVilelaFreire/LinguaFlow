SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Cozinha da familia de Nico"}, {"kind": "narrative", "text": "A familia de Nico coloca uma tigela para voce antes de decidir se confia."}, {"kind": "npc", "npc": "Nico", "line": "La mia famiglia. Il tuo posto, por enquanto.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Nico", "question": "Escolha em italiano: família", "options": [{"id": "a", "text": "Famiglia"}, {"id": "b", "text": "Mio"}, {"id": "c", "text": "Tuo"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_famiglia", "target": "Famiglia", "native": "família", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Nico"], "story": "A familia de Nico coloca uma tigela para voce antes de decidir se confia.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Ancora: Famiglia. Poi Mio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Volte para: família", "options": [{"id": "a", "text": "Famiglia"}, {"id": "b", "text": "Mio"}, {"id": "c", "text": "Tuo"}], "correct": "a", "word_id": "it_famiglia", "target": "Famiglia", "native": "família", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Nico", "question": "Agora: meu", "options": [{"id": "a", "text": "Mio"}, {"id": "b", "text": "Famiglia"}, {"id": "c", "text": "Tuo"}], "correct": "a", "word_id": "it_mio", "target": "Mio", "native": "meu", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Nico", "line": "Adesso: Mio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Use: meu", "options": [{"id": "a", "text": "Mio"}, {"id": "b", "text": "Famiglia"}, {"id": "c", "text": "Tuo"}], "correct": "a", "word_id": "it_mio", "target": "Mio", "native": "meu", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Famiglia", "Mio", "Tuo"]}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Ascolta: Tuo.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Qual carrega: teu", "options": [{"id": "a", "text": "Tuo"}, {"id": "b", "text": "Famiglia"}, {"id": "c", "text": "Mio"}], "correct": "a", "word_id": "it_tuo", "target": "Tuo", "native": "teu", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Nico", "question": "família", "options": [{"id": "a", "text": "Famiglia"}, {"id": "b", "text": "Mio"}, {"id": "c", "text": "Tuo"}], "correct": "a", "word_id": "it_famiglia", "target": "Famiglia", "native": "família", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Nico", "question": "teu", "options": [{"id": "a", "text": "Tuo"}, {"id": "b", "text": "Famiglia"}, {"id": "c", "text": "Mio"}], "correct": "a", "word_id": "it_tuo", "target": "Tuo", "native": "teu", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Nico"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Nico", "line": "Se vuoi continuare: Famiglia. Mio. Tuo.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Nico", "question": "Obstaculo final: teu", "options": [{"id": "a", "text": "Tuo"}, {"id": "b", "text": "Famiglia"}, {"id": "c", "text": "Mio"}], "correct": "a", "word_id": "it_tuo", "target": "Tuo", "native": "teu", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

