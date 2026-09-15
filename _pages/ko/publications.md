---
layout: page
permalink: /ko/publications/
title: 논문
description: Jeong Lab의 출판 전 논문과 학술지 게재 논문입니다.
nav: false
nav_order: 3
lang: ko
translation_of: /publications/
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2 class="publication-section-title">출판 전 논문 (Preprints)</h2>

{% bibliography --group_by none --query @*[status=preprint] %}

<h2 class="publication-section-title publication-section-title--peer-reviewed">학술지 게재 논문</h2>

{% bibliography --query @*[status!=preprint] %}

</div>
