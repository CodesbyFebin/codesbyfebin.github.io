## Contracts before status badges

A specification should explain the inputs, authority, transitions, outputs, and failure behavior of a system. It should be precise enough that an independent implementation or reviewer can check a defined claim. This page combines portfolio review guidance with source-linked technical references. It is not an invented standards body, RFC publication record, or certification program.

## State vocabulary

| State | What it establishes | What it does not establish |
| --- | --- | --- |
| Desired | A request or target exists | Host admission or execution |
| Admitted | A policy decision permits the request | Successful runtime behavior |
| Executing | A worker or runtime reports activity | Correct output |
| Observed | A measurement was collected | Agreement with all acceptance criteria |
| Verified | A defined check accepted the evidence | Claims outside that check’s scope |
| Unknown | Required information is missing | Healthy or failed behavior |
| Simulated | A demonstration substitutes for execution | An actual live operation |

An interface should not erase these differences to make a dashboard look healthy. If a source reports an unavailable integration, the portfolio should not convert it into a live capability. If a proof verifier establishes a limited statement, the product description should preserve that limit. Explicit state is useful both for the operator and for external developer tools.

## Evidence records

A useful record binds its claim to a source revision and an environment. It names the action, inputs, timestamps, result, and supporting artifacts. Artifact digests help identify the exact bytes that were checked. A signer identifies who attested to the record. The verification procedure explains what the consumer must do before accepting it.

Different evidence types answer different questions. Configuration evidence shows how a service was set up. Runtime evidence records what happened during execution. Source evidence identifies the implementation. Approval evidence records a decision by an authorized person or process. A complete workflow can combine these without pretending that any one of them answers everything.

## Negative controls

Acceptance tests should include rejection paths. Alter an artifact after a signature is created. Substitute a different program for a proof. Replay an expired request. Remove a required observation. Use a signer outside the admitted trust set. The system should reject the relevant condition and preserve enough context to explain the refusal.

The expected rejection must be specific. A crashed process is not the same as a verifier correctly refusing an invalid artifact. A timeout may be an infrastructure failure rather than proof of a security property. Record the result category and the supporting output so a reviewer can distinguish them.

## Model and tool boundaries

A model can propose a task, but policy should govern tool execution. Inputs should be validated against a schema before they become authoritative state. Permissions should be checked at the operation boundary. Approvals should bind to the action and its important parameters rather than a vague permission to “continue.”

Durable task systems additionally need idempotency, leases, bounded retries, and explicit terminal states. A queue can improve dispatch latency while the database remains authoritative. Replayed events should be distinguishable from newly executed work. [AgentSwarm](/systems.html#agentswarm) documents a concrete version of these boundaries and its current verification limits.

## Proof and attestation boundaries

A signature and a computational proof are different objects. A signature can authenticate an assertion made by a key holder. A proof can establish a defined relation under a proof system’s assumptions. Neither object automatically proves that the input data is true or that the surrounding business process is correct.

The Rust VM documentation is useful because it states the current instruction and witness scope. Its host-service and threat-model references below separate proving, backend routing, MCP access, and on-chain attestation. Keep those distinctions when building an application on top of the service.

## Source references

The technical references below are snapshots of project documentation reviewed on 3 October 2026. Each includes a direct source URL and the returned GitHub blob identifier. They make detailed setup and limitations available without JavaScript. Commands are documentation, not a report that this portfolio build executed the underlying project.

Use [systems](/systems.html) for architecture context and [projects](/projects.html) for repository discovery. If a specification changes, review the implementation and its conformance evidence together before updating public claims. A stable URL is useful, but it should not hide a changed contract.
