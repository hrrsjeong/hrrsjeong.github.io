---
layout: home
title: 홈
permalink: /ko/
description: Jeong Lab은 유전체 구조와 후성유전 조절을 통해 인간 진화, 노화, 신경계 질환을 연구합니다.
lang: ko
translation_of: /
---

<section class="home-hero home-wide" aria-label="Jeong Lab 연구 분야">
  <div class="home-hero-copy">
    <h1 class="home-hero-title">
      <span>Computational Genomics</span>
      <span>Evolutionary Medicine</span>
    </h1>
  </div>
</section>

<section class="home-intro" aria-label="Jeong Lab 소개">
  <p>
    Jeong Lab은 다양한 종과 세포 유형의 유전체 구조와 후성유전 조절을 비교하며 인간 진화, 노화, 신경계 질환을 연구합니다. 비교유전체학에 long-read sequencing과 single-cell multi-omics 데이터를 접목해 복잡한 유전체 영역의 구조와 조절 기능을 분석합니다. 또한 대규모 데이터에 담긴 패턴을 찾는 계산 모델을 개발하여, 유전체와 후성유전체의 차이가 유전자 조절에 어떤 영향을 미치는지 밝히고자 합니다.
  </p>
  <div class="home-actions">
    <a class="home-action home-action-primary" href="{{ '/ko/research/' | relative_url }}">연구 소개</a>
    <a class="home-action home-action-secondary" href="{{ '/ko/join/' | relative_url }}">연구실 참여 안내</a>
  </div>
</section>

<section class="recent-news home-wide" aria-labelledby="recent-news-title">
  <div class="home-section-header">
    <h2 id="recent-news-title">연구실 소식</h2>
    <a class="home-section-link" href="{{ '/ko/news/' | relative_url }}">전체 소식 보기 →</a>
  </div>

  <ol class="home-news-list">
    {% assign recent_news = site.news | sort: 'date' | reverse %}
    {% for item in recent_news limit: 6 %}
      <li class="home-news-item">
        <time class="home-news-date" datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: '%Y.%m.%d' }}</time>
        <div class="home-news-copy">{{ item.content_ko | default: item.content | strip_html | strip }}</div>
      </li>
    {% endfor %}
  </ol>
</section>

<section class="featured-publications home-wide" aria-labelledby="featured-publications-title">
  <div class="home-section-header">
    <h2 id="featured-publications-title">주요 논문</h2>
    <div class="featured-publication-actions">
      <a class="home-section-link" href="{{ '/ko/publications/' | relative_url }}">전체 논문 보기 →</a>
    </div>
  </div>

  <div class="featured-carousel-shell">
    <div class="featured-paper-grid" data-featured-carousel>
    <a class="featured-paper" href="https://doi.org/10.1038/s41588-024-02051-8">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2025-natgen-fig1-card.png' | relative_url }}"
          alt="인간의 segmental duplication을 표현한 pangenome 그림"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">유전체 구조 · 2025</div>
        <h3>Structural polymorphism and diversity of human segmental duplications</h3>
        <p>Long-read 기반 유전체 조립을 통해, 염기서열 수준에서 분석하기 어려웠던 중복 영역의 집단 내 다양성을 밝혔습니다.</p>
        <div class="featured-paper-journal">Nature Genetics</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1007/s11357-024-01450-3">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2025-geroscience-fig1-card.png' | relative_url }}"
          alt="나이에 따른 신경세포와 희소돌기아교세포의 DNA 메틸화 변화"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">후성유전적 노화 · 2024</div>
        <h3>Human brain aging is associated with dysregulation of cell type epigenetic identity</h3>
        <p>노화에 따른 DNA 메틸화 변화가 세포 고유의 특성 약화, 뇌 노화, 질환 취약성과 어떻게 연결되는지 분석했습니다.</p>
        <div class="featured-paper-journal">GeroScience</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1038/s41467-021-21917-7">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2021-natcomms-fig1-card.png' | relative_url }}"
          alt="인간과 비인간 영장류의 뇌 세포 유형별 CG·CH 메틸화 비교"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">뇌의 진화 · 2021</div>
        <h3>Evolution of DNA methylation in the human brain</h3>
        <p>세포 유형별 DNA 메틸화 지도를 비교하여 인간 계통에서 변화한 유전자 조절과 신경정신질환 위험의 연관성을 살폈습니다.</p>
        <div class="featured-paper-journal">Nature Communications</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.1038/s41586-025-08816-3">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/yoo-2025-nature-fig1-card.png' | relative_url }}"
          alt="유인원 완전 유전체의 염색체 정렬 비교"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">유인원 유전체 · 2025</div>
        <h3>Complete sequencing of ape genomes</h3>
        <p>6종의 유인원에서 haplotype별로 구분한 참조 유전체를 구축해, 이전에는 분석하기 어려웠던 영역을 살펴보았습니다.</p>
        <div class="featured-paper-journal">Nature</div>
      </div>
    </a>

    <a class="featured-paper" href="https://www.biorxiv.org/content/10.64898/2026.01.22.700871v1">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2026-kidney-fig1-card.jpg' | relative_url }}"
          alt="인간과 생쥐 신장의 세포 유형별 단일세포 DNA 메틸화 지도"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">신장 노화 · 2026</div>
        <h3>A cross-species single-cell epigenome kidney atlas</h3>
        <p>인간과 생쥐 신장의 single-cell multi-omics 데이터를 통해 세포 유형별 노화와 질환 관련 조직 복구 상태를 분석했습니다.</p>
        <div class="featured-paper-journal">Nature Aging · 게재 승인</div>
      </div>
    </a>

    <a class="featured-paper" href="https://doi.org/10.7554/eLife.79387">
      <div class="featured-paper-figure">
        <img
          src="{{ '/assets/img/home/publications/jeong-2022-elife-fig1-card.jpg' | relative_url }}"
          alt="흰목참새의 supergene과 관련된 유전체 분화"
          loading="lazy"
        >
      </div>
      <div class="featured-paper-body">
        <div class="featured-paper-meta">유전체 진화 · 2022</div>
        <h3>Dynamic molecular evolution of a supergene with suppressed recombination</h3>
        <p>집단유전체와 전사체 분석으로 척추동물 supergene 내부의 독특한 진화 양상을 밝혔습니다.</p>
        <div class="featured-paper-journal">eLife</div>
      </div>
    </a>
    </div>

    <div class="featured-carousel-controls" aria-label="주요 논문 탐색">
      <button
        class="featured-carousel-button"
        type="button"
        aria-label="이전 논문"
        data-featured-previous
      >‹</button>
      <button
        class="featured-carousel-button"
        type="button"
        aria-label="다음 논문"
        data-featured-next
      >›</button>
    </div>

  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('[data-featured-carousel]');
    const previousButton = document.querySelector('[data-featured-previous]');
    const nextButton = document.querySelector('[data-featured-next]');

    if (!carousel || !previousButton || !nextButton) return;

    const cards = Array.from(carousel.querySelectorAll('.featured-paper'));

    function visibleCardCount() {
      if (!cards.length) return 1;
      return Math.max(1, Math.round(carousel.clientWidth / cards[0].getBoundingClientRect().width));
    }

    function currentCardIndex() {
      if (!cards.length) return 0;
      const cardWidth = cards[0].getBoundingClientRect().width;
      const gap = parseFloat(window.getComputedStyle(carousel).columnGap) || 0;
      return Math.round(carousel.scrollLeft / (cardWidth + gap));
    }

    function updateButtons() {
      const index = currentCardIndex();
      previousButton.disabled = index <= 0;
      nextButton.disabled = index >= cards.length - visibleCardCount();
    }

    function moveCarousel(direction) {
      const target = Math.min(
        Math.max(currentCardIndex() + direction * visibleCardCount(), 0),
        Math.max(cards.length - visibleCardCount(), 0)
      );
      const cardWidth = cards[0].getBoundingClientRect().width;
      const gap = parseFloat(window.getComputedStyle(carousel).columnGap) || 0;
      carousel.scrollTo({ left: target * (cardWidth + gap), behavior: 'smooth' });
    }

    previousButton.addEventListener('click', function () {
      moveCarousel(-1);
    });
    nextButton.addEventListener('click', function () {
      moveCarousel(1);
    });
    carousel.addEventListener('scroll', updateButtons, { passive: true });
    window.addEventListener('resize', updateButtons);
    updateButtons();
  });
</script>
