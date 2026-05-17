type Gender = "male" | "female" | "neutral";

interface VoiceProfile {
  lang:   string;
  gender: Gender;
  pitch:  number;
  rate:   number;
  voiceName?: string;
}

const LANG_MAP: Record<string, string> = {
  es: "es-ES", it: "it-IT", de: "de-DE",
  fr: "fr-FR", en: "en-US", ja: "ja-JP", pt: "pt-BR",
};

const NPC_PROFILES: Record<string, VoiceProfile> = {
  "Don Miguel":           { lang: "es-ES", gender: "male",   pitch: 0.85, rate: 0.84 },
  "Don Miguel el Campesino": { lang: "es-ES", gender: "male", pitch: 0.85, rate: 0.84 },
  "Miguel":               { lang: "es-ES", gender: "male",   pitch: 0.95, rate: 0.9  },
  "Miguel el Campesino":  { lang: "es-ES", gender: "male",   pitch: 0.95, rate: 0.9  },
  "Rosa":                 { lang: "es-ES", gender: "female", pitch: 1.12, rate: 0.9 },
  "Rosa la Panadera":     { lang: "es-ES", gender: "female", pitch: 1.1,  rate: 0.9 },
  "Señora Carmen":        { lang: "es-ES", gender: "female", pitch: 0.95, rate: 0.88 },
  "El Vigilante":         { lang: "es-ES", gender: "male",   pitch: 0.8,  rate: 0.85 },
  "Ernesto":              { lang: "es-ES", gender: "male",   pitch: 0.82, rate: 0.82 },
  "El Mercader":          { lang: "es-ES", gender: "male",   pitch: 0.9,  rate: 1.0  },
  "Contadino":            { lang: "it-IT", gender: "male",   pitch: 0.9,  rate: 0.9  },
  "Il Condottiero":       { lang: "it-IT", gender: "male",   pitch: 0.75, rate: 0.82 },
};

const FEMALE_HINTS = /\b(female|woman|mujer)\b|paulina|helena|monica|lucia|lucía|rosa|carmen|ana|anna|alice|florence|amelie|amélie|kyoko|elvira|sabina|dalia|laura|maria|maría|paloma|zira|susan|hazel|hedda|hortense|sabine|elsa|isabella|bianca|chiara|giulia|greta|lina|marta|klara|hanna/i;
const MALE_HINTS   = /\b(male|man|hombre)\b|jorge|carlos|pablo|diego|miguel|ernesto|mercader|raul|raúl|alonso|alvaro|álvaro|marco|giovanni|hans|thomas|adam|pierre|david|mark|george|richard|paul|hector|héctor|antonio|nico|pietro|friedrich|otto|elias/i;
const PACE_MULT: Record<string, number> = { slow: 0.82, normal: 0.96, urgent: 1.12 };
const NPC_AUDIO_VOLUME: Record<string, number> = {
  "Don Miguel": 0.82,
  "Don Miguel el Campesino": 0.82,
};

const SPEED_KEY = "tts_speed";
const MUTED_KEY = "tts_muted";
const DEFAULT_SPEED = 1;

class AudioService {
  private voices: SpeechSynthesisVoice[] = [];
  private voicesReady: Promise<void> | null = null;
  private ctx: AudioContext | null = null;
  private currentAudio: HTMLAudioElement | null = null;
  speedMultiplier: number = DEFAULT_SPEED;
  muted: boolean = false;

  constructor() {
    if (typeof window === "undefined") return;
    const savedRaw = localStorage.getItem(SPEED_KEY);
    const saved = parseFloat(savedRaw ?? String(DEFAULT_SPEED));
    this.speedMultiplier = isNaN(saved) ? DEFAULT_SPEED : saved;
    if (savedRaw === "1.25") this.setSpeed(DEFAULT_SPEED);
    this.muted = localStorage.getItem(MUTED_KEY) === "1";
    if (!("speechSynthesis" in window)) return;
    const load = () => {
      this.voices = speechSynthesis.getVoices();
      if (import.meta.env.DEV) {
        console.info("[tts voices]", this.voices.map(v => `${v.name} (${v.lang})`));
      }
    };
    load();
    speechSynthesis.addEventListener("voiceschanged", load);
  }

  private loadVoices(): Promise<void> {
    if (!("speechSynthesis" in window)) return Promise.resolve();

    const current = speechSynthesis.getVoices();
    if (current.length) {
      this.voices = current;
      return Promise.resolve();
    }

    if (!this.voicesReady) {
      this.voicesReady = new Promise(resolve => {
        const finish = () => {
          this.voices = speechSynthesis.getVoices();
          speechSynthesis.removeEventListener("voiceschanged", finish);
          resolve();
        };
        speechSynthesis.addEventListener("voiceschanged", finish);
        window.setTimeout(finish, 650);
      });
    }

    return this.voicesReady;
  }

  setSpeed(multiplier: number): void {
    this.speedMultiplier = multiplier;
    localStorage.setItem(SPEED_KEY, String(multiplier));
  }

  setMuted(muted: boolean): void {
    this.muted = muted;
    localStorage.setItem(MUTED_KEY, muted ? "1" : "0");
    if (muted) this.stop();
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

  private pickVoice(lang: string, gender: Gender, preferredName?: string): SpeechSynthesisVoice | null {
    const base = lang.split("-")[0];
    const pool = this.voices.filter(v => v.lang.startsWith(base));
    const candidates = pool.length ? pool : this.voices;
    if (!candidates.length) return null;

    if (preferredName) {
      const preferred = candidates.find(v =>
        v.name.toLowerCase().includes(preferredName.toLowerCase()) ||
        v.voiceURI.toLowerCase().includes(preferredName.toLowerCase()),
      );
      if (preferred) return preferred;
    }

    const scored = candidates
      .map(voice => ({ voice, score: this.voiceScore(voice, lang, gender) }))
      .sort((a, b) => b.score - a.score);

    return scored[0]?.voice ?? candidates[0];
  }

  private voiceScore(voice: SpeechSynthesisVoice, lang: string, gender: Gender): number {
    const name = `${voice.name} ${voice.voiceURI}`;
    const base = lang.split("-")[0].toLowerCase();
    let score = 0;

    if (voice.lang.toLowerCase() === lang.toLowerCase()) score += 20;
    if (voice.lang.toLowerCase().startsWith(base)) score += 12;
    if (voice.localService) score += 2;

    if (gender === "female") {
      if (FEMALE_HINTS.test(name)) score += 80;
      if (MALE_HINTS.test(name)) score -= 120;
    } else if (gender === "male") {
      if (MALE_HINTS.test(name)) score += 80;
      if (FEMALE_HINTS.test(name)) score -= 120;
    }

    return score;
  }

  stop(): void {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.currentTime = 0;
      this.currentAudio = null;
    }
    if (!("speechSynthesis" in window)) return;
    speechSynthesis.cancel();
  }

  speakOrPlay(audioUrl: string | undefined, text: string, langCode: string, npcName?: string, pace?: string, voice?: Partial<VoiceProfile>, speechRate?: number): void {
    if (audioUrl) {
      this.playAudioUrl(audioUrl, () => this.speak(text, langCode, npcName, pace, voice, speechRate), npcName ? NPC_AUDIO_VOLUME[npcName] : undefined);
      return;
    }
    this.speak(text, langCode, npcName, pace, voice, speechRate);
  }

  private playAudioUrl(audioUrl: string, onFallback?: () => void, volume = 1): void {
    if (this.muted) return;
    this.stop();
    try {
      const audio = new Audio(audioUrl);
      audio.volume = Math.max(0, Math.min(1, volume));
      this.currentAudio = audio;
      audio.onended = () => {
        if (this.currentAudio === audio) this.currentAudio = null;
      };
      audio.onerror = () => {
        if (this.currentAudio === audio) this.currentAudio = null;
        onFallback?.();
      };
      void audio.play().catch(() => {
        if (this.currentAudio === audio) this.currentAudio = null;
        onFallback?.();
      });
    } catch {
      onFallback?.();
    }
  }

  speak(text: string, langCode: string, npcName?: string, pace?: string, voice?: Partial<VoiceProfile>, speechRate?: number): void {
    if (!("speechSynthesis" in window)) return;
    if (this.muted) return;
    speechSynthesis.cancel();

    void this.loadVoices().then(() => {
      if (this.muted) return;
      this.speakNow(text, langCode, npcName, pace, voice, speechRate);
    });
  }

  private speakNow(text: string, langCode: string, npcName?: string, pace?: string, voice?: Partial<VoiceProfile>, speechRate?: number): void {
    const profile  = { ...(npcName ? NPC_PROFILES[npcName] : undefined), ...voice };
    const lang     = profile?.lang ?? LANG_MAP[langCode.toLowerCase()] ?? langCode;
    const paceMult = PACE_MULT[pace ?? "normal"] ?? 1.0;
    const lineRate = speechRate ?? paceMult;

    const u = new SpeechSynthesisUtterance(text);
    u.lang  = lang;
    u.pitch = profile?.pitch ?? 1.0;
    u.rate  = (profile?.rate ?? 0.9) * this.speedMultiplier * lineRate;
    const v = this.pickVoice(lang, profile?.gender ?? "neutral", profile?.voiceName);
    if (v) u.voice = v;
    if (profile?.gender === "female" && v && !FEMALE_HINTS.test(`${v.name} ${v.voiceURI}`)) {
      u.pitch = Math.max(u.pitch, 1.75);
      u.rate = Math.min(u.rate * 1.06, 1.75);
    }
    if (import.meta.env.DEV) {
      console.info("[tts speak]", {
        npcName,
        requestedGender: profile?.gender,
        requestedLang: lang,
        selectedVoice: v ? `${v.name} (${v.lang})` : "browser default",
        pitch: u.pitch,
        rate: u.rate,
      });
    }

    speechSynthesis.speak(u);
  }

  playCorrect(): void {
    if (this.muted) return;
    this.tone(523, 0.08, "sine", 0.22);
    setTimeout(() => this.tone(784, 0.22, "sine", 0.20), 90);
  }

  playWrong(): void {
    if (this.muted) return;
    this.tone(200, 0.28, "sawtooth", 0.16);
  }

  playComplete(): void {
    if (this.muted) return;
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
