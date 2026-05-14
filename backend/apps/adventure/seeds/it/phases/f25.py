"""
Seed das 6 seções da Fase 25 Italiano A1 — BOSS · "El Jefe del Borgo".

⚠️ BOSS DA T1 — phase_type="boss". Recompensa: Sello del Borgo (lendário)
   + Fragmento 2 da carta (palavra 'FRATELLO' fica legível).

Vocab novo (2): vergüenza · sello
Linguagem nova: nenhuma — fase de revisão + gate puro.

ESTRUTURA DO BOSS:
   S1: chegada à salea de julgamento (narrativa heavy)
   S2: revisão pesada — Podesta interroga, você responde
   S3: O confronto direto — momento crítico
   S4: gramática-narrativa LIGHT — recap rápido
   S5: Bianca levanta-se do público (clímax)
   S6: 100% gated — você precisa responder TUDO certo. Errar trava.
       Closenzag: Podesta recua, sello, fragmento da carta.

⚠️ Item dinâmica:
   - Sello del Borgo entregue automaticamente via source_phase=25
   - Fragmento 2 da carta também via source_phase=25
   - Baú lendário também abre (chest_tier=lendario)
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "??? Sala de julgamento · Manhã · Podesta no trono central"},
                {"kind": "narrative", "text": "Pedra fria. Bandeira pendurada. Três guardas em cada lado. L'Ispettore ao lado direito do Podesta. Bianca no público — terceira fila — fingindo bordar."},
                {"kind": "npc", "npc": "Il Podesta", "line": "Forestiero — el juicio empieza adesso. Levántate.", "pace": "slow"},
                {"kind": "player", "text": "Antonio il Contadino atrás. Chiara e Nico ao lado. Lucia ao seu lado direito. Você levanta. As pernas firmes — não tremeram. A hierba ajudou."},
                {"kind": "npc", "npc": "Il Podesta", "line": "Te acusan de entrar al borgo senza permiso, de usar la palabra de los Buscadores en público, y de albergar a una persona buscada por el distrito.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio",     "native": "julgamento"},
                    {"target": "vergüenza",  "native": "vergonha"},
                    {"target": "sello",      "native": "selo"},
                ]},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você cumprimenta formale — começo de manhã:",
                 "options": [
                     {"id": "a", "text": "Benes días, señor Podesta"},
                     {"id": "b", "text": "Buona notte"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Male"},
                 ], "correct": "a",
                 "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                 "npc_reaction": "Benes días. Cortés. Ma la cortesía no decide juicios."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Il Podesta"], "story": "Il Podesta abre o livro de actas. Interrogatório formale — perguntas claras, respostas curtas.", "now": "Você responde tudo que treinou."},
            "steps": [
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "¿Cómo te chiami?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Mi chiamo [seu nome]"},
                     {"id": "b", "text": "Sono forestiero"},
                     {"id": "c", "text": "Non ricordo"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "¿Cuántos años hai?", "translation": "Quantos anni?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Ho veinte años"},
                     {"id": "b", "text": "Sono veinte"},
                     {"id": "c", "text": "Sto veinte"},
                     {"id": "d", "text": "Vado veinte"},
                 ], "correct": "a",
                 "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "¿De dónde vieni?", "translation": "De onde você vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Resposta segura (você não vai revelar o nome do envelope):",
                 "options": [
                     {"id": "a", "text": "Non ricordo"},
                     {"id": "b", "text": "Sono de aquí"},
                     {"id": "c", "text": "Sono de Sangra"},
                     {"id": "d", "text": "Vado lejos"},
                 ], "correct": "a",
                 "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                 "npc_reaction": "Convieniiente. Lucia Sangra confirmó la pérdida de memoria — questo es lo único que me deha."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "¿Cómo estás aquí, en mi borgo?", "translation": "Como você está aqui, no meu borgo?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Estado honesto (sto + bene):",
                 "options": [
                     {"id": "a", "text": "Sto bene, grazie"},
                     {"id": "b", "text": "Sono bene"},
                     {"id": "c", "text": "Ho bene"},
                     {"id": "d", "text": "Male"},
                 ], "correct": "a",
                 "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                 "npc_reaction": "Bene. Lo que el borgo te da — yo lo puedo quitar."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "¿Te gusta el borgo?Sé senzacero.", "translation": "Você gosta do borgo?Seja senzacero.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Honestidade que ele não esperava:",
                 "options": [
                     {"id": "a", "text": "Sí, mi piace"},
                     {"id": "b", "text": "Non mi piace"},
                     {"id": "c", "text": "Ho gusto"},
                     {"id": "d", "text": "Sono gusto"},
                 ], "correct": "a",
                 "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                 "npc_reaction": "Hmm. Esatto lo dicen todos prima de ser expulsados."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["Il Podesta", "L'Ispettore"], "story": "Il Podesta tira o papel-acusação. Lê em voz alta os três crimes. Pede que você responda — culpado ou inocente.", "now": "Confronto direto."},
            "steps": [
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Primer cargo — entrada al borgo senza permiso. ¿Culpable o inocente?", "translation": "Primeira acusação — entrar no borgo sem permissão. Culpado ou inocente?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você chegou sem documentos — piu Antonio il Contadino acolheu. Versão honesta:",
                 "options": [
                     {"id": "a", "text": "Entré senza saber. Antonio il Contadino me ayudó."},
                     {"id": "b", "text": "No entré"},
                     {"id": "c", "text": "Vado a entrar"},
                     {"id": "d", "text": "Sono entrar"},
                 ], "correct": "a",
                 "word_id": "it_entre", "target": "entré", "native": "entrei",
                 "npc_reaction": "Anotado: entrada senza documentos ma con ayuda local."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Segundo cargo — usar la palabra de los Buscadores en público. La notte del fuoco.", "translation": "Segunda acusação — usar a palavra dos Buscadores em público. A noite do fogo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você não sabia. Foi acidente. Resposta honesta — pretérito 1ª pessoa:",
                 "options": [
                     {"id": "a", "text": "No sabía lo que hacía"},
                     {"id": "b", "text": "Vado a saber"},
                     {"id": "c", "text": "Sono"},
                     {"id": "d", "text": "Vi todo"},
                 ], "correct": "a",
                 "word_id": "it_sabia", "target": "sabía", "native": "sabia (prima)",
                 "npc_reaction": "Excusa fácil. Ma Lucia confirmó. Anotado."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Tercer cargo — albergar a una persona buscada por el distrito. Lucia Sangra.", "translation": "Terceira acusação — abrigar uma pessoa procurada pelo distrito. Lucia Sangra.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Pra defender Lucia sem revelar tudo — você diz que ela só é guaritrice:",
                 "options": [
                     {"id": "a", "text": "Es la guaritrice del borgo"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Sono Sangra"},
                 ], "correct": "a",
                 "word_id": "it_es", "target": "es", "native": "é",
                 "npc_reaction": "Ella es más que questo. Ma veo que el forestiero protege a los suyos."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Hai que entender — sono el Jefe del Borgo. Mi palabra es la ley.", "translation": "Tem que entender — sou o Chefe do Borgo. Minha palavra é a lei.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você responde com respeito, piu firme — 'entendo, piu tenho meus motivos':",
                 "options": [
                     {"id": "a", "text": "Entiendo, ma ho mis razones"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Sono"},
                     {"id": "d", "text": "Vado"},
                 ], "correct": "a",
                 "word_id": "it_entiendo", "target": "entiendo", "native": "entendo",
                 "npc_reaction": "Hmm. Senza paura. Bene saberlo."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Il Podesta"], "story": "Il Podesta pega a pena. Vai escrever a sentença. Pausa.", "now": "Pequena pausa prima do clímax. Recapitulação leve."},
            "steps": [
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Vado a escribir la sentencia adesso.", "translation": "Vou escrever a sentença agora.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Pra você descrever o que ELE vai fazer (futuro próximo, 3ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Va a escribir"},
                     {"id": "b", "text": "Vado a escribir"},
                     {"id": "c", "text": "Vas a escribir"},
                     {"id": "d", "text": "Sono escribir"},
                 ], "correct": "a",
                 "word_id": "it_va_a", "target": "va a", "native": "vai (algo logo)",
                 "npc_reaction": "Va a escribir. Tercera persona — él."},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Pra contar pra Lucia baixinho — 'se ele escrever, estamos perdidos' (condicional com si):",
                 "options": [
                     {"id": "a", "text": "Si escribe, estamos perdidos"},
                     {"id": "b", "text": "Cuando escribe, andiamo"},
                     {"id": "c", "text": "Sono perdidos"},
                     {"id": "d", "text": "Vado perdidos"},
                 ], "correct": "a",
                 "word_id": "it_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si escribe. Condición que aún puede no pasar."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Bianca", "Il Podesta"], "story": "Bianca se levanta do banco do público. Larga o bordado no chão. Caminha até o meio da salea. Os guardas olham piu não se mexem — Bianca é da família do antigo alcalde.", "now": "CLÍMAX. Bianca vai falar."},
            "steps": [
                {"kind": "scene", "text": "👵 Bianca no centro · Postura firme · Olhos no Podesta"},
                {"kind": "npc_speak", "npc": "Bianca", "line": "Prima que firmes la sentencia — ho que decir tres cose.", "translation": "Prima de você assenzaar a sentença — tenho que dizer três coisas.", "pace": "slow"},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Doña Bianca — usted no fue convocada come testigo hoy.", "translation": "Dona Bianca — você não foi convocada come testemunha hoje.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "Bianca", "line": "No vine come testigo. Vine come tu antigua novia.", "translation": "Não vim come testemunha. Vim come tua antiga noiva.", "pace": "slow"},
                {"kind": "player", "text": "Murmúrio na salea. L'Ispettore olha pra Bianca. O Podesta empalidece — primeira vez você o vê perder a postura."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "Uno — hace veinticinco años, me prometiste matrimonio. Dos — tu padre te obligó a romper porque yo era hija de molinero. Tres — todo el borgo sabe que aún te avergüenzas de questo.", "translation": "Um — há vinte e cinco anni, você me prometeu casamento. Dois — teu pai te obrigou a quebrar porque eu era filha de moleiro. Três — o borgo inteiro sabe que ainda você se envergonha disso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Bianca falou a verdade — 25 anni guardada. Você sente o ar mudar. Pra agradecer Bianca depois (mentalmente, piu seguro):",
                 "options": [
                     {"id": "a", "text": "Grazie, Bianca"},
                     {"id": "b", "text": "Adiós Bianca"},
                     {"id": "c", "text": "Male Bianca"},
                     {"id": "d", "text": "Sono Bianca"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "Bianca nem te olha. Mas você sabe — ela ouviu."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "Si firpiu la sentencia hoy — el borgo sabe. Si sellas el pase del forestiero — el borgo olvida.", "translation": "Se você assenzaar a sentença hoje — o borgo sabe. Se carimbar o pase do forasteiro — o borgo esquece.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Il Podesta olha pra Bianca. Pra você. Pra Bianca de novo. Pensa. Decide. Pra você descrever — ele DEVE estar pensando muito (probabilidade):",
                 "options": [
                     {"id": "a", "text": "Debe estar pensando mucho"},
                     {"id": "b", "text": "Es pensar"},
                     {"id": "c", "text": "Vado pensar"},
                     {"id": "d", "text": "Sono pensar"},
                 ], "correct": "a",
                 "word_id": "it_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe. Y al final, decide."},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "...Sella el pase.", "translation": "...Carimba o pase.", "pace": "slow"},
                {"kind": "narrative", "text": "L'Ispettore empalideceu. Derreteu a cera vermelha. Apertou o selo no papel. Entregou pra você sem olhar."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Il Podesta", "Bianca", "Lucia"], "story": "Você segura o pase. Cera quente. Sello do borgo — não provisório. Definitivo. O Podesta se sentou. Bianca voltou pro banco do público — pegou o bordado. Como se nada tivesse acontecido.", "now": "Última prova. Cada palavra importa. Tudo gated."},
            "steps": [
                {"kind": "scene", "text": "🛡️ Sello del Borgo na sua mão · Cera vermelha · Símbolo do borgo"},
                {"kind": "npc_speak", "npc": "Il Podesta", "line": "Hai el pase. Permanente. Ma — una condición. Cuando salegas — no hablas de esto que pasó hoy. Nunca.", "translation": "Você tem o pase. Permanente. Mas — uma condição. Quando você sair — não fala disso que aconteceu hoje. Nunca.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você aceita — vai guardar o segredo (obrigação, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Ho que callar — lo entiendo"},
                     {"id": "b", "text": "Vado a hablar"},
                     {"id": "c", "text": "Sono callar"},
                     {"id": "d", "text": "Quiero hablar"},
                 ], "correct": "a",
                 "word_id": "it_ho_que", "target": "ho que", "native": "tenho que",
                 "npc_reaction": "Hai que. Bene. Vete.", "gated": True},
                {"kind": "multiple_choice", "npc": "Il Podesta",
                 "question": "Você agradece formale — não exagerado:",
                 "options": [
                     {"id": "a", "text": "Grazie, señor Podesta"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Ho grazie"},
                     {"id": "d", "text": "Vado"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "Vete. Benes días.", "gated": True},
                {"kind": "scene", "text": "🚪 Saindo da salea · Antonio il Contadino · Chiara · Nico · Lucia — todos atrás de você"},
                {"kind": "narrative", "text": "Bianca passa por você sem parar. Sussurra: 'Vete al norte cuando puedas. Hay alguien esperándote.' E continua andando."},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você confirma pra Bianca — ouviu (já passou):",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Vado a oír"},
                     {"id": "d", "text": "Sono oír"},
                 ], "correct": "a",
                 "word_id": "it_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Bianca acena de costas. Sumiu na multidão.", "gated": True},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Saindo, Lucia: '¿Cómo estás?'. Honesto — exausto piu vitorioso:",
                 "options": [
                     {"id": "a", "text": "Sono stanco, ma bene"},
                     {"id": "b", "text": "Sto male"},
                     {"id": "c", "text": "Sono bene"},
                     {"id": "d", "text": "Vado bene"},
                 ], "correct": "a",
                 "word_id": "it_sto_cansado", "target": "sto cansado", "native": "estou cansado",
                 "npc_reaction": "Las dos cose. Y hoy ganamos. Esatto es raro.", "gated": True},
                # ── Closenzag — Fragmento 2 da carta + Sello ──
                {"kind": "scene", "text": "🌞 Saindo na rua · Sol forte · Borgo continua come se fosse manhã qualquer"},
                {"kind": "narrative", "text": (
                    "Você fica parado um segundo. Tira a carta velha de Antonio il Contadino do bolso interno do casaco. "
                    "Olha mais uma vez.\n\n"
                    "A primeira palavra ainda está lá: **TORNI**.\n\n"
                    "Mas agora — atrás, mais clara que ontem — uma segunda palavra acendeu:\n\n"
                    "**FRATELLO.**"
                )},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Hijo — tenemos que ir al norte cuando puedas. Bianca tenía razón. Allá hay alguien.", "translation": "Filho — temos que ir ao norte quando você puder. Bianca tinha razão. Lá tem alguém.", "pace": "slow"},
                {"kind": "narrative", "text": (
                    "Você sentiu o peso da palavra 'FRATELLO' no peito — come sentiu o fuoco na noite da F5. "
                    "Não memória. Reconhecimento.\n\n"
                    "Você tem um irmão.\n\n"
                    "E ele está esperando por você no norte.\n\n"
                    "**Fim da Temporada 1 · A história continua na T2.**"
                )},
                {"kind": "scene", "text": "Gancho da T2 - estrada norte - o selo ainda quente na sua mao"},
                {"kind": "npc_speak", "npc": "Chiara", "line": "Fratello. Non e una palavra qualquer.", "translation": "Irmao. Nao e uma palavra qualquer.", "pace": "slow"},
                {"kind": "npc_speak", "npc": "Nico", "line": "Entao vamos buscar ele?Assim, agora?", "translation": "Entao vamos buscar ele?Assim, agora?", "pace": "normal"},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Agora nao. Primeiro sobrevivemos ao que vem depois do julgamento.", "translation": "Agora nao. Primeiro sobrevivemos ao que vem depois do julgamento.", "pace": "slow"},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Quando o sol baixar, pegamos a estrada norte. Se existe um fratello, existe uma historia antes desta.", "translation": "Quando o sol baixar, pegamos a estrada norte. Se existe um irmao, existe uma historia antes desta.", "pace": "slow"},
                {"kind": "narrative", "text": (
                    "O borgo aceitou voce, mas nao explicou voce.\n\n"
                    "O Podesta perdeu o julgamento, mas nao perdeu o poder.\n\n"
                    "A carta revelou uma palavra nova, mas escondeu o resto.\n\n"
                    "Ao norte, alguem espera. Talvez familia. Talvez armadilha. Talvez os dois.\n\n"
                    "**Fim da Temporada 1 - proxima temporada: O Caminho do Norte.**"
                )},            ],
        },
    },
]




