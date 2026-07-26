---
layout: page
permalink: /join/
title: Join
display_title: Join the Lab
description: Opportunities for postdocs, graduate students, bioinformatics specialists, and undergraduate researchers.
nav: true
nav_order: 4
_styles: |
  :root {
    --join-accent: #2f6f73;
    --join-soft: rgba(47, 111, 115, 0.07);
    --join-shadow: rgba(0, 0, 0, 0.055);
  }
  .join-hero {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
    padding: 1.2rem 1.35rem;
    margin-bottom: 2rem;
    background: var(--global-card-bg-color);
    box-shadow: 0 0.2rem 0.8rem var(--join-shadow);
  }
  .join-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 1.1rem;
    margin: 1.5rem 0 2rem;
  }
  .join-card {
    position: relative;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
    padding: 1.05rem;
    background: var(--global-bg-color);
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    cursor: pointer;
    min-height: 9.4rem;
  }
  .join-card:hover,
  .join-card:focus {
    border-color: var(--global-theme-color);
    box-shadow: 0 0.35rem 1.1rem var(--join-shadow);
    text-decoration: none;
  }
  .join-card .role {
    font-weight: 700;
    margin-bottom: 0.45rem;
  }
  .join-card .tagline {
    color: var(--global-text-color-light);
    font-size: 0.95rem;
  }
  .availability-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.25rem;
    padding: 0.35rem 0.5rem;
    margin-top: 0.95rem;
    color: var(--join-accent);
    background: var(--join-soft);
    font-weight: 600;
    font-size: 0.88rem;
  }
  .availability-pill i {
    color: var(--join-accent);
  }
  .availability-pill .count {
    font-variant-numeric: tabular-nums;
  }
  .availability-box {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
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
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.02rem;
    text-transform: uppercase;
  }
  .availability-box .value {
    display: block;
    font-weight: 700;
  }
  .join-section {
    border-top: 1px solid var(--global-divider-color);
    padding-top: 1.25rem;
    margin-top: 1.25rem;
  }
  .join-section h2 {
    margin-bottom: 0.75rem;
  }
  .join-badge {
    display: inline-block;
    border: 1px solid var(--global-divider-color);
    color: var(--global-text-color);
    border-radius: 0.25rem;
    padding: 0.16rem 0.48rem;
    background: var(--global-card-bg-color);
    font-size: 0.8rem;
    margin: 0 0.3rem 0.3rem 0;
  }
  .join-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    margin-top: 0.5rem;
    font-weight: 600;
  }
  .training-panel {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
    align-items: start;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
    padding: 1.15rem 1.25rem;
    margin: 0 0 2rem;
    background: var(--global-card-bg-color);
    box-shadow: 0 0.2rem 0.8rem var(--join-shadow);
  }
  .training-panel i {
    color: var(--join-accent);
    font-size: 1.25rem;
    margin-top: 0.1rem;
  }
  .training-panel h2 {
    margin: 0 0 0.5rem;
  }
  .training-panel p {
    margin-bottom: 0;
  }
---

<div class="join-hero">
  <p class="mb-0">
    The Jeong Lab is building a computational and experimental genomics group at GIST to study genome evolution, epigenomic regulation, aging, and disease susceptibility. We welcome applications from people who enjoy quantitative biology, careful data analysis, and collaborative science.
  </p>
</div>

<div class="join-grid">
  <a class="join-card" href="#postdocs">
    <div class="role">Postdocs</div>
    <div class="tagline">Lead independent projects in evolutionary genomics, epigenomics, and computational biology.</div>
    <div class="availability-pill"><i class="fa-solid fa-user-plus"></i><span class="count">1</span> opening</div>
  </a>
  <a class="join-card" href="#graduate-students">
    <div class="role">Graduate Students</div>
    <div class="tagline">Join through the Department of Life Sciences at GIST and develop a thesis project in genome science.</div>
    <div class="availability-pill"><i class="fa-solid fa-user-graduate"></i><span class="count">3</span> M.S.-Ph.D. or Ph.D.</div>
  </a>
  <a class="join-card" href="#bioinformatics-specialist">
    <div class="role">Bioinformatics Specialist</div>
    <div class="tagline">Build analysis workflows for sequencing, comparative genomics, and long-read genome projects.</div>
    <div class="availability-pill"><i class="fa-solid fa-laptop-code"></i><span class="count">1</span> opening</div>
  </a>
  <a class="join-card" href="#undergraduates">
    <div class="role">Undergraduates</div>
    <div class="tagline">Learn computational biology through hands-on research and data analysis.</div>
    <div class="availability-pill"><i class="fa-solid fa-seedling"></i>Rolling basis</div>
  </a>
</div>

<div class="training-panel">
  <i class="fa-solid fa-route"></i>
  <div>
    <h2>Training and Career Development</h2>
    <p>
      The Jeong Lab aims to train scientists who can move confidently across academic, industry, and interdisciplinary research environments. Trainees are encouraged to discuss their goals early and shape their training accordingly. Projects in the lab are designed to build rigorous scientific thinking, strong computational skills, reproducible analysis practices, and clear communication.
    </p>
  </div>
</div>

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
    The lab is seeking highly motivated postdoctoral researchers with backgrounds in evolutionary genomics, bioinformatics, genomics, epigenomics, computational biology, or related fields. Strong programming skills are expected, including experience analyzing large genomic datasets.
  </p>
  <div>
    <span class="join-badge">evolutionary genomics</span>
    <span class="join-badge">bioinformatics</span>
    <span class="join-badge">genomics</span>
    <span class="join-badge">programming</span>
  </div>
  <p>
    Applicants should send a CV, a brief statement of research interests, and the names and contact information of three references.
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
    Graduate students join the lab through the Department of Life Sciences at GIST. The lab welcomes students interested in bioinformatics, comparative genomics, epigenomics, genome evolution, long-read sequencing, single-cell genomics, and computational approaches to aging and disease biology.
  </p>
  <div>
    <span class="join-badge">comparative genomics</span>
    <span class="join-badge">epigenomics</span>
    <span class="join-badge">single-cell data</span>
    <span class="join-badge">aging</span>
  </div>
  <p>
    Prospective students should email me with a description of their research interests, relevant coursework or research experience, and an academic transcript.
  </p>
  <a class="join-cta" href="mailto:jeonglab.gist@gmail.com?subject=Prospective%20graduate%20student%20-%20Jeong%20Lab">
    <i class="fa-solid fa-envelope"></i> Email about this position
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
    The lab is recruiting a bioinformatics specialist with strong programming skills and experience analyzing sequencing or genomic datasets. Experience with workflow development, reproducible analysis, variant analysis, genome assembly, epigenomic data, or single-cell data is valuable.
  </p>
  <div>
    <span class="join-badge">Python/R</span>
    <span class="join-badge">sequencing data</span>
    <span class="join-badge">workflow development</span>
    <span class="join-badge">long-read sequencing preferred</span>
  </div>
  <p>
    Experience with long-read sequencing is preferred but not required. Applicants should send a CV or resume and a short description of relevant computational projects.
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
    The lab also welcomes undergraduate students interested in computational biology, genomics, evolution, epigenetics, or aging research. Prior programming or statistics experience is helpful, but curiosity, consistency, and willingness to learn are most important.
  </p>
  <div>
    <span class="join-badge">computational biology</span>
    <span class="join-badge">genomics</span>
    <span class="join-badge">data analysis</span>
    <span class="join-badge">research training</span>
  </div>
  <p>
    Interested students should email me with a short introduction, research interests, relevant coursework, and any programming or research experience.
  </p>
  <a class="join-cta" href="mailto:jeonglab.gist@gmail.com?subject=Undergraduate%20research%20-%20Jeong%20Lab">
    <i class="fa-solid fa-envelope"></i> Email about this position
  </a>
</div>
