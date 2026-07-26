---
layout: page
permalink: /publications/
title: Publications
description: Preprints and peer-reviewed publications from the Jeong Lab.
nav: true
nav_order: 3
_styles: |
  .publication-section-title {
    color: var(--global-text-color);
    font-size: clamp(1.45rem, 3vw, 1.9rem);
    font-weight: 620;
    letter-spacing: -0.025em;
    margin: 2.5rem 0 1rem;
  }
  .publication-section-title:first-child {
    margin-top: 0;
  }
  .publication-section-title--peer-reviewed {
    border-top: 1px solid var(--global-divider-color);
    margin-top: clamp(3rem, 7vw, 4.5rem);
    padding-top: clamp(1.8rem, 4vw, 2.5rem);
  }
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2 class="publication-section-title">Preprints</h2>

{% bibliography --group_by none --query @*[status=preprint] %}

<h2 class="publication-section-title publication-section-title--peer-reviewed">Peer-reviewed Publications</h2>

{% bibliography --query @*[status!=preprint] %}

</div>
