## A source-backed project directory

This directory brings together application repositories, infrastructure work, documentation projects, and forks associated with CodesbyFebin. Each card links to a real GitHub repository reviewed on 3 October 2026. Repository existence and metadata were checked; feature claims and deployment behavior still require source and runtime review in the relevant project.

The directory distinguishes three things that are often confused. An original application repository may contain code worth evaluating, but that does not establish production scale. A fork is a copy of an upstream project and does not establish authorship of the upstream implementation. A documentation scaffold may be an area of future work, but a generic README is not a completed cookbook or a tested example collection.

Search works on the text already present in the HTML. Category and status filters combine with search, and sorting uses the recorded GitHub snapshot. With JavaScript disabled, every repository remains visible and its source link remains usable. Star counts are dated metadata, not an engineering quality score. Contributor counts are omitted because they were not fetched and verified.

## How to inspect a repository

Start with the default branch and the purpose of the project. Then read setup instructions together with the package manifest, configuration examples, and actual scripts. A command shown in documentation should correspond to a file or executable path in the repository. If it points to a missing example or a placeholder service, record that limitation rather than assuming the implementation exists somewhere else.

Next, identify the narrowest useful demonstration. For a proof VM, run a small program and a tamper check. For a deployment mesh, ship a sample app and follow it through build, node assignment, and routing. For an agent control plane, create a mission with a configured provider and another with the provider unavailable. A focused demonstration makes the product’s real state easier to understand than a large collection of aspirational feature names.

Review security boundaries separately from functionality. A successful API request does not prove tenant isolation. A container launch does not prove hostile workload containment. A model response does not prove tool authorization. A signed result does not prove that the signer observed what it claims. The [specifications guide](/specifications.html) provides a vocabulary for making these checks precise.

## Applications, infrastructure, and references

The featured systems form the architecture-oriented core of the portfolio. Browser tooling and directories connect that work to useful public interfaces. Documentation repositories provide a place to organize future examples and learning material, with their current scaffold status visible. Forks are included where they are relevant to the research and discovery surface, with upstream attribution rather than an implied original implementation.

There is no synthetic “best project” ranking. The useful order depends on the reader’s goal. A systems reviewer may start with the Go control plane or Rust VM. A product engineer may inspect XFree or OM. An agent developer may begin with the mission worker or MCP directory. A contributor may find a narrowly scoped documentation improvement more appropriate than a runtime change.

## Contribution paths

A useful first contribution makes an existing behavior easier to reproduce or understand. That might be a minimal failing example, a corrected command, a negative control, a route fix, or a clarification of an unsupported capability. Check the repository’s contribution and security guidance before posting sensitive information. If a change alters a security boundary, explain the before/after behavior and the evidence needed to accept it.

For collaboration across several repositories, agree which project is authoritative for the work. Keep source changes and evidence in that project rather than copying stale claims between websites. The portfolio is a discovery layer: it should help readers reach the current source, not become a competing operational truth. [Open-source workflow](/contributions.html) and [contact](/contact.html) explain practical ways to begin.
