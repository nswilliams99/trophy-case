#!/bin/bash
# Parse DataForSEO keyword suggestion files and extract keyword data
# Uses only shell builtins and standard tools (no node/python)

OUTFILE="C:/Users/Nateman/Projects/trophy-case/.claude/worktrees/sharp-pike/research/phase-2-raw-keywords.md"
BASEDIR="C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results"

# Header
cat > "$OUTFILE" << 'HEADER'
# Phase 2: Raw Keyword Research Data

Extracted from DataForSEO Keyword Suggestions API results.
Only keywords with search_volume > 0 are included. Sorted by search volume (descending).

HEADER

TOTAL=0

process_file() {
  local filepath="$1"
  local label="$2"

  # Extract the inner "text" JSON string, unescape newlines, then extract keyword data
  # The file is: [{"type":"text","text":"...escaped JSON..."}]
  # We need to extract the text value and parse it

  # Step 1: Extract keyword blocks using grep -oP
  # Each item has "keyword": "...", then keyword_info with search_volume, cpc, competition_level
  # and search_intent_info with main_intent

  # First, get the text content and unescape it
  local content
  content=$(sed 's/^.*"text": "//;s/"[[:space:]]*}[[:space:]]*\]$//' "$filepath" | sed 's/\\n/ /g; s/\\"/"/g; s/\\\\/\\/g')

  # Extract items array content
  # Each item looks like: {"se_type":"google","keyword":"...","keyword_info":{...},"search_intent_info":{...}}

  # Use grep to find keyword + search_volume pairs
  # Strategy: split on "keyword": to get each item block, then extract fields

  local count=0
  local tmpfile="/tmp/kw_$$_$(echo "$label" | tr ' ' '_').txt"

  echo "$content" | tr '{}' '\n\n' | awk '
    /"keyword"/ && /"search_volume"/ {
      kw = ""; sv = 0; cpc = 0; comp = "N/A"; intent = "";
      # Extract keyword
      if (match($0, /"keyword"[[:space:]]*:[[:space:]]*"([^"]*)"/, m)) kw = m[1];
      # Extract search_volume
      if (match($0, /"search_volume"[[:space:]]*:[[:space:]]*([0-9]+)/, m)) sv = m[1];
      # Extract cpc
      if (match($0, /"cpc"[[:space:]]*:[[:space:]]*([0-9.]+)/, m)) cpc = m[1];
      # Extract competition_level
      if (match($0, /"competition_level"[[:space:]]*:[[:space:]]*"([^"]*)"/, m)) comp = m[1];

      if (sv > 0 && kw != "") {
        printf "%d\t%s\t%s\t%s\n", sv, kw, cpc, comp;
      }
    }
  ' | sort -t$'\t' -k1 -rn > "$tmpfile"

  count=$(wc -l < "$tmpfile")
  TOTAL=$((TOTAL + count))

  cat >> "$OUTFILE" << EOF
## $label

**Seed keyword category:** $label
**Keywords with volume > 0:** $count

| Keyword | Search Volume | CPC (\$) | Competition | Intent |
|---------|--------------|---------|-------------|--------|
EOF

  while IFS=$'\t' read -r sv kw cpc comp; do
    echo "| $kw | $sv | $cpc | $comp | |" >> "$OUTFILE"
  done < "$tmpfile"

  echo "" >> "$OUTFILE"
  echo "---" >> "$OUTFILE"
  echo "" >> "$OUTFILE"

  rm -f "$tmpfile"
  echo "  $label: $count keywords"
}

process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071108.txt" "Custom Medals (National)"
process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071735.txt" "Custom Plaques (National)"
process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931077619.txt" "Trophy Shop (National)"
process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931078261.txt" "Custom Trophies (National)"
process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931079539.txt" "Engraving Services (National)"
process_file "$BASEDIR/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931080266.txt" "Award Plaques (National)"

cat >> "$OUTFILE" << EOF
## Summary

**Total keywords extracted (volume > 0):** $TOTAL
EOF

echo "Done! Total: $TOTAL keywords -> $OUTFILE"
