# CodesbyFebin standalone portfolio

Ten primary HTML pages and 23 project guides. No framework, runtime package dependency, remote font, analytics script, or client-side content fetch is required. All primary content is present in static HTML.

## Build and verify

```bash
python3 scripts/build.py
python3 scripts/verify.py
python3 -m http.server 8080 --directory dist
```

Open `http://localhost:8080/`. The emitted `dist/` directory can be served by any ordinary static host. Root-level generated HTML is also committed for inspection. Page URLs use actual `.html` routes, with directory URLs for project guides. GitHub Pages has no server rewrite requirement.

`content/` contains authored page text. `data/repository-snapshots.json` contains source README snapshots and dated GitHub metadata; `data/technical-sources.json` contains selected technical references. These raw source datasets are excluded from the deployment output. `data/projects.json` is the compact public directory dataset generated from reviewed descriptions. Forks, mixed-scope projects, and documentation scaffolds have explicit statuses.

`assets/js/main.ts` is TypeScript source written entirely in JavaScript-compatible syntax. The identical `main.js` is shipped precompiled. No TypeScript compiler is required to host or rebuild this version. Browser enhancements handle theme, mobile navigation, project search/filter/sort, and local brief formatting; none is required to access the content. The contact brief builder does not send messages.

## GitHub Pages

The workflow in `.github/workflows/build-seo.yml` builds and checks pull requests. A push to `main` builds an artifact and deploys it through GitHub Pages. In repository Settings → Pages, select **GitHub Actions** as the publishing source before merging the change. Deployment uses the existing `codesbyfebin.github.io` site rather than registering another hosting provider.

The previous `portfolio.html` points to `projects.html`. Legacy `docs/` entries are aliases for the root site. Do not select `/docs` as the publishing folder for this version; use the Actions-built `dist/` artifact. This setting prevents the old documentation-only publishing layout from hiding the new root pages.

## Checks and limitations

The verifier checks internal file/anchor links, unique titles/descriptions, canonical URLs, JSON-LD parsing, H1 count, image alt presence, XML sitemap parsing, repository count, word count, CSS budget, and deployment size. See `validation-report.json` for measured values. Word counts include source documentation, code, headings, and tables inside the ten main page bodies, and exclude the navigation, footer, and project guide pages.

`scripts/browser-check.cjs` provides optional Playwright checks for desktop/mobile rendering, combined filters, empty state, sorting, theme persistence, safe brief rendering, and no-JavaScript access. Browser QA requires Playwright plus its Chromium binary; it is separate from the standard-library static build. Do not describe browser checks or Lighthouse scores as passed unless an actual run produced the corresponding report.

This website build does not run the project repositories' runtime suites. Documentation snapshots are source references, not independent security or production qualification. Search rankings, indexing, AI citations, Lighthouse scores, and Core Web Vitals are not guaranteed by metadata or content length.

## Artwork

Compressed concept artwork was supplied in `grok-workspace.zip` and reused as decorative category imagery and clearly labeled illustrations. It is not presented as a photograph of the engineer or of a measured installation. Social preview cards are local typographic PNGs. All artwork is served from this site's assets.

## Validation result
Static validation passed: 10 primary pages, 23 project guides, 19,617 words in primary-page main content including documentation and code, 1,001,772 deployed bytes. Chromium browser QA passed 24 checks at desktop/mobile widths with zero page script errors. This does not establish Lighthouse scores, Safari/Firefox results, search ranking, or production hosting configuration.
