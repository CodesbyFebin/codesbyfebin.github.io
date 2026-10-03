## Collaboration around a concrete system

I’m interested in collaboration on AI infrastructure, systems architecture, verifiable compute, self-hosted deployment, and developer tooling. A useful engagement starts with a defined problem and an inspectable outcome. This page describes possible working models, rather than publishing unverified availability, fixed prices, customer logos, or testimonials.

### AI infrastructure architecture

An architecture review can map model calls, tool access, task state, approvals, artifacts, and verification. The goal is to identify where authority lives and what happens when a dependency fails. A useful deliverable includes the current flow, the failure modes, a proposed change, and acceptance criteria that a reviewer can reproduce.

Typical questions include whether a model can mutate state directly, whether retries can duplicate side effects, how a worker lease is recovered, and how approvals bind to a particular action. The [AgentSwarm guide](/systems.html#agentswarm) provides examples of state and queue boundaries. A review should use the actual implementation instead of treating a diagram as evidence that every component exists.

### Self-hosted deployment design

A deployment review can follow source through build, scheduling, execution, observation, and rollback. It can also map identity, host admission, routing, and backup responsibilities. The scope should name the environments and workload types being considered, because a local single-machine demonstration answers different questions from a geographically distributed installation.

Useful outputs include a deployment map, an operational runbook, a recovery exercise, and an evidence manifest. Production readiness should be tied to agreed gates rather than a broad checklist with unchecked items. The [hosting systems](/systems.html#decentralized-host) show the portfolio’s focus on explicit authority and observed state.

### Verifiable compute exploration

A focused proof-system collaboration can clarify what is being proved, what inputs are public, what the verifier assumes, and which part of the application remains trusted. This is especially important when a proof service is connected to an HTTP API, MCP client, or payment workflow. The interface is not the proof statement.

Possible work includes a small instruction example, a trace explanation, a tamper test, or a documentation review of trust boundaries. This portfolio does not offer an independent cryptographic certification or claim that a small VM already implements private general-purpose AI inference. [The Rust VM](/systems.html#rust-stark-zkvm) and [specifications](/specifications.html) provide a concrete starting point.

### Developer platforms and discovery

Directories and developer tools benefit from a shared data model, consistent publication rules, useful navigation, and route-level metadata. Work can include a source-backed catalog, a technical documentation surface, or an accessible static portfolio. The acceptance criteria should describe the actual visitor flow, not promise a ranking or an AI citation score.

For discovery-oriented projects, distinguish verified record properties from unknown ones. A search engine can index a page, but no implementation can guarantee that it will rank for a particular query. Structured data should describe visible content accurately. Relevant projects can be found in [the directory](/projects.html).

## Working models

### Focused review

A focused review is appropriate when an implementation already exists and a decision is blocked. Share the repository, the current behavior, the expected behavior, and the most important uncertainty. The result should help decide what to change, what to test, or what to postpone. A short reproducible finding is more useful than an exhaustive list of hypothetical improvements.

### Implementation collaboration

Implementation work should begin with a bounded feature or corrective change. Agree on inputs, outputs, permissions, and acceptance gates before broadening the scope. Keep the code and validation in the authoritative repository. Review the final behavior using the same concrete scenario that motivated the work.

### Open-source contribution

Open-source collaboration can begin with a minimal issue, documentation correction, test fixture, or narrowly scoped pull request. A useful contribution preserves current capability boundaries and improves the reader’s ability to reproduce the result. [The contributions page](/contributions.html) describes the workflow.

## What a good brief includes

Describe the system and who operates it. Name the repository and relevant revision. Explain the behavior that needs to change. Identify data sensitivity, deployment constraints, and the decision deadline if one exists. Define what evidence would make the result acceptable. Avoid sharing secrets in public issues or initial messages.

Pricing, timelines, scope, and availability should be agreed directly after the work is understood. There is no automatic booking or payment flow on this standalone site. Use the verified public profiles on [contact](/contact.html), or generate a local brief there and copy it into the channel you choose.
