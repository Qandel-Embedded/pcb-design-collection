"""Bill of Materials generator from KiCad netlist."""
import csv, xml.etree.ElementTree as ET, sys


def parse_kicad_bom(netlist_path):
    tree = ET.parse(netlist_path)
    root = tree.getroot()
    components = {}
    for comp in root.iter("comp"):
        ref   = comp.get("ref")
        value = comp.findtext("value", "N/A")
        fp    = comp.findtext("footprint", "N/A")
        ds    = comp.findtext("datasheet", "N/A")
        key   = (value, fp)
        if key not in components:
            components[key] = {"value": value, "footprint": fp,
                               "datasheet": ds, "refs": []}
        components[key]["refs"].append(ref)
    return components


def export_csv(components, output_path="bom.csv"):
    with open(output_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Qty", "References", "Value", "Footprint", "Datasheet"])
        for (value, fp), info in sorted(components.items()):
            refs = " ".join(sorted(info["refs"]))
            w.writerow([len(info["refs"]), refs, value, fp, info["datasheet"]])
    print(f"✅ BOM exported: {output_path} ({len(components)} unique parts)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bom_generator.py <netlist.xml>")
        sys.exit(1)
    cmp = parse_kicad_bom(sys.argv[1])
    export_csv(cmp)
