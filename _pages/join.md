---
layout: page
permalink: /join/
title: Join
display_title: Join the Lab
description: Opportunities for postdocs, graduate students, bioinformatics specialists, and undergraduate researchers.
nav: true
nav_order: 4
_styles: |
  .join-hero {
    border-left: 4px solid var(--global-theme-color);
    padding: 1.25rem 1.5rem;
    margin-bottom: 2rem;
    background: var(--global-bg-color);
    box-shadow: 0 0.25rem 1rem rgba(0, 0, 0, 0.06);
  }
  .join-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0 2rem;
  }
  .join-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.5rem;
    padding: 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
    cursor: pointer;
    min-height: 9rem;
  }
  .join-card:hover,
  .join-card:focus {
    transform: translateY(-2px);
    box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.08);
    border-color: var(--global-theme-color);
    text-decoration: none;
  }
  .join-card .role {
    font-weight: 700;
    margin-bottom: 0.4rem;
  }
  .join-card .tagline {
    color: var(--global-text-color-light);
    font-size: 0.95rem;
  }
  .availability-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    border-radius: 0.45rem;
    padding: 0.45rem 0.65rem;
    margin-top: 0.85rem;
    color: #ffffff;
    background: linear-gradient(135deg, #1f7a8c, #2b9348);
    box-shadow: 0 0.35rem 1rem rgba(31, 122, 140, 0.22);
    font-weight: 700;
    font-size: 0.9rem;
  }
  .availability-pill .count {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 0.35rem;
    padding: 0.08rem 0.4rem;
    font-variant-numeric: tabular-nums;
  }
  .availability-box {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    border: 1px solid rgba(31, 122, 140, 0.35);
    border-left: 5px solid #1f7a8c;
    border-radius: 0.5rem;
    padding: 0.75rem 0.9rem;
    margin: 0.25rem 0 1rem;
    background: rgba(31, 122, 140, 0.08);
  }
  .availability-box i {
    color: #1f7a8c;
    font-size: 1.3rem;
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
    border: 1px solid var(--global-theme-color);
    color: var(--global-theme-color);
    border-radius: 999px;
    padding: 0.15rem 0.55rem;
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
    <div class="availability-pill"><i class="fa-solid fa-user-plus"></i><span class="count">2</span> openings</div>
  </a>
  <a class="join-card" href="#graduate-students">
    <div class="role">Graduate Students</div>
    <div class="tagline">Join through the Department of Life Sciences at GIST and develop a thesis project in genome science.</div>
    <div class="availability-pill"><i class="fa-solid fa-user-graduate"></i><span class="count">2</span> M.S.-Ph.D. or Ph.D.</div>
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

<div id="postdocs" class="join-section">
  <h2>Postdocs</h2>
  <div class="availability-box">
    <i class="fa-solid fa-user-plus"></i>
    <div>
      <span class="label">Available positions</span>
      <span class="value">2 postdoctoral fellow positions</span>
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
      <span class="value">2 M.S.-Ph.D. integrated or Ph.D. positions</span>
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
