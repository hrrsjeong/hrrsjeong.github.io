---
layout: page
permalink: /people/hyeonsoo-jeong/
title: Hyeonsoo "Harris" Jeong
description: Principal Investigator
nav: false
_styles: |
  .pi-profile {
    --profile-accent: #725c78;
    padding-bottom: 2.5rem;
  }
  .post > .post-header {
    display: none;
  }
  footer.fixed-bottom {
    position: static !important;
  }
  .pi-profile-header {
    align-items: start;
    display: grid;
    gap: clamp(2rem, 6vw, 4.5rem);
    grid-template-columns: minmax(13rem, 16rem) minmax(0, 1fr);
    padding: 0.5rem 0 clamp(3rem, 7vw, 5rem);
  }
  .pi-profile-photo {
    display: block;
    height: auto;
    width: 100%;
  }
  .pi-profile-name {
    color: var(--global-text-color);
    font-size: clamp(1.55rem, 3.2vw, 2.15rem);
    font-weight: 540;
    letter-spacing: -0.025em;
    line-height: 1.2;
    margin: 0 0 0.55rem;
  }
  .pi-profile-role {
    color: var(--global-text-color);
    font-size: 1.12rem;
    font-weight: 720;
    line-height: 1.4;
    margin: 0 0 0.55rem;
  }
  .pi-profile-position {
    color: var(--global-text-color);
    font-size: 1rem;
    line-height: 1.48;
    margin: 0;
  }
  .pi-contact {
    display: grid;
    font-size: 0.9rem;
    gap: 0.18rem 1rem;
    grid-template-columns: 4.2rem minmax(0, 1fr);
    line-height: 1.4;
    margin: 1.15rem 0 0;
    max-width: 35rem;
  }
  .pi-contact dt {
    color: var(--global-text-color-light);
    font-weight: 580;
    margin: 0;
  }
  .pi-contact dd {
    color: var(--global-text-color);
    margin: 0;
  }
  .pi-section {
    border-top: 1px solid var(--global-divider-color);
    display: grid;
    gap: clamp(1.6rem, 5vw, 4rem);
    grid-template-columns: minmax(11rem, 0.28fr) minmax(0, 1fr);
    padding-top: clamp(1.5rem, 4vw, 2.2rem);
  }
  .pi-section + .pi-section {
    margin-top: clamp(1.8rem, 4.5vw, 3rem);
  }
  .pi-section h2 {
    color: var(--global-text-color);
    font-size: clamp(1.45rem, 3vw, 1.9rem);
    font-weight: 620;
    letter-spacing: -0.026em;
    line-height: 1.2;
    margin: 0;
  }
  .pi-timeline {
    list-style: none;
    margin: 0;
    max-width: 48rem;
    padding: 0;
  }
  .pi-entry {
    display: grid;
    gap: 1rem;
    grid-template-columns: 8.25rem minmax(0, 1fr);
    padding: 0.78rem 0;
  }
  .pi-entry:first-child {
    padding-top: 0;
  }
  .pi-entry + .pi-entry {
    border-top: 1px solid var(--global-divider-color);
  }
  .pi-entry-period {
    color: var(--profile-accent);
    font-size: 0.84rem;
    font-weight: 670;
    line-height: 1.5;
  }
  .pi-entry h3 {
    color: var(--global-text-color);
    font-size: 1.02rem;
    font-weight: 630;
    line-height: 1.4;
    margin: 0 0 0.2rem;
  }
  .pi-entry p {
    color: var(--global-text-color-light);
    font-size: 0.92rem;
    line-height: 1.45;
    margin: 0;
  }
  .pi-entry p a {
    color: inherit;
    text-decoration: underline;
    text-decoration-color: var(--profile-accent);
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  .pi-biography-copy {
    max-width: 47rem;
  }
  .pi-biography-copy p {
    color: var(--global-text-color);
    font-size: 1rem;
    line-height: 1.75;
    margin: 0 0 1.35rem;
  }
  .pi-biography-copy p:last-child {
    margin-bottom: 0;
  }
  .pi-biography-copy a {
    color: var(--profile-accent);
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.2rem;
  }
  @media (max-width: 720px) {
    .pi-profile-header {
      gap: 1.6rem;
      grid-template-columns: 1fr;
      padding-bottom: 3rem;
    }
    .pi-profile-photo {
      max-width: 16rem;
    }
    .pi-section {
      gap: 1.25rem;
      grid-template-columns: 1fr;
    }
    .pi-entry {
      gap: 0.2rem;
      grid-template-columns: 1fr;
      padding: 0.72rem 0;
    }
    .pi-contact {
      grid-template-columns: 3.8rem minmax(0, 1fr);
    }
  }
---

{% include locale.liquid %}
{% include pi_profile.liquid %}
