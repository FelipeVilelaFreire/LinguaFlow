export function formatDate(value: string | null | undefined) {
  if (!value) return "-";
  return new Intl.DateTimeFormat("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    year: "2-digit",
  }).format(new Date(value));
}

export function formatNumber(value: number) {
  return value.toLocaleString("pt-BR");
}

export function formatCurrency(value: number) {
  return new Intl.NumberFormat("pt-BR", {
    currency: "BRL",
    style: "currency",
  }).format(value);
}

export function formatWeekdays(days: number[]) {
  if (!days.length) return "Avulso";
  if (days.length === 7) return "Todo dia";
  const labels = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"];
  return days.map((day) => labels[day]).filter(Boolean).join(", ");
}
