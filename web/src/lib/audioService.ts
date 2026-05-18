type Gender = "male" | "female" | "neutral";

interface VoiceProfile {
  lang?: string;
  gender?: Gender;
  pitch?: number;
  rate?: number;
  voiceName?: string;
}

const LANG_MAP: Record<string, string> = {
  de: "de-DE",
  en: "en-US",
  es: "es-ES",
  fr: "fr-FR",
  it: "it-IT",
  ja: "ja-JP",
  pt: "pt-BR",
};

const NPC_PROFILES: Record<string, VoiceProfile> = {
  "Don Miguel": { lang: "es-ES", gender: "male", pitch: 0.85, rate: 0.84 },
  "Don Miguel el Campesino": { lang: "es-ES", gender: "male", pitch: 0.85, rate: 0.84 },
  Miguel: { lang: "es-ES", gender: "male", pitch: 0.95, rate: 0.9 },
  "Miguel el Campesino": { lang: "es-ES", gender: "male", pitch: 0.95, rate: 0.9 },
  Rosa: { lang: "es-ES", gender: "female", pitch: 1.12, rate: 0.9 },
  "Rosa la Panadera": { lang: "es-ES", gender: "female", pitch: 1.1, rate: 0.9 },
  "Señora Carmen": { lang: "es-ES", gender: "female", pitch: 0.95, rate: 0.88 },
  "El Vigilante": { lang: "es-ES", gender: "male", pitch: 0.8, rate: 0.85 },
  Ernesto: { lang: "es-ES", gender: "male", pitch: 0.82, rate: 0.82 },
  "El Mercader": { lang: "es-ES", gender: "male", pitch: 0.9, rate: 1 },
};

const FEMALE_HINTS = /\b(female|woman|mujer)\b|paulina|helena|monica|lucia|rosa|carmen|ana|anna|alice|florence|sabine|elsa|isabella|bianca|chiara|giulia|greta|lina|marta|klara|hanna/i;
const MALE_HINTS = /\b(male|man|hombre)\b|jorge|carlos|pablo|diego|miguel|ernesto|mercader|raul|alonso|marco|giovanni|hans|thomas|adam|pierre|david|mark|george|richard|paul|hector|antonio|nico|pietro|friedrich|otto|elias/i;
const PACE_MULT: Record<string, number> = { slow: 0.82, normal: 0.96, urgent: 1.12 };
const SPEED_KEY = "tts_speed";
const MUTED_KEY = "tts_muted";

class AudioService {
  private voices: SpeechSynthesisVoice[] = [];
  private voicesReady: Promise<void> | null = null;
  private ctx: AudioContext | null = null;
  private currentAudio: HTMLAudioElement | null = null;
  speedMultiplier = 1;
  muted = false;

  constructor() {
    if (typeof window === "undefined") return;
    const saved = parseFloat(localStorage.getItem(SPEED_KEY) ?? "1");
    this.speedMultiplier = Number.isNaN(saved) ? 1 : saved;
    this.muted = localStorage.getItem(MUTED_KEY) === "1";
    if (!("speechSynthesis" in window)) return;
    const load = () => {
      this.voices = speechSynthesis.getVoices();
    };
    load();
    speechSynthesis.addEventListener("voiceschanged", load);
  }

  setMuted(muted: boolean) {
    this.muted = muted;
    localStorage.setItem(MUTED_KEY, muted ? "1" : "0");
    if (muted) this.stop();
  }

  setSpeed(multiplier: number) {
    this.speedMultiplier = multiplier;
    localStorage.setItem(SPEED_KEY, String(multiplier));
  }

  stop() {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.currentTime = 0;
      this.currentAudio = null;
    }
    if ("speechSynthesis" in window) speechSynthesis.cancel();
  }

  speakOrPlay(audioUrl: string | undefined, text: string, langCode: string, npcName?: string, pace?: string, voice?: Partial<VoiceProfile>, speechRate?: number) {
    if (this.muted) return;
    if (audioUrl) {
      this.playAudioUrl(audioUrl, () => this.speak(text, langCode, npcName, pace, voice, speechRate));
      return;
    }
    this.speak(text, langCode, npcName, pace, voice, speechRate);
  }

  speak(text: string, langCode: string, npcName?: string, pace?: string, voice?: Partial<VoiceProfile>, speechRate?: number) {
    if (typeof window === "undefined" || !("speechSynthesis" in window) || this.muted) return;
    speechSynthesis.cancel();
    void this.loadVoices().then(() => {
      if (this.muted) return;
      const profile = { ...(npcName ? NPC_PROFILES[npcName] : undefined), ...voice };
      const lang = profile.lang ?? LANG_MAP[langCode.toLowerCase()] ?? langCode;
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = lang;
      utterance.pitch = profile.pitch ?? 1;
      utterance.rate = (profile.rate ?? 0.9) * this.speedMultiplier * (speechRate ?? PACE_MULT[pace ?? "normal"] ?? 1);
      const selectedVoice = this.pickVoice(lang, profile.gender ?? "neutral", profile.voiceName);
      if (selectedVoice) utterance.voice = selectedVoice;
      speechSynthesis.speak(utterance);
    });
  }

  playCorrect() {
    this.tone(523, 0.08, "sine", 0.2);
    window.setTimeout(() => this.tone(784, 0.2, "sine", 0.18), 90);
  }

  playWrong() {
    this.tone(200, 0.25, "sawtooth", 0.14);
  }

  playComplete() {
    [523, 659, 784, 1047].forEach((freq, index) => window.setTimeout(() => this.tone(freq, 0.25, "sine", 0.17), index * 95));
  }

  private playAudioUrl(audioUrl: string, onFallback?: () => void) {
    this.stop();
    try {
      const audio = new Audio(audioUrl);
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

  private loadVoices() {
    if (!("speechSynthesis" in window)) return Promise.resolve();
    const current = speechSynthesis.getVoices();
    if (current.length) {
      this.voices = current;
      return Promise.resolve();
    }
    if (!this.voicesReady) {
      this.voicesReady = new Promise((resolve) => {
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

  private pickVoice(lang: string, gender: Gender, preferredName?: string) {
    const base = lang.split("-")[0].toLowerCase();
    const candidates = this.voices.filter((voice) => voice.lang.toLowerCase().startsWith(base));
    const pool = candidates.length ? candidates : this.voices;
    if (preferredName) {
      const preferred = pool.find((voice) => `${voice.name} ${voice.voiceURI}`.toLowerCase().includes(preferredName.toLowerCase()));
      if (preferred) return preferred;
    }
    return pool
      .map((voice) => ({ voice, score: this.voiceScore(voice, lang, gender) }))
      .sort((a, b) => b.score - a.score)[0]?.voice ?? null;
  }

  private voiceScore(voice: SpeechSynthesisVoice, lang: string, gender: Gender) {
    const name = `${voice.name} ${voice.voiceURI}`;
    let score = voice.lang.toLowerCase() === lang.toLowerCase() ? 20 : 0;
    if (voice.localService) score += 2;
    if (gender === "female") score += FEMALE_HINTS.test(name) ? 80 : MALE_HINTS.test(name) ? -120 : 0;
    if (gender === "male") score += MALE_HINTS.test(name) ? 80 : FEMALE_HINTS.test(name) ? -120 : 0;
    return score;
  }

  private audioCtx() {
    try {
      this.ctx = this.ctx && this.ctx.state !== "closed" ? this.ctx : new AudioContext();
      if (this.ctx.state === "suspended") void this.ctx.resume();
      return this.ctx;
    } catch {
      return null;
    }
  }

  private tone(freq: number, dur: number, type: OscillatorType, vol: number) {
    if (this.muted) return;
    const ctx = this.audioCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.type = type;
    osc.frequency.value = freq;
    gain.gain.setValueAtTime(vol, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
    osc.start();
    osc.stop(ctx.currentTime + dur + 0.01);
  }
}

export const audioService = new AudioService();
