// Maps NPC name (as used in section content npc_speak steps) → { slug, emoji }
// Needed in the chat where only the name string is available.
// Keep in sync with the backend character slugs.

export const CHARACTER_AVATARS: Record<string, { slug: string; emoji: string }> = {
  // Full display names
  "Don Miguel el Campesino":  { slug: "don_miguel",    emoji: "👨‍🌾" },
  "Miguel el Campesino":      { slug: "miguel",        emoji: "🤠"  },
  "El Vigilante del Mercado": { slug: "vigilante",     emoji: "💂"  },
  "Señora Carmen":            { slug: "senora_carmen", emoji: "👩"  },
  "Rosa la Panadera":         { slug: "rosa_panadera", emoji: "👩‍🍳" },
  // Short aliases used in section content npc_speak steps
  "Don Miguel":               { slug: "don_miguel",    emoji: "👨‍🌾" },
  "Miguel":                   { slug: "miguel",        emoji: "🤠"  },
  "El Vigilante":             { slug: "vigilante",     emoji: "💂"  },
  "Carmen":                   { slug: "senora_carmen", emoji: "👩"  },
  "Rosa":                     { slug: "rosa_panadera", emoji: "👩‍🍳" },
};
