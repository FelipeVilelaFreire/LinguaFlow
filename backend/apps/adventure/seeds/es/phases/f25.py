"""
Seed das 6 seções da Fase 25 Espanhol A1 — BOSS · "El Jefe del Pueblo".

⚠️ BOSS DA T1 — phase_type="boss". Recompensa: Sello del Pueblo (lendário)
   + Fragmento 2 da carta (palavra 'Hermano' fica legível).

Vocab novo (2): vergüenza · sello
Linguagem nova: nenhuma — fase de revisão + gate puro.

ESTRUTURA DO BOSS:
   S1: chegada à sala de julgamento (narrativa heavy)
   S2: revisão pesada — Alcalde interroga, você responde
   S3: O confronto direto — momento crítico
   S4: gramática-narrativa LIGHT — recap rápido
   S5: Carmen levanta-se do público (clímax)
   S6: 100% gated — você precisa responder TUDO certo. Errar trava.
       Closing: Alcalde recua, sello, fragmento da carta.

⚠️ Item dinâmica:
   - Sello del Pueblo entregue automaticamente via source_phase=25
   - Fragmento 2 da carta também via source_phase=25
   - Baú lendário também abre (chest_tier=lendario)
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "🏛️ Sala de julgamento · Manhã · Alcalde no trono central"},
                {"kind": "narrative", "text": "Pedra fria. Bandeira pendurada. Três guardas em cada lado. El Inspector ao lado direito do Alcalde. Carmen no público — terceira fila — fingindo bordar."},
                {"kind": "npc", "npc": "El Alcalde", "line": "Forastero — el juicio empieza ahora. Levántate.", "pace": "slow"},
                {"kind": "player", "text": "Don Miguel atrás. Sofía e Miguel ao lado. María ao seu lado direito. Você levanta. As pernas firmes — não tremeram. A hierba ajudou."},
                {"kind": "npc", "npc": "El Alcalde", "line": "Te acusan de entrar al pueblo sin permiso, de usar la palabra de los Buscadores en público, y de albergar a una persona buscada por el distrito.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio",     "native": "julgamento"},
                    {"target": "vergüenza",  "native": "vergonha"},
                    {"target": "sello",      "native": "selo"},
                ]},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você cumprimenta formal — começo de manhã:",
                 "options": [
                     {"id": "a", "text": "Buenos días, señor Alcalde"},
                     {"id": "b", "text": "Buenas noches"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                 "npc_reaction": "Buenos días. Cortés. Pero la cortesía no decide juicios."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["El Alcalde"], "story": "El Alcalde abre o livro de actas. Interrogatório formal — perguntas claras, respostas curtas.", "now": "Você responde tudo que treinou."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "¿Cómo te llamas?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "No me acuerdo"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "¿Cuántos años tienes?", "translation": "Quantos anos?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte años"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "¿De dónde vienes?", "translation": "De onde você vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Resposta segura (você não vai revelar o nome do envelope):",
                 "options": [
                     {"id": "a", "text": "No me acuerdo"},
                     {"id": "b", "text": "Soy de aquí"},
                     {"id": "c", "text": "Soy de Sangra"},
                     {"id": "d", "text": "Voy lejos"},
                 ], "correct": "a",
                 "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                 "npc_reaction": "Conveniente. María Sangra confirmó la pérdida de memoria — eso es lo único que me detiene."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "¿Cómo estás aquí, en mi pueblo?", "translation": "Como você está aqui, no meu pueblo?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Estado honesto (estoy + bien):",
                 "options": [
                     {"id": "a", "text": "Estoy bien, gracias"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                 "npc_reaction": "Bien. Lo que el pueblo te da — yo lo puedo quitar."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "¿Te gusta el pueblo? Sé sincero.", "translation": "Você gosta do pueblo? Seja sincero.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Honestidade que ele não esperava:",
                 "options": [
                     {"id": "a", "text": "Sí, me gusta"},
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
            "recap": {"characters": ["El Alcalde", "El Inspector"], "story": "El Alcalde tira o papel-acusação. Lê em voz alta os três crimes. Pede que você responda — culpado ou inocente.", "now": "Confronto direto."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Primer cargo — entrada al pueblo sin permiso. ¿Culpable o inocente?", "translation": "Primeira acusação — entrar no pueblo sem permissão. Culpado ou inocente?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você chegou sem documentos — mas Don Miguel acolheu. Versão honesta:",
                 "options": [
                     {"id": "a", "text": "Entré sin saber. Don Miguel me ayudó."},
                     {"id": "b", "text": "No entré"},
                     {"id": "c", "text": "Voy a entrar"},
                     {"id": "d", "text": "Soy entrar"},
                 ], "correct": "a",
                 "word_id": "es_entre", "target": "entré", "native": "entrei",
                 "npc_reaction": "Anotado: entrada sin documentos pero con ayuda local."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Segundo cargo — usar la palabra de los Buscadores en público. La noche del fuego.", "translation": "Segunda acusação — usar a palavra dos Buscadores em público. A noite do fogo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você não sabia. Foi acidente. Resposta honesta — pretérito 1ª pessoa:",
                 "options": [
                     {"id": "a", "text": "No sabía lo que hacía"},
                     {"id": "b", "text": "Voy a saber"},
                     {"id": "c", "text": "Soy"},
                     {"id": "d", "text": "Vi todo"},
                 ], "correct": "a",
                 "word_id": "es_sabia", "target": "sabía", "native": "sabia (antes)",
                 "npc_reaction": "Excusa fácil. Pero María confirmó. Anotado."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tercer cargo — albergar a una persona buscada por el distrito. María Sangra.", "translation": "Terceira acusação — abrigar uma pessoa procurada pelo distrito. María Sangra.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra defender María sem revelar tudo — você diz que ela só é curandera:",
                 "options": [
                     {"id": "a", "text": "Es la curandera del pueblo"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Soy Sangra"},
                 ], "correct": "a",
                 "word_id": "es_es", "target": "es", "native": "é",
                 "npc_reaction": "Ella es más que eso. Pero veo que el forastero protege a los suyos."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tienes que entender — soy el Jefe del Pueblo. Mi palabra es la ley.", "translation": "Tem que entender — sou o Chefe do Pueblo. Minha palavra é a lei.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você responde com respeito, mas firme — 'entendo, mas tenho meus motivos':",
                 "options": [
                     {"id": "a", "text": "Entiendo, pero tengo mis razones"},
                     {"id": "b", "text": "Adiós"},
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
            "recap": {"characters": ["El Alcalde"], "story": "El Alcalde pega a pena. Vai escrever a sentença. Pausa.", "now": "Pequena pausa antes do clímax. Recapitulação leve."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Voy a escribir la sentencia ahora.", "translation": "Vou escrever a sentença agora.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra você descrever o que ELE vai fazer (futuro próximo, 3ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Va a escribir"},
                     {"id": "b", "text": "Voy a escribir"},
                     {"id": "c", "text": "Vas a escribir"},
                     {"id": "d", "text": "Soy escribir"},
                 ], "correct": "a",
                 "word_id": "es_va_a", "target": "va a", "native": "vai (algo logo)",
                 "npc_reaction": "Va a escribir. Tercera persona — él."},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Pra contar pra María baixinho — 'se ele escrever, estamos perdidos' (condicional com si):",
                 "options": [
                     {"id": "a", "text": "Si escribe, estamos perdidos"},
                     {"id": "b", "text": "Cuando escribe, vamos"},
                     {"id": "c", "text": "Soy perdidos"},
                     {"id": "d", "text": "Voy perdidos"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si escribe. Condición que aún puede no pasar."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Carmen", "El Alcalde"], "story": "Carmen se levanta do banco do público. Larga o bordado no chão. Caminha até o meio da sala. Os guardas olham mas não se mexem — Carmen é da família do antigo alcalde.", "now": "CLÍMAX. Carmen vai falar."},
            "steps": [
                {"kind": "scene", "text": "👵 Carmen no centro · Postura firme · Olhos no Alcalde"},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Antes que firmes la sentencia — tengo que decir tres cosas.", "translation": "Antes de você assinar a sentença — tenho que dizer três coisas.", "pace": "slow"},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Doña Carmen — usted no fue convocada como testigo hoy.", "translation": "Dona Carmen — você não foi convocada como testemunha hoje.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "Carmen", "line": "No vine como testigo. Vine como tu antigua novia.", "translation": "Não vim como testemunha. Vim como tua antiga noiva.", "pace": "slow"},
                {"kind": "player", "text": "Murmúrio na sala. El Inspector olha pra Carmen. O Alcalde empalidece — primeira vez você o vê perder a postura."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Uno — hace veinticinco años, me prometiste matrimonio. Dos — tu padre te obligó a romper porque yo era hija de molinero. Tres — todo el pueblo sabe que aún te avergüenzas de eso.", "translation": "Um — há vinte e cinco anos, você me prometeu casamento. Dois — teu pai te obrigou a quebrar porque eu era filha de moleiro. Três — o pueblo inteiro sabe que ainda você se envergonha disso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen falou a verdade — 25 anos guardada. Você sente o ar mudar. Pra agradecer Carmen depois (mentalmente, mas seguro):",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "Adiós Carmen"},
                     {"id": "c", "text": "Mal Carmen"},
                     {"id": "d", "text": "Soy Carmen"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Carmen nem te olha. Mas você sabe — ela ouviu."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Si firmas la sentencia hoy — el pueblo sabe. Si sellas el pase del forastero — el pueblo olvida.", "translation": "Se você assinar a sentença hoje — o pueblo sabe. Se carimbar o pase do forasteiro — o pueblo esquece.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "El Alcalde olha pra Carmen. Pra você. Pra Carmen de novo. Pensa. Decide. Pra você descrever — ele DEVE estar pensando muito (probabilidade):",
                 "options": [
                     {"id": "a", "text": "Debe estar pensando mucho"},
                     {"id": "b", "text": "Es pensar"},
                     {"id": "c", "text": "Voy pensar"},
                     {"id": "d", "text": "Soy pensar"},
                 ], "correct": "a",
                 "word_id": "es_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe. Y al final, decide."},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "...Sella el pase.", "translation": "...Carimba o pase.", "pace": "slow"},
                {"kind": "narrative", "text": "El Inspector empalideceu. Derreteu a cera vermelha. Apertou o selo no papel. Entregou pra você sem olhar."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["El Alcalde", "Carmen", "María"], "story": "Você segura o pase. Cera quente. Sello do pueblo — não provisório. Definitivo. O Alcalde se sentou. Carmen voltou pro banco do público — pegou o bordado. Como se nada tivesse acontecido.", "now": "Última prova. Cada palavra importa. Tudo gated."},
            "steps": [
                {"kind": "scene", "text": "🛡️ Sello del Pueblo na sua mão · Cera vermelha · Símbolo do pueblo"},
                {"kind": "npc_speak", "npc": "El Alcalde", "line": "Tienes el pase. Permanente. Pero — una condición. Cuando salgas — no hablas de esto que pasó hoy. Nunca.", "translation": "Você tem o pase. Permanente. Mas — uma condição. Quando você sair — não fala disso que aconteceu hoje. Nunca.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você aceita — vai guardar o segredo (obrigação, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Tengo que callar — lo entiendo"},
                     {"id": "b", "text": "Voy a hablar"},
                     {"id": "c", "text": "Soy callar"},
                     {"id": "d", "text": "Quiero hablar"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Tienes que. Bueno. Vete.", "gated": True},
                {"kind": "multiple_choice", "npc": "El Alcalde",
                 "question": "Você agradece formal — não exagerado:",
                 "options": [
                     {"id": "a", "text": "Gracias, señor Alcalde"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Tengo gracias"},
                     {"id": "d", "text": "Voy"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Vete. Buenos días.", "gated": True},
                {"kind": "scene", "text": "🚪 Saindo da sala · Don Miguel · Sofía · Miguel · María — todos atrás de você"},
                {"kind": "narrative", "text": "Carmen passa por você sem parar. Sussurra: 'Vete al norte cuando puedas. Hay alguien esperándote.' E continua andando."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você confirma pra Carmen — ouviu (já passou):",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oír"},
                     {"id": "d", "text": "Soy oír"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Carmen acena de costas. Sumiu na multidão.", "gated": True},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Saindo, María: '¿Cómo estás?'. Honesto — exausto mas vitorioso:",
                 "options": [
                     {"id": "a", "text": "Estoy cansado, pero bien"},
                     {"id": "b", "text": "Estoy mal"},
                     {"id": "c", "text": "Soy bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                 "npc_reaction": "Las dos cosas. Y hoy ganamos. Eso es raro.", "gated": True},
                # ── Closing — Fragmento 2 da carta + Sello ──
                {"kind": "scene", "text": "🌞 Saindo na rua · Sol forte · Pueblo continua como se fosse manhã qualquer"},
                {"kind": "narrative", "text": (
                    "Você fica parado um segundo. Tira a carta velha de Don Miguel do bolso interno do casaco. "
                    "Olha mais uma vez.\n\n"
                    "A primeira palavra ainda está lá: **VUELVES**.\n\n"
                    "Mas agora — atrás, mais clara que ontem — uma segunda palavra acendeu:\n\n"
                    "**HERMANO.**"
                )},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Hijo — tenemos que ir al norte cuando puedas. Carmen tenía razón. Allá hay alguien.", "translation": "Filho — temos que ir ao norte quando você puder. Carmen tinha razão. Lá tem alguém.", "pace": "slow"},
                {"kind": "narrative", "text": (
                    "Você sentiu o peso da palavra 'hermano' no peito — como sentiu o fuego na noite da F5. "
                    "Não memória. Reconhecimento.\n\n"
                    "Você tem um irmão.\n\n"
                    "E ele está esperando por você no norte.\n\n"
                    "**Fim da Temporada 1 · A história continua na T2.**"
                )},
            ],
        },
    },
]
