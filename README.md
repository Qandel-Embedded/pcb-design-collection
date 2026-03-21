# PCB Design Collection

[![CI](https://github.com/Qandel-Embedded/pcb-design-collection/actions/workflows/ci.yml/badge.svg)](https://github.com/Qandel-Embedded/pcb-design-collection/actions)
[![KiCad](https://img.shields.io/badge/tool-KiCad%207-blue)](https://kicad.org)
[![Altium](https://img.shields.io/badge/tool-Altium%20Designer-red)](https://altium.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Professional PCB designs for robotics, IoT, and industrial applications with automated BOM and DRC tooling.

## Designs

| Board | Layers | Technology | Application |
|-------|--------|-----------|-------------|
| Motor Controller | 4 | STM32G4 + DRV8305 | 48V/15A BLDC drive |
| IoT Sensor Hub | 2 | ESP32 + solar charging | Smart home node |
| Robot Main Board | 6 | CM4 + STM32 co-proc | Autonomous robot |

## Utility Scripts

```bash
# Generate Bill of Materials from KiCad netlist
python scripts/bom_generator.py board.xml

# Run automated Design Rule Check
python scripts/design_rules_check.py board.kicad_pcb
```

## Design Standards
- IPC-2221 trace/clearance rules
- EMC pre-compliance layout (ground planes, decoupling strategy)
- IPC-7711/7721 rework guidelines documented

---
**Portfolio:** https://ahmedqandel.com | Available for hire on Upwork
