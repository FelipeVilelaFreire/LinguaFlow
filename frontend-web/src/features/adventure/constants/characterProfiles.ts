export interface CharacterProfile {
  name: string;
  role: string;
  description: string;
  quote?: string;
}

const PROFILE_BY_NAME: Record<string, CharacterProfile> = {
  "Don Miguel": {
    name: "Don Miguel",
    role: "Campesino",
    description: "Un campesino mayor de San Cristobal. Habla despacio, observa antes de actuar y guia al forastero con paciencia.",
    quote: "Primero escucha. Despues habla.",
  },
  "Don Miguel el Campesino": {
    name: "Don Miguel",
    role: "Campesino",
    description: "Un campesino mayor de San Cristobal. Habla despacio, observa antes de actuar y guia al forastero con paciencia.",
    quote: "Primero escucha. Despues habla.",
  },
  "Miguel": {
    name: "Miguel",
    role: "Campesino",
    description: "Un joven del pueblo, leal e irreverente. Conoce cada calle, cada favor pendiente y cada atajo de San Cristobal.",
  },
  "Miguel el Campesino": {
    name: "Miguel",
    role: "Campesino",
    description: "Un joven del pueblo, leal e irreverente. Conoce cada calle, cada favor pendiente y cada atajo de San Cristobal.",
  },
  "Rosa": {
    name: "Rosa",
    role: "Panadera",
    description: "La panadera del pueblo. Calida, rapida y sonriente, aparece con harina en las manos y pan recien hecho.",
    quote: "Pan fresco, forastero.",
  },
  "Rosa la Panadera": {
    name: "Rosa",
    role: "Panadera",
    description: "La panadera del pueblo. Calida, rapida y sonriente, aparece con harina en las manos y pan recien hecho.",
    quote: "Pan fresco, forastero.",
  },
  "Ernesto": {
    name: "Ernesto",
    role: "Lenador",
    description: "Un lenador viejo y reservado. Habla poco, mira el rio como si guardara secretos y entrega ayuda sin explicar demasiado.",
    quote: "La piedra recuerda mas que nosotros.",
  },
  "El Mercader": {
    name: "El Mercader",
    role: "Mercader",
    description: "Un vendedor atento y calculador. Sonrie mientras cuenta monedas, frutas y silencios ajenos en el mercado.",
    quote: "Tres naranjas, dos monedas. Buen trato.",
  },
  "Mercader": {
    name: "El Mercader",
    role: "Mercader",
    description: "Un vendedor atento y calculador. Sonrie mientras cuenta monedas, frutas y silencios ajenos en el mercado.",
    quote: "Tres naranjas, dos monedas. Buen trato.",
  },
  "Carmen": {
    name: "Senora Carmen",
    role: "Guardiana do cotidiano",
    description: "Una vecina atenta del pueblo. Conoce a todos, recuerda cada gesto y defiende las pequenas reglas de la convivencia.",
  },
  "Senora Carmen": {
    name: "Senora Carmen",
    role: "Guardiana do cotidiano",
    description: "Una vecina atenta del pueblo. Conoce a todos, recuerda cada gesto y defiende las pequenas reglas de la convivencia.",
  },
  "SeÃƒÂ±ora Carmen": {
    name: "Senora Carmen",
    role: "Guardiana do cotidiano",
    description: "Una vecina atenta del pueblo. Conoce a todos, recuerda cada gesto y defiende las pequenas reglas de la convivencia.",
  },
  "El Vigilante": {
    name: "El Vigilante",
    role: "Vigilante del Mercado",
    description: "El guardia del mercado. Vigila puertas, pases y movimientos sospechosos con una severidad dificil de ignorar.",
  },
  "El Vigilante del Mercado": {
    name: "El Vigilante",
    role: "Vigilante del Mercado",
    description: "El guardia del mercado. Vigila puertas, pases y movimientos sospechosos con una severidad dificil de ignorar.",
  },
  "Sofia": {
    name: "Sofia",
    role: "Companheira",
    description: "Una aliada curiosa y electrica, lista para unir pistas, personas y palabras que parecen lejanas.",
  },
  "SofÃƒÂ­a": {
    name: "Sofia",
    role: "Companheira",
    description: "Una aliada curiosa y electrica, lista para unir pistas, personas y palabras que parecen lejanas.",
  },
  "Maria": {
    name: "Maria",
    role: "Antagonista",
    description: "Una presencia peligrosa, elegante y decidida. Sus planes avanzan dentro de la ventana final del ritual.",
  },
  "MarÃƒÂ­a": {
    name: "Maria",
    role: "Antagonista",
    description: "Una presencia peligrosa, elegante y decidida. Sus planes avanzan dentro de la ventana final del ritual.",
  },
  "Catalina": {
    name: "Catalina",
    role: "Portadora",
    description: "Una Portadora ligada al mismo misterio del protagonista. Su memoria perdida la vuelve objetivo y clave de la historia.",
  },
  "Rodrigo": {
    name: "Rodrigo",
    role: "Mercador",
    description: "Un negociador de sonrisa facil e intenciones menos simples, siempre cerca de informacion, objetos y oportunidad.",
  },
  "James": {
    name: "James",
    role: "El Otro Forasteiro",
    description: "El otro forastero. Entiende mas sobre La Palabra Viva de lo que aparenta y cambia el eje de la jornada.",
  },
  "Valentina": {
    name: "Valentina",
    role: "Figura misteriosa",
    description: "Una figura envuelta en senales y presagios, ligada a partes de la historia que aun no se explican por completo.",
  },
};

export function getCharacterProfile(name: string): CharacterProfile {
  return PROFILE_BY_NAME[name] ?? {
    name,
    role: "",
    description: "Un personaje encontrado durante la aventura. Sus palabras ayudan a revelar el camino.",
  };
}
