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
    --research-accent-soft: rgba(114, 92, 120, 0.13);
    --research-teal: #2f6f73;
    --research-teal-soft: rgba(47, 111, 115, 0.14);
    --research-block: #dfdbe1;
    --research-block-ink: #4a4550;
    --research-tint: rgba(114, 92, 120, 0.055);
    padding-bottom: 2.5rem;
  }
  html[data-theme="dark"] .research-page {
    --research-accent: #b29cb6;
    --research-accent-soft: rgba(178, 156, 182, 0.2);
    --research-teal: #7fbcb9;
    --research-teal-soft: rgba(127, 188, 185, 0.18);
    --research-block: #3b393f;
    --research-block-ink: #e2dee5;
    --research-tint: rgba(178, 156, 182, 0.07);
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
  .research-eyebrow {
    color: var(--research-accent);
    font-size: 0.82rem;
    font-weight: 670;
    letter-spacing: 0.01em;
    margin: 0 0 0.7rem;
  }
  .research-section-title {
    color: var(--global-text-color);
    font-size: clamp(1.45rem, 3vw, 1.95rem);
    font-weight: 620;
    letter-spacing: -0.027em;
    line-height: 1.2;
    margin: 0;
  }
  .research-section-lead {
    color: var(--global-text-color-light);
    font-size: 0.98rem;
    line-height: 1.7;
    margin: 0.95rem 0 0;
    max-width: 46rem;
  }
  .research-approach {
    margin-bottom: clamp(4rem, 8vw, 6.5rem);
  }
  .research-diagram {
    margin: clamp(1.7rem, 4vw, 2.4rem) 0 0;
  }
  .research-diagram-panels {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .research-diagram-panel {
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.3rem;
    padding: 1.05rem 1.15rem 1.15rem;
  }
  .research-diagram-panel--ours {
    border-color: var(--research-accent);
    box-shadow: inset 0 3px 0 var(--research-accent);
  }
  .research-diagram-kicker {
    color: var(--global-text-color-light);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin: 0 0 0.2rem;
    text-transform: uppercase;
  }
  .research-diagram-panel--ours .research-diagram-kicker {
    color: var(--research-accent);
  }
  .research-diagram-panel h3 {
    color: var(--global-text-color);
    font-size: 1.04rem;
    font-weight: 650;
    line-height: 1.35;
    margin: 0 0 0.8rem;
  }
  .research-diagram-svg {
    display: block;
    height: auto;
    overflow: visible;
    width: 100%;
  }
  .research-diagram-caption {
    color: var(--global-text-color-light);
    font-size: 0.86rem;
    line-height: 1.55;
    margin: 0.8rem 0 0;
  }
  .research-diagram-svg text {
    font-family: inherit;
  }
  .research-diagram-svg .dx-label {
    fill: var(--global-text-color-light);
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 0.06em;
  }
  .research-diagram-svg .dx-block {
    fill: var(--research-block);
  }
  .research-diagram-svg .dx-block--dup,
  .research-diagram-svg .dx-block--inv {
    stroke: var(--research-accent);
    stroke-width: 1.4;
  }
  .research-diagram-svg .dx-block--dup {
    fill: var(--research-accent-soft);
  }
  .research-diagram-svg .dx-block--novel {
    fill: var(--research-teal-soft);
    stroke: var(--research-teal);
    stroke-width: 1.4;
  }
  .research-diagram-svg .dx-block--gap {
    fill: none;
    stroke: var(--global-text-color-light);
    stroke-dasharray: 3 3;
    stroke-width: 1;
  }
  .research-diagram-svg .dx-gap-line {
    opacity: 0.45;
    stroke: var(--global-text-color-light);
    stroke-width: 1;
  }
  .research-diagram-svg .dx-glyph {
    fill: var(--research-block-ink);
    font-size: 11px;
    font-weight: 700;
    text-anchor: middle;
  }
  .research-diagram-svg .dx-glyph--dup,
  .research-diagram-svg .dx-glyph--inv {
    fill: var(--research-accent);
  }
  .research-diagram-svg .dx-glyph--novel {
    fill: var(--research-teal);
  }
  .research-diagram-svg .dx-read {
    fill: var(--global-text-color-light);
    opacity: 0.5;
  }
  .research-diagram-svg .dx-read--pile {
    fill: var(--research-accent);
    opacity: 0.85;
  }
  .research-diagram-svg .dx-read--lost,
  .research-diagram-svg .dx-read--lost-novel {
    fill: none;
    opacity: 1;
    stroke-dasharray: 2.5 2;
    stroke-width: 1.1;
  }
  .research-diagram-svg .dx-read--lost {
    stroke: var(--research-accent);
  }
  .research-diagram-svg .dx-read--lost-novel {
    stroke: var(--research-teal);
  }
  .research-diagram-svg .dx-note {
    font-size: 11px;
    font-weight: 700;
    text-anchor: middle;
  }
  .research-diagram-svg .dx-note--pile {
    fill: var(--research-accent);
  }
  .research-diagram-svg .dx-badge {
    fill: var(--global-card-bg-color);
    stroke: var(--global-text-color-light);
    stroke-width: 1.2;
  }
  .research-diagram-svg .dx-badge-text {
    fill: var(--global-text-color-light);
    font-size: 12px;
    font-weight: 700;
    text-anchor: middle;
  }
  .research-diagram-svg .dx-stick {
    opacity: 0.8;
    stroke: var(--global-text-color-light);
    stroke-width: 1;
  }
  .research-diagram-svg .dx-meth {
    fill: var(--global-text-color);
  }
  .research-diagram-svg .dx-meth--open {
    fill: var(--global-card-bg-color);
    stroke: var(--global-text-color);
    stroke-width: 1.1;
  }
  .research-diagram-svg .dx-inv-arrow {
    fill: none;
    stroke: var(--research-accent);
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-width: 1.3;
  }
  .research-points {
    display: grid;
    gap: 1.4rem clamp(1.5rem, 4vw, 2.6rem);
    grid-template-columns: repeat(3, minmax(0, 1fr));
    list-style: none;
    margin: clamp(1.9rem, 4vw, 2.5rem) 0 0;
    padding: 0;
  }
  .research-points li {
    border-top: 2px solid var(--research-accent);
    padding-top: 0.9rem;
  }
  .research-points h3 {
    color: var(--global-text-color);
    font-size: 1rem;
    font-weight: 650;
    line-height: 1.35;
    margin: 0 0 0.4rem;
  }
  .research-points p {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.6;
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
  .research-future {
    background: var(--research-tint);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
    margin-bottom: clamp(4rem, 8vw, 6.5rem);
    padding: clamp(1.5rem, 4vw, 2.6rem);
  }
  .research-future-head {
    margin-bottom: clamp(1.5rem, 3vw, 2.1rem);
  }
  .research-future-grid {
    align-items: start;
    display: grid;
    gap: clamp(1.4rem, 4vw, 2.6rem);
    grid-template-columns: minmax(0, 0.92fr) minmax(0, 1.08fr);
  }
  .research-future h3 {
    color: var(--global-text-color);
    font-size: 1.12rem;
    font-weight: 650;
    line-height: 1.35;
    margin: 0 0 0.9rem;
  }
  .research-future-now {
    padding-top: clamp(0.4rem, 1vw, 0.6rem);
  }
  .research-future-now p {
    color: var(--global-text-color-light);
    font-size: 0.95rem;
    line-height: 1.7;
    margin: 0;
  }
  .research-future-next {
    background: var(--global-card-bg-color);
    border: 1px solid var(--research-accent);
    border-radius: 0.3rem;
    padding: clamp(1.2rem, 3vw, 1.6rem);
  }
  .research-future-next .research-future-tag {
    background: var(--research-accent-soft);
    border-radius: 999px;
    color: var(--research-accent);
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin: 0 0 0.85rem;
    padding: 0.22rem 0.62rem;
    text-transform: uppercase;
  }
  .research-future-next p {
    color: var(--global-text-color-light);
    font-size: 0.92rem;
    line-height: 1.65;
    margin: 0;
  }
  .research-future-next ul {
    list-style: none;
    margin: 0.95rem 0 0;
    padding: 0;
  }
  .research-future-next li {
    color: var(--global-text-color);
    font-size: 0.91rem;
    line-height: 1.55;
    padding-left: 1.2rem;
    position: relative;
  }
  .research-future-next li + li {
    margin-top: 0.55rem;
  }
  .research-future-next li::before {
    color: var(--research-accent);
    content: "→";
    font-weight: 700;
    left: 0;
    position: absolute;
    top: 0;
  }
  .research-future-next .research-future-note {
    border-top: 1px solid var(--global-divider-color);
    color: var(--global-text-color);
    font-size: 0.88rem;
    margin-top: 1.15rem;
    padding-top: 0.95rem;
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
    .research-diagram-panels,
    .research-future-grid {
      grid-template-columns: 1fr;
    }
    .research-points {
      gap: 1.2rem;
      grid-template-columns: 1fr;
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
    .research-approach,
    .research-work,
    .research-future {
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

  <section class="research-approach research-wide" aria-labelledby="research-approach-title">
    <p class="research-eyebrow">Our approach</p>
    <h2 class="research-section-title" id="research-approach-title">A genome for every donor</h2>
    <p class="research-section-lead">
      Most genomic studies align every sample to the same reference genome. This works well for small variants, but large insertions, deletions, inversions, and duplications that differ between people are collapsed, misplaced, or missed, along with the regulatory signals they carry. Donor-specific genome assemblies are still rare, especially in studies of gene regulation and aging. We put them at the center of our work: we assemble each donor’s genome from long reads and study large genomic changes on the donor’s own sequence rather than on the reference.
    </p>

    <figure class="research-diagram">
      <div class="research-diagram-panels">
        <div class="research-diagram-panel">
          <p class="research-diagram-kicker">Reference-based</p>
          <h3>One shared reference</h3>
          <svg class="research-diagram-svg" viewBox="0 0 400 170" role="img" aria-labelledby="diagram-reference-title diagram-reference-desc">
            <title id="diagram-reference-title">Reads from one donor aligned to a single reference genome</title>
            <desc id="diagram-reference-desc">Reads from a duplicated segment pile onto one reference copy, and reads from inverted or novel sequence cannot be placed.</desc>
            <text class="dx-label" x="4" y="148">REF</text>
            <rect class="dx-block" x="44" y="134" width="64" height="20" rx="3"/>
            <text class="dx-glyph" x="76" y="148">A</text>
            <rect class="dx-block" x="114" y="134" width="64" height="20" rx="3"/>
            <text class="dx-glyph" x="146" y="148">B</text>
            <rect class="dx-block" x="184" y="134" width="64" height="20" rx="3"/>
            <text class="dx-glyph" x="216" y="148">C</text>
            <rect class="dx-block" x="254" y="134" width="64" height="20" rx="3"/>
            <text class="dx-glyph" x="286" y="148">D</text>
            <rect class="dx-block" x="324" y="134" width="64" height="20" rx="3"/>
            <text class="dx-glyph" x="356" y="148">E</text>
            <rect class="dx-read" x="38" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="72" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="106" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="140" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="174" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="208" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="276" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="344" y="121" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="49" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="83" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="117" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="151" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="185" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="219" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="287" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="321" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="355" y="113" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="60" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="94" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="128" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="162" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="196" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="230" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="264" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="332" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read" x="366" y="105" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="186" y="97" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="220" y="97" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="195" y="89" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="186" y="81" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--pile" x="220" y="81" width="26" height="5" rx="2.5"/>
            <text class="dx-note dx-note--pile" x="216" y="72">2×</text>
            <rect class="dx-read dx-read--lost" x="282" y="30" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--lost-novel" x="318" y="22" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--lost-novel" x="352" y="34" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--lost" x="300" y="46" width="26" height="5" rx="2.5"/>
            <rect class="dx-read dx-read--lost-novel" x="338" y="50" width="26" height="5" rx="2.5"/>
            <circle class="dx-badge" cx="262" cy="36" r="10"/>
            <text class="dx-badge-text" x="262" y="40.5">?</text>
          </svg>
          <p class="research-diagram-caption">Reads from every donor are forced onto the same sequence. Extra copies pile up (2×), and inverted or new sequence has nowhere to go (?).</p>
        </div>
        <div class="research-diagram-panel research-diagram-panel--ours">
          <p class="research-diagram-kicker">Donor-specific</p>
          <h3>A genome for each donor</h3>
          <svg class="research-diagram-svg" viewBox="0 0 400 170" role="img" aria-labelledby="diagram-donor-title diagram-donor-desc">
            <title id="diagram-donor-title">The same donor's genome assembled as two haplotypes</title>
            <desc id="diagram-donor-desc">One haplotype carries an extra copy of segment C; the other carries a deletion, an inversion, and new sequence. DNA methylation is shown on every segment.</desc>
            <text class="dx-label" x="4" y="68">HAP 1</text>
            <rect class="dx-block" x="44" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="70" y="68">A</text>
            <line class="dx-stick" x1="61" y1="53" x2="61" y2="42"/>
            <circle class="dx-meth" cx="61" cy="38" r="3.6"/>
            <line class="dx-stick" x1="79" y1="53" x2="79" y2="42"/>
            <circle class="dx-meth" cx="79" cy="38" r="3.6"/>
            <rect class="dx-block" x="102" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="128" y="68">B</text>
            <line class="dx-stick" x1="119" y1="53" x2="119" y2="42"/>
            <circle class="dx-meth" cx="119" cy="38" r="3.6"/>
            <line class="dx-stick" x1="137" y1="53" x2="137" y2="42"/>
            <circle class="dx-meth dx-meth--open" cx="137" cy="38" r="3.6"/>
            <rect class="dx-block" x="160" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="186" y="68">C</text>
            <line class="dx-stick" x1="177" y1="53" x2="177" y2="42"/>
            <circle class="dx-meth dx-meth--open" cx="177" cy="38" r="3.6"/>
            <line class="dx-stick" x1="195" y1="53" x2="195" y2="42"/>
            <circle class="dx-meth" cx="195" cy="38" r="3.6"/>
            <rect class="dx-block dx-block--dup" x="218" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph dx-glyph--dup" x="244" y="68">C′</text>
            <line class="dx-stick" x1="235" y1="53" x2="235" y2="42"/>
            <circle class="dx-meth" cx="235" cy="38" r="3.6"/>
            <line class="dx-stick" x1="253" y1="53" x2="253" y2="42"/>
            <circle class="dx-meth" cx="253" cy="38" r="3.6"/>
            <rect class="dx-block" x="276" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="302" y="68">D</text>
            <line class="dx-stick" x1="293" y1="53" x2="293" y2="42"/>
            <circle class="dx-meth dx-meth--open" cx="293" cy="38" r="3.6"/>
            <line class="dx-stick" x1="311" y1="53" x2="311" y2="42"/>
            <circle class="dx-meth dx-meth--open" cx="311" cy="38" r="3.6"/>
            <rect class="dx-block" x="334" y="54" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="360" y="68">E</text>
            <line class="dx-stick" x1="351" y1="53" x2="351" y2="42"/>
            <circle class="dx-meth" cx="351" cy="38" r="3.6"/>
            <line class="dx-stick" x1="369" y1="53" x2="369" y2="42"/>
            <circle class="dx-meth" cx="369" cy="38" r="3.6"/>
            <text class="dx-label" x="4" y="148">HAP 2</text>
            <rect class="dx-block" x="44" y="134" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="70" y="148">A</text>
            <line class="dx-stick" x1="61" y1="133" x2="61" y2="122"/>
            <circle class="dx-meth" cx="61" cy="118" r="3.6"/>
            <line class="dx-stick" x1="79" y1="133" x2="79" y2="122"/>
            <circle class="dx-meth dx-meth--open" cx="79" cy="118" r="3.6"/>
            <rect class="dx-block" x="102" y="134" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="128" y="148">B</text>
            <line class="dx-stick" x1="119" y1="133" x2="119" y2="122"/>
            <circle class="dx-meth" cx="119" cy="118" r="3.6"/>
            <line class="dx-stick" x1="137" y1="133" x2="137" y2="122"/>
            <circle class="dx-meth" cx="137" cy="118" r="3.6"/>
            <rect class="dx-block dx-block--gap" x="160.5" y="134.5" width="51" height="19" rx="3"/>
            <line class="dx-gap-line" x1="168" y1="144" x2="204" y2="144"/>
            <rect class="dx-block dx-block--inv" x="218" y="134" width="52" height="20" rx="3"/>
            <text class="dx-glyph dx-glyph--inv" x="244" y="148">D</text>
            <path class="dx-inv-arrow" d="M261 159 H227 m4 -3 l-4 3 l4 3"/>
            <line class="dx-stick" x1="235" y1="133" x2="235" y2="122"/>
            <circle class="dx-meth" cx="235" cy="118" r="3.6"/>
            <line class="dx-stick" x1="253" y1="133" x2="253" y2="122"/>
            <circle class="dx-meth dx-meth--open" cx="253" cy="118" r="3.6"/>
            <rect class="dx-block dx-block--novel" x="276" y="134" width="52" height="20" rx="3"/>
            <text class="dx-glyph dx-glyph--novel" x="302" y="148">N</text>
            <line class="dx-stick" x1="293" y1="133" x2="293" y2="122"/>
            <circle class="dx-meth dx-meth--open" cx="293" cy="118" r="3.6"/>
            <line class="dx-stick" x1="311" y1="133" x2="311" y2="122"/>
            <circle class="dx-meth" cx="311" cy="118" r="3.6"/>
            <rect class="dx-block" x="334" y="134" width="52" height="20" rx="3"/>
            <text class="dx-glyph" x="360" y="148">E</text>
            <line class="dx-stick" x1="351" y1="133" x2="351" y2="122"/>
            <circle class="dx-meth" cx="351" cy="118" r="3.6"/>
            <line class="dx-stick" x1="369" y1="133" x2="369" y2="122"/>
            <circle class="dx-meth" cx="369" cy="118" r="3.6"/>
          </svg>
          <p class="research-diagram-caption">Each donor’s genome is assembled in full, so duplications (C′), deletions, inversions, and new sequence (N) are resolved along with their DNA methylation.</p>
        </div>
      </div>
    </figure>

    <ul class="research-points">
      <li>
        <h3>See large changes directly</h3>
        <p>Structural variants and duplications are resolved at the sequence level instead of being inferred from mapping artifacts.</p>
      </li>
      <li>
        <h3>Keep regulation in context</h3>
        <p>Epigenomic signals can be read on each donor’s own genome, including sequence that is missing from the reference.</p>
      </li>
      <li>
        <h3>Compare people and species</h3>
        <p>Genomes from many individuals and complete ape genomes show when large genomic changes arose and what they changed.</p>
      </li>
    </ul>
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

  <section class="research-future research-wide" aria-labelledby="research-future-title">
    <div class="research-future-head">
      <p class="research-eyebrow">Methods and AI</p>
      <h2 class="research-section-title" id="research-future-title">From new methods to AI-driven genomics</h2>
      <p class="research-section-lead">We build the computational tools our questions require, and we are expanding toward AI models that learn from genomes beyond the reference.</p>
    </div>
    <div class="research-future-grid">
      <div class="research-future-now">
        <h3>Methods we build</h3>
        <p>We develop methods to resolve structural variation in complex genomic regions, compare gene regulation across cell types and species, and reconstruct cell lineages from single-cell DNA methylation. We share them as reproducible, open tools.</p>
      </div>
      <div class="research-future-next">
        <p class="research-future-tag">Looking ahead</p>
        <h3>AI for genomes beyond the reference</h3>
        <p>
          Most genomic AI models learn from a single reference genome, so how differences between individuals, especially large structural changes, alter gene regulation remains hard to predict. Donor-specific genomes paired with cell-resolved epigenomes are the data these models need. Next, we will develop AI approaches that:
        </p>
        <ul>
          <li>Predict how large genomic changes reshape gene regulation.</li>
          <li>Read cell identity, age, and lineage from single-cell epigenomes.</li>
          <li>Pinpoint human-specific changes across complete primate genomes.</li>
        </ul>
        <p class="research-future-note">Students with backgrounds in computer science, statistics, or AI are especially welcome to help shape this direction.</p>
      </div>
    </div>
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
