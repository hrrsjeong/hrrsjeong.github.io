---
layout: page
permalink: /ko/research/
title: 연구
display_title: 연구
nav: false
nav_order: 2
lang: ko
translation_of: /research/
---

<div class="research-page">
  <section class="research-intro" aria-labelledby="research-statement">
    <h2 class="research-statement" id="research-statement"><span class="research-statement-line">모든 유전체에는 진화의 역사가,</span> <span class="research-statement-line">모든 세포에는 노화의 기록이 담겨 있습니다.</span></h2>
    <p class="research-lead">
      Jeong Lab은 유전체와 후성유전체의 변이가 인간의 진화, 노화, 질환에 어떻게 관여하는지 연구합니다. 하나의 참조 유전체(reference genome)로는 사람과 종 사이의 큰 구조적 차이를 온전히 담을 수 없기 때문에, 기증자별 유전체 조립(donor-specific genome assembly), 영장류 완전 유전체 비교, 단일세포 수준의 후성유전체 분석을 함께 활용합니다. Long-read 유전체 분석, single-cell multi-omics, 통계 모델링, 머신러닝을 결합해 연구하는 100% dry lab입니다.
    </p>
  </section>

  <section class="research-approach research-wide" aria-labelledby="research-approach-title">
    <p class="research-eyebrow">연구 접근법</p>
    <h2 class="research-section-title" id="research-approach-title">기증자마다 고유한 유전체를 조립합니다</h2>
    <p class="research-section-lead">
      대부분의 유전체 연구는 모든 시료를 같은 참조 유전체에 정렬해 분석합니다. 이 방식은 작은 변이를 찾는 데에는 효과적이지만, 사람마다 다른 큰 삽입, 결실, 역위, 중복은 하나로 뭉개지거나 잘못된 위치에 놓이거나 아예 누락되고, 그 영역에 담긴 조절 신호도 함께 사라집니다. 기증자별 유전체 조립은 특히 유전자 조절과 노화 연구에서 아직 드물게 쓰입니다. 우리는 이를 연구의 중심에 두고, long-read 데이터로 각 기증자의 유전체를 조립한 뒤 참조 유전체가 아닌 그 사람 고유의 서열 위에서 큰 유전체 변화를 분석합니다.
    </p>

    <figure class="research-diagram">
      <div class="research-diagram-panels">
        <div class="research-diagram-panel">
          <p class="research-diagram-kicker">참조 유전체 기반</p>
          <h3>하나의 공통 참조 유전체</h3>
          <svg class="research-diagram-svg" viewBox="0 0 400 170" role="img" aria-labelledby="diagram-reference-title diagram-reference-desc">
            <title id="diagram-reference-title">한 기증자의 read를 하나의 참조 유전체에 정렬한 모습</title>
            <desc id="diagram-reference-desc">중복된 구간의 read는 참조 유전체의 한 위치에 겹쳐 쌓이고, 역위되었거나 참조에 없는 서열의 read는 제자리를 찾지 못합니다.</desc>
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
          <p class="research-diagram-caption">모든 기증자의 read가 같은 서열 위에 억지로 놓입니다. 추가 복제본은 한곳에 겹쳐 쌓이고(2×), 역위되었거나 새로운 서열은 갈 곳을 잃습니다(?).</p>
        </div>
        <div class="research-diagram-panel research-diagram-panel--ours">
          <p class="research-diagram-kicker">기증자별 조립</p>
          <h3>기증자마다 고유한 유전체</h3>
          <svg class="research-diagram-svg" viewBox="0 0 400 170" role="img" aria-labelledby="diagram-donor-title diagram-donor-desc">
            <title id="diagram-donor-title">같은 기증자의 유전체를 두 haplotype으로 조립한 모습</title>
            <desc id="diagram-donor-desc">한 haplotype에는 C 구간의 추가 복제본이 있고, 다른 haplotype에는 결실, 역위, 새로운 서열이 있습니다. 모든 구간에 DNA 메틸화 신호가 표시됩니다.</desc>
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
          <p class="research-diagram-caption">기증자의 유전체를 온전히 조립하면 중복(C′), 결실, 역위, 새로운 서열(N)이 DNA 메틸화 신호와 함께 그대로 드러납니다.</p>
        </div>
      </div>
    </figure>

    <ul class="research-points">
      <li>
        <h3>큰 유전체 변화를 직접 봅니다</h3>
        <p>구조변이와 중복을 정렬 결과로 간접 추정하지 않고, 서열 수준에서 직접 규명합니다.</p>
      </li>
      <li>
        <h3>조절을 유전체 맥락 속에서 읽습니다</h3>
        <p>참조 유전체에 없는 서열까지 포함해, 각 기증자의 유전체 위에서 후성유전 신호를 해석할 수 있습니다.</p>
      </li>
      <li>
        <h3>사람과 종을 넘나들며 비교합니다</h3>
        <p>여러 사람의 유전체와 유인원 완전 유전체를 비교해 큰 유전체 변화가 언제 생겨났고 무엇을 바꾸었는지 추적합니다.</p>
      </li>
    </ul>
  </section>

  <section class="research-questions research-wide" aria-labelledby="research-questions-title">
    <div class="research-questions-heading">
      <h2 id="research-questions-title">연구 질문</h2>
      <p>유전체, 종, 세포를 아우르는 연구를 하나로 잇는 질문들입니다.</p>
    </div>
    <ul class="research-question-list">
      <li>모든 유전체를 하나의 참조 유전체와 비교할 때, 우리는 어떤 큰 유전체 변화를 놓치고 있는가?</li>
      <li>어떤 유전체·조절 변화가 인간의 뇌를 만들었고, 그 변화는 질환 위험에 어떤 영향을 미쳤는가?</li>
      <li>세포는 왜 나이가 들수록 후성유전적 정체성을 잃고, 질환에서는 왜 조직 복구에 실패하는가?</li>
      <li>AI는 참조 유전체가 아닌 각 개인의 유전체가 세포 유형별 유전자 조절을 어떻게 결정하는지 배울 수 있는가?</li>
    </ul>
  </section>

  <section class="research-work research-wide" aria-labelledby="research-work-title">
    <div class="research-work-heading">
      <h2 class="research-section-title" id="research-work-title">주요 연구 분야</h2>
    </div>

    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/structurally-complex-regions.png' | relative_url }}" alt="인간과 침팬지 유전체에서 구조가 복잡한 염색체 영역의 정렬 비교">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">유전체 구조</p>
        <h3>유전체에서 가장 복잡한 영역을 풀어냅니다</h3>
        <p class="research-story-summary">
          Segmental duplication, 역위 등 큰 구조변이는 유전체에서 가장 역동적인 영역이지만, 참조 유전체 기반 분석에서는 흔히 하나로 합쳐지거나 누락됩니다. 다양한 인간과 유인원의 long-read 유전체 조립을 활용해 이러한 영역이 개인과 종에 따라 어떻게 다른지, 새로운 유전자를 어떻게 만들어 내는지, 그리고 인간 진화와 질환에 어떤 영향을 미치는지 연구합니다.
        </p>
        <p class="research-papers">
          <span>대표 논문</span>
          <a href="https://doi.org/10.1038/s41588-024-02051-8">Jeong et al., <em>Nature Genetics</em> 2025</a> ·
          <a href="https://doi.org/10.1038/s41586-025-08816-3">Yoo et al., <em>Nature</em> 2025</a>
        </p>
      </div>
    </article>

    <article class="research-story research-story--reverse">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/epigenetic-evolution.png' | relative_url }}" alt="인간, 침팬지, 마카크의 뉴런 조절 영역 DNA 메틸화 비교. 인간 뉴런에서 메틸화가 낮게 나타남">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">유전자 조절의 진화</p>
        <h3>인간 진화 과정에서 달라진 유전자 조절을 추적합니다</h3>
        <p class="research-story-summary">
          인간을 인간답게 만드는 차이의 상당 부분은 어떤 유전자를 가졌는지뿐 아니라, 그 유전자가 어떻게 조절되는지에 있습니다. 인간과 다른 영장류의 후성유전체를 세포 유형별로 비교해 인간 계통에서만 나타난 조절 변화를 찾고, 이러한 변화가 뇌를 어떻게 형성했으며 질환 위험에 어떤 영향을 미치는지 연구합니다.
        </p>
        <p class="research-papers">
          <span>대표 논문</span>
          <a href="https://doi.org/10.1038/s41467-021-21917-7">Jeong et al., <em>Nature Communications</em> 2021</a> ·
          <a href="https://doi.org/10.1186/s13059-019-1747-7">Mendizabal et al., <em>Genome Biology</em> 2019</a>
        </p>
      </div>
    </article>

    <article class="research-story">
      <div class="research-story-media">
        <img src="{{ '/assets/img/research/epigenetic-aging.png' | relative_url }}" alt="인간과 생쥐 신장의 세포별 후성유전체 지도">
      </div>
      <div class="research-story-copy">
        <p class="research-story-topic">노화와 질환</p>
        <h3>나이가 들며 세포가 정체성을 잃는 과정을 연구합니다</h3>
        <p class="research-story-summary">
          노화는 모든 세포 유형에서 똑같이 일어나지 않습니다. 단일세포 후성유전체와 multi-omics 데이터를 활용해 어떤 세포가 가장 빠르게 노화하는지, 세포의 유전자 조절 프로그램이 어떻게 무너지는지, 만성질환에서 조직 복구가 왜 실패하는지 연구합니다.
        </p>
        <p class="research-papers">
          <span>대표 논문</span>
          <a href="https://doi.org/10.1038/s43587-026-01221-z">Jeong et al., <em>Nature Aging</em> 2026</a> ·
          <a href="https://doi.org/10.1007/s11357-024-01450-3">Jeong et al., <em>GeroScience</em> 2025</a>
        </p>
      </div>
    </article>
  </section>

  <section class="research-future research-wide" aria-labelledby="research-future-title">
    <div class="research-future-head">
      <p class="research-eyebrow">방법론과 AI</p>
      <h2 class="research-section-title" id="research-future-title">새로운 분석 방법에서 AI 기반 유전체 연구까지</h2>
      <p class="research-section-lead">연구 질문에 필요한 계산 방법을 직접 개발하며, 참조 유전체를 넘어선 유전체 데이터로 학습하는 AI 모델로 연구를 넓혀 가고 있습니다.</p>
    </div>
    <div class="research-future-grid">
      <div class="research-future-now">
        <h3>우리가 개발하는 방법</h3>
        <p>복잡한 유전체 영역의 구조변이를 규명하고, 세포 유형과 종 사이의 유전자 조절을 비교하며, 단일세포 DNA 메틸화로 세포 계통을 재구성하는 방법을 개발합니다. 개발한 방법은 재현 가능한 공개 도구로 공유합니다.</p>
      </div>
      <div class="research-future-next">
        <p class="research-future-tag">앞으로의 방향</p>
        <h3>참조 유전체를 넘어서는 유전체 AI</h3>
        <p>
          대부분의 유전체 AI 모델은 하나의 참조 유전체를 바탕으로 학습하기 때문에, 개인 간 차이, 특히 큰 구조 변화가 유전자 조절을 어떻게 바꾸는지는 아직 예측하기 어렵습니다. 기증자별 유전체와 세포 수준의 후성유전체 데이터는 이러한 모델에 꼭 필요한 데이터입니다. 앞으로 다음과 같은 AI 기반 연구를 진행하고자 합니다.
        </p>
        <ul>
          <li>큰 유전체 변화가 유전자 조절을 어떻게 바꾸는지 예측합니다.</li>
          <li>단일세포 후성유전체에서 세포의 정체성, 나이, 계통을 읽어냅니다.</li>
          <li>영장류 완전 유전체 전반에서 인간 특이적 변화를 찾아냅니다.</li>
        </ul>
        <p class="research-future-note">컴퓨터과학, 통계학, AI를 전공한 학생들이 이 연구 방향을 함께 만들어 가기를 기대합니다.</p>
      </div>
    </div>
  </section>

  <section class="research-join" aria-labelledby="research-join-title">
    <h2 id="research-join-title">연구 참여</h2>
    <div>
      <p>생명과학, 컴퓨터과학, 통계학, AI 등 다양한 배경의 학생과 연구자를 환영합니다. 모든 연구는 계산 기반으로 진행됩니다.</p>
      <div class="research-join-links">
        <a class="research-join-link" href="{{ '/ko/join/graduate-research/' | relative_url }}">대학원생 모집 안내 →</a>
        <a class="research-join-link" href="{{ '/ko/join/undergraduate-research/' | relative_url }}">학부 연구생 모집 안내 →</a>
        <a class="research-join-link" href="{{ '/ko/join/' | relative_url }}">전체 모집 안내 →</a>
      </div>
    </div>
  </section>
</div>
