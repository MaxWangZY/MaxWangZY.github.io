---
layout: default
title: Home
---

<section class="hero">
  <h1>Max Wang</h1>
  <p class="lede">"Optimization is everywhere."</p>
</section>

<section class="section">
  <h2>Intro</h2>
  <p>
    I am interested in optimization as both a research language and a practical
    way to understand markets. This site collects my work in operations
    research, technical systems, and market research around AI infrastructure.
  </p>
</section>

{% if site.data.artifacts.size > 0 %}
  <section class="section">
    <h2>Recent</h2>
    <div class="artifact-list" data-artifact-list>
      {% for artifact in site.data.artifacts limit: 5 %}
        <article class="artifact" data-artifact>
          <div class="artifact-row">
            <a class="artifact-type" href="{{ artifact.url | relative_url }}">[{{ artifact.label | downcase }}]</a>
            <button class="artifact-toggle" type="button" aria-expanded="false">
              {{ artifact.title }}
            </button>
          </div>
          <div class="artifact-detail" hidden>
            {% for paragraph in artifact.summary %}
              <p>{{ paragraph }}</p>
            {% endfor %}
            <a class="artifact-link" href="{{ artifact.url | relative_url }}">{{ artifact.cta }}</a>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
{% endif %}

<section class="section grid">
  <article>
    <h2>Experience</h2>
    <p>
      Research, market work, portfolio theses, and mini projects organized as a
      broader record of what I am building and studying.
    </p>
    <a href="{{ '/experience/' | relative_url }}">View experience</a>
  </article>
  <article>
    <h2>Blog</h2>
    <p>
      Longer notes behind selected artifacts, including market research,
      technical reflections, and ideas that need more room.
    </p>
    <a href="{{ '/blog/' | relative_url }}">Read posts</a>
  </article>
</section>
