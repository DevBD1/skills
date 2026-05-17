# Hytale Modding Java Style Guide

This document defines the coding standards for Hytale mod development. Adhering to these patterns ensures thread safety, high performance via ECS, and code maintainability.

---

## 1. General Java Conventions
- **Language Level**: Java 25.
- **Naming**: 
  - **Classes**: `PascalCase` (e.g., `TeleportSystem`).
  - **Methods/Variables**: `camelCase` (e.g., `currentHealth`).
  - **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_HEALTH_LIMIT`).
- **Formatting**: Use 4 spaces for indentation. Avoid deeply nested `if` statements; use guard clauses instead.

---

## 2. ECS Naming & Structure
To maintain clarity in a data-driven architecture, follow these naming rules:

- **Components**: Must end with the suffix `Component` (e.g., `PoisonedComponent`).
- **Systems**: Must end with the suffix `System` (e.g., `PoisonDamageSystem`).
- **Component Access**: Always follow the idiomatic 3-step read pattern:
  1. Acquire the `Ref<EntityStore>`.
  2. Access the `Store<EntityStore>`.
  3. Retrieve data via `store.getComponent(ref, ComponentType)`.

---

## 3. Threading & Safety Standards
Hytale's multi-threaded architecture requires strict discipline to avoid `IllegalStateException` crashes.

- **World Thread Access**: Any operation involving `EntityStore` (reading/writing components) MUST be performed on the world thread.
- **The execution Bridge**: Wrap logic originating from async callbacks or background tasks in `world.execute(() -> { ... })`.
- **Shared State**: Use thread-safe types for data accessed by multiple worlds:
  - Counters: `AtomicInteger`.
  - Mappings: `ConcurrentHashMap`.
  - Boolean flags: `volatile boolean`.
- **Blocking**: Never block the world thread with I/O or `future.join()`. Use async callbacks instead.

---

## 4. Performance Guidelines
- **System Queries**: Use specific `Query` filters (e.g., `Query.and()`, `Query.not()`) to minimize the number of entities processed by a system.
- **Delta Time (dt)**: Always multiply movement or periodic damage logic by `dt` in `EntityTickingSystem` to ensure frame-rate independence.
- **Archetypes**: Be mindful that changing an entity's archetype (adding/removing components) is more expensive than modifying existing component data.

---

## 5. Logging
- **Rule**: Always use `HytaleLogger` for the enclosing class.
```java
private static final HytaleLogger LOGGER = HytaleLogger.forEnclosingClass();

// Usage
LOGGER.atInfo().log("Plugin enabled");
LOGGER.atWarning().log("Something went wrong");
```

---

## 6. Configuration & Files
- **Rule**: Store configurations in a dedicated subfolder inside mods/. Pattern:

```java
// Define path
Path dataDir = Path.of("mods/MyModName");
Path configPath = dataDir.resolve("config.json");

// Load with GSON
try (BufferedReader reader = Files.newBufferedReader(configPath)) {
    config = GSON.fromJson(reader, MyConfig.class);
}
```

## 7. Localization & Text
Rule: Never hardcode user-facing strings. Use LocaleMan.

Basic Message:
```java
Message msg = LocaleMan.get(playerRef, "messages.welcome");
playerRef.sendMessage(msg);
```
With Placeholders:
```java
Message msg = LocaleMan.get(playerRef, "messages.welcome", Map.of(
    "player", playerRef.getUsername(),
    "level", String.valueOf(level)
));
```
Raw String (Console/Logs):
```java
String text = LocaleMan.getRaw("en_US", "messages.system_error");
```
Color Translation:
```java
String colored = ColorMan.translate("&cError: &fInvalid arguments");
```
---

## 8. Documentation & Javadoc
- **Rule**: Provide Javadoc for all public systems and custom component classes explaining their purpose and required queries.