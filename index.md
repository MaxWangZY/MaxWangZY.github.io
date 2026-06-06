---
layout: default
title: Home
---

<section class="hero">
  <p class="eyebrow">Personal website</p>
  <h1>Max Wang</h1>
  <p class="lede">
    I build, study, and write about technical systems that become more useful
    when they are clear, reliable, and humane.
  </p>
  <div class="actions" aria-label="Primary links">
    <a class="button primary" href="{{ '/projects/' | relative_url }}">Projects</a>
    <a class="button" href="mailto:{{ site.email }}">Email</a>
  </div>
</section>

<section class="section">
  <h2>Now</h2>
  <p>
    This site is a home for selected projects, notes, and a compact trail of
    what I am learning. The first version is intentionally small: enough to
    publish, easy to change, and ready to grow.
  </p>
</section>

<section class="section grid">
  <article>
    <h2>Projects</h2>
    <p>
      Short writeups of work worth revisiting, including the problem, approach,
      tradeoffs, and what changed after building it.
    </p>
    <a href="{{ '/projects/' | relative_url }}">View projects</a>
  </article>
  <article>
    <h2>Writing</h2>
    <p>
      Notes on software, research, systems, and the occasional idea that becomes
      clearer after being written down.
    </p>
    <a href="{{ '/writing/' | relative_url }}">Read notes</a>
  </article>
</section>
