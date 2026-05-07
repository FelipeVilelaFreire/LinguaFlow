import { ArrowLeft, Key, Languages, LogOut, Mail } from "lucide-react";

import { useStrings } from "../contexts/StringsContext";
import type { AppLocale } from "../constants/strings";
import type { User } from "../services/authService";

interface EditProfileScreenProps {
  user: User;
  uiLocale: AppLocale;
  onBack: () => void;
  onLocaleChange: (locale: AppLocale) => void;
  onLogout: () => void;
}

export default function EditProfileScreen({ user, uiLocale, onBack, onLocaleChange, onLogout }: EditProfileScreenProps) {
  const s = useStrings();

  return (
    <div className="history-shell" style={{ animation: "fadeIn 220ms ease-out" }}>

      {/* Top bar */}
      <div className="history-topbar">
        <button type="button" onClick={onBack} className="history-back-btn">
          <ArrowLeft size={18} />
        </button>
        <h1 className="history-title">{s.profile.accountSection}</h1>
        <div className="w-9" />
      </div>

      <div className="history-content">

        {/* User */}
        <section className="card p-4">
          <div className="flex items-center gap-3">
            <div className="profile-avatar">{user.username.charAt(0).toUpperCase()}</div>
            <div>
              <p className="font-bold text-slate-950">{user.username}</p>
              <p className="text-sm font-medium text-slate-500">{user.email || s.profile.noEmail}</p>
            </div>
          </div>
        </section>

        {/* Interface */}
        <section className="card-overflow">
          <p className="px-4 pt-4 pb-2 text-xs font-semibold uppercase tracking-widest text-slate-400">
            {s.layout.interfaceLanguage}
          </p>
          <div className="px-4 pb-4">
            <div className="grid grid-cols-2 gap-2 rounded-[8px] bg-slate-100 p-1">
              {(["pt", "en"] as AppLocale[]).map((locale) => (
                <button
                  key={locale}
                  type="button"
                  onClick={() => onLocaleChange(locale)}
                  className={`h-10 rounded-[6px] text-sm font-semibold transition ${uiLocale === locale ? "bg-white text-slate-950 shadow-sm" : "text-slate-500"}`}
                >
                  {locale === "pt" ? s.layout.portuguese : s.layout.english}
                </button>
              ))}
            </div>
          </div>
        </section>

        {/* Conta */}
        <section className="card-overflow divide-y divide-slate-100">
          <SettingsRow icon={<Mail size={16} className="text-slate-400" />} text={user.email || s.profile.noEmail} />
          <SettingsRow icon={<Key size={16} className="text-slate-400" />} text={s.profile.changePassword} chevron />
          <SettingsRow
            icon={<Languages size={16} className="text-slate-400" />}
            text={`${s.layout.interfaceLanguage}: ${uiLocale === "pt" ? s.layout.portuguese : s.layout.english}`}
          />
        </section>

        {/* Logout */}
        <button
          type="button"
          onClick={onLogout}
          className="flex h-12 w-full items-center justify-center gap-2 rounded-[8px] bg-white text-sm font-semibold text-red-500 ring-1 ring-red-100 transition hover:bg-red-50"
        >
          <LogOut size={16} />
          {s.profile.signOut}
        </button>

      </div>
    </div>
  );
}

function SettingsRow({ icon, text, chevron }: { icon: React.ReactNode; text: string; chevron?: boolean }) {
  return (
    <div className="flex items-center gap-3 px-4 py-3.5">
      {icon}
      <span className="flex-1 text-sm font-medium text-slate-700">{text}</span>
      {chevron && <span className="text-slate-300">›</span>}
    </div>
  );
}
