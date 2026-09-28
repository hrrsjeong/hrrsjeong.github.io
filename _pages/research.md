---
layout: page
permalink: /research/
title: Research
display_title: Research
nav: true
nav_order: 2
_styles: |
  .research-page {
    --research-accent: #725c78;
    padding-bottom: 2.5rem;
  }
  html[data-theme="dark"] .research-page {
    --research-accent: #b29cb6;
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
    margin: 0.35rem auto clamp(3.2rem, 7vw, 5.6rem);
    max-width: 55rem;
    width: 100%;
  }
  .research-statement {
    color: var(--global-text-color);
    font-size: clamp(1.75rem, 4vw, 2.7rem);
    font-weight: 620;
    letter-spacing: -0.038em;
    line-height: 1.17;
    margin: 0 0 1.35rem;
    max-width: 55rem;
  }
  .research-statement-line {
    display: inline-block;
  }
  .research-lead {
    color: var(--global-text-color-light);
    font-size: clamp(1rem, 1.5vw, 1.13rem);
    line-height: 1.72;
    margin: 0;
    max-width: 55rem;
  }
  .research-section-title {
    color: var(--global-text-color);
    font-size: clamp(1.45rem, 3vw, 1.95rem);
    font-weight: 620;
    letter-spacing: -0.027em;
    line-height: 1.2;
    margin: 0;
  }
  .research-questions {
    border-bottom: 1px solid var(--global-divider-color);
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: clamp(2rem, 6vw, 5.5rem);
    grid-template-columns: minmax(11rem, 0.3fr) 1fr;
    margin-bottom: clamp(4rem, 8vw, 6.5rem);
    padding: clamp(1.8rem, 4vw, 2.8rem) 0;
  }
  .research-questions-heading h2 {
    color: var(--global-text-color);
    font-size: clamp(1.45rem, 3vw, 1.95rem);
    font-weight: 620;
    letter-spacing: -0.027em;
    line-height: 1.2;
    margin: 0;
  }
  .research-questions-heading p {
    color: var(--global-text-color-light);
    font-size: 0.88rem;
    line-height: 1.55;
    margin: 0.65rem 0 0;
    max-width: 14rem;
  }
  .research-question-list {
    display: grid;
    gap: 1rem clamp(2rem, 5vw, 4.5rem);
    grid-template-columns: repeat(2, minmax(0, 1fr));
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .research-question-list li {
    color: var(--global-text-color);
    font-size: clamp(0.98rem, 1.4vw, 1.09rem);
    font-weight: 550;
    line-height: 1.48;
    padding-left: 1rem;
    position: relative;
  }
  .research-question-list li::before {
    background: var(--research-accent);
    border-radius: 50%;
    content: "";
    height: 0.32rem;
    left: 0;
    position: absolute;
    top: 0.58rem;
    width: 0.32rem;
  }
  .research-work {
    margin-bottom: clamp(4rem, 8vw, 6.5rem);
  }
  .research-work-heading {
    margin-bottom: clamp(2rem, 5vw, 3.2rem);
  }
  .research-story {
    align-items: center;
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: clamp(2rem, 6vw, 5.25rem);
    grid-template-columns: minmax(0, 1.12fr) minmax(18rem, 0.88fr);
    padding: clamp(2.5rem, 6vw, 4.5rem) 0;
  }
  .research-story:first-of-type {
    border-top: 0;
    padding-top: 0;
  }
  .research-story--reverse {
    grid-template-columns: minmax(18rem, 0.88fr) minmax(0, 1.12fr);
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
    min-height: 15rem;
  }
  .research-story-media img {
    display: block;
    height: auto;
    max-height: 25rem;
    object-fit: contain;
    width: 100%;
  }
  .research-story-topic {
    color: var(--research-accent);
    font-size: 0.82rem;
    font-weight: 670;
    letter-spacing: 0.01em;
    margin: 0 0 0.7rem;
  }
  .research-story h3 {
    color: var(--global-text-color);
    font-size: clamp(1.35rem, 2.7vw, 2rem);
    font-weight: 630;
    letter-spacing: -0.027em;
    line-height: 1.2;
    margin: 0 0 0.9rem;
  }
  .research-story-summary {
    color: var(--global-text-color-light);
    font-size: 0.96rem;
    line-height: 1.68;
    margin: 0;
  }
  .research-papers {
    color: var(--global-text-color-light);
    font-size: 0.84rem;
    line-height: 1.7;
    margin: 1.15rem 0 0;
  }
  .research-papers span {
    color: var(--global-text-color);
    font-weight: 650;
    margin-right: 0.25rem;
  }
  .research-papers a {
    color: var(--research-accent);
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  .research-papers a:hover,
  .research-papers a:focus {
    color: var(--research-accent);
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
    line-height: 1.6;
    margin: 0;
    max-width: 42rem;
  }
  .research-join-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem 1.5rem;
    margin-top: 0.75rem;
  }
  .research-join-link {
    color: var(--research-accent);
    display: inline-block;
    font-size: 0.9rem;
    font-weight: 670;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  .research-join-link:hover,
  .research-join-link:focus {
    color: var(--research-accent);
  }
  @media (max-width: 800px) {
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
      margin-bottom: 3.2rem;
    }
    .research-question-list {
      gap: 0.85rem;
      grid-template-columns: 1fr;
    }
    .research-questions {
      margin-bottom: 4rem;
      padding: 1.6rem 0;
    }
    .research-work {
      margin-bottom: 4rem;
    }
    .research-story {
      padding: 2.25rem 0;
    }
    .research-story-media img {
      max-height: 19rem;
    }
  }
---

<div class="research-page">
  <section class="research-intro" aria-labelledby="research-statement">
    <h2 class="research-statement" id="research-statement"><span class="research-statement-line">Every genome carries a history of evolution;</span> <span class="research-statement-line">every cell, a record of aging.</span></h2>
    <p class="research-lead">
      We study how genomic and epigenomic variation shapes human evolution, aging, and disease. Because a single reference genome cannot capture the large structural differences between people and species, we build donor-specific genome assemblies, compare complete primate genomes, and analyze epigenomes at single-cell resolution. Our work is fully computational, combining long-read genomics, single-cell multi-omics, statistical modeling, and machine learning.
    </p>
  </section>

  <section class="research-questions research-wide" aria-labelledby="research-questions-title">
    <div class="research-questions-heading">
      <h2 id="research-questions-title">Questions we ask</h2>
      <p>Questions that connect our work across genomes, species, and cells.</p>
    </div>
    <ul class="research-question-list">
      <li>What large genomic changes do we miss when every genome is compared with a single reference?</li>
      <li>Which genomic and regulatory changes shaped the human brain, and how did they affect disease risk?</li>
      <li>Why do cells lose their epigenetic identity with age, and why does tissue repair fail in disease?</li>
      <li>Can AI learn how each person’s genome, not just the reference, shapes regulation in every cell type?</li>
    </ul>
  </section>

  <section class="research-work research-wide" aria-labelledby="research-work-title">
    <div class="research-work-heading">
      <h2 class="research-section-title" id="research-work-title">Research areas</h2>
    </div>

    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/structurally-complex-regions.png' | relative_url }}" alt="Alignment of a structurally complex chromosome region between human and chimpanzee genomes">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Genome architecture</p>
        <h3>Resolving the most complex regions of the genome</h3>
        <p class="research-story-summary">
          Segmental duplications, inversions, and other large structural variants are among the most dynamic parts of the genome, yet reference-based analyses often collapse or miss them. Using long-read assemblies from diverse humans and apes, we study how these regions vary among individuals and species, how they create new genes, and how they shape human evolution and disease.
        </p>
        <p class="research-papers">
          <span>Key papers</span>
          <a href="https://doi.org/10.1038/s41588-024-02051-8">Jeong et al., <em>Nature Genetics</em> 2025</a> ·
          <a href="https://doi.org/10.1038/s41586-025-08816-3">Yoo et al., <em>Nature</em> 2025</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/epigenetic-evolution.png' | relative_url }}" alt="DNA methylation at a neuronal regulatory region in humans, chimpanzees, and macaques, with lower methylation in human neurons">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Regulatory evolution</p>
        <h3>Tracing how gene regulation changed in human evolution</h3>
        <p class="research-story-summary">
          Much of what makes us human lies in how genes are regulated, not only in which genes we have. We compare cell-type-resolved epigenomes of humans and other primates to find regulatory changes unique to the human lineage and to understand how they shaped the brain and influence disease risk.
        </p>
        <p class="research-papers">
          <span>Key papers</span>
          <a href="https://doi.org/10.1038/s41467-021-21917-7">Jeong et al., <em>Nature Communications</em> 2021</a> ·
          <a href="https://doi.org/10.1186/s13059-019-1747-7">Mendizabal et al., <em>Genome Biology</em> 2019</a>
        </p>
      </div>
    </article>

    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/epigenetic-aging.png' | relative_url }}" alt="Cell-resolved epigenomic maps of human and mouse kidney">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Aging and disease</p>
        <h3>Understanding how cells lose their identity with age</h3>
        <p class="research-story-summary">
          Aging does not affect every cell type equally. Using single-cell epigenomic and multi-omic data, we study which cells age fastest, how their regulatory programs break down, and why tissue repair fails in chronic disease.
        </p>
        <p class="research-papers">
          <span>Key papers</span>
          <a href="https://doi.org/10.1038/s43587-026-01221-z">Jeong et al., <em>Nature Aging</em> 2026</a> ·
          <a href="https://doi.org/10.1007/s11357-024-01450-3">Jeong et al., <em>GeroScience</em> 2025</a>
        </p>
      </div>
    </article>
  </section>

  <section class="research-join" aria-labelledby="research-join-title">
    <h2 id="research-join-title">Interested in these questions?</h2>
    <div>
      <p>We welcome students and researchers from biology, computer science, statistics, and AI. All of our research is computational.</p>
      <div class="research-join-links">
        <a class="research-join-link" href="{{ '/join/graduate-research/' | relative_url }}">Graduate research opportunities →</a>
        <a class="research-join-link" href="{{ '/join/undergraduate-research/' | relative_url }}">Undergraduate research →</a>
        <a class="research-join-link" href="{{ '/join/' | relative_url }}">All openings →</a>
      </div>
    </div>
  </section>
</div>
