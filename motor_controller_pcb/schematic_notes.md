# Motor Controller PCB — Design Notes

## Overview
4-layer PCB controlling 2x BLDC motors at 48V / 15A per channel.

## Layer Stack-up
| Layer | Function          | Thickness |
|-------|------------------|-----------|
| L1    | Signal + control | 0.035mm Cu |
| L2    | GND plane        | 0.035mm Cu |
| L3    | Power (48V/GND)  | 0.070mm Cu |
| L4    | Signal + feedback| 0.035mm Cu |

## Key ICs
- **MCU:** STM32G474RET6 (Cortex-M4, 170MHz, hardware FPU)
- **Gate driver:** DRV8305 (3-phase, with protection)
- **Current sense:** INA240A3 (PWM-rejection, 20ns blanking)
- **Isolated CAN:** ISO1050DUB

## Design Rules
- Trace width (power): 3.0mm min (48V/15A)
- Trace width (signal): 0.15mm min
- Clearance (HV zones): 2.5mm
- Via impedance-controlled: 100Ω differential (CAN)
