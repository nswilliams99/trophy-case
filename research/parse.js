const fs = require('fs');
const files = [
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071108.txt', label: 'Custom Medals (National)'},
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931071735.txt', label: 'Custom Plaques (National)'},
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931077619.txt', label: 'Trophy Shop (National)'},
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931078261.txt', label: 'Custom Trophies (National)'},
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931079539.txt', label: 'Engraving Services (National)'},
  {path: 'C:/Users/Nateman/.claude/projects/C--Users-Nateman-Projects-trophy-case--claude-worktrees-sharp-pike/de3c2b79-5a5e-469c-998c-045954fc6b1e/tool-results/mcp-dataforseo-dataforseo_labs_google_keyword_suggestions-1770931080266.txt', label: 'Award Plaques (National)'}
];
let out = '# Phase 2: Raw Keyword Research Data\n\nExtracted from DataForSEO Keyword Suggestions API results.\nOnly keywords with search_volume > 0 are included. Sorted by search volume (descending).\n\n';
let total = 0;
for (const f of files) {
  console.log('Processing: ' + f.label);
  const raw = fs.readFileSync(f.path, 'utf8');
  const outer = JSON.parse(raw);
  let data = outer;
  if (Array.isArray(outer) && outer.length > 0 && outer[0].text) {
    data = JSON.parse(outer[0].text);
  }
  let items = [];
  if (data.tasks && data.tasks[0] && data.tasks[0].result && data.tasks[0].result[0]) {
    items = data.tasks[0].result[0].items || [];
  } else if (data.result && data.result[0]) {
    items = data.result[0].items || [];
  } else if (data.items) {
    items = data.items;
  }
  console.log('  Found ' + items.length + ' total items');
  let kws = [];
  for (const item of items) {
    const ki = item.keyword_info || {};
    const sv = ki.search_volume || 0;
    if (sv > 0) {
      const cpc = ki.cpc || 0;
      const comp = ki.competition_level || 'N/A';
      let intent = '';
      if (item.search_intent_info && item.search_intent_info.main_intent) {
        intent = item.search_intent_info.main_intent;
      }
      kws.push({keyword: item.keyword, sv, cpc: cpc.toFixed(2), comp, intent});
    }
  }
  kws.sort((a,b) => b.sv - a.sv);
  total += kws.length;
  out += '## ' + f.label + '\n\n';
  out += '**Seed keyword category:** ' + f.label + '  \n';
  out += '**Keywords with volume > 0:** ' + kws.length + '\n\n';
  if (kws.length > 0) {
    out += '| Keyword | Search Volume | CPC ($) | Competition | Intent |\n';
    out += '|---------|--------------|---------|-------------|--------|\n';
    for (const k of kws) {
      out += '| ' + k.keyword + ' | ' + k.sv.toLocaleString() + ' | ' + k.cpc + ' | ' + k.comp + ' | ' + k.intent + ' |\n';
    }
  } else {
    out += '*No keywords with search volume > 0 found.*\n';
  }
  out += '\n---\n\n';
}
out += '## Summary\n\n**Total keywords extracted (volume > 0):** ' + total + '\n';
const outPath = 'C:/Users/Nateman/Projects/trophy-case/.claude/worktrees/sharp-pike/research/phase-2-raw-keywords.md';
fs.writeFileSync(outPath, out, 'utf8');
console.log('\nDone! Wrote ' + total + ' keywords to ' + outPath);
