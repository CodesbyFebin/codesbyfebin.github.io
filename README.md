# CodesbyFebin master portfolio

A framework-free, pre-rendered portfolio for `https://codesbyfebin.github.io`.

## Run

Python 3.10+ is sufficient; the build and audit use only the standard library.

```bash
python3 scripts/build.py
python3 scripts/audit.py
node --test scripts/ui.test.mjs
python3 -m http.server 8080 --directory dist
```

Open `http://localhost:8080`. Serve `dist`; opening HTML directly from disk is not supported because assets and navigation use site-root URLs.

## Contents

- `content/workspace-articles.json`: 100 adapted, complete workspace article fragments.
- `content/grok-guides.json`: seven newly written guides adapted from supplied platform documentation. They were not previously deployed posts.
- `data/site.json`: canonical origin and actual package date.
- `data/projects.json`: 23 project descriptions retained from the supplied 3 October snapshot, not freshly qualified runtime records.
- `scripts/build.py`: shared pages, search inventory, schemas, graph, feeds, sitemaps, discovery files.
- `scripts/audit.py`: local references and fragments, metadata, JSON-LD, XML, article inventory, and compressed footprint.
- `scripts/ui.test.mjs`: browser-local theme and search behavior using a minimal DOM harness.
- `dist/`: ready static output. No server, account, database, model call, or external JavaScript required.
- `AUDIT.json`: reproducible checks and verification limits.
- `EDITORIAL-CHANGES.json`: traceable removals and date corrections from imported drafts.

## Content and evidence boundaries

The archive has 100 source article bodies, not 100 measured production examples. Their actual source lengths ranged from roughly 700 to 2,300 words. The package does not claim a 2,000- or 2,500-word minimum, 240,000 words, indexed pages, or guaranteed rankings.

The STARK tutorial uses the bounded source note: trace, constraints, commitment, a teaching ISA, program binding, and failure modes. The documented public-program re-execution boundary is retained. Draft timings, unsupported memory and recursion implementation claims, and fake proof-success output are excluded.

Unsupported first-person benchmark, customer, deployment, and long-term operation statements were removed from other drafts. Code snippets are illustrative; examples were not compiled as full applications. The seven application guides summarize real supplied documentation without importing a second application or runtime credentials.

Schema uses Person, WebSite, WebPage, CollectionPage, TechArticle, BreadcrumbList, and FAQPage where matching visible questions exist. QAPage is not used for editorial FAQs. Speakable identifies titles and introductions; it does not establish eligibility for a search feature. No fabricated Organization, LocalBusiness, event, comment, review, or live counter is published.

Article body word counts and reading time come from cleaned body content. Dates in the future relative to this package were corrected to 4 October 2026. XML sitemaps list one canonical URL per page and omit fabricated modification dates.

The security contact points to the public contact page. No email address, signing key, or private reporting mechanism has been invented. GitHub Discussions are not automatically seeded; no messages to other people are sent by the build.

## Deployment

Copy the source files into the intended repository branch and enable GitHub Pages with **GitHub Actions** as its source. The included workflow builds, audits, tests, and uploads `dist`; deployment runs on main or a manual workflow dispatch. A pull request only validates.

For a different host, edit `data/site.json` before building. This package assumes a root-domain site, not a GitHub project subpath. Deploy only `dist`, not source inputs or the editorial change log.

After publishing, verify the live canonical URLs, submit `/sitemap.xml` to Google Search Console and Bing Webmaster, and check search-engine crawl reports. The package cannot submit to accounts without access. Crawler permission, structured data, and `llms.txt` improve access and clarity; they do not guarantee indexing, AI citations, rich results, or rank.

## Verification limits

Static checks and the local JavaScript harness are automated. Browser rendering, assistive-technology behavior, external link health, example compilation, production deployment, and search indexing need independent validation. No WCAG certification or Lighthouse score is claimed.
