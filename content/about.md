## Febin Francis · CodesbyFebin

I’m a systems engineer and open-source builder based in Kerala, India. My focus is AI infrastructure, verifiable compute, and sovereign systems. I work across agents, runtimes, protocols, control planes, proof systems, and developer tooling. The connecting theme is control: people should be able to understand what their infrastructure is doing and inspect the basis for important execution claims.

The name CodesbyFebin is the public handle for this work. GitHub is the primary source surface. The portfolio organizes those repositories so readers can move from a short explanation to architecture, limitations, and the relevant implementation. My [LinkedIn profile](https://www.linkedin.com/in/codes-by-febin/) is a professional discovery surface, and my [ORCID profile](https://orcid.org/0009-0002-8123-1531) is a research identity link. An identity link does not establish a publication record by itself.

## How I think about systems

A system is easier to trust when it has an explicit contract. Inputs, permissions, state transitions, outputs, and failure behavior should be understandable before a worker starts. An agent should not acquire a wider scope because a model produced confident prose. A deployment should not become healthy because the scheduler intended it to start. An artifact should not become verified because it exists in a directory.

I therefore separate desired, admitted, executing, observed, and verified state. Each state answers a different question. Desired describes a request. Admitted describes a policy decision. Executing describes activity. Observed describes measurements. Verified describes a check against a defined criterion. The distinction makes debugging more useful and gives operators a clearer basis for approval and recovery.

## Engineering principles

### Keep authority explicit

Authority should have an owner and a boundary. In self-hosted infrastructure, the host should retain admission authority. In an agent workflow, tools should expose clear capabilities and enforce their own policy. In a public catalog, publication rules should be consistent across HTML, feeds, and machine-readable data. A shared policy function is more reliable than several pages each inventing their own interpretation.

### Preserve uncertainty

Unknown is a useful state. If a provider does not report billing information, a dashboard should not estimate a cost and present it as an observed value. If a worker cannot reach a service, the interface should show that the operation is unavailable or failed. Clear uncertainty keeps an operator from making a decision on fabricated confidence.

### Make refusals inspectable

A refusal can be a successful policy outcome. The system should record what was requested, why it was denied, and which policy revision applied. Otherwise the operator cannot distinguish an intentional denial from a crashed worker. Positive and negative evidence both belong in a useful execution record.

### Prefer reproducible checks

A meaningful check should be repeatable by another person with the same inputs and a documented environment. Tests, source revisions, artifact digests, and command results make that possible. A badge without a link to the relevant evidence gives readers little to inspect. A detailed result without its source revision can also become misleading after the implementation changes.

### Build usable interfaces

Technical honesty should not make a product hard to use. A reader should find source links without searching through a wall of text. An operator should understand a blocked task and the action needed to resolve it. A contributor should be able to run a small example before learning every subsystem. Usability and correctness reinforce each other when the interface exposes the right distinctions.

## Areas of work

Verifiable compute includes the small Rust STARK VM, its instruction semantics, proof interfaces, and documented trust boundaries. Sovereign infrastructure includes the Go control-plane work and a separate Python deployment mesh. AI infrastructure includes persisted missions, model routing boundaries, MCP discovery, and local-service configuration. Developer tooling includes browser tools and source-backed discovery surfaces.

These areas overlap, but they should not be collapsed into one claim. A local-model configuration panel is not evidence that inference succeeded. A proof service is not automatically a private-input inference engine. A directory of MCP servers is not the same product as a managed MCP runtime. The [systems overview](/systems.html) explains the distinction between the selected projects.

## Working from Kerala, India

I’m based in Kerala, India, and use Indian Standard Time, UTC+5:30. This is useful scheduling context for collaboration, rather than a claim about offices, employees, or service coverage. Remote collaboration should begin with written scope, a shared repository, clear review points, and agreed handling of sensitive information.

This portfolio intentionally concentrates on inspectable work. Employment history, educational qualifications, customer testimonials, publication counts, and community impact totals are not added unless there is a specific authoritative record to support them. Readers can assess the repositories directly through [projects](/projects.html) and the workflow through [contributions](/contributions.html).
