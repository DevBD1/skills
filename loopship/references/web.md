# Web profile

Use this environment mapping when it matches the project:

| Environment | Frontend | Backend | Acceptance |
| --- | --- | --- | --- |
| dev | Local dev server | Local API | Local integration checks |
| stage | Stage domain | Stage API | Hosted smoke tests and relevant user journeys |
| main | Production domain | Production API | Post-deploy smoke checks and health receipts |

Discover provider, domains, project/account IDs, build roots, frontend API injection and backend resource bindings. Do not assume the local backend needs a hosted development environment. Separate frontend and backend path filters while including shared packages, lockfiles and build configuration where they affect outputs.

Record deployment order and compatibility. Prefer backend changes compatible with both old/new frontends; coordinated breaking changes or data migrations need an explicit project rollout plan. A frontend build must resolve its intended API and public URL; verify the deployed artifact/configuration and behavior, not merely the branch name. Staging must not silently use production databases or APIs.

A web release may use commit/deployment identity without a marketing version. Configure GitHub Release creation only when the project wants versioned releases, and choose its version trigger deliberately. Do not force mobile version-bump rules onto every web deploy.

Bind successful deployments to the source commit, domain and backend revision. Verify health plus a scoped user journey. Record rollback for both components, including migration compatibility; reverting frontend code alone is not a database rollback. A successful hosting job is not evidence that the application/API works.
