import { Text, View } from "react-native";
import { STRINGS } from "@linguaflow/shared-core";
import { styles } from "./ProfileScreen.styles";

export function ProfileScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{STRINGS.nav.profile}</Text>
    </View>
  );
}
