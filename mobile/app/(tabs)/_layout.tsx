import { Tabs } from "expo-router";
import { STRINGS } from "@linguaflow/shared-core";

export default function TabsLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false }}>
      <Tabs.Screen name="home" options={{ title: STRINGS.nav.home }} />
      <Tabs.Screen name="adventure" options={{ title: STRINGS.nav.adventure }} />
      <Tabs.Screen name="study" options={{ title: STRINGS.nav.study }} />
      <Tabs.Screen name="vocabulary" options={{ title: STRINGS.nav.vocabulary }} />
      <Tabs.Screen name="profile" options={{ title: STRINGS.nav.profile }} />
    </Tabs>
  );
}
