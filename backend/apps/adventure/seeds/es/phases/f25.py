"""
Seed das 6 seÃ§Ãµes da Fase 25 Espanhol A1 â€” BOSS Â· "El Jefe del Pueblo".

âš ï¸ BOSS DA T1 â€” phase_type="boss". Recompensa: Sello del Pueblo (lendÃ¡rio)
   + Fragmento 2 da carta (palavra 'Hermano' fica legÃ­vel).

Vocab novo (2): vergÃ¼enza Â· sello
Linguagem nova: nenhuma â€” fase de revisÃ£o + gate puro.

ESTRUTURA DO BOSS:
   S1: chegada Ã  sala de julgamento (narrativa heavy)
   S2: revisÃ£o pesada â€” Alcalde interroga, vocÃª responde
   S3: O confronto direto â€” momento crÃ­tico
   S4: gramÃ¡tica-narrativa LIGHT â€” recap rÃ¡pido
   S5: Carmen levanta-se do pÃºblico (clÃ­max)
   S6: 100% gated â€” vocÃª precisa responder TUDO certo. Errar trava.
       Closing: Alcalde recua, sello, fragmento da carta.

âš ï¸ Item dinÃ¢mica:
   - Sello del Pueblo entregue automaticamente via source_phase=25
   - Fragmento 2 da carta tambÃ©m via source_phase=25
   - BaÃº lendÃ¡rio tambÃ©m abre (chest_tier=lendario)
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "ðŸ›ï¸ Sala de julgamento Â· ManhÃ£ Â· Alcalde no trono central"},
                {"kind": "narrative", "text": "Pedra fria. Bandeira pendurada. TrÃªs guardas em cada lado. El Inspector ao lado direito do Alcalde. Carmen no pÃºblico â€” terceira fila â€” fingindo bordar."},
                {"kind": "npc", "npc": "El Alcalde", "line": "Forastero â€” el juicio empieza ahora. LevÃ¡ntate.", "pace": "slow"},
                {"kind": "player", "text": "Don Miguel atrÃ¡s. SofÃ­a e Miguel ao lado. MarÃ­a ao seu lado direito. VocÃª levanta. As pernas firmes â€” nÃ£o tremeram. A hierba ajudou."},
                {"kind": "npc", "npc": "El Alcalde", "line": "Te acusan de entrar al pueblo sin permiso, de usar la palabra de los Buscadores en pÃºblico, y de albergar a una persona buscada por el distrito.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio",     "native": "julgamento"},
                    {"target": "vergÃ¼enza",  "native": "vergonha"},
                    {"target": "sello",      "native": "selo"},
                ]},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª cumprimenta formal â€” comeÃ§o de manhÃ£:",
                 "options": [
                     {"id": "a", "text": "Buenos dÃ­as, seÃ±or Alcalde"},
                     {"id": "b", "text": "Buenas noches"},
                     {"id": "c", "text": "AdiÃ³s"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                 "npc_reaction": "Buenos dÃ­as. CortÃ©s. Pero la cortesÃ­a no decide juicios."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["El Alcalde"], "story": "El Alcalde abre o livro de actas. InterrogatÃ³rio formal â€” perguntas claras, respostas curtas.", "now": "VocÃª responde tudo que treinou."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Â¿CÃ³mo te llamas?", "translation": "Como vocÃª se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "No me acuerdo"},
                     {"id": "d", "text": "AdiÃ³s"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Â¿CuÃ¡ntos aÃ±os tienes?", "translation": "Quantos anos?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte aÃ±os"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Â¿De dÃ³nde vienes?", "translation": "De onde vocÃª vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Resposta segura (vocÃª nÃ£o vai revelar o nome do envelope):",
                 "options": [
                     {"id": "a", "text": "No me acuerdo"},
                     {"id": "b", "text": "Soy de aquÃ­"},
                     {"id": "c", "text": "Soy de Sangra"},
                     {"id": "d", "text": "Voy lejos"},
                 ], "correct": "a",
                 "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                 "npc_reaction": "Conveniente. MarÃ­a Sangra confirmÃ³ la pÃ©rdida de memoria â€” eso es lo Ãºnico que me detiene."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Â¿CÃ³mo estÃ¡s aquÃ­, en mi pueblo?", "translation": "Como vocÃª estÃ¡ aqui, no meu pueblo?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Estado honesto (estoy + bien):",
                 "options": [
                     {"id": "a", "text": "Estoy bien, gracias"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                 "npc_reaction": "Bien. Lo que el pueblo te da â€” yo lo puedo quitar."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Â¿Te gusta el pueblo? SÃ© sincero.", "translation": "VocÃª gosta do pueblo? Seja sincero.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Honestidade que ele nÃ£o esperava:",
                 "options": [
                     {"id": "a", "text": "SÃ­, me gusta"},
                     {"id": "b", "text": "No me gusta"},
                     {"id": "c", "text": "Tengo gusto"},
                     {"id": "d", "text": "Soy gusto"},
                 ], "correct": "a",
                 "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                 "npc_reaction": "Hmm. Eso lo dicen todos antes de ser expulsados."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["El Alcalde", "El Inspector"], "story": "El Alcalde tira o papel-acusaÃ§Ã£o. LÃª em voz alta os trÃªs crimes. Pede que vocÃª responda â€” culpado ou inocente.", "now": "Confronto direto."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Primer cargo â€” entrada al pueblo sin permiso. Â¿Culpable o inocente?", "translation": "Primeira acusaÃ§Ã£o â€” entrar no pueblo sem permissÃ£o. Culpado ou inocente?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª chegou sem documentos â€” mas Don Miguel acolheu. VersÃ£o honesta:",
                 "options": [
                     {"id": "a", "text": "EntrÃ© sin saber. Don Miguel me ayudÃ³."},
                     {"id": "b", "text": "No entrÃ©"},
                     {"id": "c", "text": "Voy a entrar"},
                     {"id": "d", "text": "Soy entrar"},
                 ], "correct": "a",
                 "word_id": "es_entre", "target": "entrÃ©", "native": "entrei",
                 "npc_reaction": "Anotado: entrada sin documentos pero con ayuda local."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Segundo cargo â€” usar la palabra de los Buscadores en pÃºblico. La noche del fuego.", "translation": "Segunda acusaÃ§Ã£o â€” usar a palavra dos Buscadores em pÃºblico. A noite do fogo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª nÃ£o sabia. Foi acidente. Resposta honesta â€” pretÃ©rito 1Âª pessoa:",
                 "options": [
                     {"id": "a", "text": "No sabÃ­a lo que hacÃ­a"},
                     {"id": "b", "text": "Voy a saber"},
                     {"id": "c", "text": "Soy"},
                     {"id": "d", "text": "Vi todo"},
                 ], "correct": "a",
                 "word_id": "es_sabia", "target": "sabÃ­a", "native": "sabia (antes)",
                 "npc_reaction": "Excusa fÃ¡cil. Pero MarÃ­a confirmÃ³. Anotado."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tercer cargo â€” albergar a una persona buscada por el distrito. MarÃ­a Sangra.", "translation": "Terceira acusaÃ§Ã£o â€” abrigar uma pessoa procurada pelo distrito. MarÃ­a Sangra.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra defender MarÃ­a sem revelar tudo â€” vocÃª diz que ela sÃ³ Ã© curandera:",
                 "options": [
                     {"id": "a", "text": "Es la curandera del pueblo"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Soy Sangra"},
                 ], "correct": "a",
                 "word_id": "es_es", "target": "es", "native": "Ã©",
                 "npc_reaction": "Ella es mÃ¡s que eso. Pero veo que el forastero protege a los suyos."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tienes que entender â€” soy el Jefe del Pueblo. Mi palabra es la ley.", "translation": "Tem que entender â€” sou o Chefe do Pueblo. Minha palavra Ã© a lei.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª responde com respeito, mas firme â€” 'entendo, mas tenho meus motivos':",
                 "options": [
                     {"id": "a", "text": "Entiendo, pero tengo mis razones"},
                     {"id": "b", "text": "AdiÃ³s"},
                     {"id": "c", "text": "Soy"},
                     {"id": "d", "text": "Voy"},
                 ], "correct": "a",
                 "word_id": "es_entiendo", "target": "entiendo", "native": "entendo",
                 "npc_reaction": "Hmm. Sin miedo. Bueno saberlo."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["El Alcalde"], "story": "El Alcalde pega a pena. Vai escrever a sentenÃ§a. Pausa.", "now": "Pequena pausa antes do clÃ­max. RecapitulaÃ§Ã£o leve."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Voy a escribir la sentencia ahora.", "translation": "Vou escrever a sentenÃ§a agora.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra vocÃª descrever o que ELE vai fazer (futuro prÃ³ximo, 3Âª pessoa):",
                 "options": [
                     {"id": "a", "text": "Va a escribir"},
                     {"id": "b", "text": "Voy a escribir"},
                     {"id": "c", "text": "Vas a escribir"},
                     {"id": "d", "text": "Soy escribir"},
                 ], "correct": "a",
                 "word_id": "es_va_a", "target": "va a", "native": "vai (algo logo)",
                 "npc_reaction": "Va a escribir. Tercera persona â€” Ã©l."},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra contar pra MarÃ­a baixinho â€” 'se ele escrever, estamos perdidos' (condicional com si):",
                 "options": [
                     {"id": "a", "text": "Si escribe, estamos perdidos"},
                     {"id": "b", "text": "Cuando escribe, vamos"},
                     {"id": "c", "text": "Soy perdidos"},
                     {"id": "d", "text": "Voy perdidos"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si escribe. CondiciÃ³n que aÃºn puede no pasar."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Carmen", "El Alcalde"], "story": "Carmen se levanta do banco do pÃºblico. Larga o bordado no chÃ£o. Caminha atÃ© o meio da sala. Os guardas olham mas nÃ£o se mexem â€” Carmen Ã© da famÃ­lia do antigo alcalde.", "now": "CLÃMAX. Carmen vai falar."},
            "steps": [
                {"kind": "scene", "text": "ðŸ‘µ Carmen no centro Â· Postura firme Â· Olhos no Alcalde"},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Antes que firmes la sentencia â€” tengo que decir tres cosas.", "translation": "Antes de vocÃª assinar a sentenÃ§a â€” tenho que dizer trÃªs coisas.", "pace": "slow"},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "DoÃ±a Carmen â€” usted no fue convocada como testigo hoy.", "translation": "Dona Carmen â€” vocÃª nÃ£o foi convocada como testemunha hoje.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "Carmen", "line": "No vine como testigo. Vine como tu antigua novia.", "translation": "NÃ£o vim como testemunha. Vim como tua antiga noiva.", "pace": "slow"},
                {"kind": "player", "text": "MurmÃºrio na sala. El Inspector olha pra Carmen. O Alcalde empalidece â€” primeira vez vocÃª o vÃª perder a postura."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Uno â€” hace veinticinco aÃ±os, me prometiste matrimonio. Dos â€” tu padre te obligÃ³ a romper porque yo era hija de molinero. Tres â€” todo el pueblo sabe que aÃºn te avergÃ¼enzas de eso.", "translation": "Um â€” hÃ¡ vinte e cinco anos, vocÃª me prometeu casamento. Dois â€” teu pai te obrigou a quebrar porque eu era filha de moleiro. TrÃªs â€” o pueblo inteiro sabe que ainda vocÃª se envergonha disso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen falou a verdade â€” 25 anos guardada. VocÃª sente o ar mudar. Pra agradecer Carmen depois (mentalmente, mas seguro):",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "AdiÃ³s Carmen"},
                     {"id": "c", "text": "Mal Carmen"},
                     {"id": "d", "text": "Soy Carmen"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Carmen nem te olha. Mas vocÃª sabe â€” ela ouviu."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Si firmas la sentencia hoy â€” el pueblo sabe. Si sellas el pase del forastero â€” el pueblo olvida.", "translation": "Se vocÃª assinar a sentenÃ§a hoje â€” o pueblo sabe. Se carimbar o pase do forasteiro â€” o pueblo esquece.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "El Alcalde olha pra Carmen. Pra vocÃª. Pra Carmen de novo. Pensa. Decide. Pra vocÃª descrever â€” ele DEVE estar pensando muito (probabilidade):",
                 "options": [
                     {"id": "a", "text": "Debe estar pensando mucho"},
                     {"id": "b", "text": "Es pensar"},
                     {"id": "c", "text": "Voy pensar"},
                     {"id": "d", "text": "Soy pensar"},
                 ], "correct": "a",
                 "word_id": "es_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe. Y al final, decide."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "...Sella el pase.", "translation": "...Carimba o pase.", "pace": "slow"},
                {"kind": "narrative", "text": "El Inspector empalideceu. Derreteu a cera vermelha. Apertou o selo no papel. Entregou pra vocÃª sem olhar."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["El Alcalde", "Carmen", "MarÃ­a"], "story": "VocÃª segura o pase. Cera quente. Sello do pueblo â€” nÃ£o provisÃ³rio. Definitivo. O Alcalde se sentou. Carmen voltou pro banco do pÃºblico â€” pegou o bordado. Como se nada tivesse acontecido.", "now": "Ãšltima prova. Cada palavra importa. Tudo gated."},
            "steps": [
                {"kind": "scene", "text": "ðŸ›¡ï¸ Sello del Pueblo na sua mÃ£o Â· Cera vermelha Â· SÃ­mbolo do pueblo"},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tienes el pase. Permanente. Pero â€” una condiciÃ³n. Cuando salgas â€” no hablas de esto que pasÃ³ hoy. Nunca.", "translation": "VocÃª tem o pase. Permanente. Mas â€” uma condiÃ§Ã£o. Quando vocÃª sair â€” nÃ£o fala disso que aconteceu hoje. Nunca.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª aceita â€” vai guardar o segredo (obrigaÃ§Ã£o, 1Âª pessoa):",
                 "options": [
                     {"id": "a", "text": "Tengo que callar â€” lo entiendo"},
                     {"id": "b", "text": "Voy a hablar"},
                     {"id": "c", "text": "Soy callar"},
                     {"id": "d", "text": "Quiero hablar"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Tienes que. Bueno. Vete.", "gated": True},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "VocÃª agradece formal â€” nÃ£o exagerado:",
                 "options": [
                     {"id": "a", "text": "Gracias, seÃ±or Alcalde"},
                     {"id": "b", "text": "AdiÃ³s"},
                     {"id": "c", "text": "Tengo gracias"},
                     {"id": "d", "text": "Voy"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Vete. Buenos dÃ­as.", "gated": True},
                {"kind": "scene", "text": "ðŸšª Saindo da sala Â· Don Miguel Â· SofÃ­a Â· Miguel Â· MarÃ­a â€” todos atrÃ¡s de vocÃª"},
                {"kind": "narrative", "text": "Carmen passa por vocÃª sem parar. Sussurra: 'Vete al norte cuando puedas. Hay alguien esperÃ¡ndote.' E continua andando."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª confirma pra Carmen â€” ouviu (jÃ¡ passou):",
                 "options": [
                     {"id": "a", "text": "Lo oÃ­"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oÃ­r"},
                     {"id": "d", "text": "Soy oÃ­r"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                 "npc_reaction": "Carmen acena de costas. Sumiu na multidÃ£o.", "gated": True},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Saindo, MarÃ­a: 'Â¿CÃ³mo estÃ¡s?'. Honesto â€” exausto mas vitorioso:",
                 "options": [
                     {"id": "a", "text": "Estoy cansado, pero bien"},
                     {"id": "b", "text": "Estoy mal"},
                     {"id": "c", "text": "Soy bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                 "npc_reaction": "Las dos cosas. Y hoy ganamos. Eso es raro.", "gated": True},
                # â”€â”€ Closing â€” Fragmento 2 da carta + Sello â”€â”€
                {"kind": "scene", "text": "ðŸŒž Saindo na rua Â· Sol forte Â· Pueblo continua como se fosse manhÃ£ qualquer"},
                {"kind": "narrative", "text": (
                    "VocÃª fica parado um segundo. Tira a carta velha de Don Miguel do bolso interno do casaco. "
                    "Olha mais uma vez.\n\n"
                    "A primeira palavra ainda estÃ¡ lÃ¡: **VUELVES**.\n\n"
                    "Mas agora â€” atrÃ¡s, mais clara que ontem â€” uma segunda palavra acendeu:\n\n"
                    "**HERMANO.**"
                )},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Hijo â€” tenemos que ir al norte cuando puedas. Carmen tenÃ­a razÃ³n. AllÃ¡ hay alguien.", "translation": "Filho â€” temos que ir ao norte quando vocÃª puder. Carmen tinha razÃ£o. LÃ¡ tem alguÃ©m.", "pace": "slow"},
                {"kind": "narrative", "text": (
                    "VocÃª sentiu o peso da palavra 'hermano' no peito â€” como sentiu o fuego na noite da F5. "
                    "NÃ£o memÃ³ria. Reconhecimento.\n\n"
                    "VocÃª tem um irmÃ£o.\n\n"
                    "E ele estÃ¡ esperando por vocÃª no norte.\n\n"
                    "**Fim da Temporada 1 Â· A histÃ³ria continua na T2.**"
                )},
            ],
        },
    },
]
