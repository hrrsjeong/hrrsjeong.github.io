---
layout: page
permalink: /join/
title: Join
display_title: Join the Lab
description: Opportunities for postdocs, graduate students, bioinformatics specialists, and undergraduate researchers at the Jeong Lab at GIST.
nav: true
nav_order: 4
_styles: |
  :root {
    --join-accent: #5d4c66;
    --join-soft: rgba(93, 76, 102, 0.075);
    --join-shadow: rgba(0, 0, 0, 0.05);
  }
  html[data-theme="dark"] {
    --join-accent: #b29cb6;
    --join-soft: rgba(178, 156, 182, 0.12);
  }
  .join-hero {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.3rem;
    padding: 1.3rem 1.45rem;
    margin-bottom: 1.8rem;
    background: var(--global-card-bg-color);
    box-shadow: 0 0.2rem 0.8rem var(--join-shadow);
    line-height: 1.72;
  }
  .join-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin: 1.4rem 0 2.2rem;
  }
  .join-card {
    position: relative;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.3rem;
    padding: 1.1rem;
    background: var(--global-bg-color);
    transition: border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
    cursor: pointer;
    min-height: 9.8rem;
  }
  .join-card:hover,
  .join-card:focus {
    border-color: var(--join-accent);
    box-shadow: 0 0.35rem 1.1rem var(--join-shadow);
    text-decoration: none;
    transform: translateY(-2px);
  }
  .join-card .role {
    color: var(--global-text-color);
    font-weight: 700;
    margin-bottom: 0.45rem;
  }
  .join-card .tagline {
    color: var(--global-text-color-light);
    font-size: 0.92rem;
    line-height: 1.52;
  }
  .availability-pill {
    display: inline-flex;
    align-items: center;
    align-self: flex-start;
    gap: 0.4rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.22rem;
    padding: 0.32rem 0.52rem;
    margin-top: auto;
    padding-top: 0.32rem;
    color: var(--join-accent);
    background: var(--join-soft);
    font-weight: 620;
    font-size: 0.84rem;
  }
  .join-card .tagline {
    margin-bottom: 0.9rem;
  }
  .availability-pill i {
    color: var(--join-accent);
  }
  .availability-pill .count {
    font-variant-numeric: tabular-nums;
  }
  .why-join-section {
    border-top: 1px solid var(--global-divider-color);
    padding-top: 1.6rem;
    margin: 0 0 2.2rem;
  }
  .why-join-section > h2 {
    font-size: clamp(1.35rem, 2.6vw, 1.7rem);
    font-weight: 630;
    letter-spacing: -0.02em;
    margin: 0 0 0.65rem;
  }
  .why-join-lead {
    color: var(--global-text-color-light);
    font-size: 0.96rem;
    line-height: 1.68;
    margin: 0 0 1.2rem;
  }
  .join-tracks {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .join-track-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.28rem;
    padding: 1.15rem 1.25rem;
    background: var(--global-card-bg-color);
  }
  .join-track-label {
    color: var(--join-accent);
    font-size: 0.74rem;
    font-weight: 740;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin: 0 0 0.38rem;
  }
  .join-track-card h3 {
    font-size: 1.04rem;
    font-weight: 650;
    line-height: 1.35;
    margin: 0 0 0.5rem;
  }
  .join-track-card p {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.62;
    margin: 0;
  }
  .training-panel {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
    align-items: start;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.28rem;
    padding: 1.15rem 1.25rem;
    background: var(--global-card-bg-color);
  }
  .training-panel i {
    color: var(--join-accent);
    font-size: 1.2rem;
    margin-top: 0.15rem;
  }
  .training-panel h3 {
    font-size: 1.04rem;
    font-weight: 650;
    margin: 0 0 0.4rem;
  }
  .training-panel p {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.62;
    margin-bottom: 0;
  }
  .availability-box {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.3rem;
    padding: 0.75rem 0.9rem;
    margin: 0.25rem 0 1rem;
    background: var(--join-soft);
  }
  .availability-box i {
    color: var(--join-accent);
    font-size: 1.15rem;
  }
  .availability-box .label {
    display: block;
    color: var(--global-text-color-light);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.04rem;
    text-transform: uppercase;
  }
  .availability-box .value {
    display: block;
    font-weight: 700;
  }
  .join-section {
    border-top: 1px solid var(--global-divider-color);
    padding-top: 1.4rem;
    margin-top: 1.4rem;
  }
  .join-section h2 {
    font-size: clamp(1.3rem, 2.4vw, 1.6rem);
    font-weight: 620;
    margin-bottom: 0.75rem;
  }
  .join-badge {
    display: inline-block;
    border: 1px solid var(--global-divider-color);
    color: var(--global-text-color);
    border-radius: 0.22rem;
    padding: 0.16rem 0.5rem;
    background: var(--global-card-bg-color);
    font-size: 0.8rem;
    margin: 0 0.3rem 0.35rem 0;
  }
  .join-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.38rem;
    margin-top: 0.5rem;
    color: var(--join-accent);
    font-weight: 650;
  }
  @media (max-width: 720px) {
    .join-tracks {
      grid-template-columns: 1fr;
    }
  }
---

<div class="join-hero">
  <p class="mb-0">
    The Jeong Lab at GIST investigates how genomes and epigenomes evolve across primates, vary across human populations, and change within individual cells during aging and disease. We are recruiting curious, motivated researchers who want to combine deep biological questions with rigorous computational and AI methods.
  </p>
</div>

<div class="join-grid">
  <a class="join-card" href="#postdocs">
    <div class="role">Postdocs</div>
    <div class="tagline">Lead independent studies in comparative genomics, pangenomes, single-cell epigenomics, or genomic AI.</div>
    <div class="availability-pill"><i class="fa-solid fa-user-plus"></i><span class="count">1</span> opening</div>
  </a>
  <a class="join-card" href="{{ '/join/graduate-research/' | relative_url }}">
    <div class="role">Graduate Students</div>
    <div class="tagline">Join through the Department of Life Sciences at GIST and lead a doctoral project in computational genomics.</div>
    <div class="availability-pill"><i class="fa-solid fa-user-graduate"></i><span class="count">3</span> M.S.-Ph.D. or Ph.D.</div>
  </a>
  <a class="join-card" href="#bioinformatics-specialist">
    <div class="role">Bioinformatics Specialist</div>
    <div class="tagline">Develop scalable workflows for long-read assemblies, pangenomes, and single-cell multi-omics datasets.</div>
    <div class="availability-pill"><i class="fa-solid fa-laptop-code"></i><span class="count">1</span> opening</div>
  </a>
  <a class="join-card" href="{{ '/join/undergraduate-research/' | relative_url }}">
    <div class="role">Undergraduates</div>
    <div class="tagline">Gain hands-on experience in large-scale genomic data analysis and quantitative biology.</div>
    <div class="availability-pill"><i class="fa-solid fa-seedling"></i>Rolling basis</div>
  </a>
</div>

<section class="why-join-section" aria-labelledby="why-join-title">
  <h2 id="why-join-title">Training Across Biology and Computation</h2>
  <p class="why-join-lead">
    Modern genome science requires researchers who understand both complex biology and quantitative modeling. We welcome members from two complementary backgrounds and tailor mentorship to each person's strengths and career goals.
  </p>

  <div class="join-tracks">
    <div class="join-track-card">
      <p class="join-track-label">Life Sciences &amp; Biomedicine</p>
      <h3>From Biological Questions to Quantitative Mastery</h3>
      <p>
        Students from biology, biotechnology, or biomedical sciences start from core questions in brain evolution, human genetic diversity, and cellular aging while receiving structured training in Linux/HPC, Python/R, pangenome analysis, single-cell multi-omics, and statistical modeling.
      </p>
    </div>
    <div class="join-track-card">
      <p class="join-track-label">CS, Statistics, Math &amp; AI</p>
      <h3>Statistical Modeling and AI for Complex Genomes</h3>
      <p>
        Researchers with quantitative backgrounds go beyond running standard bioinformatics pipelines to develop analytical methods for structurally complex genome regions, statistical models for single-cell and 3D epigenomes, and machine learning and AI models for multi-omic integration, aging, and disease.
      </p>
    </div>
  </div>

  <div class="training-panel">
    <i class="fa-solid fa-compass"></i>
    <div>
      <h3>Mentorship and Research Environment</h3>
      <p>
        Lab members work directly with large-scale long-read pangenome and single-cell multi-omics datasets alongside domestic and international collaborators. From formulating questions and designing computational approaches to biological interpretation and manuscript writing, trainees work closely with the PI and postdoctoral researchers to lead first-author publications and prepare for careers in academia, research institutes, or the biotech and AI industry.
      </p>
    </div>
  </div>
</section>

<div id="postdocs" class="join-section">
  <h2>Postdocs</h2>
  <div class="availability-box">
    <i class="fa-solid fa-user-plus"></i>
    <div>
      <span class="label">Available positions</span>
      <span class="value">1 postdoctoral fellow position</span>
    </div>
  </div>
  <p>
    We seek motivated postdoctoral researchers with a Ph.D. in evolutionary genomics, computational biology, bioinformatics, epigenomics, computer science, statistics, or a related field. Candidates should have strong programming skills and experience analyzing large-scale sequencing, single-cell, or quantitative biological datasets.
  </p>
  <div>
    <span class="join-badge">comparative &amp; pangenome genomics</span>
    <span class="join-badge">single-cell epigenomics</span>
    <span class="join-badge">statistical modeling &amp; AI</span>
    <span class="join-badge">method development</span>
  </div>
  <p>
    Please email your CV, a brief description of past research and future interests, and contact information for three references.
  </p>
  <a class="join-cta" href="mailto:jeonglab.gist@gmail.com?subject=Postdoc%20application%20-%20Jeong%20Lab">
    <i class="fa-solid fa-envelope"></i> Email about this position
  </a>
</div>

<div id="graduate-students" class="join-section">
  <h2>Graduate Students</h2>
  <div class="availability-box">
    <i class="fa-solid fa-user-graduate"></i>
    <div>
      <span class="label">Available positions</span>
      <span class="value">3 M.S.-Ph.D. integrated or Ph.D. positions</span>
    </div>
  </div>
  <p>
    Graduate students join through the Department of Life Sciences at GIST (applicants from all undergraduate majors, including biology, computer science, statistics, mathematics, and engineering, are eligible). Projects span primate and human evolution, pangenomes and complex structural variation, single-cell epigenetic aging and disease, and machine learning/AI for genomics.
  </p>
  <div>
    <span class="join-badge">genome evolution &amp; diversity</span>
    <span class="join-badge">long-read &amp; pangenome</span>
    <span class="join-badge">single-cell &amp; 3D multi-omics</span>
    <span class="join-badge">cellular aging &amp; AI</span>
  </div>
  <p>
    Prospective students are encouraged to reach out prior to formal admission with a CV or brief introduction, research interests, relevant coursework or project experience, and an academic transcript.
  </p>
  <a class="join-cta" href="{{ '/join/graduate-research/' | relative_url }}">
    <i class="fa-solid fa-arrow-right"></i> View graduate research details and project topics
  </a>
</div>

<div id="bioinformatics-specialist" class="join-section">
  <h2>Bioinformatics Specialist</h2>
  <div class="availability-box">
    <i class="fa-solid fa-laptop-code"></i>
    <div>
      <span class="label">Available positions</span>
      <span class="value">1 bioinformatics specialist position</span>
    </div>
  </div>
  <p>
    We are recruiting a bioinformatics specialist with strong Python/R and Linux skills to build reproducible pipelines and contribute to research projects involving long-read genome assembly, structural variation, epigenomic profiling, or single-cell multi-omics.
  </p>
  <div>
    <span class="join-badge">Python / R / Linux</span>
    <span class="join-badge">reproducible workflows</span>
    <span class="join-badge">long-read &amp; variant analysis</span>
    <span class="join-badge">single-cell data</span>
  </div>
  <p>
    Prior experience with long-read sequencing or single-cell analysis is helpful but not required. Please send a CV/resume and a short summary of relevant computational projects.
  </p>
  <a class="join-cta" href="mailto:jeonglab.gist@gmail.com?subject=Bioinformatics%20specialist%20-%20Jeong%20Lab">
    <i class="fa-solid fa-envelope"></i> Email about this position
  </a>
</div>

<div id="undergraduates" class="join-section">
  <h2>Undergraduates</h2>
  <div class="availability-box">
    <i class="fa-solid fa-seedling"></i>
    <div>
      <span class="label">Available positions</span>
      <span class="value">Open on a rolling basis</span>
    </div>
  </div>
  <p>
    We welcome undergraduate interns from life sciences as well as computer science, AI, statistics, or related majors. Prior coding experience is helpful, and we provide step-by-step training in Linux, Python/R, and large-scale genomic data analysis for motivated students who can participate consistently.
  </p>
  <div>
    <span class="join-badge">computational genomics</span>
    <span class="join-badge">hands-on data analysis</span>
    <span class="join-badge">machine learning</span>
    <span class="join-badge">mentored research</span>
  </div>
  <p>
    Interested students should email a short self-introduction, research interests, relevant coursework or coding experience, expected period of participation, and a transcript.
  </p>
  <a class="join-cta" href="{{ '/join/undergraduate-research/' | relative_url }}">
    <i class="fa-solid fa-arrow-right"></i> View undergraduate research details
  </a>
</div>
