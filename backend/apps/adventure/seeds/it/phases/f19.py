SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Carta sob luz de vela"}, {"kind": "narrative", "text": "O registro fala de Mateusz, polones, nem portugues nem italiano. Ele chegou antes e deixou aviso."}, {"kind": "npc", "npc": "Mateusz l'Altro", "line": "Alguns chegam antes. Alguns deixam cartas. Nord importa.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Escolha em italiano: carta", "options": [{"id": "a", "text": "Lettera"}, {"id": "b", "text": "Tu torni"}, {"id": "c", "text": "Nord"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_lettera", "target": "Lettera", "native": "carta", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Mateusz l'Altro"], "story": "O registro fala de Mateusz, polones, nem portugues nem italiano. Ele chegou antes e deixou aviso.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Mateusz l'Altro", "line": "Ancora: Lettera. Poi Tu torni.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Volte para: carta", "options": [{"id": "a", "text": "Lettera"}, {"id": "b", "text": "Tu torni"}, {"id": "c", "text": "Nord"}], "correct": "a", "word_id": "it_lettera", "target": "Lettera", "native": "carta", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Agora: você volta", "options": [{"id": "a", "text": "Tu torni"}, {"id": "b", "text": "Lettera"}, {"id": "c", "text": "Nord"}], "correct": "a", "word_id": "it_tu_torni", "target": "Tu torni", "native": "você volta", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Mateusz l'Altro", "line": "Adesso: Tu torni.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Use: você volta", "options": [{"id": "a", "text": "Tu torni"}, {"id": "b", "text": "Lettera"}, {"id": "c", "text": "Nord"}], "correct": "a", "word_id": "it_tu_torni", "target": "Tu torni", "native": "você volta", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Lettera", "Tu torni", "Nord"]}, "steps": [{"kind": "npc_speak", "npc": "Mateusz l'Altro", "line": "Ascolta: Nord.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Qual carrega: norte", "options": [{"id": "a", "text": "Nord"}, {"id": "b", "text": "Lettera"}, {"id": "c", "text": "Tu torni"}], "correct": "a", "word_id": "it_nord", "target": "Nord", "native": "norte", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "carta", "options": [{"id": "a", "text": "Lettera"}, {"id": "b", "text": "Tu torni"}, {"id": "c", "text": "Nord"}], "correct": "a", "word_id": "it_lettera", "target": "Lettera", "native": "carta", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "norte", "options": [{"id": "a", "text": "Nord"}, {"id": "b", "text": "Lettera"}, {"id": "c", "text": "Tu torni"}], "correct": "a", "word_id": "it_nord", "target": "Nord", "native": "norte", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Mateusz l'Altro"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Mateusz l'Altro", "line": "Se vuoi continuare: Lettera. Tu torni. Nord.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Mateusz l'Altro", "question": "Obstaculo final: norte", "options": [{"id": "a", "text": "Nord"}, {"id": "b", "text": "Lettera"}, {"id": "c", "text": "Tu torni"}], "correct": "a", "word_id": "it_nord", "target": "Nord", "native": "norte", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

