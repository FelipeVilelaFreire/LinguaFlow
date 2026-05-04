/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#111827",
        paper: "#f7f7f4",
        line: "#e5e7eb",
        brand: "#2563eb",
        success: "#16a34a",
        danger: "#dc2626",
      },
      boxShadow: {
        soft: "0 10px 30px rgba(17, 24, 39, 0.08)",
      },
      borderRadius: {
        app: "8px",
      },
    },
  },
  plugins: [],
};
