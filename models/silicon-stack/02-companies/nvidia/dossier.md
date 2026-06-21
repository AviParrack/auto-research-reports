---
company: nvidia
name: "NVIDIA"
url: "https://www.nvidia.com/"
tier: B
role: "Fabless designer of the finished accelerator (product owner)"
location: "Santa Clara, CA, USA"
revenue_usd: 130000000000
scaffold: false
---

## Overview

NVIDIA is the representative **product owner** for this model — a fabless designer
whose GPU-class accelerators are the finished output of the chain, and where the
[idiot index](/models/silicon-stack/idiot-index/) is largest (die value ≫ raw inputs).

## What's in a finished accelerator

A high-end accelerator (H100/H200-class) is far more than the logic die:

- **Logic die** — a ~$18k 3nm wafer ([TSMC](/models/silicon-stack/companies/tsmc/)) yields the compute die.
- **HBM** — 6–8 stacks at ~$300–500 each ⇒ ~$2,000–4,000 of memory ([SK Hynix](/models/silicon-stack/companies/sk-hynix/)), often rivaling the die cost.
- **CoWoS packaging + interposer + ABF substrate** — ~$10k CoWoS wafer ASP plus substrate.

The market for these is the growth engine — see the [Overview market chart](/models/silicon-stack/) (~25–31% CAGR for AI accelerators).

## To verify next

Per-die cost split between wafer, HBM, packaging, and margin (proprietary).
