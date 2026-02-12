# Phase 9: Technology Research — Shopify + Zakeke

## A. Shopify Platform Assessment

### Why Shopify (Validated by Competitors)
- **Trophy Depot** (19,578/mo traffic, $83K traffic value) runs on Shopify
- **K2 Awards** (88,644/mo traffic) runs on Shopify
- Both are the most successful e-commerce trophy businesses analyzed in Phase 4
- Shopify handles payments, inventory, shipping, tax — no custom development needed

### Recommended Plan: Shopify Basic ($39/mo)

| Plan | Monthly Cost | Online Rate | In-Person Rate | 3rd-Party Fee | Staff Accounts |
|---|---|---|---|---|---|
| **Basic** | $39/mo | 2.9% + 30¢ | 2.6% + 10¢ | 2% | 2 |
| Grow | $79/mo | 2.7% + 30¢ | 2.5% + 10¢ | 1% | 5 |
| Advanced | $299/mo | 2.5% + 30¢ | 2.4% + 10¢ | 0.6% | 15 |

**Basic is sufficient for launch.** At projected Year 1 e-commerce revenue of $8K-$28K, the lower transaction fees of higher tiers don't justify the cost. Upgrade to Grow when monthly e-commerce revenue consistently exceeds ~$4,000/mo (the savings on transaction fees offset the plan cost difference).

### Key Shopify Features for The Trophy Case
1. **Guest checkout** — Critical for conversion (validated by Trophy Depot analysis)
2. **Free Shopify theme (Dawn)** — Clean, fast, mobile-responsive base theme
3. **Built-in shipping calculator** — Handles rate calculation for medal/plaque shipments
4. **Discount codes** — Enable "free engraving" and promotional pricing
5. **Inventory management** — Track stock across product variants
6. **Shopify Email** — Basic email marketing included (up to 10K emails/mo free)
7. **Shopify Analytics** — Built-in conversion tracking and sales reports
8. **App ecosystem** — 8,000+ apps for extending functionality

### Shopify Annual Cost Projection

| Item | Monthly | Annual |
|---|---|---|
| Shopify Basic plan | $39 | $468 |
| Transaction fees (on $15K revenue) | ~$60 | ~$720 |
| **Total Year 1** | | **~$1,188** |

---

## B. Zakeke Product Customizer

### What Zakeke Does
Zakeke is a visual product customization platform that integrates directly into Shopify product pages. Customers can:
- Add custom text/engraving to products with real-time preview
- Upload logos and artwork
- Choose colors, fonts, and layouts
- View 3D/AR previews of their customized product
- Save and share designs for approval before ordering

### Why Zakeke (Competitive Advantage)
From Phase 4 analysis:
- **Trophy Depot** has NO visual product designer — customers order blind
- **Crown Trophy** has NO real-time customization preview
- **K2 Awards** has a basic "Design Online" tool but not as feature-rich
- **Zakeke integration gives The Trophy Case a genuine competitive edge** that no mid-tier competitor offers

### Zakeke Pricing

| Plan | Monthly | Annual (30% off) | Products | Views/mo | Features |
|---|---|---|---|---|---|
| **Starter** | $19/mo | ~$160/yr | 50 products | 1,000 | 2D/3D config, AR viewer |
| **Grow** | $49/mo | ~$412/yr | 100 products | 2,500 | + Priority support |
| Scale | $99/mo | ~$832/yr | Unlimited | 10,000 | + API access, white label |

**Additional fee:** 1.7-1.9% transaction fee on customized product sales (varies by plan).

**Recommendation: Start with Starter ($19/mo).** 50 products is sufficient for launch. Upgrade to Grow when approaching 50 published customizable products or 1,000 views/month.

### Zakeke Integration Points (for Shopify)
1. **Install from Shopify App Store** — No custom development needed
2. **"Customize" button** appears on enabled product pages
3. **Real-time preview** renders text, logos, colors on the product image
4. **Template library** — Pre-built layouts for common use cases (awards, plaques, medals)
5. **File upload** — Customers upload custom artwork/logos
6. **Save & share** — Teams/committees can review designs before ordering
7. **14-day free trial** — Test before committing

### Zakeke Annual Cost Projection

| Item | Monthly | Annual |
|---|---|---|
| Zakeke Starter plan | $19 | $228 |
| Transaction fees (on $10K customized revenue) | ~$180 | ~$180 |
| **Total Year 1** | | **~$408** |

---

## C. Next.js Lead-Gen Site (Option 1 & 2)

### Technology Stack
| Component | Technology | Cost |
|---|---|---|
| Framework | Next.js 14+ (App Router, SSG) | Free |
| Hosting | Vercel (Hobby/Pro) | Free-$20/mo |
| Domain | thetrophycasefremont.com (existing) | ~$15/yr |
| Forms | Formspree (free tier: 50 submissions/mo) | Free |
| Analytics | Google Analytics 4 + Search Console | Free |
| Maps | Google Maps embed | Free |
| Images | Next.js Image component (auto WebP/AVIF) | Free |
| CMS | Markdown files in repo | Free |

### Key Technical Decisions
1. **Static Site Generation (SSG)** — All pages pre-rendered at build time for maximum speed and SEO
2. **No database needed** — Content managed as markdown files; forms handled by Formspree
3. **Vercel hosting** — Free tier handles ~100K requests/month (far exceeds projected traffic)
4. **Schema markup** — JSON-LD for LocalBusiness, Service, FAQ, Review, BreadcrumbList
5. **Responsive design** — Mobile-first; Tailwind CSS for utility-first styling

### Estimated Monthly Hosting Cost: $0-$20/mo
Vercel's free tier is sufficient for projected traffic levels (270-1,840 visits/mo by Month 24). Pro tier ($20/mo) only needed if team collaboration features are required.

---

## D. Integration Architecture (Option 2)

### Two Approaches for Shopify + Next.js

| Approach | How It Works | Pros | Cons |
|---|---|---|---|
| **Subdomain** (`shop.thetrophycasefremont.com`) | Shopify hosted separately on subdomain | Easy setup; clear separation | Google treats as separate site; split SEO authority |
| **Subfolder** (`/shop/`) via Vercel rewrites | Vercel reverse-proxies `/shop/*` to Shopify | Consolidated SEO authority; one domain | More complex config; potential caching issues |

**Recommendation: Start with subdomain approach.** While subfolder is better for SEO long-term, the subdomain approach is simpler to implement and maintain. The SEO difference is marginal at the traffic levels projected for Year 1-2. Can migrate to subfolder later if needed.

### Simplified Architecture

```
thetrophycasefremont.com (Vercel/Next.js)
├── / → Homepage
├── /services/* → Service pages
├── /about → About page
├── /contact → Contact page
├── /gallery → Portfolio
├── /blog/* → Blog posts
└── /shop → Link to shop.thetrophycasefremont.com

shop.thetrophycasefremont.com (Shopify)
├── / → Store homepage
├── /collections/* → Product collections
├── /products/* → Individual products (with Zakeke)
└── /cart, /checkout → Purchase flow
```

### Cross-Site Linking Strategy
- Every Next.js service page links to relevant Shopify collections
- Shopify store links back to Next.js for local services, about, contact
- Shared navigation header/footer styling for visual consistency
- GA4 cross-domain tracking configured for unified analytics

---

## E. Total Technology Cost Summary

### Option 1: Lead-Gen Only

| Item | Monthly | Annual |
|---|---|---|
| Vercel hosting | $0 | $0 |
| Domain renewal | — | $15 |
| Formspree (free tier) | $0 | $0 |
| **Total** | **$0** | **$15** |

### Option 2: Lead-Gen + E-Commerce

| Item | Monthly | Annual |
|---|---|---|
| Vercel hosting | $0 | $0 |
| Domain renewal | — | $15 |
| Shopify Basic | $39 | $468 |
| Zakeke Starter | $19 | $228 |
| Formspree (free tier) | $0 | $0 |
| **Total** | **$58** | **$711** |

### Cost vs Revenue (Option 2)

| Period | Platform Costs | Projected Revenue | Net |
|---|---|---|---|
| Year 1 | ~$711 | $8,000-$28,000 | +$7,289-$27,289 |
| Year 2 | ~$711 | $50,000-$180,000 | +$49,289-$179,289 |

**Platform costs are less than 1-9% of projected revenue.** Shopify + Zakeke pay for themselves within the first 1-2 months of e-commerce sales.

---

## F. Key Findings for Proposal

1. **Shopify Basic ($39/mo) is the right starting plan.** Validated by Trophy Depot and K2 Awards. Upgrade when revenue justifies it.

2. **Zakeke Starter ($19/mo) provides a genuine competitive advantage** that no mid-tier competitor offers. Real-time visual customization is the single biggest UX differentiator available.

3. **Total platform costs for Option 2 are ~$58/mo ($711/yr)** — trivial relative to projected revenue.

4. **Subdomain approach recommended for simplicity** at launch. The SEO impact is minimal at early traffic levels and can be migrated later.

5. **Next.js + Vercel for the lead-gen site is essentially free** and provides best-in-class performance for SEO.

6. **No custom development needed for Zakeke** — it's a Shopify App Store install with configuration, not code.

---

*Phase 9 Complete - Saved to research/phase-9-technology-research.md*
