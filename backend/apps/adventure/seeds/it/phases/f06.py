SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Quarto trancado de Antonio"}, {"kind": "narrative", "text": "Chiara chega com tinta nos dedos e duvida nos olhos. Ela pede prova, nao historia."}, {"kind": "npc", "npc": "Chiara", "line": "Non dire fuoco. Di luce. Piano.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Chiara", "question": "Escolha em italiano: luz", "options": [{"id": "a", "text": "Luce"}, {"id": "b", "text": "Scintilla"}, {"id": "c", "text": "Lampada"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_luce", "target": "Luce", "native": "luz", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Chiara"], "story": "Chiara chega com tinta nos dedos e duvida nos olhos. Ela pede prova, nao historia.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ancora: Luce. Poi Scintilla.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Volte para: luz", "options": [{"id": "a", "text": "Luce"}, {"id": "b", "text": "Scintilla"}, {"id": "c", "text": "Lampada"}], "correct": "a", "word_id": "it_luce", "target": "Luce", "native": "luz", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Agora: faísca", "options": [{"id": "a", "text": "Scintilla"}, {"id": "b", "text": "Luce"}, {"id": "c", "text": "Lampada"}], "correct": "a", "word_id": "it_scintilla", "target": "Scintilla", "native": "faísca", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Chiara", "line": "Adesso: Scintilla.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Use: faísca", "options": [{"id": "a", "text": "Scintilla"}, {"id": "b", "text": "Luce"}, {"id": "c", "text": "Lampada"}], "correct": "a", "word_id": "it_scintilla", "target": "Scintilla", "native": "faísca", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Luce", "Scintilla", "Lampada"]}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Ascolta: Lampada.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Qual carrega: lâmpada", "options": [{"id": "a", "text": "Lampada"}, {"id": "b", "text": "Luce"}, {"id": "c", "text": "Scintilla"}], "correct": "a", "word_id": "it_lampada", "target": "Lampada", "native": "lâmpada", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "luz", "options": [{"id": "a", "text": "Luce"}, {"id": "b", "text": "Scintilla"}, {"id": "c", "text": "Lampada"}], "correct": "a", "word_id": "it_luce", "target": "Luce", "native": "luz", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Chiara", "question": "lâmpada", "options": [{"id": "a", "text": "Lampada"}, {"id": "b", "text": "Luce"}, {"id": "c", "text": "Scintilla"}], "correct": "a", "word_id": "it_lampada", "target": "Lampada", "native": "lâmpada", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Chiara"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Chiara", "line": "Se vuoi continuare: Luce. Scintilla. Lampada.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Chiara", "question": "Obstaculo final: lâmpada", "options": [{"id": "a", "text": "Lampada"}, {"id": "b", "text": "Luce"}, {"id": "c", "text": "Scintilla"}], "correct": "a", "word_id": "it_lampada", "target": "Lampada", "native": "lâmpada", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

