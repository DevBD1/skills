# Migration from Autoscrum

Use when replacing an installed Autoscrum document/workflow binding with
LoopDocs. This is a documentation migration, not automatic adoption of a new
development tracker or release system.

1. Inspect existing instructions, docs, scripts and CI consumers. Identify
   durable product/design/architecture content, active work, release policy
   and historical records before changing any path.
2. Map useful documentation to its existing owners using the document hierarchy.
   Preserve valid content and established names. Update Autoscrum skill
   references and active entrypoint bindings to LoopDocs's documentation role.
   Do not keep duplicate installed skills or a compatibility rulebook.
3. Remove superseded sprint requirements from active agent/contributor guidance
   as authorized by the migration. Preserve historical sprint records and their
   links; do not delete history as part of dropping the process. If active work
   is stored there, use LoopDev's migration rules and the user's chosen inventory
   to transfer it without losing items. Until resolved, retain a clear pointer
   to that active work rather than falsely declaring migration complete.
4. Keep release policies, valid runbooks and existing CI intact. LoopShip owns
   their adoption or repair. A documentation rename does not authorize deleting
   or activating workflows. Link established release owners; do not invent a
   release contract or versioning scheme to replace an old reference.
5. Update inbound links, indexes and consumers together. If historical material
   is moved under the repo's archive convention, preserve provenance and record
   the old-to-new mapping. Remove an obsolete process document only after useful
   content and active consumers are accounted for.
6. Validate discovery and links. Report what documentation changed, what history
   was retained, and any work/release migration still outstanding.
