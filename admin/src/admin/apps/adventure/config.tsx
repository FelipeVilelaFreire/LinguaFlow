import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import { Panel } from "../../shared/components/Panel";
import type { AdminAppConfig } from "../../shared/types";

type AdventureRecord =
  | { entity: "phase"; id: number; title: string; chapter: string; language: string; type: string; meta: string }
  | { entity: "character"; id: number; title: string; chapter: string; language: string; type: string; meta: string }
  | { entity: "item"; id: number; title: string; chapter: string; language: string; type: string; meta: string };

export const adventureConfig: AdminAppConfig<AdventureRecord> = {
  key: "adventure",
  group: "content",
  icon: "AV",
  title: STRINGS.admin.apps.adventure.title,
  description: STRINGS.admin.apps.adventure.description,
  searchPlaceholder: "Buscar fase, personagem, item ou capitulo",
  getRecords: (data) => {
    const adventure = data.adventure;
    if (!adventure) return [];
    return [
      ...adventure.phases.map((phase) => ({
        chapter: phase.chapter,
        entity: "phase" as const,
        id: phase.id,
        language: phase.language,
        meta: `Fase ${phase.number} / ${phase.section_count} secoes`,
        title: phase.title,
        type: phase.phase_type,
      })),
      ...adventure.characters.map((character) => ({
        chapter: character.chapter,
        entity: "character" as const,
        id: character.id,
        language: character.lang_bridge ? "bridge" : "-",
        meta: `${character.emoji} ${character.role}`,
        title: character.name,
        type: character.character_type,
      })),
      ...adventure.items.map((item) => ({
        chapter: item.chapter,
        entity: "item" as const,
        id: item.id,
        language: item.skill || "-",
        meta: `${item.emoji} ${item.rarity} / ${item.action}`,
        title: item.name,
        type: item.item_tag || "item",
      })),
    ];
  },
  columns: [
    { key: "entity", label: "Entidade", value: (row) => <Badge tone={row.entity === "character" ? "good" : "neutral"}>{row.entity}</Badge> },
    { key: "title", label: STRINGS.admin.shared.fields.title, value: (row) => row.title },
    { key: "chapter", label: "Capitulo", value: (row) => row.chapter },
    { key: "language", label: STRINGS.admin.shared.fields.language, value: (row) => row.language },
    { key: "type", label: STRINGS.admin.shared.fields.type, value: (row) => row.type },
    { key: "meta", label: "Detalhe", value: (row) => row.meta },
  ],
  getMetrics: (data) => [
    { label: "Capitulos", value: data.adventure?.chapters.length ?? 0 },
    { label: "Fases", value: data.adventure?.phases.length ?? 0 },
    { label: "Personagens", value: data.adventure?.characters.length ?? 0 },
    { label: "Itens", value: data.adventure?.items.length ?? 0 },
  ],
  renderAside: (data) => (
    <Panel eyebrow="Narrativa" title="Personagens e imagens">
      <div className="admin-stack">
        {(data.adventure?.characters ?? []).slice(0, 10).map((character) => (
          <div className="admin-inline-row" key={character.id}>
            <strong>{character.emoji} {character.name}</strong>
            <span>{character.character_type}</span>
          </div>
        ))}
      </div>
    </Panel>
  ),
};
