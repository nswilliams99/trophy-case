# Phase 1: The Trophy Case - Current Website & Business Audit

## Business Overview

| Field | Detail |
|---|---|
| **Business Name** | The Trophy Case |
| **Owner** | Gregg Schmidt |
| **Address** | 303 N Main St, Fremont, NE 68025 |
| **Phone** | (402) 721-2106 |
| **Email** | thetrophycase@qwestoffice.net |
| **Hours** | 10:00 AM - 5:30 PM Mon-Thu |
| **Google Rating** | 4.3 stars (6 reviews) |
| **Facebook** | 72 likes, 11 "were here" |
| **Website** | thetrophycasefremont.com |
| **Platform** | Wix (SSR Runtime detected) |
| **Location Context** | Fremont, NE (pop ~27k), 30 miles NW of Omaha |

## Products & Services Offered

Based on site content and catalog page:
- **Customized Trophies** (sports, corporate, general)
- **Award Medals** (various styles/finishes - gold, silver, bronze)
- **Plaques** (personalized with fonts, colors, messages)
- **Engraving Services** (laser-etching on various materials)
- **Acrylic Awards** (modern/sleek recognition awards)
- **Glass Awards** (laser-etched, elegant)
- **Corporate Awards** (branded recognition pieces)
- **Commemorative Event Awards** (graduations, anniversaries, ceremonies)

### Supplier Catalogs (linked from /catalogue page)
- Premier Crystal & Glass
- Premier Sports
- Premier Acrylic
- Premier Corporate
- 2024 JDS Components Catalog

*Note: No actual products are listed on the website. The catalog page simply links to external supplier flipbooks. There are no prices, no product images of their own work, and no way to order online.*

---

## Website Architecture

### Site Map

```
thetrophycasefremont.com/
├── / (Homepage)
├── /fremont-ne/award-medals
├── /fremont-ne/engraving
├── /fremont-ne/plaques
├── /catalogue
├── /reviews (EMPTY - no content)
├── /#SERVICES (anchor)
├── /#CONTACT (anchor)
└── /#FAQ (anchor)
```

**Total pages: 6** (including 1 empty reviews page)

### Navigation Structure
- HOME
- SERVICES (dropdown)
  - Customized Trophies (links to /#SERVICES anchor)
  - Award Medals (/fremont-ne/award-medals)
  - Engraving (/fremont-ne/engraving)
  - Plaques (/fremont-ne/plaques)
- CATALOG
- CONTACT (links to /#CONTACT anchor)
- FAQ (links to /#FAQ anchor)
- CALL US button (tel: link)

### Title Tags by Page

| Page | Title Tag |
|---|---|
| Homepage | Customized Trophies \| Fremont, NE \| 402-721-2106 |
| Award Medals | Award Medals \| Fremont, NE \| 402-721-2106 |
| Engraving | Engraving \| Fremont, NE \| 402-721-2106 |
| Plaques | Plaques \| Fremont, NE \| 402-721-2106 |
| Catalog | (not captured - links to supplier flipbooks) |
| Reviews | Customized Trophies \| Fremont, NE \| 402-721-2106 (same as homepage!) |

---

## Critical Issues Found

### 1. Massive Duplicate Content (SEVERE)
The three service pages (/award-medals, /engraving, /plaques) contain **nearly identical content**. The middle ~80% of each page is copy-pasted word-for-word. The only differences are:
- The hero section heading/intro paragraph (unique per page)
- The "Why is The Trophy Case so popular" section at the bottom (tailored per page)

Everything else - the product gallery section, award medals section, commemorative events section, plaques section, engraving section, acrylic awards section, "Craftsmanship Beyond Your Expectations" section, customized trophies section, "Why The Trophy Case Is Your Best Choice" section, FAQ, and contact form - is **identical across all three pages and the homepage**.

This is a textbook duplicate content problem that severely hurts SEO.

### 2. Placeholder Content Not Filled In (SEVERE)
Every page contains multiple image carousels with placeholder text that was never replaced:
```
"Slide title"
"Write your caption here"
"Button"
```
The homepage has 3 carousel placeholders. The service pages each have 3 sets of carousel placeholders (totaling ~15+ unfilled carousels across the site). This looks extremely unprofessional and signals to both users and search engines that the site is unfinished.

### 3. Template Error - Wrong City (MODERATE)
The homepage contains a reference to "The Woodlands" which is a city in Texas. This is a Wix template artifact that was never corrected, suggesting the site was built from a template for a different business and not properly customized.

### 4. Reviews Page Is Empty (MODERATE)
The /reviews page exists in the navigation but contains zero review content - just the header, footer, a logo, and a map widget. This is a dead-end page that wastes a potential SEO opportunity.

### 5. No Product Images or Pricing (MODERATE)
The site contains no photos of actual products or completed work. All images appear to be stock photos. There is no pricing information of any kind. The catalog page links to external supplier PDFs rather than showing actual products.

### 6. Mismatched Section Headers (MINOR)
The "Engraving Services" section on every page has a description that talks about glass awards rather than engraving: "Our glass awards combine elegance and sophistication..." This is likely another copy-paste error.

### 7. FAQ Links to External Directories (MINOR)
The FAQ answers (on homepage) contain outbound links to Yelp, Yellow Pages, BBB, Foursquare, and Facebook search pages. This is an outdated SEO tactic that provides poor user experience and bleeds link equity.

---

## SEO Baseline Performance

### Organic Keyword Rankings

| Keyword | Position | Search Volume | CPC | Competition |
|---|---|---|---|---|
| the trophy case | 21 | 590/mo | $0.73 | LOW |
| northeast trophies | 40 | 320/mo | - | - |
| trophy shop omaha | 97 | 110/mo | - | HIGH |
| trophy shop lincoln ne | 115 | 20/mo | - | - |
| accolades laser engraving | 108 | 50/mo | - | - |

**Total organic keywords: 5**
**Keywords in top 10: 0**
**Keywords in top 20: 0**
**Keywords in top 40: 1** ("the trophy case" at #21)

### Traffic Estimates
- **Estimated organic traffic**: ~0.8 visits/month (essentially ZERO)
- **Estimated traffic value**: $3.27/month
- **Domain authority/rank**: Minimal (no significant backlink profile)

### Ranking Distribution
| Position Range | # Keywords |
|---|---|
| 1-10 | 0 |
| 11-20 | 0 |
| 21-30 | 1 |
| 31-40 | 0 |
| 41-50 | 1 |
| 51-80 | 0 |
| 81-100 | 2 |
| 100+ | 1 |

### SERP Presence for Branded Search
For "the trophy case fremont ne":
- **Position #1** in organic results (branded search)
- Google Knowledge Panel present: "Trophy shop in Fremont, Nebraska"
- Listed on: Yelp, MapQuest, Yellow Pages, CMac, Fremont Tribune, D&B, Historic Downtown Fremont

---

## Digital Presence Audit

### What Exists
- Wix website (analyzed above)
- Google Business Profile (Knowledge Panel shows up)
- Facebook page (72 likes, minimal activity)
- Directory listings (Yelp, Yellow Pages, MapQuest, D&B, etc.)

### What's Missing
- No Google Business Profile optimization strategy
- No social media strategy (Facebook barely used)
- No Instagram (visual platform ideal for showcasing trophy/award work)
- No Google reviews strategy (only 6 reviews at 4.3 stars)
- No blog or content marketing
- No email marketing
- No schema markup / structured data on website
- No sitemap optimization
- No local SEO strategy beyond basic directory listings

---

## Key Takeaways for Proposal

1. **The current site is effectively invisible online.** With ~0.8 organic visits/month and zero keywords in the top 20, the website generates virtually no business from search.

2. **The Wix site is template-based and poorly executed.** Duplicate content across every page, unfilled placeholder carousels, wrong city name, and an empty reviews page indicate a low-quality build that was never properly finished.

3. **There is massive upside potential.** Starting from near-zero means any competently built and SEO-optimized site will show dramatic percentage improvements. The competition in a 27k-population market 30 miles from Omaha is likely moderate.

4. **The business has real products and services** but the website completely fails to showcase them. No product photos, no pricing, no portfolio of completed work, and no online ordering capability.

5. **Local SEO is the primary opportunity** for the lead-generation option (Option 1). Capturing searches for "trophy shop near me," "custom trophies fremont ne," "engraving services omaha area," etc. represents the most immediate traffic opportunity.

6. **National e-commerce for medals/plaques** (Option 2) requires separate analysis of search volume and competition for those specific product categories. The catalog page already shows supplier relationships (Premier, JDS) that could support e-commerce inventory.

---

*Phase 1 Complete - Ready for validation before proceeding to Phase 2: Keyword Research & Search Landscape Discovery*
