import math
from pathlib import Path

def calc_angle(a, b, c):
    # a=N, b=CA, c=C
    ba = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
    bc = (c[0]-b[0], c[1]-b[1], c[2]-b[2])

    dot = ba[0]*bc[0] + ba[1]*bc[1] + ba[2]*bc[2]
    mag_ba = math.sqrt(ba[0]**2 + ba[1]**2 + ba[2]**2)
    mag_bc = math.sqrt(bc[0]**2 + bc[1]**2 + bc[2]**2)

    cos_angle = dot / (mag_ba * mag_bc)
    cos_angle = max(-1.0, min(1.0, cos_angle)) # clamp
    angle = math.degrees(math.acos(cos_angle))
    return angle

pdb_file = Path("1aki.pdb")
residues = {}

with open(pdb_file) as f:
    for line in f:
        if not line.startswith("ATOM"):
            continue
        atom_name = line[12:16].strip()
        res_id = int(line[22:26])
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])

        if res_id not in residues:
            residues[res_id] = {}
        if atom_name in ('N', 'CA', 'C'):
            residues[res_id][atom_name] = (x,y,z)

print("=== PDB Geometry 03: N-CA-C Angle Check ===")
print(f"File: {pdb_file.name} | Total residues: {len(residues)}\n")

violations = 0
for res_id in sorted(residues.keys()):
    if 'N' in residues[res_id] and 'CA' in residues[res_id] and 'C' in residues[res_id]:
        ang = calc_angle(residues[res_id]['N'], residues[res_id]['CA'], residues[res_id]['C'])
        status = "OK" if 100 <= ang <= 125 else "VIOLATION"
        if status == "VIOLATION":
            violations += 1
        print(f"Residue {res_id:3d} N-CA-C : {ang:.2f} deg [{status}]")

print(f"\nTotal violations: {violations}")
print("Ideal N-CA-C angle should be ~111 deg")