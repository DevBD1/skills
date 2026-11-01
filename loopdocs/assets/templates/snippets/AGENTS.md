## Documentation routing

<!-- Merge into the existing agent entrypoint. Resolve paths and remove rows
for absent documents; do not install a second rulebook. -->

| Question | Owning source |
| --- | --- |
| What is this project and how do I use/run it? | `README.md` |
| Where are detailed guides, references and operational docs? | `docs/README.md` |
| Who is the product for and what guides scope? | `PRODUCT.md` |
| How should the UI behave and look? | `DESIGN.md` |
| How does the current system work? | `ARCHITECTURE.md` |
| How does this component run? | `<component>/README.md` |
| How is work selected, implemented and reviewed? | `.agents/skills/loopdev/config.md` |
| What governs releases, promotion and delivery? | `.agents/skills/loopship/config.md` |
| What has shipped? | `CHANGELOG.md` |
| Where are content ideas, drafts and post lessons? | `docs/content/README.md` |

Keep documentation current with the change that affects it. Use LoopDocs when
available to maintain roles, content and links; the table above is the local
map even when the skill is unavailable. Preserve one owner per rule or fact
and reference it elsewhere. Product intent, current behavior, work status and
shipped history are distinct kinds of information.
