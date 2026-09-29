## 🔗 PDB Geometry 03 - Bond Angle

A pure-Python tool that validates protein bond angle geometry. Checks if N-CA-C angle in each residue is ~111 degrees, a core rule of protein backbone structure.

**👤 Author
Urva Sohail**

## ✨ Features
- **📐 Angle Check:** Calculates N-CA-C angle for each residue
- **✅ Validation:** Flags angles outside 100-125 deg range
- **📊 Summary:** Counts total violations
- **🧹 Clean Repo:** PDB ignored via .gitignore
- **🐍 Pure Python:** Only math + pathlib

## 🧠 Logic
1. **Parse PDB:** Read 1aki.pdb line by line, filter only ATOM lines
2. **Extract Atoms:** For each residue, get N, CA, C atoms (x,y,z)
3. **Store:** residues[res_id] = {'N': (x,y,z), 'CA': (x,y,z), 'C': (x,y,z)}
4. **Calculate Angle:** Use vector dot product at CA: angle between N-CA and C-CA
5. **Validate:** If 100 <= angle <= 125 => [OK], else [VIOLATION]
6. **Report:** Count total violations

## 💻 Technologies Used
- **Python 3+:** Core language
- **math.acos & math.degrees:** For angle calculation
- **pathlib:** For file handling
- **PDB Parser:** Custom ATOM line parser

## 🚀 How to Run
Using VS Code
1. Open folder pdb-geometry-03-bond-angle-
2. Copy 1aki.pdb from Project 01 into this folder
3. Run:
```
python main.py
```

## 📥 Sample Input & Output
## Input
1aki.pdb file (Lysozyme 129aa)

## Output
```
=== PDB Geometry 03: N-CA-C Angle Check ===
File: 1aki.pdb | Total residues: 129
Residue   1 N-CA-C : 110.45 deg [OK]
Residue   2 N-CA-C : 111.20 deg [OK]
Residue   3 N-CA-C : 110.88 deg [OK]
...
Residue 128 N-CA-C : 109.42 deg [OK]
Residue 129 N-CA-C : 109.69 deg [OK]
Total violations: 0
Ideal N-CA-C angle should be ∼111 deg
```

## 📊 Result
- Total Residues Parsed: 129
- Total Angles Checked: 129
- Angle Range Found: 109-112 deg
- Average N-CA-C Angle: ~110.8 deg
- Violations: 0
- Status: PASS - All bond angles are in ideal geometry

## ⚙️ How It Works
- Program parses 1aki.pdb and reads ATOM lines
- For each residue, it extracts N, CA, C atom xyz
- It creates two vectors: N-CA and C-CA
- It calculates angle using cos(angle) = dot(a,b)/(|a||b|)
- If angle is between 100 and 125 deg, it marks OK else VIOLATION
- At end it prints total violations (ideal 0 for good PDB)

## 🔮 Future Improvements
- [ ] Check CA-C-N angle also
- [ ] Export violations to CSV for analysis
- [ ] Check phi/psi dihedral angles
- [ ] Add .cif format support
- [ ] Visualize violations in PyMOL
