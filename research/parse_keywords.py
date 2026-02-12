import json
import os

# File paths and their category labels
files = [
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071108.txt",
        "label": "Custom Medals (National)"
    },
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071735.txt",
        "label": "Custom Plaques (National)"
    },
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931077619.txt",
        "label": "Trophy Shop (National)"
    },
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931078261.txt",
        "label": "Custom Trophies (National)"
    },
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931079539.txt",
        "label": "Engraving Services (National)"
    },
    {
        "path": r"C:\Users\Nateman\.claude\projects\C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike\de3c2b79-5a5e-469c-998c-045954fc6b1e\tool-results\mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931080266.txt",
        "label": "Award Plaques (National)"
    },
]

output_path = r"C:\Users\Nateman\Projects\trophy-case\.claude\worktrees\sharp-pike\research\phase-2-raw-keywords.md"

def extract_keywords(file_path):
    """Extract keywords from a DataForSEO keyword suggestions result file."""
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # The file is a JSON array with one element that has a "text" field
    outer = json.loads(raw)

    # Check structure
    if isinstance(outer, list) and len(outer) > 0:
        item = outer[0]
        if "text" in item:
            inner_text = item["text"]
            data = json.loads(inner_text)
        else:
            data = outer
    elif isinstance(outer, dict):
        data = outer
    else:
        print(f"  Unexpected structure for {file_path}")
        return []

    # Navigate to the items array
    # DataForSEO structure: { tasks: [ { result: [ { items: [...] } ] } ] }
    keywords = []

    tasks = data.get("tasks", [])
    if not tasks:
        # Maybe the data is already the result
        if "items" in data:
            items = data["items"]
        elif "result" in data:
            results = data["result"]
            if isinstance(results, list) and len(results) > 0:
                items = results[0].get("items", [])
            else:
                items = []
        else:
            print(f"  No tasks found in {file_path}, keys: {list(data.keys())[:10]}")
            return []
    else:
        task = tasks[0]
        results = task.get("result", [])
        if not results:
            print(f"  No results in task for {file_path}")
            return []
        items = results[0].get("items", [])

    for item in items:
        kw = item.get("keyword", "")
        ki = item.get("keyword_info", {})
        if ki is None:
            ki = {}

        search_volume = ki.get("search_volume", 0) or 0
        cpc = ki.get("cpc", 0) or 0
        competition_level = ki.get("competition_level", "N/A") or "N/A"

        # Search intent
        search_intent = ""
        si = ki.get("search_intent", None)
        if si is None:
            si_info = item.get("search_intent_info", {})
            if si_info:
                main_intent = si_info.get("main_intent", "")
                search_intent = main_intent if main_intent else ""
            else:
                search_intent = ""
        elif isinstance(si, dict):
            search_intent = si.get("main_intent", "")
        elif isinstance(si, str):
            search_intent = si

        if search_volume > 0:
            keywords.append({
                "keyword": kw,
                "search_volume": search_volume,
                "cpc": round(cpc, 2),
                "competition_level": competition_level,
                "search_intent": search_intent,
            })

    # Sort by search volume descending
    keywords.sort(key=lambda x: x["search_volume"], reverse=True)
    return keywords


def format_table(keywords):
    """Format keywords as a markdown table."""
    lines = []
    lines.append("| Keyword | Search Volume | CPC ($) | Competition | Intent |")
    lines.append("|---------|--------------|---------|-------------|--------|")
    for kw in keywords:
        lines.append(f"| {kw['keyword']} | {kw['search_volume']:,} | {kw['cpc']:.2f} | {kw['competition_level']} | {kw['search_intent']} |")
    return "\n".join(lines)


# Build the output
output_lines = []
output_lines.append("# Phase 2: Raw Keyword Research Data")
output_lines.append("")
output_lines.append("Extracted from DataForSEO Keyword Suggestions API results.")
output_lines.append("Only keywords with search_volume > 0 are included. Sorted by search volume (descending).")
output_lines.append("")

total_keywords = 0

for file_info in files:
    print(f"Processing: {file_info['label']}...")
    keywords = extract_keywords(file_info["path"])
    total_keywords += len(keywords)

    output_lines.append(f"## {file_info['label']}")
    output_lines.append("")
    output_lines.append(f"**Seed keyword category:** {file_info['label']}")
    output_lines.append(f"**Keywords with volume > 0:** {len(keywords)}")
    output_lines.append("")

    if keywords:
        output_lines.append(format_table(keywords))
    else:
        output_lines.append("*No keywords with search volume > 0 found.*")

    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")

# Summary
output_lines.append("## Summary")
output_lines.append("")
output_lines.append(f"**Total keywords extracted (volume > 0):** {total_keywords}")
output_lines.append("")

# Write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"\nDone! Wrote {total_keywords} keywords to {output_path}")
