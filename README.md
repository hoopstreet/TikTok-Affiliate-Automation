# 🏗️ TikTok-Affiliate-Automation (Architect v4.0)

Welcome to the **Master Control Center**. This repository is the persistent storage layer for a multi-tenant AI automation system built on **n8n**, **Supabase**, and **Telegram**.

## 🎯 System Overview
This is a self-evolving "Mother Workflow" system designed to manage five distinct business niches. It uses dynamic pathing to update roadmaps and backup workflow JSONs automatically.

### 🏢 The 5 Projects
1.  **Workflow-Builder** (The Mother): Manages system health, self-healing, and new node creation.
2.  **MK-Online-Store**: High-speed price scraping and e-commerce automation.
3.  **Hoopstreet**: Inventory management and API integration.
4.  **Daily-Drive-PH**: TikTok Affiliate content generation and metadata optimization.
5.  **Budget-Accessories**: Sourcing and retail automation.

---

## 📊 Technical Architecture

### 🧠 The Brain (Supabase)
The system state is managed via the `public` schema in Supabase:
* **`builder_memory`**: Stores the `active_project` context for the Telegram bot.
* **`project_roadmaps`**: Tracks progress and next steps for all 5 niches.
* **`integration_vault`**: Securely holds API credentials for BrightData, TikTok, and more.

### 🛠️ The Workers (n8n)
The workflows are designed to be context-aware. 
* **Dynamic Save Path**: `{{active_project}}/roadmap.md`
* **Daily Victory Report**: Automated 9 AM summary of all project statuses sent to Telegram.
* **Self-Healing**: Automatic rollback to `last_stable_json` if a node execution fails.

---

## 📁 Repository Structure
```text
.
├── Workflow-Builder/     # System Mother & Self-Healing logic
├── MK-Online-Store/      # Scraping & E-commerce workflows
├── Hoopstreet/           # API & Inventory syncs
├── Daily-Drive-PH/       # TikTok Affiliate automation
├── Budget-Accessories/   # Retail & Sourcing management
└── README.md             # This control document
