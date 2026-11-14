---
layout: page
permalink: /ko/research/
title: 연구
display_title: 연구
description: 영장류와 인간의 진화, 복잡한 유전체 구조와 집단 내 다양성, 세포 노화와 질환, 계산 방법론과 AI 모델링을 중심으로 한 Jeong Lab의 주요 연구 분야입니다.
nav: false
nav_order: 2
lang: ko
translation_of: /research/
---

<div class="research-page">
  <section class="research-intro" aria-labelledby="research-statement">
    <h2 class="research-statement" id="research-statement">인간 유전체는 어떻게 진화하고, 개인마다 달라지며, 세포 수준에서 노화하는가</h2>
    <p class="research-lead">
      유전체와 후성유전체의 변화는 수백만 년의 영장류 진화, 인류 집단 내 개인 간 분화, 그리고 한 사람의 일생에 걸친 개별 세포의 노화라는 서로 다른 스케일에서 일어납니다. Jeong Lab은 long-read genome assembly와 pangenome, single-cell 및 3D multi-omics, 그리고 통계와 AI 모델링을 결합하여 유전체와 후성유전체의 변화가 세포 기능, 노화, 질병 취약성으로 이어지는 원리를 연구합니다.
    </p>
  </section>

  <figure class="research-overview-figure research-wide">
    <img
      src="{{ '/assets/img/research/research-overview-diagram.png' | relative_url }}"
      alt="영장류 진화, 인간 pangenome, 단일세포 후성유전체 데이터를 계산 및 AI 모델링으로 통합하여 뇌 진화와 질환, 집단 내 형질 다양성, 세포 노화와 복구 실패를 규명하는 Jeong Lab 연구 개요도"
    >
    <figcaption class="research-overview-caption">
      영장류 비교유전체, 인간 pangenome, 단일세포 및 3D 후성유전체 데이터(왼쪽)를 알고리즘, 통계 모델, 유전체 AI(가운데)로 통합하여 뇌 조절 진화, 집단 내 형질 다양성, 세포 노화와 조직 복구 기전(오른쪽)을 연구합니다.
    </figcaption>
  </figure>

  <section class="research-questions research-wide" aria-labelledby="research-questions-title">
    <div class="research-questions-heading">
      <h2 id="research-questions-title">핵심 질문</h2>
      <p>유전체 구조와 세포별 조절, 인간 질환을 관통하는 연구 질문들입니다.</p>
    </div>
    <ul class="research-question-list">
      <li>인간과 다른 영장류를 구분 짓는 유전체 재편성과 세포 유형별 조절 변화는 무엇이며, 왜 신경정신질환 취약성으로 이어지는가?</li>
      <li>하나의 reference genome이 담지 못하는 segmental duplication과 대규모 구조변이는 어떻게 개인 간 다양성과 새로운 중복 유전자를 만들어내는가?</li>
      <li>살아가는 동안 세포마다 축적되는 epimutation은 어떻게 세포 정체성을 약화시키고, 조직 복구 실패와 노화 관련 만성 질환으로 이어지는가?</li>
      <li>유전체 서열과 3차원 후성유전체 정보가 세포 상태와 표현형으로 이어지는 규칙을 통계 모델과 AI로 어떻게 정량화하고 예측할 수 있는가?</li>
    </ul>
  </section>

  <section class="research-work research-wide" aria-label="주요 연구 분야">
    <article class="research-story" id="evolution">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/epigenetic-evolution.png' | relative_url }}" alt="인간, 침팬지, 마카크 원숭이 뇌의 신경세포 및 희소돌기아교세포별 DNA 메틸화 진화 비교">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">01 / Evolutionary Scale</p>
        <h3>영장류와 인간의 진화</h3>
        <p>
          인간과 비인간 영장류는 유전체 서열의 대부분을 공유하지만, 진화 과정에서 축적된 유전변이와 유전자 조절 변화는 인간 고유의 뇌 발달과 인지 기능을 만들었습니다. 인간과 유인원의 high-quality genome assembly 및 발달 단계별, 세포 유형별 후성유전체를 비교하여 인간 계통에서 새롭게 출현한 유전자와 조절 요소를 규명합니다.
        </p>
        <p>
          특히 신경세포와 교세포에서 진화적으로 빠르게 변화한 조절 영역이 조현병을 비롯한 신경발달장애 및 신경정신질환 위험 변이와 어떻게 맞물려 있는지 분석합니다.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Primate comparative genomics</span>
          <span class="research-focus-tag">Cell-type brain epigenomes</span>
          <span class="research-focus-tag">Human-specific regulation</span>
          <span class="research-focus-tag">Neuropsychiatric risk</span>
        </div>
        <p class="research-story-papers">
          관련 대표 논문:
          <a href="https://doi.org/10.1038/s41467-021-21917-7"><em>Nature Communications</em> (2021)</a>,
          <a href="https://doi.org/10.1038/s41586-025-08816-3"><em>Nature</em> (2025)</a>,
          <a href="https://doi.org/10.1038/s41586-024-07473-2"><em>Nature</em> (2024)</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse" id="diversity">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/structurally-complex-regions.png' | relative_url }}" alt="구조변이와 segmental duplication이 집중된 복잡한 염색체 영역의 정렬 비교">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">02 / Population Scale</p>
        <h3>복잡한 유전체 구조와 집단 내 다양성</h3>
        <p>
          흔히 사람들의 유전체가 거의 동일하다고 배우지만, 실제로는 개인마다 유전체 구조에 상당한 차이가 존재합니다. 큰 DNA 블록이 반복되는 segmental duplication과 역위, 결실, 복제수 변이 등 대규모 구조변이(structural variation)는 유전체에서 가장 역동적으로 재조합되는 영역으로, 새로운 중복 유전자(duplicated genes)의 출현과 질환 취약성에 중요하게 작용합니다.
        </p>
        <p>
          기존 short-read sequencing으로는 서열 수준에서 분해하기 어려웠던 이러한 복잡 영역을 long-read genome assembly와 human pangenome 수준에서 정밀하게 분석하고, 집단 내 유전적 및 후성유전적 다양성이 유전자 발현과 표현형 차이로 이어지는 과정을 밝힙니다.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Segmental duplication</span>
          <span class="research-focus-tag">Structural variation</span>
          <span class="research-focus-tag">Duplicated gene emergence</span>
          <span class="research-focus-tag">Human pangenome</span>
        </div>
        <p class="research-story-papers">
          관련 대표 논문:
          <a href="https://doi.org/10.1038/s41588-024-02051-8"><em>Nature Genetics</em> (2025)</a>,
          <a href="https://doi.org/10.1016/j.cell.2024.01.052"><em>Cell</em> (2024)</a>,
          <a href="https://doi.org/10.7554/eLife.79387"><em>eLife</em> (2022)</a>
        </p>
      </div>
    </article>

    <article class="research-story" id="aging">
      <div class="research-story-media">
        <div class="research-story-media-box">
          <img src="{{ '/assets/img/research/epigenetic-aging.png' | relative_url }}" alt="인간과 생쥐 신장의 세포 유형별 단일세포 후성유전체 지도">
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">03 / Cellular Scale</p>
        <h3>세포 노화와 질환</h3>
        <p>
          노화와 만성 질환은 조직 전체의 평균이 아니라 개별 세포의 후성유전체 변화에서 시작됩니다. 뇌와 신장 등 주요 조직의 single-cell DNA methylation, 염색질 접근성, 3D 유전체 구조, 전사체 데이터를 통합하여 나이가 들면서 세포마다 epimutation이 어떻게 쌓이고 세포 고유의 정체성(cell identity)이 약화되는지, 그리고 손상된 조직의 복구가 왜 실패하는지 추적합니다.
        </p>
        <p>
          아울러 인간과 모델 생물의 단일세포 후성유전체를 비교해 진화적으로 보존된 노화 경로를 규명하고, 세포 리프로그래밍 및 노화 역전 과정에서 후성유전체가 어떻게 재편되는지 연구합니다.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Single-cell &amp; 3D epigenomics</span>
          <span class="research-focus-tag">Somatic epimutation</span>
          <span class="research-focus-tag">Cell identity &amp; failed repair</span>
          <span class="research-focus-tag">Cellular rejuvenation</span>
        </div>
        <p class="research-story-papers">
          관련 대표 논문:
          <a href="https://doi.org/10.1038/s43587-026-01221-z"><em>Nature Aging</em> (2026)</a>,
          <a href="https://doi.org/10.1007/s11357-024-01450-3"><em>GeroScience</em> (2025)</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse" id="methods">
      <div class="research-story-media">
        <div class="research-method-stack" aria-label="주요 계산 및 AI 방법론 분야">
          <div class="research-method-card">
            <h4>Pangenome &amp; Structural Variation Algorithms</h4>
            <p>반복 서열이 밀집된 segmental duplication, 복합 구조변이, 개인별 genome assembly 간 차이를 염기서열 수준에서 정밀 분석하는 알고리즘</p>
          </div>
          <div class="research-method-card">
            <h4>Single-Cell &amp; 3D Epigenome Modeling</h4>
            <p>희소한 single-cell DNA methylation과 3D 염색질 구조, 다중 오믹스 데이터를 정량적으로 통합하고 세포 상태 변화를 추론하는 통계 모델</p>
          </div>
          <div class="research-method-card">
            <h4>Machine Learning &amp; Genomic AI</h4>
            <p>DNA 서열 변이와 염색질 맥락이 세포 유형별 유전자 조절과 표현형으로 이어지는 규칙을 학습하고 예측하는 딥러닝 및 foundation model 연구</p>
          </div>
        </div>
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">04 / Methods &amp; AI</p>
        <h3>계산 방법론과 AI 모델링</h3>
        <p>
          구조가 복잡한 유전체 영역과 대규모 single-cell multi-omics 데이터를 정확하게 해석하기 위한 통계 모델과 생물정보학 알고리즘을 개발합니다. 반복 서열과 reference bias로 인한 왜곡을 보정하여 실제 생물학적 변이를 분리하고, 단일세포 후성유전체 데이터로부터 세포 상태 전이나 체세포 epimutation에 기반한 세포 계통 관계(clonal lineage) 등을 추론하는 계산 프레임워크를 구축합니다.
        </p>
        <p>
          이와 함께 유전체 서열과 세포 유형별 유전자 조절, 진화적 보존성, 질환 변이의 기능적 영향을 연결하는 머신러닝 및 AI 모델을 연구하며, 개발한 방법론을 재현 가능한 오픈소스 도구로 공개합니다.
        </p>
        <div class="research-focus-tags">
          <span class="research-focus-tag">Pangenome bioinformatics</span>
          <span class="research-focus-tag">Single-cell statistical models</span>
          <span class="research-focus-tag">Sequence-to-regulation AI</span>
          <span class="research-focus-tag">Open-source tools</span>
        </div>
        <p class="research-story-papers">
          관련 대표 논문:
          <a href="https://doi.org/10.1038/s43587-026-01221-z"><em>Nature Aging</em> (2026)</a>,
          <a href="https://doi.org/10.1038/s41588-024-02051-8"><em>Nature Genetics</em> (2025)</a>,
          <a href="https://doi.org/10.1093/nar/gkv1245"><em>Nucleic Acids Research</em> (2016)</a>
        </p>
      </div>
    </article>
  </section>

  <section class="research-join" aria-labelledby="research-join-title">
    <h2 id="research-join-title">연구실 참여</h2>
    <div>
      <p>
        생명과학과 의생명 전공자뿐 아니라 컴퓨터과학, 통계학, 수리과학, AI 배경에서 유전체 진화와 다양성, 세포 노화 연구에 도전하고 싶은 연구자와 학생을 환영합니다.
      </p>
      <a class="research-join-link" href="{{ '/ko/join/' | relative_url }}">모집 안내 자세히 보기 →</a>
    </div>
  </section>
</div>
