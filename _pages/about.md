---
layout: home
title: Home
permalink: /
description: The Jeong Lab at GIST studies genome evolution, complex structural diversity, and single-cell epigenetic aging and disease using pangenomes, multi-omics, and AI.
_styles: |
  .lab-home {
    --home-accent: #806986;
    --home-accent-dark: #5d4c66;
    --home-paper-bg: #eeece7;
    padding-bottom: 2.5rem;
  }
  .home-wide {
    margin-left: auto;
    margin-right: auto;
    max-width: 57rem;
    width: 100%;
  }
  .home-hero {
    position: relative;
    isolation: isolate;
    aspect-ratio: 3 / 1;
    overflow: hidden;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.28rem;
    background-color: #f4f2ed;
    box-shadow: 0 0.55rem 1.8rem rgba(49, 45, 70, 0.08);
  }
  .home-hero::before {
    position: absolute;
    z-index: 0;
    inset: 0;
    background-image: url("/assets/img/home/jeong-lab-layered-primates-v8-featureless.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    content: "";
    transform: translateX(5%);
  }
  .home-hero::after {
    position: absolute;
    z-index: 1;
    inset: 0;
    background: linear-gradient(
      to right,
      rgba(244, 242, 237, 0.88) 0%,
      rgba(244, 242, 237, 0.42) 34%,
      rgba(244, 242, 237, 0) 54%
    );
    content: "";
    pointer-events: none;
  }
  .home-hero-copy {
    position: absolute;
    z-index: 2;
    top: 50%;
    left: clamp(1.4rem, 5vw, 4.25rem);
    color: #3f3a46;
    text-align: left;
    transform: translateY(-50%);
  }
  .home-hero-eyebrow {
    margin: 0 0 0.45rem;
    color: #5d4c66;
    font-size: clamp(0.68rem, 1.05vw, 0.8rem);
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }
  .home-hero-title {
    margin: 0;
    color: #18171b;
    font-size: clamp(1.15rem, 2.25vw, 2rem);
    font-weight: 760;
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
    margin: clamp(2.6rem, 5.5vw, 4.4rem) auto clamp(2.8rem, 5.5vw, 4.4rem);
    width: 100%;
  }
  .home-intro-heading {
    color: var(--global-text-color);
    font-size: clamp(1.55rem, 3.2vw, 2.25rem);
    font-weight: 640;
    letter-spacing: -0.03em;
    line-height: 1.22;
    margin: 0 0 1.15rem;
  }
  .home-intro p {
    color: var(--global-text-color);
    font-size: clamp(1rem, 1.45vw, 1.11rem);
    line-height: 1.78;
    margin: 0 0 1rem;
  }
  .home-intro p:last-of-type {
    color: var(--global-text-color-light);
    margin-bottom: 0;
  }
  .home-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-top: 1.65rem;
  }
  .home-action {
    display: inline-flex;
    align-items: center;
    min-height: 2.75rem;
    border: 1px solid var(--home-accent-dark);
    border-radius: 0.15rem;
    padding: 0.65rem 1.05rem;
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
  .home-pillars,
  .recent-news,
  .featured-publications {
    border-top: 1px solid var(--global-divider-color);
    padding-top: 2.1rem;
  }
  .home-pillars,
  .featured-publications,
  .recent-news {
    margin-bottom: clamp(3rem, 6vw, 4.6rem);
  }
  .home-section-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.35rem;
  }
  .home-section-header h2 {
    font-size: clamp(1.5rem, 2.8vw, 1.98rem);
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
  .home-pillar-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .home-pillar-card {
    display: flex;
    flex-direction: column;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.2rem;
    padding: 1.3rem 1.35rem 1.25rem;
    background: var(--global-card-bg-color);
    color: var(--global-text-color);
    transition: border-color 0.15s ease, transform 0.15s ease;
  }
  .home-pillar-card:hover,
  .home-pillar-card:focus {
    border-color: var(--home-accent);
    color: var(--global-text-color);
    text-decoration: none;
    transform: translateY(-2px);
  }
  .home-pillar-index {
    color: var(--home-accent-dark);
    font-size: 0.74rem;
    font-weight: 750;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
  }
  .home-pillar-card h3 {
    color: var(--global-text-color);
    font-size: 1.12rem;
    font-weight: 650;
    letter-spacing: -0.015em;
    line-height: 1.32;
    margin: 0 0 0.55rem;
  }
  .home-pillar-card p {
    color: var(--global-text-color-light);
    font-size: 0.91rem;
    line-height: 1.62;
    margin: 0;
  }
  .home-pillar-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-top: auto;
    padding-top: 0.95rem;
  }
  .home-pillar-tag {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.18rem;
    padding: 0.14rem 0.46rem;
    color: var(--global-text-color-light);
    font-size: 0.76rem;
    font-weight: 560;
    line-height: 1.4;
  }
  .featured-publication-actions {
    align-items: center;
    display: flex;
    gap: 0.85rem;
  }
  .featured-carousel-shell {
    position: relative;
  }
  .featured-carousel-controls {
    inset: 0;
    pointer-events: none;
    position: absolute;
    z-index: 3;
  }
  .featured-carousel-button {
    align-items: center;
    background: var(--global-bg-color);
    border: 1px solid var(--home-accent);
    border-radius: 50%;
    box-shadow: 0 0.35rem 1.15rem rgba(49, 45, 70, 0.16);
    color: var(--home-accent-dark);
    display: flex;
    font-size: 1.65rem;
    height: 3.35rem;
    justify-content: center;
    line-height: 1;
    padding: 0;
    pointer-events: auto;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    transition:
      background-color 0.15s ease,
      border-color 0.15s ease,
      box-shadow 0.15s ease,
      color 0.15s ease,
      opacity 0.15s ease,
      transform 0.15s ease,
      visibility 0.15s ease;
    width: 3.35rem;
  }
  .featured-carousel-button[data-featured-previous] {
    left: -1.45rem;
  }
  .featured-carousel-button[data-featured-next] {
    right: -1.45rem;
  }
  .featured-carousel-button:hover,
  .featured-carousel-button:focus {
    background: var(--home-accent-dark);
    border-color: var(--home-accent-dark);
    box-shadow: 0 0.5rem 1.35rem rgba(49, 45, 70, 0.24);
    color: #fff;
    transform: translateY(-50%) scale(1.04);
  }
  .featured-carousel-button:disabled {
    cursor: default;
    opacity: 0;
    pointer-events: none;
    visibility: hidden;
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
    grid-auto-columns: calc((100% - 2rem) / 3);
    grid-auto-flow: column;
    gap: 1rem;
    overflow-x: auto;
    scroll-behavior: smooth;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
  }
  .featured-paper-grid::-webkit-scrollbar {
    display: none;
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
    scroll-snap-align: start;
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
  .home-join-callout {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.22rem;
    background: var(--global-card-bg-color);
    padding: clamp(1.35rem, 3vw, 1.9rem) clamp(1.35rem, 3.2vw, 2.1rem);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
  }
  .home-join-callout h2 {
    font-size: clamp(1.2rem, 2.2vw, 1.45rem);
    font-weight: 630;
    letter-spacing: -0.02em;
    margin: 0 0 0.4rem;
  }
  .home-join-callout p {
    color: var(--global-text-color-light);
    font-size: 0.94rem;
    line-height: 1.62;
    margin: 0;
    max-width: 40rem;
  }
  .home-join-callout .home-action {
    flex-shrink: 0;
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
      grid-auto-columns: calc((100% - 1rem) / 2);
    }
    .featured-carousel-button[data-featured-previous] {
      left: 0.55rem;
    }
    .featured-carousel-button[data-featured-next] {
      right: 0.55rem;
    }
  }
  @media (max-width: 760px) {
    .home-pillar-grid {
      grid-template-columns: 1fr;
    }
    .home-join-callout {
      flex-direction: column;
      align-items: flex-start;
    }
  }
  @media (max-width: 620px) {
    .home-hero {
      aspect-ratio: 2 / 1;
    }
    .home-hero::before {
      background-position: 50% center;
      transform: none;
    }
    .home-hero-copy {
      left: 0.8rem;
      width: 46%;
    }
    .home-hero-eyebrow {
      font-size: 0.56rem;
      margin-bottom: 0.25rem;
    }
    .home-hero-title {
      font-size: clamp(0.72rem, 3.25vw, 0.84rem);
      font-weight: 780;
      letter-spacing: 0.008em;
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
    .featured-publication-actions {
      justify-content: space-between;
      width: 100%;
    }
    .featured-paper-grid {
      grid-auto-columns: 100%;
    }
    .featured-carousel-button {
      font-size: 1.45rem;
      height: 2.9rem;
      width: 2.9rem;
    }
    .featured-carousel-button[data-featured-previous] {
      left: 0.55rem;
    }
    .featured-carousel-button[data-featured-next] {
      right: 0.55rem;
    }
  }
---

<section class="home-hero home-wide" aria-label="Jeong Lab research identity">
  <div class="home-hero-copy">
    <p class="home-hero-eyebrow">GIST / Life Sciences</p>
    <h1 class="home-hero-title">
      <span>Computational Genomics</span>
      <span>Evolutionary Medicine</span>
    </h1>
  </div>
</section>

<section class="home-intro" aria-labelledby="home-intro-heading">
  <h2 class="home-intro-heading" id="home-intro-heading">Genome Evolution, Diversity, and Cellular Aging</h2>
  <p>
    The human genome is far more dynamic than a single reference genome suggests. Across primate evolution, structural rearrangements and shifts in gene regulation shaped uniquely human brain functions, while large genomic segments continue to recombine and vary substantially across individuals today. Over a lifetime, epigenetic alterations (epimutations) also accumulate within individual cells, eroding cell identity and contributing to aging and disease.
  </p>
  <p>
    At the Jeong Lab, we integrate long-read genome assemblies and pangenomes, single-cell and 3D multi-omics, and statistical and AI modeling to understand how genomic and epigenomic variation shapes cellular states, phenotypes, and disease vulnerability.
  </p>
  <div class="home-actions">
    <a class="home-action home-action-primary" href="{{ '/research/' | relative_url }}">Explore Our Research</a>
    <a class="home-action home-action-secondary" href="{{ '/join/' | relative_url }}">Join the Lab</a>
  </div>
</section>

<section class="home-pillars home-wide" aria-labelledby="home-pillars-title">
  <div class="home-section-header">
    <h2 id="home-pillars-title">Research Directions</h2>
    <a class="home-section-link" href="{{ '/research/' | relative_url }}">Detailed overview →</a>
  </div>

  <div class="home-pillar-grid">
    <a class="home-pillar-card" href="{{ '/research/#evolution' | relative_url }}">
      <div class="home-pillar-index">01 / Evolution</div>
      <h3>Primate and Human Evolution</h3>
      <p>
        Comparing high-quality primate genome assemblies and cell-type-resolved brain epigenomes to uncover human-specific genes, regulatory changes, and evolutionary links to neuropsychiatric disease risk.
      </p>
      <div class="home-pillar-tags">
        <span class="home-pillar-tag">Comparative genomics</span>
        <span class="home-pillar-tag">Brain epigenomics</span>
        <span class="home-pillar-tag">Regulatory evolution</span>
      </div>
    </a>

    <a class="home-pillar-card" href="{{ '/research/#diversity' | relative_url }}">
      <div class="home-pillar-index">02 / Diversity</div>
      <h3>Complex Genome Architecture and Human Diversity</h3>
      <p>
        Resolving segmental duplications, large structural variation, and newly emerging duplicated genes across population-scale pangenomes that were previously inaccessible to short-read sequencing.
      </p>
      <div class="home-pillar-tags">
        <span class="home-pillar-tag">Long-read assembly</span>
        <span class="home-pillar-tag">Pangenome</span>
        <span class="home-pillar-tag">Structural variation</span>
      </div>
    </a>

    <a class="home-pillar-card" href="{{ '/research/#aging' | relative_url }}">
      <div class="home-pillar-index">03 / Aging &amp; Disease</div>
      <h3>Cellular Aging and Disease</h3>
      <p>
        Integrating single-cell DNA methylation, 3D genome architecture, and multi-omics to investigate how accumulating epimutations erode cell identity, drive failed tissue repair in disease, and remodel during cellular rejuvenation.
      </p>
      <div class="home-pillar-tags">
        <span class="home-pillar-tag">Single-cell multi-omics</span>
        <span class="home-pillar-tag">Epigenetic aging</span>
        <span class="home-pillar-tag">Tissue repair</span>
      </div>
    </a>

    <a class="home-pillar-card" href="{{ '/research/#methods' | relative_url }}">
      <div class="home-pillar-index">04 / Methods &amp; AI</div>
      <h3>Computational Methods and AI</h3>
      <p>
        Developing analytical methods for complex genome regions, statistical models for single-cell and 3D epigenome integration, and machine learning and AI models connecting multi-omics to cellular states and disease.
      </p>
      <div class="home-pillar-tags">
        <span class="home-pillar-tag">Statistical modeling</span>
        <span class="home-pillar-tag">Multi-omic ML &amp; AI</span>
        <span class="home-pillar-tag">Bioinformatics tools</span>
      </div>
    </a>
  </div>
</section>

<section class="featured-publications home-wide" aria-labelledby="featured-publications-title">
  <div class="home-section-header">
    <h2 id="featured-publications-title">Featured Publications</h2>
    <div class="featured-publication-actions">
      <a class="home-section-link" href="{{ '/publications/' | relative_url }}">View all publications →</a>
    </div>
  </div>

  <div class="featured-carousel-shell">
    <div class="featured-paper-grid" data-featured-carousel>
    <a class="featured-paper" href="https://doi.org/10.1038/s43587-026-01221-z">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2026-kidney-fig1-card.jpg' | relative_url }}"
          alt="Figure 1 single-cell DNA methylome atlas of human and mouse kidney cell types"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">2026</div>
        <h3>A cross-species single-cell kidney epigenome atlas reveals epithelial-dominant aging-like states in disease</h3>
        <p>Cross-species single-cell methylome and multi-omics maps reveal conserved epithelial aging trajectories and maladaptive repair states in kidney disease.</p>
        <div class="featured-paper-journal">Nature Aging</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1038/s41588-024-02051-8">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2025-natgen-fig1-card.png' | relative_url }}"
          alt="Figure 1 pangenome representation of human segmental duplications"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">2025</div>
        <h3>Structural polymorphism and diversity of human segmental duplications</h3>
        <p>Analysis of 170 haplotype-resolved human genome assemblies uncovers 47.4 Mb of previously uncharacterized duplicated sequence and over 200 candidate duplicated genes.</p>
        <div class="featured-paper-journal">Nature Genetics</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1038/s41586-025-08816-3">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/yoo-2025-nature-fig1-card.png' | relative_url }}"
          alt="Figure 1 chromosomal alignments across complete great ape genomes"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">2025</div>
        <h3>Complete sequencing of ape genomes</h3>
        <p>Telomere-to-telomere, haplotype-resolved reference genomes across six ape species resolve structurally divergent loci and lineage-specific gene families.</p>
        <div class="featured-paper-journal">Nature</div>
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
        <div class="featured-paper-meta">2021</div>
        <h3>Evolution of DNA methylation in the human brain</h3>
        <p>Neuron- and glia-resolved primate methylomes identify human-specific CG and CH regulatory evolution enriched for schizophrenia genetic risk.</p>
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
        <div class="featured-paper-meta">2025</div>
        <h3>Human brain aging is associated with dysregulation of cell type epigenetic identity</h3>
        <p>Cell-type-resolved brain methylomes show how progressive erosion of epigenetic cell identity links aging to neurological vulnerability.</p>
        <div class="featured-paper-journal">GeroScience</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.7554/eLife.79387">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2022-elife-fig1-card.jpg' | relative_url }}"
          alt="Figure 1 genomic differentiation associated with the white-throated sparrow supergene"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">2022</div>
        <h3>Dynamic molecular evolution of a supergene with suppressed recombination</h3>
        <p>Population genomic and allele-specific expression analyses reveal degeneration and regulatory divergence across a chromosomal inversion supergene.</p>
        <div class="featured-paper-journal">eLife</div>
      </div>
    </a>
    </div>

    <div class="featured-carousel-controls" aria-label="Featured publication navigation">
      <button
        class="featured-carousel-button"
        type="button"
        aria-label="Previous featured publications"
        data-featured-previous
      >‹</button>
      <button
        class="featured-carousel-button"
        type="button"
        aria-label="Next featured publications"
        data-featured-next
      >›</button>
    </div>

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
        <div class="home-news-copy">{{ item.content | remove: '<p>' | remove: '</p>' | strip }}</div>
      </li>
    {% endfor %}
  </ol>
</section>

<section class="home-join-callout home-wide" aria-labelledby="home-join-callout-title">
  <div>
    <h2 id="home-join-callout-title">Join the Jeong Lab at GIST</h2>
    <p>
      We welcome prospective graduate students, postdocs, and undergraduates from both biology/medicine and computer science, statistics, or AI who want to tackle challenging questions in human genomics and aging.
    </p>
  </div>
  <a class="home-action home-action-primary" href="{{ '/join/' | relative_url }}">View Open Positions</a>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('[data-featured-carousel]');
    const previousButton = document.querySelector('[data-featured-previous]');
    const nextButton = document.querySelector('[data-featured-next]');

    if (!carousel || !previousButton || !nextButton) return;

    const cards = Array.from(carousel.querySelectorAll('.featured-paper'));

    function visibleCardCount() {
      if (!cards.length) return 1;
      return Math.max(1, Math.round(carousel.clientWidth / cards[0].getBoundingClientRect().width));
    }

    function currentCardIndex() {
      if (!cards.length) return 0;
      const cardWidth = cards[0].getBoundingClientRect().width;
      const gap = parseFloat(window.getComputedStyle(carousel).columnGap) || 0;
      return Math.round(carousel.scrollLeft / (cardWidth + gap));
    }

    function updateButtons() {
      const index = currentCardIndex();
      previousButton.disabled = index <= 0;
      nextButton.disabled = index >= cards.length - visibleCardCount();
    }

    function moveCarousel(direction) {
      const target = Math.min(
        Math.max(currentCardIndex() + direction * visibleCardCount(), 0),
        Math.max(cards.length - visibleCardCount(), 0)
      );
      const cardWidth = cards[0].getBoundingClientRect().width;
      const gap = parseFloat(window.getComputedStyle(carousel).columnGap) || 0;
      carousel.scrollTo({ left: target * (cardWidth + gap), behavior: 'smooth' });
    }

    previousButton.addEventListener('click', function () {
      moveCarousel(-1);
    });
    nextButton.addEventListener('click', function () {
      moveCarousel(1);
    });
    carousel.addEventListener('scroll', updateButtons, { passive: true });
    window.addEventListener('resize', updateButtons);
    updateButtons();
  });
</script>
