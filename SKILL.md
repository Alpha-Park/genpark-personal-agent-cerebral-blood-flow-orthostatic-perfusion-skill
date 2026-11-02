---
name: genpark-personal-agent-cerebral-blood-flow-orthostatic-perfusion-skill
version: "1.0.0"
description: "Zero-dependency Transcranial Doppler (TCD) Middle Cerebral Artery (MCA) velocity modeler, Gosling Pulsatility Index (PI) calculator, and hypocapnic hyperventilation vasoconstriction evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Cerebral Blood Flow Orthostatic Perfusion Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate cerebral hemodynamics, compute Transcranial Doppler (TCD) Middle Cerebral Artery (MCA) flow velocities ($V_s, V_d, V_m$), calculate Gosling Pulsatility Index ($PI = \frac{V_s - V_d}{V_m}$) and Pourcelot Resistive Index ($RI$), and model acute cerebral vasoconstriction induced by hypocapnic hyperventilation ($\text{ETCO}_2$ wash-out).

## Agent In-Context Capabilities

- **Intracranial Hemodynamic Resistance Profiling**: Uses the Gosling PI to differentiate normal downstream arteriolar compliance ($0.70 - 1.10$) from elevated distal microvascular resistance or intracranial pressure ($> 1.25$).
- **Cerebrovascular $\text{CO}_2$ Reactivity**: Models the clinical $-3.0\%$ per mmHg cerebral blood flow drop caused by acute over-breathing and hypocapnic alkalosis.
- **Prefrontal Perfusion Rescue**: Prescribes specific breathwork and carbon dioxide retention protocols to reverse acute cerebral oligemia and cognitive fog.

## Tools Summary

1. `calculate_cerebral_perfusion_and_pulsatility`: Returns Gosling PI, Pourcelot RI, and microvascular resistance classification.
2. `model_hypocapnic_hyperventilation_vasoconstriction`: Projects cerebral blood flow reduction percentage and clinical symptom forecasts.
