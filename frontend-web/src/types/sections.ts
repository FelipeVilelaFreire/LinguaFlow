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
  | { kind: "npc";       npc: string; line: string; translation?: string }
  | { kind: "player";    text: string };

// ── Step types — all step-based sections ─────────────────────────────────────

export type SectionStep =
  | { kind: "narrative";       text: string }
  | { kind: "scene";           text: string }
  | { kind: "npc_speak";       npc: string; line: string; translation?: string }
  | { kind: "player_react";    text: string }
  | { kind: "reveal";          phrase: string; meaning: string; note?: string }
  | { kind: "pattern";         parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { kind: "vocab_list";      items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Array<{ id: string; text: string }>; correct: string; explanation?: string; word_id?: string; tier?: WordTier }
  | { kind: "fill_blank";      prompt: string; answer: string }
  | { kind: "translate";       source: string; answer: string }
  | { kind: "write_word";      prompt: string; word_id: string; answer: string; tier: Extract<WordTier, "diamante" | "esmeralda">; hint?: string };

// ── Section types (backend architecture — never visible to player) ────────────

export interface NarrativaSection          { type: "narrativa";           beats: NarrativaBeat[]; exercises?: SectionStep[] }
export interface RevisaoSrsSection         { type: "revisao_srs";         steps: SectionStep[] }
export interface PraticaAplicadaSection    { type: "pratica_aplicada";    steps: SectionStep[] }
export interface GramaticaNarrativaSection { type: "gramatica_narrativa"; steps: SectionStep[] }
export interface ReforcoSection            { type: "reforco";             steps: SectionStep[] }
export interface ObstaculoSection          { type: "obstaculo";           steps: SectionStep[] }

export type PhaseSection =
  | NarrativaSection
  | RevisaoSrsSection
  | PraticaAplicadaSection
  | GramaticaNarrativaSection
  | ReforcoSection
  | ObstaculoSection;
