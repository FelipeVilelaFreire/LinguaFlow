SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Mesa apertada na casa de Antonio"}, {"kind": "narrative", "text": "Antonio, Nico, Chiara e Lucia sentam juntos pela primeira vez. A sopa pesa mais que silencio."}, {"kind": "npc", "npc": "Lucia", "line": "Zuppa prima. Domande dopo.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Lucia", "question": "Escolha em italiano: sopa", "options": [{"id": "a", "text": "Zuppa"}, {"id": "b", "text": "Tavola"}, {"id": "c", "text": "Voglio"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_zuppa", "target": "Zuppa", "native": "sopa", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Lucia"], "story": "Antonio, Nico, Chiara e Lucia sentam juntos pela primeira vez. A sopa pesa mais que silencio.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ancora: Zuppa. Poi Tavola.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Volte para: sopa", "options": [{"id": "a", "text": "Zuppa"}, {"id": "b", "text": "Tavola"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_zuppa", "target": "Zuppa", "native": "sopa", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Agora: mesa", "options": [{"id": "a", "text": "Tavola"}, {"id": "b", "text": "Zuppa"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_tavola", "target": "Tavola", "native": "mesa", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Lucia", "line": "Adesso: Tavola.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Use: mesa", "options": [{"id": "a", "text": "Tavola"}, {"id": "b", "text": "Zuppa"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_tavola", "target": "Tavola", "native": "mesa", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Zuppa", "Tavola", "Voglio"]}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ascolta: Voglio.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Qual carrega: eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Zuppa"}, {"id": "c", "text": "Tavola"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "sopa", "options": [{"id": "a", "text": "Zuppa"}, {"id": "b", "text": "Tavola"}, {"id": "c", "text": "Voglio"}], "correct": "a", "word_id": "it_zuppa", "target": "Zuppa", "native": "sopa", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Zuppa"}, {"id": "c", "text": "Tavola"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Lucia"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Se vuoi continuare: Zuppa. Tavola. Voglio.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Obstaculo final: eu quero", "options": [{"id": "a", "text": "Voglio"}, {"id": "b", "text": "Zuppa"}, {"id": "c", "text": "Tavola"}], "correct": "a", "word_id": "it_voglio", "target": "Voglio", "native": "eu quero", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

