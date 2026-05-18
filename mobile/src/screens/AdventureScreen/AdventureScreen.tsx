import { Feather } from "@expo/vector-icons";
import { Link } from "expo-router";
import { STRINGS } from "@linguaflow/shared-core";
import { ScrollView, Text, View } from "react-native";
import { AdventureTransitionButton } from "@/src/components/features/adventure";
import { styles } from "./AdventureScreen.styles";

const SHORTCUTS = [
  { href: "/adventure/map", label: STRINGS.adventure.mapTitle, icon: "map" },
  { href: "/adventure/inventory", label: STRINGS.adventure.inventory, icon: "box" },
  { href: "/adventure/chests", label: STRINGS.adventure.chests, icon: "archive" },
  { href: "/adventure/words", label: STRINGS.adventure.words, icon: "book-open" },
  { href: "/adventure/hero", label: STRINGS.adventure.hero, icon: "shield" },
  { href: "/adventure/characters", label: STRINGS.adventure.characters, icon: "star" },
] as const;

export function AdventureScreen() {
  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.hero}>
        <Text style={styles.eyebrow}>{STRINGS.adventure.title}</Text>
        <Text style={styles.title}>{STRINGS.adventure.hubTitle}</Text>
        <Text style={styles.subtitle}>{STRINGS.adventure.hubSubtitle}</Text>
        <AdventureTransitionButton href="/adventure/map" style={styles.primaryAction}>
          <Feather name="map" size={18} color="#ffffff" />
          <Text style={styles.primaryText}>{STRINGS.adventure.openMap}</Text>
        </AdventureTransitionButton>
      </View>

      <View style={styles.shortcuts}>
        {SHORTCUTS.map((item, index) => (
          <Link href={item.href} key={item.href} style={[styles.shortcut, index === 0 ? styles.highlightShortcut : null]}>
            <Feather name={item.icon} size={18} color={index === 0 ? "#fef3c7" : "rgba(255,255,255,0.7)"} />
            <Text style={index === 0 ? styles.highlightShortcutText : styles.shortcutText}>{item.label}</Text>
          </Link>
        ))}
      </View>
    </ScrollView>
  );
}

