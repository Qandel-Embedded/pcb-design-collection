"""
Automated PCB Design Rule Checker.
Parses KiCad .kicad_pcb files and checks for common violations.
"""
import re, sys
from pathlib import Path


RULES = {
    "min_trace_width_mm": 0.15,
    "min_clearance_mm": 0.15,
    "min_via_drill_mm": 0.2,
    "min_annular_ring_mm": 0.125,
}


def parse_traces(pcb_text):
    """Extract trace widths from KiCad PCB file."""
    widths = [float(w) for w in re.findall(r'\(width ([0-9.]+)\)', pcb_text)]
    return widths


def parse_vias(pcb_text):
    """Extract via drill sizes."""
    drills = [float(d) for d in re.findall(r'\(drill ([0-9.]+)\)', pcb_text)]
    return drills


def check(pcb_path):
    text = Path(pcb_path).read_text()
    errors = []

    for w in parse_traces(text):
        if w < RULES["min_trace_width_mm"]:
            errors.append(f"Trace width {w}mm < min {RULES['min_trace_width_mm']}mm")

    for d in parse_vias(text):
        if d < RULES["min_via_drill_mm"]:
            errors.append(f"Via drill {d}mm < min {RULES['min_via_drill_mm']}mm")

    if errors:
        print(f"❌ {len(errors)} DRC violation(s) in {pcb_path}:")
        for e in errors: print(f"   • {e}")
        return False
    else:
        print(f"✅ DRC passed: {pcb_path}")
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python design_rules_check.py <file.kicad_pcb>")
        sys.exit(1)
    sys.exit(0 if check(sys.argv[1]) else 1)
