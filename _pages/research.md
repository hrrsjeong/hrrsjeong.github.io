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
  .research-lead {
    color: var(--global-text-color-light);
    font-size: clamp(1rem, 1.5vw, 1.13rem);
    line-height: 1.72;
    margin: 0;
    max-width: 55rem;
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
  .research-story-copy > p:not(.research-story-topic) {
    color: var(--global-text-color-light);
    font-size: 0.96rem;
    line-height: 1.68;
    margin: 0;
  }
  .research-story-link {
    color: var(--research-accent);
    display: inline-block;
    font-size: 0.86rem;
    font-weight: 660;
    margin-top: 1.15rem;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  .research-story-link:hover,
  .research-story-link:focus {
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
  .research-join-link {
    color: var(--research-accent);
    display: inline-block;
    font-size: 0.9rem;
    font-weight: 670;
    margin-top: 0.65rem;
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
    <h2 class="research-statement" id="research-statement">We study genome structure and epigenetic regulation across species and cell types.</h2>
    <p class="research-lead">
      We investigate how genomic and epigenomic variation relates to human evolution, aging, and neurological disorders. Our work combines comparative genomics with statistical modeling, machine learning, and bioinformatics method development to resolve complex genomic regions and identify regulatory patterns in large-scale data.
    </p>
  </section>

  <section class="research-questions research-wide" aria-labelledby="research-questions-title">
    <div class="research-questions-heading">
      <h2 id="research-questions-title">Questions we ask</h2>
      <p>Questions that connect our work across biological systems and data types.</p>
    </div>
    <ul class="research-question-list">
      <li>How do complex genomic regions vary among individuals and species?</li>
      <li>How has gene regulation changed during human evolution?</li>
      <li>How does cell-type-specific regulation change with aging and disease?</li>
      <li>How can we distinguish biological variation from reference, annotation, and technical effects?</li>
    </ul>
  </section>

  <section class="research-work research-wide" aria-label="Selected research">
    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/structurally-complex-regions.png' | relative_url }}" alt="Alignment of a structurally complex chromosome region between human and chimpanzee genomes">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Genome architecture</p>
        <h3>Resolving the most complex regions of the genome</h3>
        <p>
          We study segmental duplications, copy-number variation, and other structurally complex loci using long-read and complete genome assemblies. These regions provide a view into recent human variation, primate evolution, and the emergence of new gene functions.
        </p>
        <a class="research-story-link" href="https://doi.org/10.1038/s41588-024-02051-8">Read the related work ↗</a>
      </div>
    </article>

    <article class="research-story research-story--reverse">
      <div class="research-story-media">
        <img src="{{ '/assets/img/home/publications/jeong-2021-natcomms-fig1-card.png' | relative_url }}" alt="Comparative cell-type-resolved methylation patterns across primate brains">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Regulatory evolution</p>
        <h3>Tracing changes in gene regulation across species</h3>
        <p>
          We compare cell-type-resolved epigenomic data from humans and non-human primates to identify lineage-specific regulatory changes and examine their relationships with gene expression, neurodevelopment, and disease risk.
        </p>
        <a class="research-story-link" href="https://doi.org/10.1038/s41467-021-21917-7">Read the related work ↗</a>
      </div>
    </article>

    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/epigenetic-aging.png' | relative_url }}" alt="Cell-resolved epigenomic maps of human and mouse kidney">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">Aging and disease</p>
        <h3>Understanding how cell identity changes with age</h3>
        <p>
          We analyze cell-resolved genomic and epigenomic data to determine how regulatory programs change with aging, disease, and failed tissue repair. Current work spans the brain, kidney, and comparative models of human biology.
        </p>
        <a class="research-story-link" href="https://doi.org/10.64898/2026.01.22.700871">Read the related work ↗</a>
      </div>
    </article>
  </section>

  <section class="research-join" aria-labelledby="research-join-title">
    <h2 id="research-join-title">Interested in these questions?</h2>
    <div>
      <p>We welcome researchers interested in genomics, evolution, aging, and disease.</p>
      <a class="research-join-link" href="{{ '/join/' | relative_url }}">Learn about joining the lab →</a>
    </div>
  </section>
</div>
