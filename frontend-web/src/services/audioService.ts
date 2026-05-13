type Gender = "male" | "female" | "neutral";

interface VoiceProfile {
  lang:   string;
  gender: Gender;
  pitch:  number;
  rate:   number;
}

const LANG_MAP: Record<string, string> = {
  es: "es-ES", it: "it-IT", de: "de-DE",
  fr: "fr-FR", en: "en-US", ja: "ja-JP", pt: "pt-BR",
};

const NPC_PROFILES: Record<string, VoiceProfile> = {
  "Don Miguel":           { lang: "es-ES", gender: "male",   pitch: 0.85, rate: 0.88 },
  "Rosa la Panadera":     { lang: "es-ES", gender: "female", pitch: 1.1,  rate: 0.95 },
  "Señora Carmen":        { lang: "es-ES", gender: "female", pitch: 0.95, rate: 0.88 },
  "El Vigilante":         { lang: "es-ES", gender: "male",   pitch: 0.8,  rate: 0.85 },
  "Contadino":            { lang: "it-IT", gender: "male",   pitch: 0.9,  rate: 0.9  },
  "Il Condottiero":       { lang: "it-IT", gender: "male",   pitch: 0.75, rate: 0.82 },
};

const FEMALE_HINTS = /female|woman|paulina|helena|monica|lucia|rosa|carmen|anna|alice|florence|amélie|kyoko/i;
const MALE_HINTS   = /male|man|jorge|carlos|pablo|marco|giovanni|hans|thomas|adam|pierre/i;
const PACE_MULT: Record<string, number> = { slow: 0.72, normal: 1.0, urgent: 1.35 };

const SPEED_KEY = "tts_speed";

class AudioService {
  private voices: SpeechSynthesisVoice[] = [];
  private ctx: AudioContext | null = null;
  speedMultiplier: number = 1.5;

  constructor() {
    if (typeof window === "undefined") return;
    const saved = parseFloat(localStorage.getItem(SPEED_KEY) ?? "1.5");
    this.speedMultiplier = isNaN(saved) ? 1.5 : saved;
    if (!("speechSynthesis" in window)) return;
    const load = () => { this.voices = speechSynthesis.getVoices(); };
    load();
    speechSynthesis.addEventListener("voiceschanged", load);
  }

  setSpeed(multiplier: number): void {
    this.speedMultiplier = multiplier;
    localStorage.setItem(SPEED_KEY, String(multiplier));
  }

  private audioCtx(): AudioContext | null {
    try {
      if (!this.ctx || this.ctx.state === "closed") {
        this.ctx = new AudioContext();
      }
      if (this.ctx.state === "suspended") this.ctx.resume();
      return this.ctx;
    } catch {
      return null;
    }
  }

  private pickVoice(lang: string, gender: Gender): SpeechSynthesisVoice | null {
    const base = lang.split("-")[0];
    const pool = this.voices.filter(v => v.lang.startsWith(base));
    if (!pool.length) return null;
    if (gender === "female") return pool.find(v => FEMALE_HINTS.test(v.name)) ?? pool[0];
    if (gender === "male")   return pool.find(v => MALE_HINTS.test(v.name))   ?? pool[0];
    return pool[0];
  }

  stop(): void {
    if (!("speechSynthesis" in window)) return;
    speechSynthesis.cancel();
  }

  speak(text: string, langCode: string, npcName?: string, pace?: string): void {
    if (!("speechSynthesis" in window)) return;
    speechSynthesis.cancel();

    const profile  = npcName ? NPC_PROFILES[npcName] : undefined;
    const lang     = profile?.lang ?? LANG_MAP[langCode.toLowerCase()] ?? langCode;
    const paceMult = PACE_MULT[pace ?? "normal"] ?? 1.0;

    const u = new SpeechSynthesisUtterance(text);
    u.lang  = lang;
    u.pitch = profile?.pitch ?? 1.0;
    u.rate  = (profile?.rate ?? 0.9) * this.speedMultiplier * paceMult;
    const v = this.pickVoice(lang, profile?.gender ?? "neutral");
    if (v) u.voice = v;

    speechSynthesis.speak(u);
  }

  playCorrect(): void {
    this.tone(523, 0.08, "sine", 0.22);
    setTimeout(() => this.tone(784, 0.22, "sine", 0.20), 90);
  }

  playWrong(): void {
    this.tone(200, 0.28, "sawtooth", 0.16);
  }

  playComplete(): void {
    [523, 659, 784, 1047].forEach((f, i) =>
      setTimeout(() => this.tone(f, 0.28, "sine", 0.18), i * 95)
    );
  }

  private tone(freq: number, dur: number, type: OscillatorType, vol: number): void {
    try {
      const ctx = this.audioCtx();
      if (!ctx) return;
      const osc  = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.type            = type;
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(vol, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
      osc.start();
      osc.stop(ctx.currentTime + dur + 0.01);
    } catch { /* no audio context */ }
  }
}

export const audioService = new AudioService();
