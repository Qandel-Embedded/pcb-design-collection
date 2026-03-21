"""Unit tests for PCB utility scripts."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import io, csv


def test_bom_csv_structure():
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(['Qty', 'References', 'Value', 'Footprint', 'Datasheet'])
    writer.writerow([2, 'R1 R2', '10k', 'R_0402', 'N/A'])
    buf.seek(0)
    rows = list(csv.DictReader(buf))
    assert rows[0]['Qty'] == '2'
    assert 'R1' in rows[0]['References']


def test_drc_rule_constants():
    import design_rules_check as drc
    assert drc.RULES['min_trace_width_mm'] > 0
    assert drc.RULES['min_via_drill_mm'] > 0


def test_parse_traces_finds_widths():
    import design_rules_check as drc
    sample = '(segment (start 10 10) (end 20 20) (width 0.25) (layer F.Cu))'
    widths = drc.parse_traces(sample)
    assert 0.25 in widths


def test_parse_vias_finds_drills():
    import design_rules_check as drc
    sample = '(via (at 10 10) (size 0.8) (drill 0.4) (layers F.Cu B.Cu))'
    drills = drc.parse_vias(sample)
    assert 0.4 in drills
