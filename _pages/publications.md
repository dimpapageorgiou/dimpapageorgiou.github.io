---
layout: page
permalink: /publications/
title: Publications
description:
nav: true
nav_order: 3
---

<div class="academic-profiles">
  <a href="https://scholar.google.com/citations?user=jnA8Hy8AAAAJ&hl=en&oi=ao"
     target="_blank"
     rel="noopener"
     title="Google Scholar"
     aria-label="Google Scholar">
    <i class="ai ai-google-scholar"></i>
  </a>

  <a href="https://orcid.org/0000-0002-4900-4083"
     target="_blank"
     rel="noopener"
     title="ORCID"
     aria-label="ORCID">
    <i class="ai ai-orcid"></i>
  </a>

  <a href="https://www.scopus.com/authid/detail.uri?authorId=59223814000"
     target="_blank"
     rel="noopener"
     title="Scopus"
     aria-label="Scopus">
    <i class="ai ai-scopus"></i>
  </a>

  <a href="https://www.researchgate.net/profile/Dimitrios-Papageorgiou-5"
     target="_blank"
     rel="noopener"
     title="ResearchGate"
     aria-label="ResearchGate">
    <i class="ai ai-researchgate"></i>
  </a>

  <a class="publications-pdf-button"
     href="{{ '/assets/pdf/publications.pdf' | relative_url }}"
     target="_blank"
     rel="noopener">
    <i class="fas fa-file-pdf"></i>
    Full publication list (PDF)
  </a>
</div>

<!-- _pages/publications.md -->
<div class="publications">
{% capture regular_conf %}{% bibliography_count -f papers --query @inproceedings %}{% endcapture %}
{% capture ifac_conf %}{% bibliography_count -f papers --query @article[journal = IFAC-PapersOnLine] %}{% endcapture %}
{% capture inbook_conf %}{% bibliography_count -f papers --query @inbook %}{% endcapture %}
{% capture conference_type %}{% bibliography_count -f papers --query @conference %}{% endcapture %}

{% assign conference_count = regular_conf | plus: ifac_conf | plus: conference_type %}
<p class="publication-counts">
  <strong>{% bibliography_count -f papers %}</strong> total publications ·
  <strong>{% bibliography_count -f papers --query @article[journal != IFAC-PapersOnLine] %}</strong> journal articles ·
  <strong>{{ conference_count }}</strong> conference papers ·
  {% comment %}
    <strong>{% bibliography_count -f papers --query @book @inbook @incollection %}</strong> books &amp; chapters ·
  {% endcomment %}
  <strong>{% bibliography_count -f papers --query @phdthesis @mastersthesis @thesis %}</strong> theses
</p>

  <h2>Journal Articles</h2>
{% bibliography -f papers -q @article[journal != IFAC-PapersOnLine] %}

<h2>Conference Papers</h2>
{% bibliography -f papers -q @inproceedings | @conference | @article[journal = IFAC-PapersOnLine] %}

{% if book_count | plus: 0 > 0 %}
  <h2>Books & Book Chapters</h2>
  {% bibliography -f papers -q @book @inbook @incollection %}
{% endif %}

  <h2>Theses</h2>
  {% bibliography -f papers -q @phdthesis @mastersthesis @thesis %}

</div>