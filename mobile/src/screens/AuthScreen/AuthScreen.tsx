import { router } from "expo-router";
import { useState } from "react";
import { Pressable, Text, TextInput, View } from "react-native";
import { ROUTES, STRINGS, authService, contentService } from "@linguaflow/shared-core";
import { styles } from "./AuthScreen.styles";

type Mode = "login" | "register";

export function AuthScreen() {
  const [mode, setMode] = useState<Mode>("login");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function submit() {
    if (mode === "register") {
      if (!username.trim()) return setError(STRINGS.auth.usernameRequiredRegister);
      if (!email.trim()) return setError(STRINGS.auth.emailRequired);
      if (password.length < 6) return setError(STRINGS.auth.errorPasswordLength);
      if (password !== confirmPassword) return setError(STRINGS.auth.passwordsDoNotMatch);
    } else {
      if (!username.trim()) return setError(STRINGS.auth.usernameRequiredLogin);
      if (!password) return setError(STRINGS.auth.passwordRequired);
    }

    setLoading(true);
    setError("");
    try {
      if (mode === "login") await authService.login(username, password);
      else await authService.register(username, email, password);

      try {
        await contentService.getCurrentGoal();
        router.replace("/(tabs)/home");
      } catch {
        router.replace(ROUTES.onboarding as never);
      }
    } catch {
      setError(mode === "login" ? STRINGS.auth.errorLoginFallback : STRINGS.auth.errorRegisterFallback);
    } finally {
      setLoading(false);
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.logo}>Talkly</Text>
      <Text style={styles.subtitle}>Aprenda idiomas vivendo a historia</Text>

      <View style={styles.tabs}>
        <Pressable style={[styles.tab, mode === "login" ? styles.activeTab : null]} onPress={() => setMode("login")}>
          <Text style={mode === "login" ? styles.activeTabText : styles.tabText}>{STRINGS.auth.loginTab}</Text>
        </Pressable>
        <Pressable style={[styles.tab, mode === "register" ? styles.activeTab : null]} onPress={() => setMode("register")}>
          <Text style={mode === "register" ? styles.activeTabText : styles.tabText}>{STRINGS.auth.registerTab}</Text>
        </Pressable>
      </View>

      <TextInput style={styles.input} value={username} onChangeText={setUsername} placeholder={STRINGS.auth.usernameLabel} autoCapitalize="none" />
      {mode === "register" ? (
        <TextInput style={styles.input} value={email} onChangeText={setEmail} placeholder={STRINGS.auth.emailLabel} autoCapitalize="none" keyboardType="email-address" />
      ) : null}
      <TextInput style={styles.input} value={password} onChangeText={setPassword} placeholder={STRINGS.auth.passwordLabel} secureTextEntry />
      {mode === "register" ? (
        <TextInput style={styles.input} value={confirmPassword} onChangeText={setConfirmPassword} placeholder={STRINGS.auth.confirmPasswordLabel} secureTextEntry />
      ) : null}

      {error ? <Text style={styles.error}>{error}</Text> : null}

      <Pressable style={styles.submit} onPress={submit} disabled={loading}>
        <Text style={styles.submitText}>{loading ? "Carregando..." : mode === "login" ? STRINGS.auth.loginTab : STRINGS.auth.registerTab}</Text>
      </Pressable>
    </View>
  );
}
