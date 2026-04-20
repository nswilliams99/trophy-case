# Graph Report - C:\Users\Nateman\Projects\trophy-case  (2026-04-20)

## Corpus Check
- 9 files · ~64,873 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 15 nodes · 6 edges · 10 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]

## God Nodes (most connected - your core abstractions)
1. `extract_keywords()` - 2 edges
2. `format_table()` - 2 edges
3. `Extract keywords from a DataForSEO keyword suggestions result file.` - 1 edges
4. `Format keywords as a markdown table.` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
Cohesion: 0.67
Nodes (2): extract_keywords(), Extract keywords from a DataForSEO keyword suggestions result file.

### Community 1 - "Community 1"
Cohesion: 1.0
Nodes (2): format_table(), Format keywords as a markdown table.

### Community 2 - "Community 2"
Cohesion: 1.0
Nodes (0): 

### Community 3 - "Community 3"
Cohesion: 1.0
Nodes (0): 

### Community 4 - "Community 4"
Cohesion: 1.0
Nodes (0): 

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (0): 

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (0): 

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (0): 

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (0): 

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **2 isolated node(s):** `Extract keywords from a DataForSEO keyword suggestions result file.`, `Format keywords as a markdown table.`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 1`** (2 nodes): `format_table()`, `Format keywords as a markdown table.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 2`** (2 nodes): `layout.tsx`, `RootLayout()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 3`** (2 nodes): `utils.ts`, `cn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (1 nodes): `eslint.config.mjs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (1 nodes): `next-env.d.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (1 nodes): `next.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 7`** (1 nodes): `postcss.config.mjs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (1 nodes): `parse.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (1 nodes): `page.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `format_table()` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **What connects `Extract keywords from a DataForSEO keyword suggestions result file.`, `Format keywords as a markdown table.` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._