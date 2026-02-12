# Website Proposal Research & Generation Prompt

Copy and paste the section below into a new Claude conversation that has access to DataForSEO MCP tools. Fill in the bracketed fields with your client's information.

---

## THE PROMPT

```
I need you to research a local business and build a complete website proposal. Work through each phase sequentially — complete one before starting the next. Use DataForSEO tools for all research. Do NOT make up numbers — every projection must trace back to real keyword data, competitor traffic, and conversion benchmarks.

### CLIENT INFORMATION

- **Business name:** [e.g., "The Trophy Case"]
- **Owner:** [e.g., "Gregg Schmidt"]
- **Address:** [e.g., "303 N Main St, Fremont, NE 68025"]
- **Industry:** [e.g., "trophy shop / awards / engraving"]
- **Current website:** [e.g., "thetrophycasefremont.com" or "none"]
- **Annual revenue:** [e.g., "$85,000"]
- **Annual profit:** [e.g., "$48,000"]
- **Current website cost:** [e.g., "$100/mo for Wix site" or "none"]
- **Primary city/market:** [e.g., "Fremont, NE (pop 35,000)"]
- **Secondary market:** [e.g., "Omaha metro (pop 950,000)"]
- **What they want to sell online (if anything):** [e.g., "medals and plaques only — trophies are too custom/fragile to ship"]
- **Special context:** [e.g., "Owner wants to sell the business in 1-2 years for $45-$80K. Revenue depends heavily on personal relationships (wrestling meets, car shows). Website needs to add transferable value for a buyer."]

### MY PRICING

- **Option 1 (full site + e-commerce):** $[amount] build + $[amount]/mo
- **Option 2 (lead-gen site only):** $[amount] build + $[amount]/mo
- **Monthly SEO management included in monthly fee:** Yes/No
- **E-commerce platform:** [e.g., "Shopify Basic $39/mo"]
- **Product customizer (if applicable):** [e.g., "Zakeke $19/mo"]

If no e-commerce is needed, skip Option 1 and just do a lead-gen proposal with one option.

### RESEARCH PHASES

Complete each phase and save results to a `research/` folder before moving to the next.

**Phase 1: Keyword Research**
- Use `dataforseo_labs_google_keyword_suggestions` and `dataforseo_labs_google_related_keywords` for the business's core services + city names
- Search for "[service] + [city]", "[service] near me", "custom [product]", etc.
- Record: keyword, monthly search volume, keyword difficulty, CPC
- Save to `research/phase-1-keywords.md`

**Phase 2: Competitor Identification**
- Use `dataforseo_labs_google_serp_competitors` with the top keywords from Phase 1
- Use `serp_organic_live_advanced` to see who ranks for key local terms
- Identify 5-8 competitors (local + national)
- Save to `research/phase-2-competitors.md`

**Phase 3: Competitor Deep Dive**
- For each competitor, use `dataforseo_labs_google_ranked_keywords` and `dataforseo_labs_google_domain_rank_overview`
- Get: total organic traffic, number of ranked keywords, top pages, technology stack
- Use `domain_analytics_technologies_domain_technologies` for tech stack
- Save to `research/phase-3-competitor-analysis.md`

**Phase 4: Backlink Analysis**
- Use `backlinks_summary` and `backlinks_referring_domains` for top 3 competitors
- Assess how hard it will be to compete on backlinks
- Save to `research/phase-4-backlinks.md`

**Phase 5: Local SEO Assessment**
- Check Google Business Profile status (reviews, ratings) from SERP data
- Assess local pack competition for key terms
- Use `business_data_business_listings_search` if available for the category
- Save to `research/phase-5-local-seo.md`

**Phase 6: Market Sizing**
- Total addressable search volume for the business's services in their market(s)
- Segment by: local searches, "near me" searches, national/e-commerce searches
- Estimate capturable traffic at Month 6, 12, 18, 24
- Save to `research/phase-6-market-sizing.md`

**Phase 7: Revenue Projections**
- Convert traffic projections to revenue using:
  - Local leads: 5-8% conversion rate on qualified traffic, average order value from competitor pricing
  - E-commerce (if applicable): 1.5-3% conversion rate, AOV from competitor product pricing
- Build month-by-month tables for Year 1 and Year 2
- Calculate annual totals with low and high ranges
- Year 1 low-end for the cheaper option should be at least 15-20% above annual costs (worst case still covers investment)
- Save to `research/phase-7-revenue-projections.md`

**Phase 8: Technical Architecture**
- Recommend tech stack based on competitor analysis and client needs
- Calculate monthly/annual platform costs
- Save to `research/phase-8-technical.md`

**Phase 9: Ad Cost Comparison**
- Use CPC data from Phase 1 to calculate what it would cost to get the same traffic via Google Ads
- Show that SEO is dramatically more cost-effective
- Save to `research/phase-9-ad-comparison.md`

### PROPOSAL GENERATION

After all 9 phases are complete, compile everything into `PROPOSAL.md` with this structure:

1. **Executive Summary** — Frame around the client's specific situation and goals. Lead with the business problem, not the technical solution. If they're selling, frame around sale price. If they're growing, frame around revenue.

2. **The Problem** — Current website performance vs. competitors. Include what they're currently paying (if anything) for their existing site. Make the gap obvious.

3. **Market Opportunity** — Search demand data, competition level, seasonality.

4. **Option 1** (if applicable — e-commerce + lead-gen):
   - What they get
   - Technology & monthly costs
   - Traffic projections table (Month 6/12/18/24)
   - Revenue projections (Year 1, Year 2)
   - Investment & ROI table
   - Compare monthly cost to what they currently pay

5. **Option 2** (lead-gen only):
   - Same structure as Option 1
   - Compare monthly cost to what they currently pay

6. **Side-by-Side Comparison** — Table comparing both options on all key metrics

7. **How This Increases Value** — For sale context: show how website revenue changes the business profit and sale multiple. For growth context: show cumulative ROI over 24 months.

8. **Google Business Profile** — Immediate priority regardless of which option they choose

9. **Why Not Paid Ads** — Use Phase 9 data to show SEO is 100-600x more efficient

10. **Timeline** — Week-by-week build schedule

11. **What's Included** — Itemized deliverables

12. **Recommendation** — Pick one option and explain why

13. **Next Steps** — Clear action items

### IMPORTANT RULES

- Every revenue number must trace back to real keyword volumes and documented conversion benchmarks. No made-up numbers.
- Use conservative projections throughout. Low-end estimates should be genuinely pessimistic.
- Year 1 low-end for the cheapest option must cover annual costs plus 15-20% minimum — if it doesn't, adjust or be transparent about the loss period.
- If e-commerce has a Year 1 loss, call it out explicitly and show when it turns profitable.
- All projections are for NEW business only — existing revenue is additive on top.
- Frame costs against what the client currently pays for their website (if anything).
- Match the tone to the client — a small-town shop owner doesn't want agency jargon.
- Commit all research files and the final proposal to git as you go.
```

---

## NOTES

- If the client has no e-commerce needs, delete the Option 1 sections and just present a single lead-gen option
- If the client isn't selling the business, replace the "sale price" framing with ROI/growth framing
- The 9-phase research process takes 30-60 minutes with DataForSEO tools — don't skip phases
- Revenue projections are only as good as the keyword data — if search volume is very low, be honest about it
- For highly competitive industries, keyword difficulty matters more — adjust traffic ramp-up timelines accordingly
