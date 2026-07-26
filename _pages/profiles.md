---
layout: page
permalink: /people/
title: Team
nav: true
nav_order: 1
_styles: |
  .principal-section {
    margin-bottom: clamp(2.8rem, 7vw, 4.8rem);
  }
  .principal-card {
    display: grid;
    grid-template-columns: minmax(220px, 29%) 1fr;
    gap: clamp(1.6rem, 4vw, 3.5rem);
    align-items: center;
    border-top: 1px solid var(--global-divider-color);
    border-bottom: 1px solid var(--global-divider-color);
    color: var(--global-text-color);
    padding: clamp(1.2rem, 3vw, 2rem) 0;
  }
  .principal-card img {
    width: 100%;
    aspect-ratio: 4 / 4.35;
    border-radius: 0.35rem;
    display: block;
    object-fit: cover;
    object-position: center 28%;
  }
  .principal-label,
  .team-section-label {
    color: var(--global-theme-color);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    margin: 0 0 0.7rem;
    text-transform: uppercase;
  }
  .principal-name {
    font-size: clamp(1.65rem, 4vw, 2.45rem);
    font-weight: 650;
    letter-spacing: -0.025em;
    line-height: 1.1;
    margin: 0 0 0.55rem;
  }
  .principal-role {
    color: var(--global-text-color-light);
    font-size: 0.96rem;
    font-weight: 600;
    line-height: 1.55;
    margin-bottom: 0;
  }
  .principal-link {
    color: var(--global-theme-color);
    display: inline-block;
    font-size: 0.86rem;
    font-weight: 650;
    margin-top: 1rem;
  }
  .principal-link:hover,
  .principal-link:focus,
  .team-member-link:hover,
  .team-member-link:focus {
    color: var(--global-hover-color);
  }
  .team-section-header {
    align-items: baseline;
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.1rem;
  }
  .team-section-title {
    font-size: clamp(1.45rem, 3vw, 1.9rem);
    font-weight: 600;
    letter-spacing: -0.02em;
    margin: 0;
  }
  .team-member-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: clamp(1.5rem, 5vw, 3.5rem);
  }
  .team-member {
    align-items: center;
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    grid-template-columns: 7.25rem 1fr;
    gap: 1.25rem;
    min-height: 11.5rem;
    padding: 1.35rem 0;
  }
  .team-member:nth-last-child(-n + 2) {
    border-bottom: 1px solid var(--global-divider-color);
  }
  .team-member-media {
    aspect-ratio: 4 / 5;
    overflow: hidden;
    width: 100%;
  }
  .team-member-media img {
    display: block;
    height: 100%;
    object-fit: cover;
    object-position: center 25%;
    width: 100%;
  }
  .team-member-initials {
    align-items: center;
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.3rem;
    color: var(--global-theme-color);
    display: flex;
    font-size: 1rem;
    font-weight: 720;
    height: 100%;
    justify-content: center;
    letter-spacing: 0.06em;
    width: 100%;
  }
  .team-member-name {
    font-size: 1.08rem;
    font-weight: 680;
    line-height: 1.3;
    margin: 0 0 0.3rem;
  }
  .team-member-role {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.45;
    margin: 0;
  }
  .team-member-link {
    color: var(--global-theme-color);
    display: inline-block;
    font-size: 0.82rem;
    font-weight: 650;
    margin-top: 0.85rem;
  }
  @media (max-width: 767px) {
    .principal-card {
      grid-template-columns: minmax(130px, 36%) 1fr;
      gap: 1.2rem;
      align-items: start;
    }
    .team-member-grid {
      grid-template-columns: 1fr;
    }
    .team-member:nth-last-child(-n + 2) {
      border-bottom: 0;
    }
    .team-member:last-child {
      border-bottom: 1px solid var(--global-divider-color);
    }
  }
  @media (max-width: 520px) {
    .principal-card {
      grid-template-columns: 1fr;
    }
    .principal-card img {
      aspect-ratio: 4 / 3.2;
      object-position: center 24%;
    }
    .principal-link {
      margin-top: 0.85rem;
    }
    .team-member {
      grid-template-columns: 6.5rem 1fr;
      min-height: 10.5rem;
    }
  }
---

<section class="principal-section" aria-labelledby="principal-investigator-title">
  <div class="principal-card">
    <img src="{{ '/assets/img/IMG_9534.jpg' | relative_url }}" alt="Hyeonsoo Harris Jeong">
    <div class="principal-copy">
      <p class="principal-label">Principal Investigator</p>
      <h2 class="principal-name" id="principal-investigator-title">Hyeonsoo “Harris” Jeong</h2>
      <div class="principal-role">Assistant Professor · Department of Life Sciences · GIST</div>
      <a class="principal-link" href="{{ '/people/hyeonsoo-jeong/' | relative_url }}">View profile →</a>
    </div>
  </div>
</section>

<section aria-labelledby="lab-members-title">
  <div class="team-section-header">
    <div>
      <p class="team-section-label">Jeong Lab</p>
      <h2 class="team-section-title" id="lab-members-title">Lab Members</h2>
    </div>
  </div>

  <div class="team-member-grid">
    <article class="team-member">
      <div class="team-member-media">
        <div class="team-member-initials" aria-hidden="true">JL</div>
      </div>
      <div>
        <h3 class="team-member-name">Jaewoong Lee</h3>
        <p class="team-member-role">Postdoctoral Researcher</p>
        <a class="team-member-link" href="{{ '/people/jaewoong-lee/' | relative_url }}">View profile →</a>
      </div>
    </article>

    <article class="team-member">
      <div class="team-member-media">
        <div class="team-member-initials" aria-hidden="true">YL</div>
      </div>
      <div>
        <h3 class="team-member-name">Youngseo Lee</h3>
        <p class="team-member-role">Undergraduate Researcher</p>
        <a class="team-member-link" href="{{ '/people/youngseo-lee/' | relative_url }}">View profile →</a>
      </div>
    </article>

    <article class="team-member">
      <div class="team-member-media">
        <div class="team-member-initials" aria-hidden="true">DK</div>
      </div>
      <div>
        <h3 class="team-member-name">Dongkyun Kang</h3>
        <p class="team-member-role">Undergraduate Researcher</p>
        <a class="team-member-link" href="{{ '/people/dongkyun-kang/' | relative_url }}">View profile →</a>
      </div>
    </article>

    <article class="team-member">
      <div class="team-member-media">
        <div class="team-member-initials" aria-hidden="true">DR</div>
      </div>
      <div>
        <h3 class="team-member-name">Dayoung Ryu</h3>
        <p class="team-member-role">Undergraduate Researcher</p>
        <a class="team-member-link" href="{{ '/people/dayoung-ryu/' | relative_url }}">View profile →</a>
      </div>
    </article>
  </div>
</section>
