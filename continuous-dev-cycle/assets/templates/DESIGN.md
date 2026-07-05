# Design

This is the UI/UX source of truth: flows, layout, interaction, and visual system. Implementation conventions belong in service READMEs or code; product vision belongs in `PRODUCT.md`.

## Flows

Describe the primary user journeys end to end. One subsection per flow.

### Flow: <name>

- **Entry:** where the user starts.
- **Steps:** the screens/states in order and what moves the user forward.
- **Exit / success:** what done looks like.
- **Errors and empty states:** what the user sees when things are missing or fail.

## Layout

- **Structure:** overall page/screen anatomy (navigation, content areas, common regions).
- **Responsive rules:** breakpoints and what changes at each.

## Interaction

- **Patterns:** how selection, editing, confirmation, undo, and destructive actions behave.
- **Feedback:** loading, progress, success, and error conventions.
- **Accessibility:** keyboard, focus, contrast, and screen-reader expectations.

## Visual System

- **Color:** palette and semantic roles (primary, surface, danger, …).
- **Typography:** families, scale, and usage rules.
- **Spacing and shape:** spacing scale, radii, elevation.
- **Components:** the canonical component set and where each is used.
