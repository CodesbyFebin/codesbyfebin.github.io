# Keyword Research & Content Strategy — 100 Posts

**Site:** alexrivera.dev (Alex Rivera — AI Engineering, Systems & Self-Hosting)
**Generated:** 2026-10-03 · **Companion data:** `docs/content-plan.json` (machine-readable, drives batch execution)

---

## 1. Executive summary

Two tracks, 100 posts, one internal-link graph:

- **Track A — 50 "keyword" guides**: high-traffic, low-to-medium competition head and mid-tail terms in the hybrid niche (AI/LLM engineering + evergreen developer tooling/self-hosting). These are authority builders: in-depth explainers, comparisons, and decision frameworks that earn backlinks and rank in AI Overviews / answer engines.
- **Track B — 50 "UGC" tutorials**: long-tail, near-zero-competition step-by-step walkthroughs and error-fix posts with massive impression potential relative to their difficulty. These are traffic capture: exact-match queries ("how to run ollama in docker with gpu", "fix: docker no space left on device") where a genuinely complete tutorial wins the SERP outright.

Tracks interlock three ways: (1) Track B tutorials implement concepts from Track A guides and link up to them; (2) both link into the six **open-source projects** (/projects/) and five **systems** (/systems/), which act as hub pages concentrating authority; (3) every post ships with the same AEO surface (TL;DR box, takeaways, FAQ + FAQPage schema, direct-answer opening).

## 2. Methodology & honesty note

Volume/difficulty figures are **directional estimates** synthesized from practitioner knowledge of the 2025–2026 AI/dev search landscape (keyword tool ranges, SERP feature observation, competitor depth), not live exports from Ahrefs/GSC — no tool API was available at generation time. Before each batch ships, re-validate that batch's keywords in Google Keyword Planner / Search Console / Ahrefs and adjust titles if a better phrasing surfaces. The *structure* (two tracks, hub-and-spoke links, project anchors) is the durable part; individual volume numbers are the replaceable part.

Competition ratings assume a new domain: "Low" = winnable in 2–4 months with 10+ internal links; "Medium" = winnable in 4–9 months, needs the full hub support; "Very low" = long-tail/error queries where a complete, tested tutorial can page one within weeks.

## 3. Site-wide SEO/AEO architecture (already implemented)

- **URL routing:** `/blog/{slug}/`, `/projects/{slug}/`, `/systems/{slug}/`, `/tags/{tag}/`, `/about/`, trailing-slash canonical everywhere
- **Schema.org graph:** WebSite+SearchAction, Person (author E-E-A-T), BlogPosting (per post), FAQPage (per post, from frontmatter), BreadcrumbList (every page), SoftwareApplication (projects), ItemList (indexes)
- **AEO surfaces:** TL;DR + key takeaways box at top of every post; FAQ section rendered on-page and as schema; first paragraph answers the target query directly; comparison tables; glossary blocks; question-shaped H2/H3s
- **Crawler infrastructure:** sitemap-index.xml, RSS 2.0 full feed, robots.txt explicitly allowing GPTBot/PerplexityBot/ClaudeBot/Google-Extended, **llms.txt** generated from the content collections
- **Frontmatter as data layer:** every post carries `targetKeyword`, `secondaryKeywords`, `track`, `faq[]`, `takeaways[]`, `related[]`, `project`, `system` — the keyword map is executable, not a side document

## 4. Track A — 50 high-traffic / low-competition guides

| # | Batch | Target keyword | Post (slug) | Intent | Est. vol | Competition | Project/System |
|---|---|---|---|---|---|---|---|
| 1 | 1 | **what is retrieval augmented generation** | What Is Retrieval-Augmented Generation (RAG)? The Practical Guide (`what-is-retrieval-augmented-generation`) | Informational | 14K/mo | Medium | `knowledge-pipeline` |
| 2 | 1 | **context engineering** | Context Engineering: The Complete Guide for AI Practitioners (`context-engineering-guide`) | Informational | 9K/mo | Low | `context-stack` |
| 3 | 1 | **how to build an mcp server** | How to Build an MCP Server in Python: Step-by-Step With Code (`how-to-build-an-mcp-server`) | Informational | 6K/mo | Low | — |
| 4 | 1 | **ollama vs lm studio** | Ollama vs LM Studio: Which Local LLM Runtime Should You Use in 2026? (`ollama-vs-lm-studio`) | Commercial investigation | 5K/mo | Low | — |
| 5 | 1 | **docker compose best practices** | Docker Compose Best Practices: 15 Rules for Stacks That Survive Production (`docker-compose-best-practices`) | Informational | 4K/mo | Medium | `weekend-server` |
| 6 | 1 | **how to reduce llm api costs** | How to Reduce LLM API Costs: 12 Tactics That Actually Work (`how-to-reduce-llm-api-costs`) | Informational | 2K/mo | Low | `costguard`  |
| 11 | 2 | **ai agents vs workflows** | AI Agents vs Workflows: When to Use Each (Decision Framework) (`ai-agents-vs-workflows`) | Commercial investigation | 3K/mo | Low | — |
| 12 | 2 | **llm evaluation metrics** | LLM Evaluation Metrics Explained: The 2026 Practitioner’s Guide (`llm-evaluation-metrics`) | Informational | 4K/mo | Medium | `eval-first-loop` |
| 13 | 2 | **best local llm for coding** | Best Local LLMs for Coding in 2026: Benchmarked on Real Tasks (`best-local-llm-for-coding`) | Informational | 8K/mo | Medium | — |
| 14 | 2 | **semantic caching llm** | Semantic Caching Explained: How It Cuts LLM Latency and Cost (`semantic-caching-explained`) | Informational | 1K/mo | Low | `llmcache`  |
| 15 | 2 | **what to self host** | What to Self-Host in 2026: 25 Services Worth Running Yourself (`what-to-self-host`) | Informational | 6K/mo | Low | `homeforge` `weekend-server` |
| 19 | 2 | **rag chunking strategies** | RAG Chunking Strategies: 7 Approaches Ranked by Retrieval Quality (`rag-chunking-strategies`) | Informational | 2K/mo | Low | — |
| 21 | 3 | **rag vs fine tuning** | RAG vs Fine-Tuning: Which Should You Use? (With Decision Tree) (`rag-vs-fine-tuning`) | Commercial investigation | 5K/mo | Medium | — |
| 22 | 3 | **vector database comparison** | Vector Database Comparison 2026: pgvector vs Qdrant vs Chroma vs Milvus (`vector-database-comparison`) | Commercial investigation | 4K/mo | Medium | — |
| 23 | 3 | **best embedding model** | Best Embedding Models in 2026: Benchmarks, Costs, and Picks (`best-embedding-models`) | Informational | 5K/mo | Medium | — |
| 24 | 3 | **rag vs long context** | RAG vs Long Context Windows: The 2026 Verdict (`rag-vs-long-context`) | Commercial investigation | 1K/mo | Low | — |
| 25 | 3 | **homelab beginner guide** | The Beginner Homelab Guide: From Zero to Self-Hosted in a Weekend (`homelab-beginner-guide`) | Informational | 5K/mo | Medium | `weekend-server` |
| 31 | 4 | **llm structured output** | LLM Structured Output: How to Get Reliable JSON from Any Model (`llm-structured-output`) | Informational | 3K/mo | Low | — |
| 32 | 4 | **function calling llm** | Function Calling Explained: How LLMs Actually Use Tools (`function-calling-explained`) | Informational | 3K/mo | Medium | — |
| 33 | 4 | **llm observability** | LLM Observability: Tracing, Logging, and Debugging AI Apps (`llm-observability`) | Informational | 2K/mo | Low | `eval-first-loop` |
| 34 | 4 | **prompt engineering best practices** | Prompt Engineering Best Practices: 21 Rules from Production Systems (`prompt-engineering-best-practices`) | Informational | 12K/mo | Medium | `context-stack` |
| 35 | 4 | **system prompt best practices** | System Prompt Design: Anatomy of Prompts That Hold Up in Production (`system-prompt-design`) | Informational | 2K/mo | Low | `context-stack` |
| 41 | 5 | **llm temperature explained** | LLM Temperature and top_p Explained (With Visual Intuition) (`llm-temperature-explained`) | Informational | 4K/mo | Medium | — |
| 42 | 5 | **gguf quantization explained** | GGUF Quantization Explained: Q4_K_M, Q8_0, and What You Lose (`gguf-quantization-explained`) | Informational | 2K/mo | Low | — |
| 43 | 5 | **how to run llm locally** | How to Run an LLM Locally in 2026: The Complete Hardware + Software Guide (`run-llm-locally-guide`) | Informational | 6K/mo | Medium | — |
| 44 | 5 | **context window tokens explained** | Context Windows and Tokens Explained: What 1M Tokens Actually Means (`context-window-tokens-explained`) | Informational | 3K/mo | Medium | `context-stack` |
| 45 | 5 | **reduce llm hallucinations** | How to Reduce LLM Hallucinations: 10 Techniques Ranked by Impact (`reduce-llm-hallucinations`) | Informational | 4K/mo | Medium | — |
| 51 | 6 | **cursor vs copilot** | AI Coding Assistants Compared 2026: Copilot vs Cursor vs Claude Code vs Codex (`ai-coding-assistants-compared`) | Commercial investigation | 15K/mo | Medium | `context-stack` |
| 52 | 6 | **multi agent design patterns** | Multi-Agent Design Patterns: 6 Architectures for Production AI (`multi-agent-design-patterns`) | Informational | 1K/mo | Low | `agentmesh`  |
| 53 | 6 | **prompt management** | Prompt Management for Teams: Versioning, Review, and Rollback (`prompt-management`) | Informational | 700/mo | Very low | `promptkit`  |
| 54 | 6 | **llm router** | LLM Routing Explained: Send Each Request to the Cheapest Model That Works (`llm-router-explained`) | Informational | 800/mo | Very low | `costguard`  |
| 55 | 6 | **how to build an ai chatbot** | How to Build an AI Chatbot with RAG: End-to-End in One Afternoon (`build-ai-chatbot-rag`) | Informational | 10K/mo | Medium | `vaultrag`  |
| 61 | 7 | **docker vs podman** | Docker vs Podman in 2026: Which Container Engine Should You Use? (`docker-vs-podman`) | Commercial investigation | 8K/mo | Medium | — |
| 62 | 7 | **reverse proxy explained** | Reverse Proxies Explained: Nginx vs Caddy vs Traefik for Self-Hosters (`reverse-proxy-explained`) | Commercial investigation | 4K/mo | Low | `weekend-server` |
| 63 | 7 | **tailscale vs wireguard** | Tailscale vs WireGuard: Which VPN Fits Your Homelab? (`tailscale-vs-wireguard`) | Commercial investigation | 5K/mo | Low | `weekend-server` |
| 64 | 7 | **sqlite vs postgres** | SQLite vs Postgres: The Honest 2026 Comparison (and When to Switch) (`sqlite-vs-postgres`) | Commercial investigation | 6K/mo | Medium | — |
| 65 | 7 | **rest vs graphql vs grpc** | REST vs GraphQL vs gRPC: Choosing an API Style in 2026 (`rest-vs-graphql-vs-grpc`) | Commercial investigation | 5K/mo | Medium | — |
| 71 | 8 | **git rebase vs merge** | Git Rebase vs Merge: A Practical Guide for Teams (`git-rebase-vs-merge`) | Commercial investigation | 10K/mo | Medium | — |
| 72 | 8 | **git worktree** | Git Worktrees: The Feature-Branch Workflow Upgrade You’re Missing (`git-worktree-guide`) | Informational | 4K/mo | Low | — |
| 73 | 8 | **dotfiles management** | Dotfiles Management: 5 Approaches Compared (Bare Repo Wins) (`dotfiles-management`) | Commercial investigation | 2K/mo | Low | — |
| 74 | 8 | **tmux guide** | The Pragmatic tmux Guide: From First Session to Daily Driver (`tmux-guide`) | Informational | 5K/mo | Medium | — |
| 75 | 8 | **linux server hardening checklist** | The Linux Server Hardening Checklist I Run on Every Machine (`linux-server-hardening-checklist`) | Informational | 2K/mo | Low | `weekend-server` |
| 81 | 9 | **prometheus grafana guide** | Prometheus + Grafana Monitoring: A Self-Hoster’s Complete Guide (`prometheus-grafana-monitoring`) | Informational | 4K/mo | Medium | `weekend-server` |
| 82 | 9 | **github actions tips** | 17 GitHub Actions Tips That Cut CI Time and Bill (`github-actions-tips`) | Informational | 800/mo | Very low | — |
| 83 | 9 | **secrets management small teams** | Secrets Management for Small Teams: .env Files to Vault Without Overkill (`secrets-management-small-teams`) | Informational | 500/mo | Very low | — |
| 84 | 9 | **webhooks explained** | Webhooks Explained: How to Build, Secure, and Debug Them (`webhooks-explained`) | Informational | 5K/mo | Low | — |
| 85 | 9 | **3 2 1 backup strategy** | The 3-2-1 Backup Strategy, Implemented: A restic + B2 Walkthrough (`backup-strategy-3-2-1`) | Informational | 2K/mo | Low | `homeforge` `weekend-server` |
| 91 | 10 | **ssh config guide** | The SSH Config Guide: Aliases, Keys, Jumps, and Multiplexing (`ssh-config-guide`) | Informational | 2K/mo | Low | — |
| 92 | 10 | **cron alternative** | Job Scheduling Beyond Cron: systemd Timers, Queues, and Orchestrators (`job-scheduling-beyond-cron`) | Informational | 800/mo | Very low | `weekend-server` |
| 93 | 10 | **vllm vs ollama** | vLLM vs Ollama: Serving LLMs in Production vs on Your Laptop (`vllm-vs-ollama`) | Commercial investigation | 3K/mo | Low | — |

## 5. Track B — 50 UGC long-tail tutorials (near-zero competition)

| # | Batch | Target keyword | Post (slug) | Intent | Est. vol | Competition | Project/System |
|---|---|---|---|---|---|---|---|
| 7 | 1 | **llm semantic cache setup** | How to Set Up a Semantic Cache for LLM APIs (LLMCache Quickstart) (`llm-semantic-cache-setup`) | How-to / Fix | 700/mo | Very low | `llmcache`  |
| 8 | 1 | **ollama docker gpu** | How to Run Ollama in Docker with GPU Passthrough (NVIDIA, AMD, Apple Silicon) (`run-ollama-in-docker-with-gpu`) | How-to / Fix | 3K/mo | Low | — |
| 9 | 1 | **rag over obsidian vault** | RAG Over Your Markdown Vault: Build a Private Second Brain with VaultRAG (`rag-over-markdown-vault`) | How-to / Fix | 500/mo | Very low | `vaultrag` `knowledge-pipeline` |
| 10 | 1 | **llm as a judge tutorial** | LLM-as-a-Judge Evals: A Step-by-Step Tutorial (with PromptKit) (`llm-as-a-judge-tutorial`) | How-to / Fix | 1K/mo | Low | `promptkit` `eval-first-loop` |
| 16 | 2 | **ollama keeps unloading model** | Fix: Ollama Unloads Your Model After 5 Minutes (keep_alive Explained) (`ollama-keep-alive-fix`) | How-to / Fix | 400/mo | Very low | — |
| 17 | 2 | **self host langfuse** | Self-Host Langfuse with Docker Compose: LLM Tracing on Your Own Hardware (`self-host-langfuse`) | How-to / Fix | 900/mo | Very low | `eval-first-loop` |
| 18 | 2 | **prompt version control** | How to Version Control Prompts with Git (And Stop Losing Regressions) (`prompt-version-control`) | How-to / Fix | 300/mo | Very low | `promptkit` `eval-first-loop` |
| 20 | 2 | **cosine similarity embeddings python** | Embeddings and Cosine Similarity from Scratch in Python (No Frameworks) (`embeddings-cosine-similarity-python`) | How-to / Fix | 800/mo | Very low | — |
| 26 | 3 | **open webui remote ollama** | How to Connect Open WebUI to a Remote Ollama Server (`open-webui-remote-ollama`) | How-to / Fix | 700/mo | Very low | — |
| 27 | 3 | **ollama json output** | Structured JSON Output with Ollama: The format Parameter Explained (`ollama-structured-json-output`) | How-to / Fix | 1K/mo | Very low | — |
| 28 | 3 | **cloudflare tunnel docker compose** | Cloudflare Tunnel + Docker Compose: Expose Self-Hosted Apps Without Opening Ports (`cloudflare-tunnel-docker-compose`) | How-to / Fix | 2K/mo | Low | `weekend-server` |
| 29 | 3 | **caddy reverse proxy** | Caddy Reverse Proxy with Automatic HTTPS: A Complete Tutorial (`caddy-reverse-proxy-https`) | How-to / Fix | 2K/mo | Low | `weekend-server` |
| 30 | 3 | **sqlite litestream** | SQLite in Production: Automatic Backups to S3 with Litestream (`sqlite-litestream-production`) | How-to / Fix | 600/mo | Very low | `weekend-server` |
| 36 | 4 | **fastapi sse streaming llm** | Streaming LLM Responses in FastAPI with Server-Sent Events (`stream-llm-fastapi-sse`) | How-to / Fix | 500/mo | Very low | — |
| 37 | 4 | **llm api rate limit retry** | Retry and Backoff Patterns for Rate-Limited LLM APIs (`llm-rate-limit-retry`) | How-to / Fix | 300/mo | Very low | — |
| 38 | 4 | **ai code review github actions** | Build an AI Code Reviewer with GitHub Actions (That Devs Don’t Hate) (`ai-code-reviewer-github-actions`) | How-to / Fix | 400/mo | Very low | — |
| 39 | 4 | **vector search cli python** | Build a Vector Search CLI for Your Notes in 100 Lines of Python (`vector-search-cli-notes`) | How-to / Fix | 200/mo | Very low | `vaultrag`  |
| 40 | 4 | **hybrid search bm25 embeddings** | Hybrid Search: BM25 + Embeddings for Retrieval That Doesn’t Miss (`hybrid-search-bm25-embeddings`) | How-to / Fix | 500/mo | Very low | `vaultrag`  |
| 46 | 5 | **tiktoken count tokens** | How to Count Tokens Before You Call an LLM API (tiktoken Guide) (`tiktoken-token-counting`) | How-to / Fix | 900/mo | Very low | `costguard`  |
| 47 | 5 | **faster-whisper tutorial** | Local Meeting Transcription with faster-whisper: A Complete Setup (`faster-whisper-transcription`) | How-to / Fix | 1K/mo | Very low | — |
| 48 | 5 | **rag reranker tutorial** | Add a Reranker to Your RAG Pipeline (bge-reranker Tutorial) (`rag-reranker-tutorial`) | How-to / Fix | 400/mo | Very low | `vaultrag`  |
| 49 | 5 | **huggingface cli download model** | How to Download Models from Hugging Face with the CLI (and Cache Them Right) (`huggingface-cli-download-models`) | How-to / Fix | 1K/mo | Very low | — |
| 50 | 5 | **cuda out of memory llm** | Fix: CUDA Out of Memory When Loading a 7B Model (`cuda-out-of-memory-fix`) | How-to / Fix | 600/mo | Very low | — |
| 56 | 6 | **multi agent pipeline tutorial** | Build a Multi-Agent Research Pipeline with AgentMesh (Step by Step) (`agentmesh-research-pipeline`) | How-to / Fix | 200/mo | Very low | `agentmesh`  |
| 57 | 6 | **agent handoff pattern** | Agent Handoffs and Shared Memory: Patterns That Survive Real Workloads (`agent-handoff-patterns`) | How-to / Fix | 200/mo | Very low | `agentmesh`  |
| 58 | 6 | **build ai agent python from scratch** | Build a Tool-Using AI Agent in Python from Scratch (No Frameworks) (`python-agent-tool-use-scratch`) | How-to / Fix | 1K/mo | Very low | `agentmesh`  |
| 59 | 6 | **local voice assistant llm** | Build a Fully Local Voice Assistant: Whisper + Ollama + Piper (`local-voice-assistant`) | How-to / Fix | 600/mo | Very low | — |
| 60 | 6 | **track openai api spend** | Track OpenAI Spend per Project with CostGuard (Setup Tutorial) (`costguard-openai-spend`) | How-to / Fix | 200/mo | Very low | `costguard`  |
| 66 | 7 | **traefik labels** | Traefik Docker Labels Cheat Sheet: Working Examples for Compose (`traefik-docker-labels`) | How-to / Fix | 1K/mo | Very low | — |
| 67 | 7 | **wireguard vps setup** | WireGuard VPN on a VPS: Step-by-Step Setup (Ubuntu 24.04) (`wireguard-vps-setup`) | How-to / Fix | 2K/mo | Low | `weekend-server` |
| 68 | 7 | **headscale setup** | Headscale Setup Guide: Self-Hosted Tailscale Control Server (`headscale-self-hosted-tailscale`) | How-to / Fix | 1K/mo | Very low | `weekend-server` |
| 69 | 7 | **postgres docker production** | Running Postgres in Docker Safely: Volumes, Backups, and Tuning (`postgres-docker-production`) | How-to / Fix | 1K/mo | Very low | `weekend-server` |
| 70 | 7 | **ubuntu vps hardening** | Harden a New Ubuntu VPS in 20 Minutes: UFW, fail2ban, SSH (`ubuntu-vps-hardening`) | How-to / Fix | 1K/mo | Low | `weekend-server` |
| 76 | 8 | **dotfiles bare repo** | Manage Dotfiles with a Git Bare Repository: Full Walkthrough (`dotfiles-bare-repo`) | How-to / Fix | 400/mo | Very low | — |
| 77 | 8 | **docker no space left on device** | Fix: Docker No Space Left on Device (and Never See It Again) (`docker-no-space-left`) | How-to / Fix | 2K/mo | Low | — |
| 78 | 8 | **docker compose healthcheck** | Docker Compose Healthchecks That Actually Work (`docker-compose-healthchecks`) | How-to / Fix | 1K/mo | Very low | `weekend-server` |
| 79 | 8 | **ssh certificate authority** | Set Up an SSH Certificate Authority for Your Homelab (`ssh-certificate-authority`) | How-to / Fix | 200/mo | Very low | `weekend-server` |
| 80 | 8 | **nginx rate limiting** | Nginx Rate Limiting: Configuration Examples That Hold Up (`nginx-rate-limiting`) | How-to / Fix | 1K/mo | Very low | — |
| 86 | 9 | **n8n self hosted tutorial** | Self-Hosted n8n: Your First Automation Workflow (Docker Setup) (`n8n-self-hosted-tutorial`) | How-to / Fix | 2K/mo | Low | `weekend-server` |
| 87 | 9 | **homelab docker stack** | One-Command Homelab: The HomeForge Stack Explained (`homeforge-one-command-homelab`) | How-to / Fix | 300/mo | Very low | `homeforge` `weekend-server` |
| 88 | 9 | **uptime kuma healthchecks setup** | Self-Hosted Monitoring Bundle: Uptime Kuma + Healthchecks in 15 Minutes (`uptime-kuma-healthchecks`) | How-to / Fix | 400/mo | Very low | `homeforge`  |
| 89 | 9 | **restic backup tutorial** | Automated Encrypted Backups with restic: S3, B2, or a Raspberry Pi (`restic-encrypted-backups`) | How-to / Fix | 1K/mo | Very low | `homeforge`  |
| 90 | 9 | **llm token budget alert** | Set Token Budgets and Alerts for LLM Apps (CostGuard Guide) (`token-budgets-alerts`) | How-to / Fix | 100/mo | Very low | `costguard`  |
| 94 | 10 | **llm cache redis** | LLMCache + Redis: The Full Docker Compose Setup (Annotated) (`llmcache-redis-compose`) | How-to / Fix | 150/mo | Very low | `llmcache`  |
| 95 | 10 | **llm cache hit rate** | Measure Your LLM Cache Hit Rate: Building a Savings Dashboard (`cache-hit-rate-dashboard`) | How-to / Fix | 100/mo | Very low | `llmcache`  |
| 96 | 10 | **llm gateway rate limiting** | Cache-Aware Rate Limiting for Your LLM Gateway (`cache-aware-rate-limiting`) | How-to / Fix | 100/mo | Very low | `llmcache`  |
| 97 | 10 | **prompt regression testing** | Prompt Regression Testing: Catch Breakage Before Your Users Do (PromptKit) (`prompt-regression-testing`) | How-to / Fix | 200/mo | Very low | `promptkit` `eval-first-loop` |
| 98 | 10 | **ab test system prompt** | A/B Testing System Prompts Safely in Production (`ab-testing-system-prompts`) | How-to / Fix | 150/mo | Very low | `promptkit`  |
| 99 | 10 | **mkdocs material tutorial** | Ship Beautiful Docs: MkDocs Material Setup Tutorial (`mkdocs-material-docs-site`) | How-to / Fix | 1K/mo | Very low | — |
| 100 | 10 | **renovate vs dependabot** | Renovate vs Dependabot: Auto-Update Dependencies Without the Noise (`renovate-dependabot-guide`) | How-to / Fix | 500/mo | Very low | — |

## 6. Internal linking rules

1. **Every post links to ≥3 others** (frontmatter `related` + contextual body links); every Track B post links up to its Track A concept post.
2. **Project hub pattern:** each Track B post tied to a project links `/projects/{slug}/`; project pages auto-list their tutorials (built from frontmatter — no manual maintenance).
3. **System hub pattern:** concept posts declare their `system`; system pages auto-list implementing guides.
4. **Breadcrumbs** everywhere (users + schema).
5. **Related-posts algorithm:** explicit `related` slugs first, then tag/project/system overlap score — already implemented in `src/pages/blog/[slug].astro`.
6. Forward references (links to posts in later batches) are safe: the related algorithm skips missing slugs, and body links go live as batches land.

## 7. Batch schedule & progress

| Batch | Posts | Focus | Status |
|---|---|---|---|
| 1 | 1–10 | Flagship anchors: RAG, context engineering, MCP, Ollama vs LM Studio, compose, costs + 4 project tutorials | ✅ **written** |
| 2 | 11–20 | Agents vs workflows, eval metrics, local coding LLMs, self-host list + Ollama fixes, Langfuse, prompt VC | ⏳ next |
| 3 | 21–30 | RAG decisions (fine-tune/long-context/vector DB/embeddings) + homelab networking (tunnels, Caddy, Litestream) | planned |
| 4 | 31–40 | Structured output, function calling, observability, prompting canon + streaming/retry/code-review/vector-CLI | planned |
| 5 | 41–50 | Sampling params, quantization, local-LLM hardware, tokens, hallucinations + whisper/rerank/HF-cli/CUDA-OOM | planned |
| 6 | 51–60 | Assistants compared, multi-agent patterns, routing, chatbot build + AgentMesh/voice/CostGuard tutorials | planned |
| 7 | 61–70 | Container/proxy/VPN/DB/API comparisons + Traefik/WireGuard/Headscale/Postgres/VPS hardening | planned |
| 8 | 71–80 | Git canon (rebase, worktree), dotfiles, tmux, hardening checklist + bare-repo/disk-space/healthchecks/SSH-CA/nginx | planned |
| 9 | 81–90 | Monitoring, CI tips, secrets, webhooks, backups + n8n/HomeForge/Uptime-Kuma/restic/budgets | planned |
| 10 | 91–100 | SSH config, scheduling, vLLM vs Ollama + LLMCache deep-dives, prompt testing, docs/dependency automation | planned |

**Progress: 10/100 written** (updated as batches land; `docs/content-plan.json` is the source of truth)

## 8. Post-publication process

1. Submit sitemap to Google Search Console + Bing Webmaster on day one.
2. Weekly GSC review: impressions without clicks → improve title/meta; position 5–15 → add internal links + FAQ depth.
3. Quarterly refresh of fast-moving posts (model comparisons, pricing, version pins) with `updatedDate` bumps — schema `dateModified` + visible "Updated" label already wired.
4. Answer-engine tracking: monthly spot-checks of ChatGPT/Perplexity/AI Overviews for head terms; llms.txt and FAQ schema are the levers.
5. Every new batch: re-validate keywords (section 2), write posts, flip `status` in `docs/content-plan.json`.
