import json, re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL = sys.argv[1] if len(sys.argv) > 1 else "claude-sonnet-5-5"

# read your hand ratings from data/hand-ratings.md
hand, doc = {}, None
for line in (ROOT / "data" / "hand-ratings.md").read_text().splitlines():
    if line.startswith("## "):
        doc = line[3:].strip().removesuffix(".md")
        hand[doc] = {}
    m = re.match(r"\|\s*(\d+)\s*\|[^|]*\|\s*([^|]*?)\s*\|", line)
    if doc and m and m.group(2):
        hand[doc][int(m.group(1))] = m.group(2).split()[0]  # "Good (borderline)" -> "Good"

agree = total = 0
base = collections.Counter()
for doc, ratings in hand.items():
    f = ROOT / "results" / f"{doc}__{MODEL}.json"
    if not f.exists():
        print(f"(no results yet for {doc})")
        continue
    tool = {x["criterion"]: x["rating"] for x in json.loads(f.read_text())}
    print(f"\n{doc}")
    for n in sorted(ratings):
        h, t = ratings[n], tool.get(n, "?")
        total += 1
        agree += (h == t)
        base[h] += 1
        print(f"  {n}: you={h:<8} tool={t:<8} {'ok' if h == t else '<-- differs'}")

if total:
    print(f"\nAgreement: {agree}/{total} = {agree / total:.0%}")
    top, cnt = base.most_common(1)[0]
    print(f"Baseline (always say '{top}'): {cnt}/{total} = {cnt / total:.0%}")
