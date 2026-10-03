# CodesbyFebin — master portfolio package

This package contains the populated, standalone website for https://codesbyfebin.github.io/ and its editable build sources. Open `index.html` to browse locally, or run `python -m http.server 8080` and visit http://localhost:8080. No frontend dependency installation is required.

## Included implementation

- Ten primary portfolio pages and 23 project guides, rendered as static HTML.
- Contextual cross-links, shared navigation/footer, related repositories, project breadcrumbs, and a machine-readable discovery index.
- Unique canonical titles/descriptions, social preview images, robots.txt, XML/JSON sitemaps, Person/WebSite/WebPage/BreadcrumbList structured data, repository SoftwareSourceCode and directory ItemList schemas.
- Ten visible direct answers with matching FAQPage structured data. These do not guarantee search rich results.
- Kerala, India location content and IN-KL geographic metadata. No invented street address, precise personal coordinates or business registration is claimed.
- Combined project search/category/status filters, numeric/date sorting, persisted theme, accessible mobile menu and a local contact-brief builder. Contact uses public GitHub/LinkedIn links; the brief builder does not send messages.
- System fonts, framework-free JavaScript/TypeScript source, compressed decorative artwork, reduced-motion support and content available without JavaScript.

## Build and verification

Run from the extracted root with Python 3:

```sh
python scripts/build.py
python scripts/verify.py
python scripts/discovery-check.py
```

The `dist/` directory produced by the build contains only the deployable site. Content edits go in `content/`; the populated project records and source snapshots are in `data/`. The builder imports `scripts/discovery.py` for direct answers and editorial links. Python uses its standard library. The TypeScript file mirrors the JavaScript-compatible source; browsers load the supplied JavaScript directly.

`validation-report.json`, `discovery-report.json`, and `browser-report.json` record completed checks. The content word count includes repository documentation, code and tables. Browser verification uses optional Playwright/Chromium tooling and is not needed to build or deploy.

## GitHub Pages deployment

Copy the extracted package into the CodesbyFebin.github.io repository root. In repository Settings → Pages, choose **GitHub Actions** as the source. The supplied `.github/workflows/build-seo.yml` validates the build, uploads `dist/`, and deploys on pushes to `main`. Do not select `/docs` as the publishing folder: those files are legacy redirects. A separate host can serve `dist/` directly without a Node server.

The canonical domain is already populated. If deploying to another domain, update `BASE` in `scripts/build.py`, rebuild, and validate. Root-level pages intentionally use `.html` canonical URLs supported by GitHub Pages; project guides use directory URLs. No server rewrite is required. The root-level custom 404 links assume this user-site root deployment.

## Source boundaries

Repository metadata is a dated snapshot, not live telemetry. Scaffolds, forks, review status and source documentation are labeled. No unverified employment, education, customers, citations, testimonials, star totals, response times, or runtime guarantees are included. Concept artwork is decorative. Technical source documentation retains source links and identifiers.

Internal links and discovery metadata are implemented; search rankings, indexing, AI answer selection and SEO/Lighthouse scores are not guaranteed. This archive does not change the live site automatically.
