SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Banca fechada de Bianca"}, {"kind": "narrative", "text": "Bianca espera o mercado esvaziar para dizer que silencio tambem tem preco."}, {"kind": "npc", "npc": "Bianca", "line": "Denaro compra pane. Moneta compra tempo. Verita costa di piu.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Bianca", "question": "Escolha em italiano: dinheiro", "options": [{"id": "a", "text": "Denaro"}, {"id": "b", "text": "Moneta"}, {"id": "c", "text": "Voglio"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_denaro", "target": "Denaro", "native": "dinheiro", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Bianca"], "story": "Bianca espera o mercado esvaziar para dizer que silencio tambem tem preco.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Ancora: Denaro. Poi Moneta.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Volte para: dinheiro", "options": [{"id": "a", "text": "Denaro"}, {"id": "b", "text": "Moneta"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_denaro", "target": "Denaro", "native": "dinheiro", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Agora: moeda", "options": [{"id": "a", "text": "Moneta"}, {"id": "b", "text": "Denaro"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_moneta", "target": "Moneta", "native": "moeda", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Bianca", "line": "Adesso: Moneta.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Use: moeda", "options": [{"id": "a", "text": "Moneta"}, {"id": "b", "text": "Denaro"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_moneta", "target": "Moneta", "native": "moeda", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Denaro", "Moneta", "Voglio"]}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Ascolta: Voglio.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Qual carrega: eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Denaro"}, {"id": "c", "text": "Moneta"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "dinheiro", "options": [{"id": "a", "text": "Denaro"}, {"id": "b", "text": "Moneta"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_denaro", "target": "Denaro", "native": "dinheiro", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Bianca", "question": "eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Denaro"}, {"id": "c", "text": "Moneta"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Bianca"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Bianca", "line": "Se vuoi continuare: Denaro. Moneta. Voglio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Bianca", "question": "Obstaculo final: eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Denaro"}, {"id": "c", "text": "Moneta"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

