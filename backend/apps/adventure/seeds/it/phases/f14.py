SECTIONS = [
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {"beats": [{"kind": "scene", "text": "Janta nos fundos da casa de Lucia"}, {"kind": "narrative", "text": "Lucia transforma revisao em medicina amarga: artigo por artigo, palavra por palavra."}, {"kind": "npc", "npc": "Lucia", "line": "Il pane. La zuppa. La tavola. Prima gli articoli.", "pace": "slow"}], "exercises": [{"kind": "multiple_choice", "npc": "Lucia", "question": "Escolha em italiano: o pão", "options": [{"id": "a", "text": "Il pane"}, {"id": "b", "text": "La zuppa"}, {"id": "c", "text": "La tavola"}, {"id": "d", "text": "Non lo so"}], "correct": "a", "word_id": "it_il_pane", "target": "Il pane", "native": "o pão", "npc_reaction": "A palavra encaixa na cena."}]},
    },
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {"recap": {"characters": ["Lucia"], "story": "Lucia transforma revisao em medicina amarga: artigo por artigo, palavra por palavra.", "now": "As palavras antigas voltam dentro da cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ancora: Il pane. Poi La zuppa.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Volte para: o pão", "options": [{"id": "a", "text": "Il pane"}, {"id": "b", "text": "La zuppa"}, {"id": "c", "text": "La tavola"}], "correct": "a", "word_id": "it_il_pane", "target": "Il pane", "native": "o pão", "npc_reaction": "Isso. Continua."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Agora: a sopa", "options": [{"id": "a", "text": "La zuppa"}, {"id": "b", "text": "Il pane"}, {"id": "c", "text": "La tavola"}], "correct": "a", "word_id": "it_la_zuppa", "target": "La zuppa", "native": "a sopa", "npc_reaction": "Boa memoria."}]},
    },
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {"steps": [{"kind": "narrative", "text": "A cena exige a palavra antes de deixar voce passar."}, {"kind": "npc_speak", "npc": "Lucia", "line": "Adesso: La zuppa.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Use: a sopa", "options": [{"id": "a", "text": "La zuppa"}, {"id": "b", "text": "Il pane"}, {"id": "c", "text": "La tavola"}], "correct": "a", "word_id": "it_la_zuppa", "target": "La zuppa", "native": "a sopa", "npc_reaction": "A resposta muda o clima.", "gated": True}]},
    },
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {"grammar": {"title": "Padrao italiano da fase", "explanation": "A gramatica aparece pela necessidade da cena, nao como aula solta.", "examples": ["Il pane", "La zuppa", "La tavola"]}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Ascolta: La tavola.", "pace": "slow"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Qual carrega: a mesa", "options": [{"id": "a", "text": "La tavola"}, {"id": "b", "text": "Il pane"}, {"id": "c", "text": "La zuppa"}], "correct": "a", "word_id": "it_la_tavola", "target": "La tavola", "native": "a mesa", "npc_reaction": "O padrao basta por agora."}]},
    },
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {"steps": [{"kind": "narrative", "text": "O borgo testa se as palavras continuam vivas enquanto a historia anda."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "o pão", "options": [{"id": "a", "text": "Il pane"}, {"id": "b", "text": "La zuppa"}, {"id": "c", "text": "La tavola"}], "correct": "a", "word_id": "it_il_pane", "target": "Il pane", "native": "o pão", "npc_reaction": "Ainda esta ai."}, {"kind": "multiple_choice", "npc": "Lucia", "question": "a mesa", "options": [{"id": "a", "text": "La tavola"}, {"id": "b", "text": "Il pane"}, {"id": "c", "text": "La zuppa"}], "correct": "a", "word_id": "it_la_tavola", "target": "La tavola", "native": "a mesa", "npc_reaction": "Agora use."}]},
    },
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {"recap": {"characters": ["Lucia"], "story": "A fase fecha com uma escolha pequena e consequencia grande.", "now": "Errar trava; acertar move a cena."}, "steps": [{"kind": "npc_speak", "npc": "Lucia", "line": "Se vuoi continuare: Il pane. La zuppa. La tavola.", "pace": "normal"}, {"kind": "multiple_choice", "npc": "Lucia", "question": "Obstaculo final: a mesa", "options": [{"id": "a", "text": "La tavola"}, {"id": "b", "text": "Il pane"}, {"id": "c", "text": "La zuppa"}], "correct": "a", "word_id": "it_la_tavola", "target": "La tavola", "native": "a mesa", "npc_reaction": "A palavra abre caminho.", "gated": True}, {"kind": "narrative", "text": "A estrada norte continua esperando."}]},
    },
]

