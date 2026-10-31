import json, re, sys, pathlib
import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from your .env file

MODEL = "claude-sonnet-5-5"  # later try "claude-haiku-5-5" to compare cost and quality
ROOT = pathlib.Path(__file__).resolve().parent.parent
RUBRIC = (ROOT / "docs" / "rubric.md").read_text()

SYSTEM = f"""You are a careful reviewer of product requirement documents (PRDs).
Rate the document against each of the 9 criteria in the rubric below.

For each criterion return a JSON object with:
- "criterion": the number 1-9
- "name": the criterion name
- "rating": exactly one of "Missing", "Weak", "Good"
- "evidence": one exact quote copied from the document (max 40 words), or "" if nothing relevant exists
- "reason": one sentence linking the evidence to the rubric's Good and Weak lines

Rules:
- Quote only text that really appears in the document. Never invent or paraphrase quotes.
- A heading with no content, an unfilled template placeholder, or "N/A" counts as Missing.
- Judge structure and clarity only, not whether the product idea is good.
- Return ONLY a JSON list of 9 objects, with no other text.

RUBRIC:
{RUBRIC}
"""

def clean(text):
    # remove HTML comments, such as leftover template instructions
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)

def norm(s):
    return " ".join(s.split()).lower()

def review(prd_text):
    client = anthropic.Anthropic(default_headers={"Accept-Encoding": "identity"})
    msg = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=SYSTEM,
        messages=[{"role": "user", "content": "Review this document:\n\n" + prd_text}],
    )
    raw = "".join(b.text for b in msg.content if b.type == "text").strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw), msg.usage

if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1])
    prd = clean(path.read_text())
    findings, usage = review(prd)
    for f in findings:
        # guardrail: every quote must really appear in the document
        ok = f["evidence"] == "" or norm(f["evidence"]) in norm(prd)
        flag = "" if ok else "  [QUOTE NOT FOUND IN DOCUMENT]"
        print(f'{f["criterion"]}. {f["name"]}: {f["rating"]}{flag}')
        print(f'   {f["reason"]}')
    print(f"\nTokens in: {usage.input_tokens}, out: {usage.output_tokens}")
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    (out / f"{path.stem}__{MODEL}.json").write_text(json.dumps(findings, indent=2))
