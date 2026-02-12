# Phase 8: Site Architecture Design

## A. Option 1: Local Lead-Generation Website

### Technology Stack
- **Framework:** Next.js (static site generation for speed + SEO)
- **Hosting:** Vercel (free tier sufficient for local lead-gen)
- **CMS:** Markdown files or simple headless CMS (no database needed)
- **Forms:** Formspree or Netlify Forms (quote request handling)
- **Analytics:** Google Analytics 4 + Google Search Console
- **Maps:** Google Maps embed on contact/location pages

### Site Map (22-28 pages at launch)

```
thetrophycasefremont.com/
│
├── / (Homepage)
│   ├── Hero: "Fremont's Award & Trophy Experts Since [Year]"
│   ├── Services overview grid (6 categories)
│   ├── Trust signals (years in business, review stars, local badge)
│   ├── Featured work gallery (6-8 photos)
│   ├── CTA: Request a Quote / Call Now
│   └── Google Reviews widget
│
├── /services/
│   ├── /services/custom-trophies
│   ├── /services/award-medals
│   ├── /services/plaques
│   ├── /services/engraving
│   ├── /services/acrylic-awards
│   ├── /services/glass-awards
│   └── /services/corporate-awards
│
├── /gallery/
│   ├── Portfolio of completed work (photos)
│   └── Organized by category
│
├── /about/
│   ├── Gregg's story + expertise
│   ├── Shop history
│   └── Community involvement
│
├── /areas-served/
│   ├── /areas-served/fremont-ne
│   ├── /areas-served/omaha-ne
│   ├── /areas-served/wahoo-ne
│   ├── /areas-served/blair-ne
│   └── /areas-served/dodge-county
│
├── /contact/
│   ├── Address, phone, hours, map
│   ├── Quote request form
│   └── Driving directions from Omaha
│
├── /reviews/
│   └── Customer testimonials + Google review feed
│
├── /blog/ (launch with 3-5 posts, add 2/month)
│   ├── /blog/how-to-choose-sports-trophies
│   ├── /blog/corporate-award-ideas
│   ├── /blog/custom-engraving-guide
│   └── (additional posts over time)
│
├── /faq/
├── /privacy-policy/
└── /sitemap.xml
```

### Key Page Templates

#### Service Page Template
Each of the 7 service pages follows this structure:
1. **H1:** "[Service Type] in Fremont & Omaha, NE"
2. **Hero image:** Real photo of that product type
3. **Service description:** 200-400 words, unique per page
4. **Product options/materials:** What they can customize
5. **Pricing indicator:** "Starting from $XX" or "Request a quote for custom pricing"
6. **Photo gallery:** 4-8 images of completed work in this category
7. **FAQ section:** 3-5 questions specific to that service
8. **CTA:** "Request a Free Quote" form + phone number
9. **Schema markup:** LocalBusiness + Service schema

#### Area-Served Page Template
Each location page targets "[service] + [city]" keywords:
1. **H1:** "Trophies & Awards in [City], NE"
2. **Content:** 300-500 words about serving that area
3. **Distance/directions from that city to Fremont shop
4. **Embedded Google Map centered on that city
5. **Local testimonials from that area (if available)
6. **Schema markup:** LocalBusiness with service area

### Technical SEO Requirements
- Server-side rendered (Next.js SSG) for fast page loads
- Schema markup: LocalBusiness, Service, FAQ, Review, BreadcrumbList
- Open Graph + Twitter Card meta tags on every page
- XML sitemap auto-generated
- Robots.txt allowing full crawl
- Canonical tags on all pages
- Mobile-first responsive design
- Core Web Vitals targets: LCP <2.5s, FID <100ms, CLS <0.1
- Image optimization with next/image (WebP, lazy loading)
- Internal linking strategy: every service page links to related services + contact

---

## B. Option 2: Hybrid (Lead-Gen + Shopify E-Commerce)

### Technology Stack
- **Lead-gen site:** Next.js on Vercel (same as Option 1)
- **E-commerce:** Shopify (validated by Trophy Depot and K2 Awards)
- **Product customizer:** Zakeke (visual product designer integration)
- **Domain strategy:**
  - `thetrophycasefremont.com` → Lead-gen site (local SEO)
  - `shop.thetrophycasefremont.com` OR `/shop/` path → Shopify store (e-commerce)
- **Analytics:** GA4 across both properties with cross-domain tracking
- **Email:** Shopify Email or Klaviyo for e-commerce marketing
- **Reviews:** Shopify Reviews + Google Reviews integration

### Site Map - Lead-Gen Component
Same as Option 1, with these additions:
```
├── / (Homepage)
│   └── Added: "Shop Online" CTA linking to Shopify store
│
├── /services/ (same 7 pages)
│   └── Each page adds: "Order Online" links for products available in shop
│
└── Shop link in main navigation → Shopify store
```

### Site Map - Shopify E-Commerce Component

```
shop.thetrophycasefremont.com/  (or /shop/ subdirectory)
│
├── / (Store Homepage)
│   ├── Hero: "Custom Awards, Shipped Nationwide"
│   ├── Featured collections
│   ├── "Design Your Own" CTA (Zakeke)
│   └── Trust badges (free engraving, satisfaction guarantee)
│
├── /collections/
│   ├── /collections/medals
│   │   ├── /collections/medals-gold
│   │   ├── /collections/medals-silver
│   │   ├── /collections/medals-bronze
│   │   ├── /collections/medals-custom
│   │   ├── /collections/medals-running
│   │   ├── /collections/medals-swimming
│   │   ├── /collections/medals-soccer
│   │   ├── /collections/medals-basketball
│   │   ├── /collections/medals-baseball
│   │   └── /collections/medals-academic
│   │
│   ├── /collections/plaques
│   │   ├── /collections/plaques-wood
│   │   ├── /collections/plaques-acrylic
│   │   ├── /collections/plaques-glass
│   │   ├── /collections/plaques-metal
│   │   ├── /collections/plaques-photo
│   │   ├── /collections/plaques-corporate
│   │   └── /collections/plaques-retirement
│   │
│   ├── /collections/trophies
│   │   ├── /collections/trophies-sports
│   │   ├── /collections/trophies-corporate
│   │   └── /collections/trophies-custom
│   │
│   └── /collections/all
│
├── /products/ (individual product pages with Zakeke integration)
│   ├── Each product has: photos, pricing, description, Zakeke customizer
│   └── Target: 50-100 products at launch, growing to 200+
│
├── /pages/
│   ├── /pages/about
│   ├── /pages/free-engraving
│   ├── /pages/shipping-info
│   ├── /pages/bulk-orders
│   ├── /pages/design-guide
│   └── /pages/faq
│
├── /blogs/
│   ├── /blogs/award-ideas
│   ├── /blogs/customization-tips
│   └── (SEO-driven content)
│
├── /cart
├── /checkout (guest + account options)
└── /account
```

### Shopify Theme Requirements
- Clean, professional theme (Dawn or similar free theme as base)
- Mega-menu for collections navigation
- Quick-view product modals
- Zakeke "Customize" button on product pages
- Guest checkout enabled
- Mobile-optimized with bottom-sticky "Add to Cart"
- Product filtering by sport, material, price range, color
- Live inventory indicators
- Related products / "Customers also bought" sections

### Zakeke Integration Points
1. **Product page "Design Your Own" button** → Opens Zakeke visual editor
2. **Real-time preview** of engraving text, logos, colors on the product
3. **Template library** for common use cases (sports awards, corporate recognition)
4. **File upload** for custom artwork/logos
5. **Save & share designs** for team/committee approval before ordering

### Collection Page SEO Strategy
Each collection page targets a specific keyword cluster:

| Collection | Primary Keyword Target | Monthly Volume |
|---|---|---|
| /collections/medals | custom medals | 4,400 |
| /collections/medals-running | custom running medals | 210 |
| /collections/plaques | custom plaques | 6,600 |
| /collections/plaques-wood | custom wood plaques | 720 |
| /collections/plaques-acrylic | custom acrylic plaques | 480 |
| /collections/plaques-corporate | custom award plaques | 1,900 |

**Target: 50+ optimized collection/product pages at launch to begin ranking for long-tail terms immediately.**

---

## C. Domain & URL Strategy

### Recommended Approach

**Option 1:** `thetrophycasefremont.com` (keep existing domain)
- Redirect all existing Wix URLs to new page equivalents
- Set up proper 301 redirects to preserve any minimal existing authority

**Option 2:** Two options for e-commerce integration:

| Approach | Pros | Cons |
|---|---|---|
| **Subdomain:** `shop.thetrophycasefremont.com` | Easy to set up; clear separation | Google treats as separate domain; slower SEO |
| **Subfolder:** `thetrophycasefremont.com/shop/` | Shares domain authority; better SEO | More complex to configure with Shopify |

**Recommendation: Subfolder approach** (`/shop/`) using Shopify's custom domain routing. This consolidates all SEO authority under one domain and is the approach used by most successful hybrid sites.

---

## D. Information Architecture Principles

1. **Every page targets a specific keyword cluster.** No orphan pages, no duplicate content.
2. **Maximum 3 clicks from homepage to any page.** Flat hierarchy for crawlability.
3. **Internal linking connects related services and products.** Service pages link to shop products; shop products link to service pages.
4. **Schema markup on every page.** LocalBusiness, Product, FAQ, BreadcrumbList, Review as appropriate.
5. **Mobile-first design.** 60%+ of local searches happen on mobile.

---

## E. Key Findings for Proposal

1. **Option 1 requires ~22-28 pages at launch** - achievable in a standard website build timeline of 4-6 weeks.

2. **Option 2 requires ~80-120 pages at launch** (lead-gen site + 50-100 Shopify products/collections) - requires 8-12 weeks build time.

3. **The subfolder approach for Shopify integration** (`/shop/`) is recommended over a subdomain for maximum SEO benefit.

4. **Zakeke integrates directly into Shopify product pages** - no custom development needed, just theme configuration and product setup.

5. **Area-served pages are a high-value, low-effort local SEO tactic.** Five pages targeting nearby cities can capture uncontested geographic keywords.

6. **Content architecture follows the hub-and-spoke model:** Homepage → Service category pages → Individual product/service pages, with cross-linking throughout.

---

*Phase 8 Complete - Saved to research/phase-8-site-architecture.md*
