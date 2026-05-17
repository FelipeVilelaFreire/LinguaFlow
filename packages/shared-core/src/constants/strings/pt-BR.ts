export const PT_BR = {
  app: {
    name: "Talkly",
    subtitle: "Aprenda idiomas vivendo a historia",
    loading: "Carregando Talkly...",
  },
  actions: {
    back: "Voltar",
    continue: "Continuar",
    start: "Comecar",
    finish: "Concluir",
    retry: "Tentar novamente",
    close: "Fechar",
    save: "Salvar",
    cancel: "Cancelar",
  },
  nav: {
    home: "Home",
    adventure: "Aventura",
    study: "Estudo",
    vocabulary: "Vocabulario",
    profile: "Perfil",
  },
  home: {
    title: "Hoje",
    headline: "Continue de onde parou.",
    adventureCta: "Continuar aventura",
    studyCta: "Estudar agora",
  },
  adventure: {
    title: "Aventura",
    mapTitle: "Mapa",
    loading: "Carregando aventura...",
    empty: "Nenhuma aventura disponivel.",
    phaseLabel: (n: number) => `Fase ${n}`,
    sectionProgress: (done: number, total: number) => `${done}/${total} secoes`,
    backToMap: "Voltar ao mapa",
  },
  errors: {
    generic: "Nao foi possivel concluir a acao.",
  },
} as const;
