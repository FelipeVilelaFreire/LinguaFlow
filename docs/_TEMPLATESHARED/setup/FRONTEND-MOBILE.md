# Frontend — Mobile (React Native + Expo)

> Concrete patterns for the mobile side. Read this when creating mobile routes, screens, components, or platform-specific wrappers.

Stack: **React Native 0.76+ · Expo SDK 52+ · Expo Router · TypeScript 5 · @react-native-async-storage/async-storage · React Native Reanimated 3 · @hobbymap/shared-core**.

The mobile app is **render-only**. All logic comes from `@{{project}}/shared-core`. This file describes only the platform wrapper and rendering.

Shared features should mirror the web tree by responsibility. If a mobile feature intentionally differs from web, record it in `docs/PARITY-AUDIT-EXECUTION.md`.

---

## 📁 Mobile Folder Structure

```
mobile/
├── app/                          # Expo Router (file-based routing)
│   ├── _layout.tsx               # Root layout, font loading, providers
│   ├── (auth)/
│   │   ├── _layout.tsx
│   │   ├── login.tsx
│   │   └── register.tsx
│   ├── (tabs)/
│   │   ├── _layout.tsx           # Tab bar
│   │   ├── home.tsx
│   │   └── profile.tsx
│   └── {{entity}}/[id].tsx
│
├── src/
│   ├── components/
│   │   ├── ui/                   # Primitives: Button, Input, BottomSheet, Icon
│   │   ├── shared/               # Header, TabBar, SafeAreaWrap
│   │   ├── features/             # {{Entity}}Detail/, etc.
│   │   └── cards/
│   ├── screens/                  # Fetch wrapper (mirrors shared-core hook)
│   ├── hooks/                    # Platform wrappers (thin, 5-line files)
│   ├── lib/
│   │   ├── apiClient.ts          # axios instance + JWT, set via shared-core
│   │   ├── storageAdapter.ts     # AsyncStorage adapter
│   │   └── iconMapper.ts         # FontAwesome registration
│   └── types/                    # Mobile-only types (rare — Props mostly)
│
├── assets/                       # Fonts, images, icons
├── app.json                      # Expo config
├── package.json
├── tsconfig.json
└── babel.config.js
```

---

## 🛣️ Routing — Expo Router

Same model as Next.js App Router but file extensions are `.tsx` directly (no `page.tsx` wrapper).

```typescript
// app/(tabs)/home.tsx
import { HomeScreen } from '@/src/screens/HomeScreen';
export default function Page() {
  return <HomeScreen />;
}
```

```typescript
// app/{{entity}}/[id].tsx
import { useLocalSearchParams } from 'expo-router';
import { {{Entity}}Screen } from '@/src/screens/{{Entity}}Screen';

export default function Page() {
  const { id } = useLocalSearchParams<{ id: string }>();
  return <{{Entity}}Screen id={Number(id)} />;
}
```

Rules:
- 5-line wrapper at most
- Zero logic
- All state and fetch in the screen via the shared-core hook

---

## 🔌 Boot — set adapters from shared-core

```typescript
// app/_layout.tsx
import { Stack } from 'expo-router';
import { useEffect } from 'react';
import { useFonts } from 'expo-font';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { setStorageAdapter, setApiClient } from '@{{project}}/shared-core';
import { apiClient } from '@/src/lib/apiClient';

export default function RootLayout() {
  useEffect(() => {
    setStorageAdapter({
      getItem:    AsyncStorage.getItem,
      setItem:    AsyncStorage.setItem,
      removeItem: AsyncStorage.removeItem,
      multiRemove: AsyncStorage.multiRemove,
    });
    setApiClient(apiClient);
  }, []);

  const [loaded] = useFonts({
    Manrope: require('../assets/fonts/Manrope-Bold.ttf'),
    Inter:   require('../assets/fonts/Inter-Regular.ttf'),
  });
  if (!loaded) return null;

  return <Stack screenOptions={{ headerShown: false }} />;
}
```

---

## 🎨 Styling — StyleSheet + shared-core tokens

```typescript
// src/components/features/{{Entity}}Detail/{{Entity}}Detail.tsx
import { View, Text, StyleSheet } from 'react-native';
import { SPACING, COLORS, RADIUS, FONT_SIZE, FONT_FAMILY } from '@{{project}}/shared-core';
import { STRINGS } from '@{{project}}/shared-core';
import type { {{Entity}} } from '@{{project}}/shared-core';

interface Props { entity: {{Entity}}; }

export function {{Entity}}Detail({ entity }: Props) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{STRINGS.{{entity}}.detail.title}</Text>
      <Text style={styles.body}>{entity.description}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: SPACING.lg,
    backgroundColor: COLORS.white,
    borderRadius: RADIUS.xl,
  },
  title: {
    fontFamily: FONT_FAMILY.bold,
    fontSize: FONT_SIZE['2xl'],
    color: COLORS.gray900,
    letterSpacing: -0.5,
  },
  body: {
    fontFamily: FONT_FAMILY.regular,
    fontSize: FONT_SIZE.base,
    color: COLORS.gray700,
    marginTop: SPACING.md,
  },
});
```

Rules:
- Never hardcode `padding: 16` — use `SPACING.lg`
- Never hardcode `color: '#fff'` — use `COLORS.white`
- Never use `fontWeight: 'bold'` — use `fontFamily: FONT_FAMILY.bold` (RN renders fonts differently from CSS)
- One file per component, `StyleSheet.create` at the bottom

---

## 🪝 Hook Wrappers

Every shared-core hook gets a thin mobile wrapper that injects router/Alert:

```typescript
// src/hooks/{{entity}}/use{{Entity}}Screen.ts
import { use{{Entity}}Screen as useCore } from '@{{project}}/shared-core';
import { router } from 'expo-router';
import { Alert } from 'react-native';
import { ROUTES } from '@{{project}}/shared-core';

export function use{{Entity}}Screen(id: number) {
  return useCore({
    id,
    onSuccess: () => router.back(),
    onError: (msg) => Alert.alert('Erro', msg),
  });
}
```

The screen consumes this wrapper:

```typescript
// src/screens/{{Entity}}Screen/{{Entity}}Screen.tsx
import { View, ActivityIndicator } from 'react-native';
import { use{{Entity}}Screen } from '@/src/hooks/{{entity}}/use{{Entity}}Screen';
import { {{Entity}}Detail } from '@/src/components/features/{{Entity}}Detail';

export function {{Entity}}Screen({ id }: { id: number }) {
  const { data, loading, error, handleSave, handleDelete } = use{{Entity}}Screen(id);
  if (loading) return <ActivityIndicator />;
  if (error || !data) return null;
  return <{{Entity}}Detail entity={data} onSave={handleSave} onDelete={handleDelete} />;
}
```

---

## 📱 Mobile-specific primitives

| Primitive | Web equivalent | Notes |
|-----------|---------------|-------|
| `View` | `<div>` | Default container |
| `Text` | `<span>` / `<p>` | Always wrap text in `Text` (RN crashes otherwise) |
| `Pressable` | `<button>` | Preferred over `TouchableOpacity` in 0.76+ |
| `ScrollView` / `FlatList` | `<div>` + `.map()` | Use `FlatList` for large lists |
| `BottomSheetModal` | `BottomModal` web | From `@gorhom/bottom-sheet` |
| `Alert.alert()` | `window.alert()` | Native dialog |
| `Animated`, `Reanimated` | CSS transitions | Use Reanimated 3 for performance |

---

## 🌐 Strings & Icons

Same as web — imported from shared-core:

```typescript
import { STRINGS, ICON_NAMES } from '@{{project}}/shared-core';
import { Icon } from '@/src/components/ui/Icon';

<Text>{STRINGS.{{entity}}.title}</Text>
<Icon name={ICON_NAMES.heart} size={24} color={COLORS.primary} />
```

The `Icon` component is platform-specific (uses `@fortawesome/react-native-fontawesome`), but consumes the same `ICON_NAMES` from shared-core.

---

## 🚦 Pre-merge Mobile Checklist

- [ ] No business logic in components? (only shared-core hooks)
- [ ] Hook wrappers are thin (~5 lines, just inject router/Alert)?
- [ ] Feature/component tree mirrors web where the feature exists on both platforms?
- [ ] All text via `STRINGS` from shared-core?
- [ ] New strings exist in `pt-BR.ts`, `en.ts`, and `de-DE.ts` in shared-core?
- [ ] All visual values use shared-core tokens (`SPACING`, `COLORS`, `RADIUS`, `FONT_*`)?
- [ ] No `fontWeight` — only `fontFamily`?
- [ ] All `Text` wraps actual text (no bare strings in `<View>`)?
- [ ] AsyncStorage adapter registered in `app/_layout.tsx`?
- [ ] API client registered in `app/_layout.tsx`?
- [ ] Icons registered in `lib/iconMapper.ts`?
- [ ] Component folder has barrel `index.ts`?
