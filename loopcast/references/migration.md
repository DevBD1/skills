# Migration from Buildcast

Use only within the requested repository when updating an existing Buildcast
installation or binding to LoopCast. The shared skill rename does not authorize
modifying every project on disk.

- Inspect agent bindings, the content hub and automation prompts for the old
  skill name or invocation. Update active references to LoopCast / `$loopcast`.
- Preserve the existing content directory, post filenames, URLs, published text,
  follow-up links, metrics snapshots, retros, playbook and reply queue. The skill
  rename does not require renaming `docs/content/` or resetting its templates.
- Patch the existing binding and content hub; do not install a duplicate content
  system or compatibility rulebook. Reconcile any conflicting new/old owners
  before declaring the migration complete.
- Link the content hub from the existing documentation index. Keep development
  and delivery status with their LoopDev/LoopShip or existing repository owners.
- Preserve historical branding where it records what was actually published.
  Update controllable consumers in scope; report inaccessible external consumers
  as pending rather than claiming complete cutover. Do not enable or reschedule
  automations as a side effect of renaming.
