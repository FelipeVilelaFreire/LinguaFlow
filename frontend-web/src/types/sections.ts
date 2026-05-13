// ── Word mastery tier — determines exercise type per word per user ────────────
//
// Bronze  → múltipla escolha (4 opções)           → sobe com 3 acertos
// Prata   → múltipla escolha (distratores difíceis) → sobe com 5 acertos
// Ouro    → múltipla escolha (sem contexto extra)  → sobe com 5 acertos
// Diamante→ write_word (escrever do zero)          → sobe escrevendo 5x seguidas
// Esmeralda → maestria confirmada
export type WordTier = "bronze" | "prata" | "ouro" | "diamante" | "esmeralda";

// ── Beat types — narrativa section only ──────────────────────────────────────

export type NarrativaBeat =
  | { kind: "scene";     text: string }
  | { kind: "narrative"; text: string }
  | { kind: "npc";       npc: string; line: string; translation?: string; pace?: "slow" | "normal" | "urgent" }
  | { kind: "player";    text: string };

// ── Step types — all step-based sections ─────────────────────────────────────

export type SectionStep =
  | { kind: "narrative";       text: string }
  | { kind: "scene";           text: string }
  | { kind: "npc_speak";       npc: string; line: string; translation?: string; is_new_npc?: boolean; pace?: "slow" | "normal" | "urgent" }
  | { kind: "player_react";    text: string }
  | { kind: "reveal";          phrase: string; meaning: string; note?: string }
  | { kind: "pattern";         parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { kind: "vocab_list";      items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Array<{ id: string; text: string }>; correct: string; explanation?: string; word_id?: string; target?: string; native?: string; tier?: WordTier; npc?: string; npc_reaction?: string }
  | { kind: "fill_blank";      prompt: string; answer: string }
  | { kind: "translate";       source: string; answer: string }
  | { kind: "write_word";      prompt: string; word_id: string; answer: string; tier: Extract<WordTier, "diamante" | "esmeralda">; hint?: string };

// ── Section recap — "Me relembre onde paramos" card, triggered by the player ──
// `story` is a narrative continuation of what literally happened in the
// previous section(s). `characters` lists NPC names that should appear with
// their avatar at the top of the card. `now` is an optional one-liner about
// what's about to happen in this section.

export interface SectionRecap {
  story:       string;
  now?:        string;
  characters?: string[];
}

// ── Section types (backend architecture — never visible to player) ────────────

interface BaseSection { recap?: SectionRecap }

export interface NarrativaSection          extends BaseSection { type: "narrativa";           beats: NarrativaBeat[]; exercises?: SectionStep[] }
export interface RevisaoSrsSection         extends BaseSection { type: "revisao_srs";         steps: SectionStep[] }
export interface PraticaAplicadaSection    extends BaseSection { type: "pratica_aplicada";    steps: SectionStep[] }
export interface GramaticaNarrativaSection extends BaseSection { type: "gramatica_narrativa"; steps: SectionStep[] }
export interface ReforcoSection            extends BaseSection { type: "reforco";             steps: SectionStep[] }
export interface ObstaculoSection          extends BaseSection { type: "obstaculo";           steps: SectionStep[] }

export type PhaseSection =
  | NarrativaSection
  | RevisaoSrsSection
  | PraticaAplicadaSection
  | GramaticaNarrativaSection
  | ReforcoSection
  | ObstaculoSection;
