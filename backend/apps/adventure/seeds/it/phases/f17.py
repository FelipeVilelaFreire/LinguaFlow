SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Muro atras da capela"}, {"kind": "narrative", "text": "Chiara encontra o sinal antigo onde a chuva nao apaga."}, {"kind": "npc", "npc": "Chiara", "line": "Gia qui. Non nuovo. Non ancora capito.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Chiara", "question": "Escolha em italiano: marca", "options": [{"id": "a", "text": "Segno"}, {"id": "b", "text": "Gia"}, {"id": "c", "text": "Non ancora"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_segno", "target": "Segno", "native": "marca", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Chiara"], "story": "Chiara encontra o sinal antigo onde a chuva nao apaga.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ancora: Segno. Poi Gia.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Volte para: marca", "options": [{"id": "a", "text": "Segno"}, {"id": "b", "text": "Gia"}, {"id": "c", "text": "Non ancora"}], "correct": "a", "word_id": "it_segno", "target": "Segno", "native": "marca", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Agora: já", "options": [{"id": "a", "text": "Gia"}, {"id": "b", "text": "Segno"}, {"id": "c", "text": "Non ancora"}], "correct": "a", "word_id": "it_gia", "target": "Gia", "native": "já", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Chiara", "line": "Adesso: Gia.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Use: já", "options": [{"id": "a", "text": "Gia"}, {"id": "b", "text": "Segno"}, {"id": "c", "text": "Non ancora"}], "correct": "a", "word_id": "it_gia", "target": "Gia", "native": "já", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Segno", "Gia", "Non ancora"]}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ascolta: Non ancora.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Qual carrega: ainda não", "options": [{"id": "a", "text": "Non ancora"}, {"id": "b", "text": "Segno"}, {"id": "c", "text": "Gia"}], "correct": "a", "word_id": "it_non_ancora", "target": "Non ancora", "native": "ainda não", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "marca", "options": [{"id": "a", "text": "Segno"}, {"id": "b", "text": "Gia"}, {"id": "c", "text": "Non ancora"}], "correct": "a", "word_id": "it_segno", "target": "Segno", "native": "marca", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "ainda não", "options": [{"id": "a", "text": "Non ancora"}, {"id": "b", "text": "Segno"}, {"id": "c", "text": "Gia"}], "correct": "a", "word_id": "it_non_ancora", "target": "Non ancora", "native": "ainda não", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Chiara"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Se vuoi continuare: Segno. Gia. Non ancora.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Obstaculo final: ainda não", "options": [{"id": "a", "text": "Non ancora"}, {"id": "b", "text": "Segno"}, {"id": "c", "text": "Gia"}], "correct": "a", "word_id": "it_non_ancora", "target": "Non ancora", "native": "ainda não", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

