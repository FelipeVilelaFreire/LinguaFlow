import type { ReactNode } from "react";
import { Modal, Pressable, Text, View } from "react-native";
import type { ModalProps, StyleProp, ViewStyle } from "react-native";
import { styles } from "./BaseModal.styles";

type BaseModalProps = {
  animationType?: ModalProps["animationType"];
  children: ReactNode;
  contentStyle?: StyleProp<ViewStyle>;
  onClose: () => void;
  panelStyle?: StyleProp<ViewStyle>;
  visible: boolean;
};

export function BaseModal({
  animationType = "fade",
  children,
  contentStyle,
  onClose,
  panelStyle,
  visible,
}: BaseModalProps) {
  return (
    <Modal animationType={animationType} transparent visible={visible} onRequestClose={onClose}>
      <Pressable style={[styles.backdrop, contentStyle]} onPress={onClose}>
        <Pressable style={[styles.panel, panelStyle]} onPress={(event) => event.stopPropagation()}>
          <Pressable style={styles.closeButton} onPress={onClose}>
            <Text style={styles.closeButtonText}>x</Text>
          </Pressable>
          {children}
        </Pressable>
      </Pressable>
    </Modal>
  );
}
