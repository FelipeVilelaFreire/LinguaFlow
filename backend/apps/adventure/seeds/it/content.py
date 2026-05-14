from apps.adventure.models import AdventureItem


SOURCE_LANGUAGE = {"code": "PT", "name": "PortuguÃªs", "is_ready": False}
TARGET_LANGUAGE = {"code": "IT", "name": "Italiano", "is_ready": True}

CHAPTER = {
    "slug": "it-a1-t1",
    "level": "A1",
    "order": 3,
    "title": "Il Borgo",
    "subtitle": "T1 - A chegada",
    "background": "it_borgo",
    "boss_name": "Il Podesta",
    "boss_intro": "O homem que controla o selo do borgo. Ninguem segue pela estrada norte sem a permissao dele.",
    "reward_name": "Sigillo del Borgo",
    "reward_description": "Cera vermelha, papel antigo. Prova que voce sobreviveu ao borgo e as regras dele.",
}

SCENARIOS = [
    ("it-sociale", "Sociale", "Saudacoes, nomes e convivencia."),
    ("it-luoghi", "Luoghi", "Direcoes, ruas, praca e estrada."),
    ("it-cibo", "Cibo", "Comida, sede, fome e mesa."),
    ("it-mercato", "Mercato", "Precos, moedas e compras."),
    ("it-salute", "Salute", "Corpo, cansaco, remedios e cuidado."),
    ("it-lavoro", "Lavoro", "Oficios, rotina e obrigacoes."),
    ("it-memoria", "Memoria", "Passado, carta, familia e segredo."),
    ("it-prova", "Prova", "Conflito, autoridade, julgamento e boss."),
]

PHRASES = [
    ("OlÃ¡", "Ciao", "it-sociale"),
    ("Bom dia", "Buongiorno", "it-sociale"),
    ("Boa noite", "Buonasera", "it-sociale"),
    ("Meu nome Ã©", "Mi chiamo", "it-sociale"),
    ("Como vocÃª se chama?", "Come ti chiami?", "it-sociale"),
    ("Por favor", "Per favore", "it-sociale"),
    ("Obrigado", "Grazie", "it-sociale"),
    ("Sim", "Si", "it-sociale"),
    ("NÃ£o", "No", "it-sociale"),
    ("Amigo", "Amico", "it-sociale"),
    ("Forasteiro", "Straniero", "it-sociale"),
    ("Onde fica?", "Dov'e?", "it-luoghi"),
    ("Aqui", "Qui", "it-luoghi"),
    ("Ali", "Li", "it-luoghi"),
    ("Esquerda", "Sinistra", "it-luoghi"),
    ("Direita", "Destra", "it-luoghi"),
    ("A praÃ§a", "La piazza", "it-luoghi"),
    ("O portÃ£o", "Il cancello", "it-luoghi"),
    ("A estrada", "La strada", "it-luoghi"),
    ("Estou com fome", "Ho fame", "it-cibo"),
    ("Estou com sede", "Ho sete", "it-cibo"),
    ("Ãgua", "Acqua", "it-cibo"),
    ("PÃ£o", "Pane", "it-cibo"),
    ("Sopa", "Zuppa", "it-cibo"),
    ("MaÃ§Ã£", "Mela", "it-cibo"),
    ("Quero comer", "Voglio mangiare", "it-cibo"),
    ("Quanto custa?", "Quanto costa?", "it-mercato"),
    ("Caro", "Caro", "it-mercato"),
    ("Barato", "Economico", "it-mercato"),
    ("Dinheiro", "Denaro", "it-mercato"),
    ("Moeda", "Moneta", "it-mercato"),
    ("Um", "Uno", "it-mercato"),
    ("Dois", "Due", "it-mercato"),
    ("TrÃªs", "Tre", "it-mercato"),
    ("Estou doente", "Sono malato", "it-salute"),
    ("DÃ³i aqui", "Mi fa male qui", "it-salute"),
    ("RemÃ©dio", "Medicina", "it-salute"),
    ("MÃ£o", "Mano", "it-salute"),
    ("CabeÃ§a", "Testa", "it-salute"),
    ("Trabalho", "Lavoro", "it-lavoro"),
    ("Guarda", "Guardia", "it-lavoro"),
    ("Preciso ir", "Devo andare", "it-lavoro"),
    ("Posso ajudar", "Posso aiutare", "it-lavoro"),
    ("NÃ£o me lembro", "Non ricordo", "it-memoria"),
    ("Meu passado", "Il mio passato", "it-memoria"),
    ("Segredo", "Segreto", "it-memoria"),
    ("Verdade", "Verita", "it-memoria"),
    ("Mentira", "Bugia", "it-memoria"),
    ("IrmÃ£o", "Fratello", "it-memoria"),
    ("Prova", "Prova", "it-prova"),
    ("Mostrar", "Mostrare", "it-prova"),
    ("Respeito", "Rispetto", "it-prova"),
    ("Julgamento", "Giudizio", "it-prova"),
    ("Selo", "Sigillo", "it-prova"),
    ("Fogo", "Fuoco", "it-prova"),
    ("Bem-vindo", "Benvenuto", "it-prova"),
]

PHASES = [
    {"number": 1, "phase_type": "story", "title": "O Despertar no Campo", "scenario_slug": "it-sociale", "phrase_count": 8, "key_words": ["ciao", "mi chiamo", "straniero"], "new": [("olÃ¡", "Ciao"), ("meu nome Ã©", "Mi chiamo"), ("forasteiro", "Straniero")]},
    {"number": 2, "phase_type": "story", "title": "Il Borgo Desperta", "scenario_slug": "it-cibo", "phrase_count": 8, "key_words": ["pane", "acqua", "fame"], "new": [("pÃ£o", "Pane"), ("Ã¡gua", "Acqua"), ("estou com fome", "Ho fame")]},
    {"number": 3, "phase_type": "story", "title": "La Strada di Terra", "scenario_slug": "it-luoghi", "phrase_count": 8, "key_words": ["strada", "pietra", "qui"], "new": [("a estrada", "La strada"), ("pedra", "Pietra"), ("aqui", "Qui")]},
    {"number": 4, "phase_type": "story", "title": "Il Mercato", "scenario_slug": "it-mercato", "phrase_count": 8, "key_words": ["uno", "due", "tre"], "new": [("um", "Uno"), ("dois", "Due"), ("trÃªs", "Tre")]},
    {"number": 5, "phase_type": "story", "title": "La Prima Scintilla", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["fuoco", "paura", "corri"], "new": [("fogo", "Fuoco"), ("medo", "Paura"), ("corra", "Corri!")]},
    {"number": 6, "phase_type": "story", "title": "O Que Chiara Viu", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["luce", "scintilla", "lampada"], "new": [("luz", "Luce"), ("faÃ­sca", "Scintilla"), ("lÃ¢mpada", "Lampada")]},
    {"number": 7, "phase_type": "story", "title": "Un Giorno Normale", "scenario_slug": "it-luoghi", "phrase_count": 8, "key_words": ["sinistra", "destra", "cancello"], "new": [("esquerda", "Sinistra"), ("direita", "Destra"), ("portÃ£o", "Cancello")]},
    {"number": 8, "phase_type": "story", "title": "La Guaritrice", "scenario_slug": "it-salute", "phrase_count": 8, "key_words": ["malato", "medicina", "mano"], "new": [("doente", "Malato"), ("remÃ©dio", "Medicina"), ("mÃ£o", "Mano")]},
    {"number": 9, "phase_type": "story", "title": "Quattro a Tavola", "scenario_slug": "it-cibo", "phrase_count": 8, "key_words": ["zuppa", "tavola", "voglio"], "new": [("sopa", "Zuppa"), ("mesa", "Tavola"), ("eu quero", "Voglio")]},
    {"number": 10, "phase_type": "story", "title": "L'Ombra della Guardia", "scenario_slug": "it-lavoro", "phrase_count": 8, "key_words": ["guardia", "lavoro", "permesso"], "new": [("guarda", "Guardia"), ("trabalho", "Lavoro"), ("permissÃ£o", "Permesso")]},
    {"number": 11, "phase_type": "story", "title": "Il Palazzo", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["podesta", "sigillo", "giudizio"], "new": [("selo", "Sigillo"), ("julgamento", "Giudizio"), ("autoridade", "Autorita")]},
    {"number": 12, "phase_type": "story", "title": "Tre Giorni", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["ieri", "oggi", "domani"], "new": [("ontem", "Ieri"), ("hoje", "Oggi"), ("eu ouvi", "Ho sentito")]},
    {"number": 13, "phase_type": "story", "title": "A Familia de Nico", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["famiglia", "mio", "tuo"], "new": [("famÃ­lia", "Famiglia"), ("meu", "Mio"), ("teu", "Tuo")]},
    {"number": 14, "phase_type": "review", "title": "A Janta de Lucia", "scenario_slug": "it-cibo", "phrase_count": 8, "key_words": ["il", "la", "lo"], "new": [("o pÃ£o", "Il pane"), ("a sopa", "La zuppa"), ("a mesa", "La tavola")]},
    {"number": 15, "phase_type": "story", "title": "A Primeira Testemunha", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["testimone", "vero", "piccolo"], "new": [("testemunha", "Testimone"), ("verdadeiro", "Vero"), ("pequeno", "Piccolo")]},
    {"number": 16, "phase_type": "story", "title": "O Aviso de Bianca", "scenario_slug": "it-mercato", "phrase_count": 8, "key_words": ["denaro", "moneta", "voglio"], "new": [("dinheiro", "Denaro"), ("moeda", "Moneta"), ("eu quero", "Voglio")]},
    {"number": 17, "phase_type": "story", "title": "Il Segno", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["segno", "gia", "non ancora"], "new": [("marca", "Segno"), ("jÃ¡", "Gia"), ("ainda nÃ£o", "Non ancora")]},
    {"number": 18, "phase_type": "story", "title": "Antonio Lembra", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["ricordo", "passato", "segreto"], "new": [("lembrar", "Ricordare"), ("passado", "Passato"), ("segredo", "Segreto")]},
    {"number": 19, "phase_type": "review", "title": "A Carta Abre", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["lettera", "torni", "nord"], "new": [("carta", "Lettera"), ("vocÃª volta", "Tu torni"), ("norte", "Nord")]},
    {"number": 20, "phase_type": "story", "title": "L'Ispettore", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["ispettore", "devo", "andare"], "new": [("eu devo", "Devo"), ("ir", "Andare"), ("inspetor", "Ispettore")]},
    {"number": 21, "phase_type": "story", "title": "Encarando Lucia", "scenario_slug": "it-salute", "phrase_count": 8, "key_words": ["quando", "erba", "aiutare"], "new": [("quando", "Quando"), ("erva", "Erba"), ("ajudar", "Aiutare")]},
    {"number": 22, "phase_type": "story", "title": "A Verdade de Bianca", "scenario_slug": "it-memoria", "phrase_count": 8, "key_words": ["verita", "bugia", "busta"], "new": [("verdade", "Verita"), ("mentira", "Bugia"), ("envelope", "Busta")]},
    {"number": 23, "phase_type": "story", "title": "Diante do Podesta", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["se", "mostrare", "rispetto"], "new": [("mostrar", "Mostrare"), ("respeito", "Rispetto"), ("se", "Se")]},
    {"number": 24, "phase_type": "story", "title": "A Vespera", "scenario_slug": "it-lavoro", "phrase_count": 8, "key_words": ["devi", "pronto", "domani"], "new": [("vocÃª deve", "Devi"), ("pronto", "Pronto"), ("amanhÃ£", "Domani")]},
    {"number": 25, "phase_type": "boss", "title": "Giudizio al Cancello", "scenario_slug": "it-prova", "phrase_count": 8, "key_words": ["sigillo", "fratello", "benvenuto"], "new": [("selo", "Sigillo"), ("irmÃ£o", "Fratello"), ("bem-vindo", "Benvenuto")]},
]

CHARACTERS = [
    ("antonio_contadino", "Antonio il Contadino", "Contadino", "ðŸŒ¾", "ally", True, 1, 1, "Um campones mais velho que fala devagar e protege antes de confiar.", "Passo dopo passo, amico."),
    ("nico", "Nico", "Figlio del contadino", "ðŸ§‘â€ðŸŒ¾", "ally", True, 1, 2, "Filho de Antonio, ponte do jogador, fala portugues quebrado e italiano rapido.", "Fica perto de mim, straniero."),
    ("giulia_fornaia", "Giulia la Fornaia", "Fornaia", "ðŸ¥–", "npc", False, 1, 3, "A padeira do borgo, calorosa e atenta demais.", "Il pane e caldo."),
    ("pietro", "Pietro", "Boscaiolo", "ðŸª“", "npc", False, 3, 4, "Lenhador reservado que conhece a estrada e os sinais antigos.", "Il bosco ricorda."),
    ("mercante", "Il Mercante", "Mercante", "ðŸŽ", "npc", False, 4, 5, "Vendedor que pesa fruta, moeda e silencio.", "Tre mele, due monete."),
    ("guardia", "La Guardia", "Guardia", "ðŸ’‚", "npc", False, 5, 6, "Guarda do mercado, duro com passes e nomes faltando.", "Permesso o cancello."),
    ("bianca", "Bianca", "Vicina", "ðŸ—ï¸", "npc", False, 4, 7, "Vizinha que sabe mais do que diz.", "La verita costa."),
    ("chiara", "Chiara", "Scrittrice", "âœ’ï¸", "ally", False, 6, 8, "A jovem escriba que ve a palavra acender uma lampada e decide acreditar.", "Le parole hanno peso."),
    ("lucia_guaritrice", "Lucia la Guaritrice", "Guaritrice", "ðŸŒ¿", "ally", False, 8, 9, "Curandeira que conhece ervas e segredos velhos.", "La malattia mente meno delle persone."),
    ("donna_elena", "Donna Elena", "Madre", "👵", "npc", False, 13, 10, "Mae de Nico, presenca familiar da fase 13 e equivalente local de Dona Lucia.", "Mangia prima. Le domande aspettano."),
    ("podesta", "Il Podesta", "Podesta", "⚖️", "boss", False, 11, 11, "Autoridade do borgo que transforma regra em arma.", "Uno straniero resta solo se il borgo permette."),
    ("ispettore", "L'Ispettore", "Ispettore", "🧾", "npc", False, 20, 12, "Homem de fora, frio, formal e perigoso.", "Io faccio domande."),
    ("mateusz", "Mateusz l'Altro", "Altro straniero", "📜", "npc", False, 19, 13, "Rastro polones nos registros: nem portugues, nem italiano.", "Alguns chegam antes. Alguns deixam cartas."),
]

PHASE1_ITEMS = [
    {"slug": "pane_fresco", "emoji": "ðŸ¥–", "name": "Pane Fresco", "word_id": "it_pane", "item_tag": AdventureItem.TAG_COMIDA, "action": AdventureItem.ACTION_USAR, "source_character_slug": "giulia_fornaia", "order": 1, "lore": "Quente do forno de Giulia. Primeiro gesto gentil do borgo."},
    {"slug": "mela_del_campo", "emoji": "ðŸŽ", "name": "Mela del Campo", "word_id": "it_mela", "item_tag": AdventureItem.TAG_COMIDA, "action": AdventureItem.ACTION_USAR, "source_character_slug": "antonio_contadino", "order": 2, "lore": "Pequena e doce, dada por Antonio sem explicacao."},
    {"slug": "acqua_del_pozzo", "emoji": "ðŸ’§", "name": "Acqua del Pozzo", "word_id": "it_acqua", "item_tag": AdventureItem.TAG_BEBIDA, "action": AdventureItem.ACTION_USAR, "source_character_slug": None, "order": 3, "lore": "Agua fria do poco da piazza."},
    {"slug": "moneta_di_rame", "emoji": "ðŸª™", "name": "Moneta di Rame", "word_id": "it_moneta", "item_tag": AdventureItem.TAG_MONEDA, "action": AdventureItem.ACTION_ENTREGAR, "source_character_slug": "nico", "order": 4, "lore": "Moeda pequena, gasta por muitas maos."},
]

CHEST_POOL = [
    {"slug": "coltello_tascabile", "emoji": "ðŸ”ª", "name": "Coltello Tascabile", "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_ARMA, "lore": "Serve para pao, corda ou carta selada."},
    {"slug": "focaccia_avvolta", "emoji": "ðŸ¥–", "name": "Focaccia Avvolta", "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA, "lore": "Fria, mas sustenta."},
    {"slug": "brocca_d_acqua", "emoji": "ðŸº", "name": "Brocca d'Acqua", "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_BEBIDA, "lore": "Barro frio por dentro."},
    {"slug": "bende_pulite", "emoji": "ðŸ©¹", "name": "Bende Pulite", "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_REMEDIO, "lore": "Linho fervido de Lucia."},
    {"slug": "mezza_mappa", "emoji": "ðŸ—ºï¸", "name": "Mezza Mappa", "rarity": AdventureItem.RARITY_RARO, "tag": AdventureItem.TAG_DOCUMENTO, "lore": "Mostra a estrada norte. Falta a metade importante."},
    {"slug": "moneta_d_argento", "emoji": "ðŸª™", "name": "Moneta d'Argento", "rarity": AdventureItem.RARITY_RARO, "tag": AdventureItem.TAG_MONEDA, "lore": "Pesada demais para compra comum."},
    {"slug": "libro_d_erbe", "emoji": "ðŸ“•", "name": "Libro d'Erbe", "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_DOCUMENTO, "lore": "Notas de Lucia, uma pagina arrancada."},
    {"slug": "anello_vecchio", "emoji": "ðŸ’", "name": "Anello Vecchio", "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM, "lore": "Ouro fino com sinal gravado por dentro."},
    {"slug": "ducato_antico", "emoji": "ðŸ…", "name": "Ducato Antico", "rarity": AdventureItem.RARITY_LENDARIO, "tag": AdventureItem.TAG_MONEDA, "lore": "Ouro de um borgo que nao aparece mais no mapa."},
]

DEGRADED = [
    {"slug": "pane_secco", "emoji": "ðŸ¥–", "name": "Pane Secco", "of": "pane_fresco", "lore": "Versao temporaria ate dominar pane."},
    {"slug": "acqua_stantia", "emoji": "ðŸ’§", "name": "Acqua Stantia", "of": "acqua_del_pozzo", "lore": "Ajuda, mas nao satisfaz."},
    {"slug": "mela_ammaccata", "emoji": "ðŸŽ", "name": "Mela Ammaccata", "of": "mela_del_campo", "lore": "Fruta machucada para uma palavra instavel."},
]

CHEST_PHASES = {2: "comum", 3: "comum", 6: "comum", 9: "comum", 11: "comum", 13: "comum", 17: "comum", 22: "comum", 7: "raro", 12: "raro", 16: "raro", 20: "raro", 8: "epico", 14: "epico", 19: "epico"}

BOSS_REWARDS = [
    {"slug": "sigillo_del_borgo", "emoji": "ðŸ›¡ï¸", "name": "Sigillo del Borgo", "rarity": AdventureItem.RARITY_LENDARIO, "action": AdventureItem.ACTION_EXAMINAR, "item_tag": AdventureItem.TAG_DOCUMENTO, "word_id": "it_sigillo", "order": 25, "lore": "O selo do Podesta em cera vermelha."},
    {"slug": "frammento_lettera_2", "emoji": "ðŸ“œ", "name": "Frammento 2 della Lettera", "rarity": AdventureItem.RARITY_LENDARIO, "action": AdventureItem.ACTION_EXAMINAR, "item_tag": AdventureItem.TAG_DOCUMENTO, "word_id": "it_fratello", "order": 26, "lore": "A segunda palavra aparece: FRATELLO."},
]

