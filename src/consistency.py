import sys, json, pathlib
from review import review, clean

ROOT = pathlib.Path(__file__).resolve().parent.parent
path = pathlib.Path(sys.argv[1])
runs = int(sys.argv[2]) if len(sys.argv) > 2 else 3
prd = clean(path.read_text())

all_runs = []
for i in range(runs):
    findings, _ = review(prd)
    all_runs.append({f["criterion"]: f["rating"] for f in findings})
    print(f"run {i + 1} of {runs} done")

stable = 0
print()
for n in range(1, 10):
    vals = [r.get(n, "?") for r in all_runs]
    same = len(set(vals)) == 1
    stable += same
    print(f"{n}: {' / '.join(vals)}  {'stable' if same else '<-- flips'}")
print(f"\nStable criteria: {stable}/9 over {runs} runs")

out = ROOT / "results"
out.mkdir(exist_ok=True)
(out / f"consistency__{path.stem}.json").write_text(json.dumps(all_runs, indent=2))
