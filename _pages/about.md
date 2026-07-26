---
layout: home
title: Home
permalink: /
description: The Jeong Lab studies genome structure and epigenetic regulation across evolution, aging, and neurological disease.
_styles: |
  .lab-home {
    --home-accent: #806986;
    --home-accent-dark: #5d4c66;
    --home-paper-bg: #eeece7;
    --home-wide: min(1120px, calc(100vw - 2rem));
    padding-bottom: 2.5rem;
  }
  .home-wide {
    width: var(--home-wide);
    margin-left: 50%;
    transform: translateX(-50%);
  }
  .home-hero {
    position: relative;
    aspect-ratio: 3 / 1;
    overflow: hidden;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.28rem;
    background-color: #f4f2ed;
    background-image: url("/assets/img/home/jeong-lab-layered-primates-v8-featureless.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    box-shadow: 0 0.55rem 1.8rem rgba(49, 45, 70, 0.08);
  }
  .home-hero::after {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to right,
      rgba(244, 242, 237, 0.82) 0%,
      rgba(244, 242, 237, 0.34) 31%,
      rgba(244, 242, 237, 0) 50%
    );
    content: "";
    pointer-events: none;
  }
  .home-hero-copy {
    position: absolute;
    z-index: 1;
    top: 50%;
    left: clamp(1.4rem, 5vw, 4.25rem);
    color: #3f3a46;
    text-align: left;
    transform: translateY(-50%);
  }
  .home-hero-title {
    margin: 0;
    color: #34313a;
    font-size: clamp(1.15rem, 2.25vw, 2rem);
    font-weight: 720;
    letter-spacing: 0.025em;
    line-height: 1.08;
    text-transform: uppercase;
  }
  .home-hero-title span {
    display: block;
    white-space: nowrap;
  }
  .home-intro {
    max-width: 57rem;
    margin: clamp(2.8rem, 6vw, 5rem) auto;
  }
  .home-intro p {
    color: var(--global-text-color);
    font-size: clamp(1.03rem, 1.5vw, 1.16rem);
    line-height: 1.78;
    margin-bottom: 0;
  }
  .home-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-top: 1.7rem;
  }
  .home-action {
    display: inline-flex;
    align-items: center;
    min-height: 2.75rem;
    border: 1px solid var(--home-accent-dark);
    border-radius: 0.15rem;
    padding: 0.65rem 1rem;
    font-size: 0.92rem;
    font-weight: 650;
    transition: background-color 0.15s ease, color 0.15s ease;
  }
  .home-action:hover,
  .home-action:focus {
    text-decoration: none;
  }
  .home-action-primary {
    color: #fff;
    background: var(--home-accent-dark);
  }
  .home-action-primary:hover,
  .home-action-primary:focus {
    color: #fff;
    background: #494257;
  }
  .home-action-secondary {
    color: var(--home-accent-dark);
    background: transparent;
  }
  .home-action-secondary:hover,
  .home-action-secondary:focus {
    color: #fff;
    background: var(--home-accent-dark);
  }
  .recent-news,
  .featured-publications {
    border-top: 1px solid var(--global-divider-color);
    padding-top: 2.1rem;
  }
  .recent-news {
    margin-bottom: clamp(3rem, 6vw, 4.8rem);
  }
  .home-section-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.35rem;
  }
  .home-section-header h2 {
    font-size: clamp(1.55rem, 3vw, 2.05rem);
    font-weight: 600;
    letter-spacing: -0.025em;
    margin: 0;
  }
  .home-section-link {
    color: var(--home-accent-dark);
    font-size: 0.9rem;
    font-weight: 650;
    white-space: nowrap;
  }
  .home-news-list {
    border-top: 1px solid var(--global-divider-color);
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .home-news-item {
    display: grid;
    grid-template-columns: minmax(7.7rem, 0.22fr) 1fr;
    gap: clamp(1rem, 3vw, 2.5rem);
    border-bottom: 1px solid var(--global-divider-color);
    padding: 0.92rem 0;
  }
  .home-news-date {
    color: var(--global-text-color-light);
    font-size: 0.78rem;
    font-weight: 620;
    letter-spacing: 0.055em;
    text-transform: uppercase;
  }
  .home-news-copy {
    color: var(--global-text-color);
    font-size: 0.96rem;
    line-height: 1.5;
  }
  .featured-paper-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
  .featured-paper {
    display: flex;
    flex-direction: column;
    min-width: 0;
    overflow: hidden;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.15rem;
    color: var(--global-text-color);
    background: var(--global-card-bg-color);
    transition: border-color 0.15s ease, transform 0.15s ease;
  }
  .featured-paper:hover,
  .featured-paper:focus {
    border-color: var(--home-accent);
    color: var(--global-text-color);
    text-decoration: none;
    transform: translateY(-2px);
  }
  .featured-paper-figure {
    height: 12rem;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-bottom: 1px solid var(--global-divider-color);
    background: #fff;
  }
  .featured-paper-figure img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
  }
  .featured-paper-body {
    display: flex;
    flex: 1;
    flex-direction: column;
    padding: 1.1rem 1.15rem 1.2rem;
  }
  .featured-paper-meta {
    color: var(--home-accent-dark);
    font-size: 0.72rem;
    font-weight: 750;
    letter-spacing: 0.075em;
    margin-bottom: 0.65rem;
    text-transform: uppercase;
  }
  .featured-paper h3 {
    font-size: 1.05rem;
    font-weight: 650;
    line-height: 1.35;
    margin: 0 0 0.65rem;
  }
  .featured-paper p {
    color: var(--global-text-color-light);
    font-size: 0.88rem;
    line-height: 1.55;
    margin: 0;
  }
  .featured-paper-journal {
    margin-top: auto;
    padding-top: 1rem;
    color: var(--global-text-color);
    font-size: 0.82rem;
    font-weight: 600;
  }
  html[data-theme="dark"] .lab-home {
    --home-accent: #b29cb6;
    --home-accent-dark: #b29cb6;
    --home-paper-bg: #202224;
  }
  html[data-theme="dark"] .featured-paper-figure img {
    mix-blend-mode: normal;
  }
  html[data-theme="dark"] .home-action-primary,
  html[data-theme="dark"] .home-action-secondary:hover,
  html[data-theme="dark"] .home-action-secondary:focus {
    color: #1d2426;
    background: var(--home-accent);
  }
  @media (max-width: 900px) {
    .featured-paper-grid {
      grid-template-columns: 1fr 1fr;
    }
    .featured-paper:last-child {
      grid-column: 1 / -1;
      display: grid;
      grid-template-columns: minmax(15rem, 0.9fr) 1.1fr;
    }
    .featured-paper:last-child .featured-paper-figure {
      height: 100%;
      min-height: 13rem;
      border-right: 1px solid var(--global-divider-color);
      border-bottom: 0;
    }
  }
  @media (max-width: 620px) {
    .lab-home {
      --home-wide: calc(100vw - 1.25rem);
    }
    .home-hero {
      aspect-ratio: 2 / 1;
      background-position: 55% center;
    }
    .home-hero-copy {
      left: 0.8rem;
      width: 43%;
    }
    .home-hero-title {
      font-size: clamp(0.6rem, 2.9vw, 0.72rem);
      letter-spacing: 0.012em;
      line-height: 1.12;
    }
    .home-section-header {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.35rem;
    }
    .home-news-item {
      grid-template-columns: 1fr;
      gap: 0.25rem;
      padding: 0.85rem 0;
    }
    .featured-paper-grid {
      grid-template-columns: 1fr;
    }
    .featured-paper:last-child {
      display: flex;
      grid-column: auto;
    }
    .featured-paper:last-child .featured-paper-figure {
      height: 12rem;
      min-height: 0;
      border-right: 0;
      border-bottom: 1px solid var(--global-divider-color);
    }
  }
---

<section class="home-hero home-wide" aria-label="Jeong Lab research identity">
  <div class="home-hero-copy">
    <h1 class="home-hero-title">
      <span>Computational Genomics</span>
      <span>Evolutionary Medicine</span>
    </h1>
  </div>
</section>

<section class="home-intro" aria-label="About the Jeong Lab">
  <p>
    At the Jeong Lab, we examine genome structure and epigenetic regulation across species and cell types to better understand human evolution, aging, and neurological disorders. We combine comparative genomics with long-read sequencing and single-cell multi-omics data to resolve complex genomic regions and characterize their regulatory activity. We develop computational models to identify complex patterns and infer how genomic and epigenomic variation influences gene regulation.
  </p>
  <div class="home-actions">
    <a class="home-action home-action-primary" href="{{ '/research/' | relative_url }}">Explore Our Research</a>
    <a class="home-action home-action-secondary" href="{{ '/join/' | relative_url }}">Join the Lab</a>
  </div>
</section>

<section class="recent-news home-wide" aria-labelledby="recent-news-title">
  <div class="home-section-header">
    <h2 id="recent-news-title">Recent News</h2>
    <a class="home-section-link" href="{{ '/news/' | relative_url }}">View all news →</a>
  </div>

  <ol class="home-news-list">
    {% assign recent_news = site.news | sort: 'date' | reverse %}
    {% for item in recent_news limit: 6 %}
      <li class="home-news-item">
        <time class="home-news-date" datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: '%m/%d/%Y' }}</time>
        <div class="home-news-copy">{{ item.content | strip_html | strip }}</div>
      </li>
    {% endfor %}
  </ol>
</section>

<section class="featured-publications home-wide" aria-labelledby="featured-publications-title">
  <div class="home-section-header">
    <h2 id="featured-publications-title">Featured Publications</h2>
    <a class="home-section-link" href="{{ '/publications/' | relative_url }}">View all publications →</a>
  </div>

  <div class="featured-paper-grid">
    <a class="featured-paper" href="https://doi.org/10.1038/s41588-024-02051-8">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2025-natgen-fig1-card.png' | relative_url }}"
          alt="Figure 1 pangenome representation of human segmental duplications"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">Genome Structure · 2025</div>
        <h3>Structural polymorphism and diversity of human segmental duplications</h3>
        <p>Long-read assemblies reveal population-scale diversity in duplicated regions that have been difficult to resolve at sequence level.</p>
        <div class="featured-paper-journal">Nature Genetics</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1038/s41467-021-21917-7">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2021-natcomms-fig1-card.png' | relative_url }}"
          alt="Figure 1 comparison of CG and CH methylation across human and non-human primate brain cell types"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">Brain Evolution · 2021</div>
        <h3>Evolution of DNA methylation in the human brain</h3>
        <p>Cell type-resolved methylomes identify human-lineage regulatory changes and their relationship to neuropsychiatric disease risk.</p>
        <div class="featured-paper-journal">Nature Communications</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1007/s11357-024-01450-3">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2025-geroscience-fig1-card.png' | relative_url }}"
          alt="Figure 1 variation of DNA methylation in neurons and oligodendrocytes across age"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">Epigenetic Aging · 2025</div>
        <h3>Human brain aging is associated with dysregulation of cell type epigenetic identity</h3>
        <p>Age-associated DNA methylation changes connect declining cell identity with brain aging and disease vulnerability.</p>
        <div class="featured-paper-journal">GeroScience</div>
      </div>
    </a>
  </div>
</section>
