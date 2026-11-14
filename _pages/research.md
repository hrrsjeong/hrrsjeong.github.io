---
layout: page
permalink: /research/
title: Research
display_title: Research
description: Research directions in primate and human evolution, pangenome structural diversity, single-cell epigenetic aging, and computational and AI methods at the Jeong Lab.
nav: true
nav_order: 2
_styles: |
  .research-page {
    --research-accent: #725c78;
    --research-accent-soft: rgba(114, 92, 120, 0.08);
    padding-bottom: 2.5rem;
  }
  html[data-theme="dark"] .research-page {
    --research-accent: #b29cb6;
    --research-accent-soft: rgba(178, 156, 182, 0.12);
  }
  footer.fixed-bottom {
    position: static !important;
  }
  .research-wide {
    margin-left: auto;
    margin-right: auto;
    max-width: 55rem;
    width: 100%;
  }
  .research-intro {
    margin: 0.35rem auto clamp(2.2rem, 4.5vw, 3.2rem);
    max-width: 55rem;
    width: 100%;
  }
  .research-statement {
    color: var(--global-text-color);
    font-size: clamp(1.65rem, 3.6vw, 2.45rem);
    font-weight: 630;
    letter-spacing: -0.034em;
    line-height: 1.2;
    margin: 0 0 1.25rem;
    max-width: 53rem;
  }
  .research-lead {
    color: var(--global-text-color-light);
    font-size: clamp(1rem, 1.48vw, 1.11rem);
    line-height: 1.76;
    margin: 0;
    max-width: 53rem;
  }
  .research-questions {
    border-bottom: 1px solid var(--global-divider-color);
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: clamp(1.8rem, 5vw, 4.5rem);
    grid-template-columns: minmax(11rem, 0.28fr) 1fr;
    margin-bottom: clamp(3.8rem, 7.5vw, 6rem);
    padding: clamp(1.8rem, 4vw, 2.7rem) 0;
  }
  .research-questions-heading h2 {
    color: var(--global-text-color);
    font-size: clamp(1.4rem, 2.8vw, 1.85rem);
    font-weight: 620;
    letter-spacing: -0.025em;
    line-height: 1.22;
    margin: 0;
  }
  .research-questions-heading p {
    color: var(--global-text-color-light);
    font-size: 0.88rem;
    line-height: 1.58;
    margin: 0.65rem 0 0;
    max-width: 14rem;
  }
  .research-question-list {
    display: grid;
    gap: 1.15rem clamp(1.8rem, 4.5vw, 3.6rem);
    grid-template-columns: repeat(2, minmax(0, 1fr));
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .research-question-list li {
    color: var(--global-text-color);
    font-size: clamp(0.95rem, 1.32vw, 1.03rem);
    font-weight: 540;
    line-height: 1.55;
    padding-left: 1rem;
    position: relative;
  }
  .research-question-list li::before {
    background: var(--research-accent);
    border-radius: 50%;
    content: "";
    height: 0.34rem;
    left: 0;
    position: absolute;
    top: 0.58rem;
    width: 0.34rem;
  }
  .research-work {
    margin-bottom: clamp(4rem, 8vw, 6rem);
  }
  .research-story {
    align-items: center;
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: clamp(2rem, 5.5vw, 4.6rem);
    grid-template-columns: minmax(0, 0.94fr) minmax(0, 1.06fr);
    padding: clamp(2.6rem, 6vw, 4.4rem) 0;
    scroll-margin-top: 5.5rem;
  }
  .research-story:first-of-type {
    border-top: 0;
    padding-top: 0;
  }
  .research-story--reverse {
    grid-template-columns: minmax(0, 1.06fr) minmax(0, 0.94fr);
  }
  .research-story--reverse .research-story-media {
    order: 2;
  }
  .research-story--reverse .research-story-copy {
    order: 1;
  }
  .research-story-media {
    align-items: center;
    display: flex;
    justify-content: center;
    min-height: 14rem;
  }
  .research-story-media-box {
    background: #ffffff;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.25rem;
    padding: 0.95rem;
    width: 100%;
  }
  .research-story-media img {
    display: block;
    height: auto;
    max-height: 22rem;
    margin: 0 auto;
    object-fit: contain;
    width: 100%;
  }
  .research-method-stack {
    display: grid;
    gap: 0.8rem;
    width: 100%;
  }
  .research-method-card {
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-left: 3px solid var(--research-accent);
    border-radius: 0.22rem;
    padding: 0.95rem 1.05rem;
  }
  .research-method-card h4 {
    color: var(--global-text-color);
    font-size: 0.94rem;
    font-weight: 660;
    margin: 0 0 0.28rem;
  }
  .research-method-card p {
    color: var(--global-text-color-light);
    font-size: 0.85rem;
    line-height: 1.52;
    margin: 0;
  }
  .research-story-topic {
    color: var(--research-accent);
    font-size: 0.78rem;
    font-weight: 720;
    letter-spacing: 0.06em;
    margin: 0 0 0.6rem;
    text-transform: uppercase;
  }
  .research-story h3 {
    color: var(--global-text-color);
    font-size: clamp(1.32rem, 2.5vw, 1.85rem);
    font-weight: 630;
    letter-spacing: -0.025em;
    line-height: 1.24;
    margin: 0 0 0.85rem;
  }
  .research-story-copy > p:not(.research-story-topic):not(.research-story-papers) {
    color: var(--global-text-color-light);
    font-size: 0.95rem;
    line-height: 1.7;
    margin: 0 0 0.8rem;
  }
  .research-focus-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.38rem;
    margin: 0.95rem 0 0;
  }
  .research-focus-tag {
    background: var(--research-accent-soft);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.18rem;
    color: var(--global-text-color);
    font-size: 0.78rem;
    font-weight: 560;
    padding: 0.18rem 0.52rem;
  }
  .research-story-papers {
    color: var(--global-text-color-light);
    font-size: 0.85rem;
    line-height: 1.55;
    margin: 0.95rem 0 0;
  }
  .research-story-papers a {
    color: var(--research-accent);
    font-weight: 620;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.18rem;
  }
  .research-join {
    align-items: baseline;
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: 1.5rem;
    grid-template-columns: minmax(11rem, 0.3fr) 1fr;
    margin-left: auto;
    margin-right: auto;
    max-width: 55rem;
    padding-top: 2rem;
    width: 100%;
  }
  .research-join h2 {
    color: var(--global-text-color);
    font-size: clamp(1.35rem, 2.7vw, 1.8rem);
    font-weight: 620;
    letter-spacing: -0.025em;
    line-height: 1.2;
    margin: 0;
  }
  .research-join p {
    color: var(--global-text-color-light);
    line-height: 1.65;
    margin: 0;
    max-width: 42rem;
  }
  .research-join-link {
    color: var(--research-accent);
    display: inline-block;
    font-size: 0.92rem;
    font-weight: 670;
    margin-top: 0.7rem;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  .research-join-link:hover,
  .research-join-link:focus {
    color: var(--research-accent);
  }
  @media (max-width: 820px) {
    .research-questions,
    .research-join {
      gap: 1.4rem;
      grid-template-columns: 1fr;
    }
    .research-questions-heading p {
      max-width: 28rem;
    }
    .research-story,
    .research-story--reverse {
      gap: 1.6rem;
      grid-template-columns: 1fr;
    }
    .research-story--reverse .research-story-media,
    .research-story--reverse .research-story-copy {
      order: initial;
    }
    .research-story-media {
      min-height: 0;
    }
  }
  @media (max-width: 620px) {
    .research-intro {
      margin-bottom: 2.4rem;
    }
    .research-question-list {
      gap: 0.85rem;
      grid-template-columns: 1fr;
    }
    .research-questions {
      margin-bottom: 3.4rem;
      padding: 1.6rem 0;
    }
    .research-work {
      margin-bottom: 3.6rem;
    }
    .research-story {
      padding: 2.2rem 0;
    }
    .research-story-media img {
      max-height: 18rem;
    }
  }
---

<div class="research-page">
  <section class="research-intro" aria-labelledby="research-statement">
    <h2 class="research-statement" id="research-statement">How Do Human Genomes Evolve, Diversify Across Individuals, and Age Within Cells?</h2>
    <p class="research-lead">
      Genomic and epigenomic changes unfold across vastly different scales: across millions of years of primate divergence, across diverse human populations, and across individual cells over a human lifespan. We combine long-read genome assembly and pangenomes, single-cell and 3D multi-omics, and statistical and AI modeling to connect sequence and epigenomic variation with cellular function, aging, and disease susceptibility.
    </p>
  </section>

  <section class="research-questions research-wide" aria-labelledby="research-questions-title">
    <div class="research-questions-heading">
      <h2 id="research-questions-title">Core Questions</h2>
      <p>Questions linking genome architecture, cellular regulation, and human disease.</p>
    </div>
    <ul class="research-question-list">
      <li>What genomic rearrangements and cell-type regulatory shifts shaped the human brain, and why do they confer vulnerability to neuropsychiatric disorders?</li>
      <li>How do segmental duplications and large structural variants reshape human diversity and generate newly duplicated genes beyond a single reference genome?</li>
      <li>How do somatic epimutations accumulate over a lifetime to erode cell identity, impair tissue repair, and drive age-associated chronic disease?</li>
      <li>How can statistical models and machine learning integrate multi-scale genomic and epigenomic data to explain cellular states and disease phenotypes?</li>
    </ul>
  </section>

  <section class="research-work research-wide" aria-label="Research areas">
    <article class="research-story" id="evolution">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/topic-01-primate-evolution.png' | relative_url }}" alt="Comparative primate genome synteny and cell-type-resolved brain DNA methylation divergence across human, chimpanzee, and macaque">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">01 / Evolutionary Scale</p>
        <h3>Primate and Human Evolution</h3>
        <p>
          Humans share most of their DNA sequence with non-human primates, yet accumulated structural changes and shifts in gene regulation have produced distinctive human brain development and cognition. By comparing high-quality primate genome assemblies and cell-type-resolved epigenomes across developmental stages and tissues, we identify human-specific genes and cis-regulatory innovations.
        </p>
        <p>
          We further examine why evolutionary changes in neuronal and glial regulatory landscapes disproportionately harbor genetic risk for human neurodevelopmental and neuropsychiatric conditions such as schizophrenia.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Complete primate genomes</span>
          <span class="research-focus-tag">Cell-type brain epigenomes</span>
          <span class="research-focus-tag">Human-specific regulation</span>
          <span class="research-focus-tag">Neuropsychiatric risk</span>
        </div>
        <p class="research-story-papers">
          Selected work:
          <a href="https://doi.org/10.1038/s41467-021-21917-7"><em>Nature Communications</em> (2021)</a>,
          <a href="https://doi.org/10.1038/s41586-025-08816-3"><em>Nature</em> (2025)</a>,
          <a href="https://doi.org/10.1038/s41586-024-07473-2"><em>Nature</em> (2024)</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse" id="diversity">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/topic-02-structural-diversity.png' | relative_url }}" alt="Haplotype-resolved structural variation, segmental duplications, inversions, and newly duplicated genes across human genomes">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">02 / Population Scale</p>
        <h3>Complex Genome Architecture and Human Diversity</h3>
        <p>
          Although human genomes are often described as nearly identical, individual genomes differ extensively across structurally dynamic regions. Large blocks of repeated sequence known as segmental duplications, together with inversions and copy-number variants, undergo rapid rearrangement, create newly duplicated genes, and predispose chromosomes to recurrent disease-associated mutations.
        </p>
        <p>
          Because short-read sequencing fails to resolve highly identical repeats, we leverage long-read genome assemblies and human pangenomes to characterize population-scale structural and epigenomic diversity and link it to gene expression and complex traits.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Segmental duplications</span>
          <span class="research-focus-tag">Structural variation</span>
          <span class="research-focus-tag">Duplicated gene emergence</span>
          <span class="research-focus-tag">Human pangenomes</span>
        </div>
        <p class="research-story-papers">
          Selected work:
          <a href="https://doi.org/10.1038/s41588-024-02051-8"><em>Nature Genetics</em> (2025)</a>,
          <a href="https://doi.org/10.1016/j.cell.2024.01.052"><em>Cell</em> (2024)</a>,
          <a href="https://doi.org/10.7554/eLife.79387"><em>eLife</em> (2022)</a>
        </p>
      </div>
    </article>

    <article class="research-story" id="aging">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/topic-03-cellular-aging.png' | relative_url }}" alt="Somatic epimutations, erosion of cell-type epigenetic identity, and single-cell trajectories toward aging and failed tissue repair">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">03 / Cellular Scale</p>
        <h3>Cellular Aging and Disease</h3>
        <p>
          Aging and chronic disease emerge at the level of individual cells rather than bulk tissue averages. Integrating single-cell DNA methylation, chromatin accessibility, 3D genome conformation, and transcriptomes across organs such as the brain and kidney, we investigate how somatic epimutations accumulate across cells, how epigenetic cell identity degrades with age, and how injured cells enter maladaptive repair states.
        </p>
        <p>
          We further compare single-cell epigenomes across species to distinguish conserved aging programs from disease-associated remodeling, and evaluate how cellular reprogramming and rejuvenation interventions reshape the epigenome.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Single-cell &amp; 3D epigenomics</span>
          <span class="research-focus-tag">Somatic epimutation</span>
          <span class="research-focus-tag">Cell identity &amp; failed repair</span>
          <span class="research-focus-tag">Cellular rejuvenation</span>
        </div>
        <p class="research-story-papers">
          Selected work:
          <a href="https://doi.org/10.1038/s43587-026-01221-z"><em>Nature Aging</em> (2026)</a>,
          <a href="https://doi.org/10.1007/s11357-024-01450-3"><em>GeroScience</em> (2025)</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse" id="methods">
      <div class="research-story-media">
        <div class="research-method-stack" aria-label="Core computational method areas">
          <div class="research-method-card">
            <h4>Complex Genome &amp; Structural Variation Analysis</h4>
            <p>Computational approaches for resolving segmental duplications, multi-allelic copy-number variation, and complex rearrangements across haplotype assemblies.</p>
          </div>
          <div class="research-method-card">
            <h4>Single-Cell &amp; Multi-Omic Statistical Modeling</h4>
            <p>Probabilistic and statistical frameworks for sparse single-cell methylomes, 3D chromatin, and quantitative inference of cellular state transitions.</p>
          </div>
          <div class="research-method-card">
            <h4>Machine Learning &amp; AI for Genomics</h4>
            <p>Integrative machine learning and AI modeling to link genomic and epigenomic variation with cell-type regulation, aging trajectories, and disease risk.</p>
          </div>
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">04 / Methods &amp; AI</p>
        <h3>Computational Methods and AI</h3>
        <p>
          Extracting accurate biological signal from structurally complex genomes and sparse single-cell multi-omics requires tailored statistical and computational frameworks. We develop analytical methods to resolve repetitive genomic regions, separate true biological variation from reference and technical biases, and infer cellular state transitions as well as somatic epimutation-based clonal lineages from single-cell epigenomic data.
        </p>
        <p>
          In parallel, we apply and develop machine learning and AI models to integrate multi-omic datasets and connect genomic and epigenomic variation with cellular states, aging, and disease, sharing our methods as reproducible open-source tools.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Complex locus analysis</span>
          <span class="research-focus-tag">Single-cell statistical models</span>
          <span class="research-focus-tag">Multi-omic ML &amp; AI</span>
          <span class="research-focus-tag">Open-source tools</span>
        </div>
        <p class="research-story-papers">
          Selected work:
          <a href="https://doi.org/10.1038/s43587-026-01221-z"><em>Nature Aging</em> (2026)</a>,
          <a href="https://doi.org/10.1038/s41588-024-02051-8"><em>Nature Genetics</em> (2025)</a>,
          <a href="https://doi.org/10.1093/nar/gkv1245"><em>Nucleic Acids Research</em> (2016)</a>
        </p>
      </div>
    </article>
  </section>

  <section class="research-join" aria-labelledby="research-join-title">
    <h2 id="research-join-title">Work With Us</h2>
    <div>
      <p>
        We welcome researchers from life sciences and biomedicine as well as computer science, statistics, mathematics, and AI who are excited to study genome evolution, human diversity, and cellular aging.
      </p>
      <a class="research-join-link" href="{{ '/join/' | relative_url }}">Explore opportunities to join the lab →</a>
    </div>
  </section>
</div>
