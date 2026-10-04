## Research interests and inspectable experiments

My research interests include execution integrity, sovereign infrastructure, agent governance, and small proof-system implementations. This page organizes questions and source-backed experiments. It does not claim a peer-reviewed publication count, academic appointment, citation total, or award record. The [ORCID profile](https://orcid.org/0009-0002-8123-1531) is an identity reference; publication details should be checked on that record and the relevant publisher.

## Execution integrity

An execution claim has several parts: a source identity, a requested operation, an admission decision, an observed result, and a verification criterion. A useful research question is how to preserve those parts without making the operator reconstruct them from unrelated logs. The answer may involve a shared event format, a source-bound evidence manifest, or a small independent verifier.

The strongest experiment has a negative control. Alter an artifact, replace a signer, change the source revision, or remove a required observation and confirm the result is rejected. A check that accepts the happy path but cannot identify the manipulated one gives less confidence than its green output suggests. The [specifications reference](/specifications.html) develops these questions into review criteria.

## Small proof systems

A deliberately limited VM provides an approachable setting for studying execution traces and constraints. The instruction semantics should be understandable alongside the AIR and verifier. The proof should bind to the program that the reader believes was executed. The privacy assumptions should be explicit before discussing possible applications.

The [rust-stark-zkvm repository](https://github.com/CodesbyFebin/rust-stark-zkvm) is a concrete source surface for this work. Its roadmap and threat model distinguish the present implementation from future directions. The portfolio does not reinterpret those future directions as delivered features, and it does not claim contributions to the upstream Winterfell project without specific contribution records.

## Sovereign control planes

Sovereign infrastructure raises questions about who can authorize work, revoke authority, recover identity, and inspect state. A control plane can request a placement, but a host’s policy should determine admission within its own boundary. A network can preserve agreement on some state while still lacking fresh observations about a workload.

Research and implementation meet at those boundaries. Replay tests can examine whether an old request remains admissible. Partition tests can examine whether a host makes an unsafe assumption when observations are stale. Recovery tests can examine whether evidence remains consistent after a process restart. A result should name the environment and the workload so readers can understand its limits.

## Agent governance

An agent runtime combines probabilistic model output with deterministic authority checks. It is useful to study where those worlds meet. Structured validation can reject an invalid plan before tasks are created. A tool gateway can enforce permission regardless of the model’s phrasing. A durable lease can prevent two workers from independently claiming the same task.

Completion needs a defined criterion. Persisting an artifact is a different claim from verifying its content. An approval should refer to the action being admitted, and a later revision may need a new decision. The [AgentSwarm documentation](/systems.html#agentswarm) offers a practical source for examining these mechanisms and remaining hardening work.

## A reproducible experiment record

A useful experiment record names the question, the revision, the environment, the inputs, the commands, and the result. It explains how errors and missing data were handled. It includes enough artifacts for another person to check the conclusion, and it distinguishes a product failure from an infrastructure failure.

Benchmarks need the same discipline. A latency result without hardware, workload, concurrency, and measurement method is difficult to compare. A proof size without security parameters and trace scope can mislead. A recovery time without the fault and the health criterion can hide an incomplete recovery. This page therefore avoids unsupported performance totals.

## Collaboration and publication

I’m interested in collaboration that produces a concrete experiment, a transparent implementation, or a useful technical explanation. A publication should identify what was measured and what remains an open question. Source code and documentation help make the work inspectable, but they do not establish peer review on their own.

If you want to discuss research, describe the question and the smallest experiment that could answer it. Link the relevant paper or repository and explain what result would change the decision. Use [contact](/contact.html) to reach the public profiles, or review [systems](/systems.html) to find a project with a suitable starting point.
