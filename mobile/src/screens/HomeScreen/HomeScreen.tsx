import { Link } from "expo-router";
import { Text, View } from "react-native";
import { ROUTES, STRINGS } from "@linguaflow/shared-core";
import { styles } from "./HomeScreen.styles";

export function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.eyebrow}>{STRINGS.home.title}</Text>
      <Text style={styles.title}>{STRINGS.home.headline}</Text>
      <Link href={ROUTES.adventureMap as never} style={styles.primaryAction}>
        {STRINGS.home.adventureCta}
      </Link>
    </View>
  );
}
