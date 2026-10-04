## Systems with explicit boundaries

The selected systems explore different layers of the same engineering problem: how to connect intent to execution and preserve enough evidence to inspect the result. They are separate repositories with different languages, assumptions, and maturity. The descriptions below are based on source documentation reviewed on 3 October 2026. A documentation review is not a new runtime qualification, security audit, or production deployment test.

### What each system is for

| System | Primary question | Inspect first |
| --- | --- | --- |
| rust-stark-zkvm | How can a small VM execution be checked with a STARK proof? | ISA, AIR, verifier, threat model |
| Decentralized.Host | Who admits work, and how does observed state differ from intent? | Local policy, identity, protocol, evidence |
| decentralized.hosting | How does uploaded source become a running container? | Build path, scheduler, agent, edge routing |
| AgentSwarm | How does an agent mission survive worker and queue failures? | Database state, leases, events, artifacts |
| OM | How can a personal AI workspace expose service readiness honestly? | Workspace records, model configuration, setup boundaries |
| XFree | How can browser tools and a discovery site remain distinct products? | Marketing repository and app repository |

## rust-stark-zkvm

The Rust project combines an interpreter, an algebraic intermediate representation, and Winterfell proving and verification. Its small instruction set includes arithmetic, forward conditional jumps, and a fixed register file. This scope makes it possible to inspect how a program becomes an execution trace and how the proof binds to the expected program.

The repository documents an important limitation: this implementation has no private witness, and its verifier re-executes the program to determine expected trace information. It should therefore not be marketed as general private LLM inference, arbitrary confidential analytics, or a production replacement for a general-purpose zkVM. Its value is an inspectable implementation of a defined computation contract.

The HTTP host exposes proving and verification interfaces. The MCP tools provide another interface to the same underlying service. Neither interface changes what the proof establishes. The on-chain demo also has its own trust boundary: an attested proof result is different from a fully on-chain STARK verifier. [Technical specifications](/specifications.html#zkvm-threat-model) include the source threat model and service documentation.

For a first review, read the instruction parser, execution semantics, and AIR together. Check what happens when the program, claimed result, active flags, or register selectors are changed. A negative control is particularly useful because a verifier that accepts everything can still appear to pass a collection of positive examples. The repository guide below preserves the original setup commands and explicit limitations.

## Decentralized.Host

Decentralized.Host is the Go repository at [CodesbyFebin/Decentralized-](https://github.com/CodesbyFebin/Decentralized-). The portfolio’s existing identity describes signed intent, Ed25519 identities, per-host admission, content-addressed storage, Raft, and WireGuard. Its central principle is that an execution host retains authority over the work it admits.

The current README contains both broad infrastructure descriptions and a provider-discovery direction, with some capabilities assigned to later versions. That mixed scope makes a blanket production-readiness claim inappropriate. This portfolio links to the source and conformance documentation without treating every README badge as independently reproduced evidence.

When inspecting this system, ask which state is authoritative for the decision you are making. A control-plane request can describe desired placement without establishing that a host accepted it. A host observation can establish a process or workload exists without proving application behavior. A cryptographic signature can establish the signer without establishing operational correctness. Each layer needs its own check.

Review local policy, admission failure behavior, revocation, replay handling, source-bound evidence, and recovery under failure. Protocol conformance can show agreement between implementations for defined vectors. It does not replace a qualification on the actual machines, network, operating system, and workload combination used in an installation. [The conformance reference](/specifications.html#dh-conformance) explains the documented test surface.

## Deployment mesh

The separate [decentralized.hosting repository](https://github.com/CodesbyFebin/decentralized.hosting) is a Python deployment mesh. Its documented architecture uses a FastAPI control plane, PostgreSQL, a Docker node agent, Traefik, a local registry, and the dhost CLI. It is a runnable local MVP with a concrete upload, build, schedule, and route path.

The distinction between the developer machine and the execution host matters. The documented ship workflow uploads a source snapshot to the control plane. The node agent builds and runs the workload on the host Docker daemon. The developer does not need to run the container build locally for that path. The older init/deploy workflow remains a different path that performs a local build.

A good review follows the same deployment through every component. Confirm the snapshot identity, build result, selected node, container state, and route. Then make an update and inspect the release history before exercising rollback. The README describes optional blockchain credits as devnet-only and disabled by default; that is not evidence of a production financial settlement service.

Host Docker access is an important trust boundary. An operator should inspect the node agent’s access and the deployment environment before admitting workloads. The project’s documented local workflow is useful evidence of scope, but it does not by itself establish hostile multitenant isolation. Its source guide below is presented as project documentation, with commands linked back to the repository.

## AgentSwarm

AgentSwarm connects a React command center to a Fastify API, PostgreSQL durable state, worker execution, a configured model provider, events, and artifacts. Its README now describes a real backend path rather than a client-side timer simulation. The worker’s state transitions remain distinct from the model’s generated output.

PostgreSQL is documented as the source of mission and task truth. Redis/BullMQ provides wake-up signals, while persisted claims and leases govern execution. This design makes a queue message a hint rather than a second source of authority. A fallback poll supports progress when the queue is unavailable, and bounded retries keep recovery from becoming an unlimited execution loop.

The repository documents real authentication and organization/project boundaries, together with remaining production-hardening work. Its current completion check verifies that succeeded tasks have persisted artifacts. That check is useful but narrow: it is not a build gate, security review, or proof that the task’s reasoning was correct. The source guide makes this limitation explicit.

When evaluating an agent mission, inspect approval handling, expired lease recovery, event replay, and artifact provenance. Try a provider-unavailable path as well as a successful model call. Missing billing or token data should remain unknown. The [collaboration page](/services.html) describes how these questions can become a focused architecture or verification engagement.

## OM

OM is a personal AI workspace that brings missions, agents, notes, prompts, findings, and infrastructure setup into one interface. The current repository documents workspace persistence and configuration surfaces for models, vector memory, object storage, and owned execution services. Those surfaces should not be confused with already-configured external infrastructure.

The README explicitly distinguishes available workspace features from services that need endpoints, credentials, bindings, or owned workers. Local inference requires a reachable model service. Semantic retrieval requires the configured memory system. Autonomous execution requires an owned sandbox worker. These are operational requirements, not decorative badges.

A practical review begins with durable workspace records and service readiness. Create and retrieve a note or project, then inspect what the application reports for an unavailable model endpoint. Check whether opting into a cloud provider is explicit. Follow the documented self-hosting requirements before calling the complete deployment sovereign or private.

## XFree

XFree is a browser tooling and discovery project. The current marketing repository is [xfree.in](https://github.com/CodesbyFebin/xfree.in), while [xfree-app](https://github.com/CodesbyFebin/xfree-app) is a separate application repository. The current marketing README documents a Next.js site and explicitly says the app lives elsewhere.

This differs from the supplied draft, which described XFree as a cryptographic library with private messaging and anonymous credentials. Those claims do not belong in this portfolio. Useful inspection questions concern the actual tools, their client/server boundary, input handling, discoverability, and the relationship between the marketing site and the application.

## Read the source guides

The following sections preserve selected technical documentation from the public repositories. They are reference snapshots, with retrieval dates and source-file identifiers. Statements about prior tests belong to the source documentation; this website build does not rerun those project test suites. Use the linked repository to inspect current implementation and evidence before making a deployment decision.
