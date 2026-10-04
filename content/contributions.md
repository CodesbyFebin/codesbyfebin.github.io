## Contributions that readers can inspect

Open source works best when a contribution can be understood and reproduced by someone who was not present during its development. My portfolio links to source repositories, describes their scope, and preserves the distinction between original work, forks, and documentation scaffolds. It does not infer merged pull requests, mentoring totals, or upstream authorship from repository ownership.

GitHub is the primary place to inspect the work. Follow the [project directory](/projects.html) to the repository, then review its history, contribution guidance, and test surface. A fork can be a useful learning or integration surface, but copying an upstream repository is not evidence that its implementation was written here. Upstream links are included where the GitHub record identifies a parent.

## Start with a reproducible problem

A good issue describes the revision, environment, command, expected behavior, and observed behavior. Include the smallest input that demonstrates the problem. Explain whether the result is a failure, an unavailable dependency, or an unknown state. This gives maintainers enough context to reproduce the issue without guessing which assumption was different.

Screenshots are useful for interface problems, while logs and artifacts are useful for runtime behavior. Remove credentials, personal data, and unrelated information before sharing them. For a suspected security problem, read the repository’s security policy and use the appropriate private reporting route rather than publishing an exploit path in a general issue.

## Make a focused change

A focused pull request explains the trigger and the resulting behavior. If a worker previously retried indefinitely, describe the limit and the terminal state. If a verifier accepted a tampered artifact, show the negative control that now fails. If a documentation command was wrong, connect the correction to the actual file or script.

Tests should address the failure mode rather than mirror the implementation. A negative control can show that a gate rejects the condition it was designed to reject. A recovery scenario can show that persisted state survives a worker restart. A route check can show that a link reaches a real page. Scale validation to the change and keep the result reviewable.

## Documentation is part of the interface

Documentation should distinguish setup, implementation, and roadmap. A configuration example is not a measured integration. A tool schema is not proof that the tool is safe. A local run is not production qualification. Readers need these boundaries to decide whether the project is appropriate for their environment.

Some cookbook repositories in this portfolio currently have generic templates and placeholder examples. Those are labeled as documentation scaffolds. A useful contribution replaces a placeholder with a real minimal example, names its dependencies, and records what was tested. Adding more optimistic prose to the same scaffold would not improve its evidence.

## Upstream dependencies and attribution

Projects rely on upstream tools, libraries, and protocols. Winterfell is an upstream proving system used by the Rust VM; using the library does not establish a contribution to its maintainers. Docker, Traefik, PostgreSQL, model APIs, and framework libraries likewise remain separate projects with their own contracts and licenses.

Before reusing code, inspect the repository’s actual license file. GitHub license metadata is a helpful discovery hint but should not substitute for the text and the relevant scope. Preserve attribution when adapting upstream work. For a fork, explain whether the portfolio is documenting a local integration, a specific change, or simply a reference copy.

## Review as a collaboration habit

Review should check the behavior, the boundary, and the explanation together. Does the interface report the state the backend actually has? Does the source implement the feature the page describes? Does the test check the relevant failure? Does the documentation point to the current command? These questions make a contribution useful beyond the first merge.

The same approach applies to this website. Project metadata is a dated snapshot. Public claims should remain conservative when a repository’s documentation is mixed or incomplete. Changes to the portfolio should make source discovery clearer and correct stale explanations rather than manufacture impact statistics.

## Ways to collaborate

Start with a small issue, a bounded source change, an example program, an architecture explanation, or a documentation correction. If work crosses repository boundaries, agree on the authoritative source and acceptance criteria. Use [contact](/contact.html) for a broader collaboration proposal and [services](/services.html) for the kinds of focused reviews that fit this portfolio.
