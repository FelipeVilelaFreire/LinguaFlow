import { useRouter } from "expo-router";
import type { ReactNode } from "react";
import { useEffect, useRef, useState } from "react";
import { Modal, Pressable, StyleSheet, Text, View } from "react-native";
import { STRINGS } from "@linguaflow/shared-core";

export function AdventureTransitionButton({
  children,
  href,
  style,
}: {
  children: ReactNode;
  href: string;
  style?: object;
}) {
  const router = useRouter();
  const [visible, setVisible] = useState(false);
  const timers = useRef<ReturnType<typeof setTimeout>[]>([]);

  useEffect(() => {
    return () => {
      timers.current.forEach((timer) => clearTimeout(timer));
    };
  }, []);

  function navigate() {
    setVisible(true);
    timers.current.push(setTimeout(() => router.push(href as never), 550));
    timers.current.push(setTimeout(() => setVisible(false), 980));
  }

  return (
    <>
      <Pressable style={style} onPress={navigate}>
        {children}
      </Pressable>
      <Modal transparent visible={visible} animationType="fade" statusBarTranslucent>
        <View style={transitionStyles.overlay}>
          <View style={transitionStyles.content}>
            <View style={transitionStyles.mark} />
            <Text style={transitionStyles.title}>{STRINGS.adventure.title}</Text>
            <Text style={transitionStyles.subtitle}>{STRINGS.adventure.loading}</Text>
          </View>
        </View>
      </Modal>
    </>
  );
}

const transitionStyles = StyleSheet.create({
  overlay: {
    alignItems: "center",
    backgroundColor: "#160700",
    flex: 1,
    justifyContent: "center",
  },
  content: {
    alignItems: "center",
    gap: 16,
    paddingHorizontal: 32,
  },
  mark: {
    backgroundColor: "rgba(217,119,6,0.4)",
    height: 1,
    width: 32,
  },
  title: {
    color: "#faf3e0",
    fontSize: 20,
    fontWeight: "800",
    textAlign: "center",
  },
  subtitle: {
    color: "rgba(245,158,11,0.55)",
    fontSize: 11,
    fontWeight: "800",
    textAlign: "center",
    textTransform: "uppercase",
  },
});
