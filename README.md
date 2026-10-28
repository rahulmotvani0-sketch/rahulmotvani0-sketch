<div align="center">

# Hi there, I'm Rahul Motvani 👋
### 🛡️ Senior DevOps, DevSecOps & Site Reliability Engineer (SRE)

<p align="center">
  <b>4+ Years Architecting Enterprise Cloud Infrastructure, Zero-Secrets GitOps, Production Kubernetes & Shift-Left DevSecOps</b>
</p>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rahul%20Motvani-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahulmotvani/)
[![Live Portfolio](https://img.shields.io/badge/Live%20Portfolio-rahul.techiking.com-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://rahul.techiking.com)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Top%203%25-red?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/rahulmotvani8gma)
[![Email](https://img.shields.io/badge/Email-rahulmotvani8%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rahulmotvani8@gmail.com)
[![Location](https://img.shields.io/badge/Location-Ahmedabad%2C%20India%20%7C%20Remote-2ea44f?style=for-the-badge&logo=googlemaps&logoColor=white)](https://github.com/rahulmotvani0-sketch)

</div>

---

### 👨‍💻 Engineering Profile & Core Philosophy

- 🔭 **Cloud Infrastructure:** Operating high-availability, multi-region production workloads across **AWS** (EKS, ECS, Lambda, DynamoDB, WAFv2, IAM least-privilege) and **Azure** (AKS, Application Insights, Azure Monitor).
- 🔐 **Zero-Secrets & DevSecOps:** Enterprise secrets management with **HashiCorp Vault** & **External Secrets Operator (ESO)**; shift-left supply chain security enforcing SAST, DAST, SCA, container image signing with **Sigstore Cosign**, and **CycloneDX/SPDX SBOMs**.
- ☸️ **Kubernetes & GitOps:** Production container orchestration (EKS / AKS / Kind), declarative **ArgoCD App-of-Apps**, Zero-Trust mesh with **Istio**, and automated **HPA v2 / PDB** autoscaling.
- 📈 **SRE & Observability:** Google Golden Signals / RED metrics instrumentation with **Prometheus**, **Alertmanager**, **Grafana**, and **Loki** distributed logging.
- 🎯 **Security Ranking:** Ranked in the **Top 3% worldwide** on TryHackMe.

---

### 🛠️ Technical Competencies

<div align="center">

| Domain | Tools & Technologies |
| :--- | :--- |
| **Cloud Platforms** | `AWS (EKS, ECS, Lambda, DynamoDB, WAFv2, IAM, VPC, CloudWatch)` • `Azure (AKS, Azure Monitor, Key Vault)` |
| **Secrets & Identity** | `HashiCorp Vault (Dynamic Database Engine)` • `External Secrets Operator (ESO)` • `OIDC Keyless Auth` |
| **Container & Orchestration** | `Kubernetes (K8s)` • `Docker` • `Helm` • `ArgoCD (App-of-Apps GitOps)` • `Istio Service Mesh` • `Kind` |
| **Infrastructure as Code** | `Terraform (Modular / Remote State / Locking)` • `AWS CDK` • `HCL` • `Makefiles` |
| **CI/CD & Automation** | `GitHub Actions (Reusable Composite Actions)` • `Jenkins` • `GitLab CI` • `Bash / POSIX Automation` |
| **DevSecOps & Supply Chain** | `Trivy (SCA & Containers)` • `Semgrep (SAST)` • `Gitleaks` • `Checkov (IaC)` • `Cosign` • `Syft (SBOM)` |
| **SRE & Resilience** | `Prometheus` • `Grafana` • `Alertmanager` • `Loki & Promtail` • `Velero (Disaster Recovery)` • `SLI / SLO` |
| **Languages & Systems** | `Python` • `TypeScript` • `Node.js` • `Bash` • `Go` • `Rust / Tauri` • `SQL / PostgreSQL` |

</div>

---

### 🚀 Featured Production & Open-Source Projects

#### 🔐 [Zero-Secrets GitOps: HashiCorp Vault & External Secrets Operator](https://github.com/rahulmotvani0-sketch/vault-secrets-operator-k8s)
* Enterprise reference architecture eliminating 100% of static credentials and achieving true **Zero Secrets in Git**.
* **HashiCorp Vault Dynamic Database Secrets Engine** mints on-demand, short-lived PostgreSQL credentials (1h TTL) with automated role revocation on expiry.
* **External Secrets Operator (ESO)** synchronizes credentials into native Kubernetes Secrets via ServiceAccount JWT auth, eliminating intrusive sidecars.
* `Tags:` *HashiCorp Vault • External Secrets Operator • Kubernetes • PostgreSQL • GitOps • DevSecOps*

#### ☸️ [Kubernetes GitOps & SRE Observability Platform](https://github.com/rahulmotvani0-sketch/kubernetes-gitops-observability-platform)
* Turnkey multi-node Kind cluster bootstrapping driven declaratively by the **ArgoCD App-of-Apps pattern**.
* Complete **Prometheus & Grafana RED** monitoring stack with Alertmanager routing and automated chaos engineering failure recovery.
* Full distributed logging pipeline using **Grafana Loki** and **Promtail DaemonSet**.
* `Tags:` *Kubernetes • GitOps • ArgoCD • Prometheus • Grafana • Loki • SRE • Chaos Engineering*

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

### 📊 GitHub Activity & Insights

<div align="center">

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=rahulmotvani0-sketch&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="Rahul's GitHub Stats" width="48%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=rahulmotvani0-sketch&theme=tokyonight&hide_border=true" alt="Rahul's Streak" width="48%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rahulmotvani0-sketch&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</p>

</div>

---

### 💬 Let's Connect & Collaborate

- 💼 **LinkedIn:** [linkedin.com/in/rahulmotvani](https://www.linkedin.com/in/rahulmotvani/)
- 🌐 **Interactive Portfolio:** [rahul.techiking.com](https://rahul.techiking.com)
- 🎯 **TryHackMe:** [tryhackme.com/p/rahulmotvani8gma](https://tryhackme.com/p/rahulmotvani8gma)
- 📧 **Direct Email:** [rahulmotvani8@gmail.com](mailto:rahulmotvani8@gmail.com)
- 🤝 **Open to:** Senior DevOps Engineer, DevSecOps Specialist, SRE, and Cloud Platform Engineering roles.
