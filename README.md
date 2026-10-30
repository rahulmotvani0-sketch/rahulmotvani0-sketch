<div align="center">

# Hi there, I'm Rahul Motvani 👋
### 🛡️ DevOps & DevSecOps Engineer | SRE, Cloud Infrastructure & AI Systems

<p align="center">
  <b>Architecting Zero-Trust Cloud Platforms, Shift-Left Security Pipelines, Resilient Kubernetes & AI Infrastructure</b>
</p>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rahul%20Motvani-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahulmotvani/)
[![Live Portfolio](https://img.shields.io/badge/Live%20Portfolio-rahul.techiking.com-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://rahul.techiking.com)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Top%203%25-red?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/rahulmotvani8gma)
[![Email](https://img.shields.io/badge/Email-rahulmotvani8%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rahulmotvani8@gmail.com)
[![Location](https://img.shields.io/badge/Location-Ahmedabad%2C%20India%20%7C%20Remote-2ea44f?style=for-the-badge&logo=googlemaps&logoColor=white)](https://github.com/rahulmotvani0-sketch)

</div>

---

### 👨‍💻 Engineering Profile & Core Philosophy

- ☁️ **Cloud Infrastructure & IaC:** Operating high-availability, multi-region production workloads across **AWS** (EKS, ECS, Lambda ARM64, DynamoDB, WAFv2, IAM least-privilege) and **Azure** (AKS, Azure Monitor, Key Vault). Enforcing immutable infrastructure via modular **Terraform** with remote state locking and automated drift detection.
- 🔐 **Zero-Secrets & DevSecOps:** Enterprise secrets management with **HashiCorp Vault** (Dynamic Database Engine) & **External Secrets Operator (ESO)**; shift-left supply chain security enforcing SAST, DAST, SCA, container image signing with **Sigstore Cosign**, and **CycloneDX/SPDX SBOMs**.
- ☸️ **Kubernetes & GitOps Orchestration:** Production container orchestration across **EKS**, **AKS**, and **Kind**, declarative **ArgoCD App-of-Apps** patterns, Zero-Trust service mesh with **Istio** (STRICT mTLS & L7 policies), and automated **HPA v2 / PDB** autoscaling.
- 📈 **SRE, Observability & Resilience:** Google Golden Signals / RED metrics instrumentation with **Prometheus**, **Alertmanager**, **Grafana**, and **Loki** distributed logging. Automated disaster recovery drills and snapshotting with **Velero** (RTO < 15 min).
- 🤖 **AI Systems & Platform Engineering:** Deploying local-first offline LLM inference (**Ollama**, **Qwen2.5**, **LLaMA**), semantic RAG pipelines, autonomous agent discovery networks with 14+ ATS connectors, and cross-platform desktop security tooling with **Rust** and **Tauri**.
- 🎯 **Security Ranking:** Ranked in the **Top 3% worldwide** on TryHackMe.

---

### 🛠️ Technical Competencies

<div align="center">

| Domain | Tools & Technologies |
| :--- | :--- |
| **Cloud Platforms** | `AWS (EKS, ECS, Lambda, DynamoDB, WAFv2, IAM, VPC, CloudWatch)` • `Azure (AKS, Azure Monitor, Key Vault)` |
| **Secrets & Identity** | `HashiCorp Vault (Dynamic Database Engine)` • `External Secrets Operator (ESO)` • `OIDC Keyless Auth` • `IAM Least-Privilege` |
| **Container & Orchestration** | `Kubernetes (K8s)` • `Docker` • `Helm` • `ArgoCD (App-of-Apps GitOps)` • `Istio Service Mesh` • `Kind` |
| **Infrastructure as Code** | `Terraform (Modular / Remote State / Locking)` • `AWS CDK` • `HCL` • `Makefiles` • `Drift Detection` |
| **CI/CD & Automation** | `GitHub Actions (Reusable Composite Actions)` • `Jenkins` • `GitLab CI` • `Bash / POSIX Automation` |
| **DevSecOps & Supply Chain** | `Trivy (SCA & Containers)` • `Semgrep (SAST)` • `Gitleaks` • `Checkov (IaC)` • `Sigstore Cosign` • `Syft (SBOM)` |
| **SRE & Resilience** | `Prometheus` • `Grafana` • `Alertmanager` • `Loki & Promtail` • `Velero (Disaster Recovery)` • `Chaos Engineering` • `SLI / SLO` |
| **AI Systems & Agents** | `Ollama (Local LLM Inference)` • `vLLM` • `FastEmbed` • `RAG Pipelines` • `Autonomous ATS Connectors` • `LLM Agent Workflows` |
| **Languages & Systems** | `Python` • `TypeScript` • `Go` • `Rust / Tauri` • `Bash / Shell` • `Node.js` • `SQL / PostgreSQL / SQLite` |

</div>

---

### 🚀 Featured Production & Open-Source Projects

#### 🔐 [Zero-Secrets GitOps: HashiCorp Vault & External Secrets Operator](https://github.com/rahulmotvani0-sketch/vault-secrets-operator-k8s)
* Enterprise reference architecture eliminating 100% of static credentials and achieving true **Zero Secrets in Git**.
* **HashiCorp Vault Dynamic Database Secrets Engine** mints on-demand, short-lived PostgreSQL credentials (1h TTL) with automated role revocation on expiry.
* **External Secrets Operator (ESO)** synchronizes credentials into native Kubernetes Secrets via ServiceAccount JWT auth, eliminating intrusive sidecars.
* `Tags:` *HashiCorp Vault • External Secrets Operator • Kubernetes • PostgreSQL • GitOps • DevSecOps*

#### 🤖 [Autonomous AI Job Discovery & Application Automation Platform](https://github.com/rahulmotvani0-sketch/ai-job-discovery-platform)
* Autonomous local-first career command center featuring a distributed **Global Connector System** (14+ platforms: Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Recruitee, RemoteOK, Himalayas, YC, USAJobs).
* **Local-first offline AI inference** via **Ollama** (`qwen2.5:7b`, `llama3.2`) with semantic scoring and fact-grounded ATS tailoring.
* Strict **human-in-the-loop security gate**, enterprise SQLite WAL persistence, constant-time token comparison, and deep anti-SSRF defenses.
* `Tags:` *AI Agents • Ollama • ATS Automation • Python / TypeScript • SSRF Hardening • SQLite WAL • Local-First*

#### 🛡️ [Enterprise DevSecOps CI/CD Pipeline Template](https://github.com/rahulmotvani0-sketch/devsecops-secure-cicd-template)
* 7 modular, reusable composite GitHub Actions providing shift-left security quality gates adopting with 3 lines of YAML.
* Automated multi-stage scanning: **Gitleaks** (secret detection), **Semgrep** (SAST), **Trivy** (dependency/container SCA), and **Checkov** (IaC validation).
* Generates CycloneDX/SPDX SBOMs with **Syft** and performs keyless OIDC container signing with **Sigstore Cosign**.
* `Tags:` *DevSecOps • CI/CD • GitHub Actions • Semgrep • Trivy • Checkov • SBOM • Cosign*

#### ⚡ [AWS Serverless Secure API](https://github.com/rahulmotvani0-sketch/aws-serverless-secure-api)
* High-performance, zero-trust URL Shortener & Link Analytics API powered by AWS Lambda (Graviton2 ARM64) and DynamoDB.
* Hardened against **SSRF** (strict IP / RFC 1918 / IMDS filtering), regional **AWS WAFv2** rate limiting, and KMS envelope encryption.
* Fully automated infrastructure provisioning via **Terraform** and keyless GitHub Actions **OIDC federation**.
* `Tags:` *AWS • Terraform • Lambda • DynamoDB • API Gateway • WAFv2 • Security • Python*

#### ☸️ [Kubernetes GitOps & SRE Observability Platform](https://github.com/rahulmotvani0-sketch/kubernetes-gitops-observability-platform)
* Turnkey multi-node Kind cluster bootstrapping driven declaratively by the **ArgoCD App-of-Apps pattern**.
* Complete **Prometheus & Grafana RED** monitoring stack with Alertmanager routing and automated chaos engineering failure recovery.
* Full distributed logging pipeline using **Grafana Loki** and **Promtail DaemonSet**.
* `Tags:` *Kubernetes • GitOps • ArgoCD • Prometheus • Grafana • Loki • SRE • Chaos Engineering*

#### 🖥️ [DevSecOps AI Assistant & Security Lab Desktop App](https://github.com/rahulmotvani0-sketch/DEVSECOPS-AI-WORKSPACE)
* Cross-platform desktop application built with **Rust**, **Tauri**, and **TypeScript**.
* Local security workbench for offline vulnerability scanning, IaC remediation, and AI-assisted DevOps workflows.
* `Tags:` *Rust • Tauri • TypeScript • DevSecOps • Desktop App • Security Analysis*

---

### 🧪 Cloud-Native & Production Labs Showcase

| Project | Tech Stack | Architecture & Description |
| :--- | :--- | :--- |
| 🛡️ [**Distroless Container Hardening**](https://github.com/rahulmotvani0-sketch/docker-multistage-production-hardening) | Docker, Distroless, Trivy | Multi-stage Distroless runtime (<15MB), non-root (`65532:65532`), `read_only` rootfs, `cap_drop: ALL`, Trivy vulnerability gates. |
| ☸️ [**K8s High Availability & Autoscaling**](https://github.com/rahulmotvani0-sketch/k8s-autoscaling-high-availability) | Kubernetes, HPA v2, PDB | HPA v2 autoscaling (2 to 10 replicas), PodAntiAffinity across nodes, PodDisruptionBudgets (`minAvailable: 1`), zero-downtime rolling updates. |
| 🕸️ [**Istio Zero-Trust Service Mesh**](https://github.com/rahulmotvani0-sketch/istio-service-mesh-zero-trust) | Istio, Envoy, mTLS | STRICT mTLS encryption across pods, default-deny L7 `AuthorizationPolicy`, SPIFFE service account authentication, and 90/10 Canary traffic splitting. |
| 💾 [**Velero Disaster Recovery & Backup**](https://github.com/rahulmotvani0-sketch/velero-disaster-recovery-backup) | Velero, AWS S3 / GCS | Daily automated backup schedules, volume snapshotting, 30-day retention, and one-command disaster recovery drill script (RTO < 15 min). |
| 🐧 [**Linux SRE Automation Engine**](https://github.com/rahulmotvani0-sketch/linux-shell-automation-engine) | Bash, POSIX, Cron | SRE threshold monitoring (CPU/Mem/Disk), Slack/Teams webhook alerts, rotating backups with SHA-256 integrity verification. |

---

### 🌐 [Interactive Cloud Engineering Portfolio](https://github.com/rahulmotvani0-sketch/portfolio)
👉 Experience the live interactive portfolio at **[rahul.techiking.com](https://rahul.techiking.com)**:
* **Interactive SRE Sandbox:** Real-time incident response simulator testing automated playbooks against 4 production failure scenarios.
* **System Topology Explorer:** Visual architecture diagrams for DevSecOps pipelines, AI microservices, and multi-cloud IaC.
* **Recruiter & ATS Matrix:** Executive skill matrix tailored for engineering leaders and hiring teams.

---

### 📊 GitHub Activity & Insights

<div align="center">

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=rahulmotvani0-sketch&theme=tokyonight&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="Rahul's GitHub Streak" width="49%" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=rahulmotvani0-sketch&theme=tokyonight" alt="Rahul's GitHub Stats" width="49%" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=rahulmotvani0-sketch&theme=tokyonight" alt="Top Languages" width="100%" />
</p>

</div>

#### ⚡ Recent Engineering & Delivery Activity

<!-- RECENT_ACTIVITY_START -->

| Activity | Target Repository | Date |
| :--- | :--- | :--- |
| 🚀 Pushed code to | [`rahulmotvani0-sketch/devsecops-secure-cicd-template`](https://github.com/rahulmotvani0-sketch/devsecops-secure-cicd-template) | `2026-10-28` |
| 🚀 Pushed code to | [`rahulmotvani0-sketch/aws-serverless-secure-api`](https://github.com/rahulmotvani0-sketch/aws-serverless-secure-api) | `2026-10-28` |
| 🚀 Pushed code to | [`rahulmotvani0-sketch/vault-secrets-operator-k8s`](https://github.com/rahulmotvani0-sketch/vault-secrets-operator-k8s) | `2026-10-28` |
| 📦 Created repository/branch in | [`rahulmotvani0-sketch/velero-disaster-recovery-backup`](https://github.com/rahulmotvani0-sketch/velero-disaster-recovery-backup) | `2026-10-28` |
| 📦 Created repository/branch in | [`rahulmotvani0-sketch/k8s-autoscaling-high-availability`](https://github.com/rahulmotvani0-sketch/k8s-autoscaling-high-availability) | `2026-10-28` |
| 📦 Created repository/branch in | [`rahulmotvani0-sketch/vault-secrets-operator-k8s`](https://github.com/rahulmotvani0-sketch/vault-secrets-operator-k8s) | `2026-10-28` |

*Updated automatically via GitHub Actions • Last synced: 2026-10-30 05:34 UTC*

<!-- RECENT_ACTIVITY_END -->

---

### 💬 Let's Connect & Collaborate

- 💼 **LinkedIn:** [linkedin.com/in/rahulmotvani](https://www.linkedin.com/in/rahulmotvani/)
- 🌐 **Interactive Portfolio:** [rahul.techiking.com](https://rahul.techiking.com)
- 🎯 **TryHackMe:** [tryhackme.com/p/rahulmotvani8gma](https://tryhackme.com/p/rahulmotvani8gma)
- 📧 **Direct Email:** [rahulmotvani8@gmail.com](mailto:rahulmotvani8@gmail.com)
- 🤝 **Open to:** Senior DevOps Engineer, DevSecOps Specialist, SRE, and Cloud Platform Engineering roles.
