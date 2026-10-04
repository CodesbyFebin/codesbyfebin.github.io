## Infrastructure you can inspect

I’m Febin Francis, an open-source systems builder based in Kerala, India. My work connects AI infrastructure, verifiable compute, and sovereign systems. I’m interested in a practical question: when software reports that work happened, what can another person independently check? That question shapes the way I approach agents, deployment tools, proof systems, and developer platforms.

An execution result is more useful when it comes with context. Which source revision ran? Which policy admitted it? What did the worker observe? Where is the artifact? What does verification cover? A system should preserve these distinctions so operators can make informed decisions. A polished interface helps people understand the evidence; it cannot replace the evidence.

This portfolio brings those ideas together through selected systems, repository guides, technical notes, and collaboration topics. Start with [the systems overview](/systems.html) for architecture, or use [the project directory](/projects.html) to inspect source. Every repository card links to an actual public repository. Documentation projects, forks, and application repositories are identified separately.

## Four connected engineering concerns

### AI infrastructure

AI applications need more than a model endpoint. They need tool permissions, durable task state, bounded retries, approval records, usable artifacts, and clear failure handling. A model can propose work, but the surrounding system must decide what is allowed to happen. My interest is in making that boundary understandable and testable. [AgentSwarm](/systems.html#agentswarm) explores persisted missions and worker execution, while [OM](/systems.html#om) brings projects, knowledge, and infrastructure configuration into one workspace.

### Verifiable compute

Cryptographic proofs can make a specific computation independently checkable under a defined proof system. They do not automatically prove that the input was accurate, that a business decision was justified, or that an entire application is secure. [rust-stark-zkvm](/systems.html#rust-stark-zkvm) provides a deliberately small setting for inspecting an instruction set, execution trace, constraints, prover, and verifier. Its documented limitations are part of the engineering story.

### Sovereign infrastructure

Self-hosting becomes meaningful when an operator can understand and control identity, admission, data, updates, and recovery. Running a container on owned hardware is only one part of that work. The control plane must represent what was requested and what the host actually accepted. [Decentralized.Host](/systems.html#decentralized-host) focuses on those distinctions. The separate [Python deployment mesh](/systems.html#deployment-mesh) explores a concrete FastAPI, Docker, PostgreSQL, and Traefik workflow.

### Developer discovery

Directories should explain where their information came from. A listing with an evidence source, publication status, and retrieval date is easier to inspect than a synthetic ranking. XFree, MCPserver.in, and the BestAIAgent repository are different discovery and tooling surfaces. Their roles are described in [projects](/projects.html), with source links instead of invented reviews, popularity totals, or guaranteed search outcomes.

## Proof over promises

The phrase “proof over promises” is an operating principle, not a claim that every project is formally verified. Different systems need different evidence. A static website can be checked for broken routes, readable HTML, and valid metadata. A deployment platform additionally needs runtime observations and recovery tests. A proof system needs precise statements about constraints and verifier behavior. Matching the evidence to the claim matters more than applying the same green badge everywhere.

My preferred workflow begins with intent, checks policy, records execution, preserves observations, and verifies the resulting artifact. Missing data remains unknown. A configured integration remains configured until an operation has actually succeeded. An example remains an example until its boundaries have been tested in the relevant environment. [The specifications page](/specifications.html) expands these ideas into concrete review questions.

## Build, measure, verify, improve

The languages across this work include Rust, Go, TypeScript, Python, and Shell. The interesting part is how those tools support a contract. Rust can make a VM implementation inspectable; Go can support control-plane and host processes; TypeScript can connect a product interface to persisted state; Python can make deployment and evidence tooling approachable. Language choice should follow the failure modes and operational needs of the system.

If you are evaluating the work, look at the source and the documented boundaries together. If you want to contribute, start with a small reproducible issue or an improvement that makes a system easier to operate. If you want to collaborate, describe the system, the decision you need to make, and the evidence that would make the result useful. [Contact options](/contact.html) and [collaboration models](/services.html) provide a starting point.
