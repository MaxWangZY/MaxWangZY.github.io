---
layout: default
title: Blog
permalink: /blog/
---

# Blog

<p class="page-intro">
  Analytical notes on markets, systems, and ideas I am trying to understand more
  clearly.
</p>

{% if site.posts.size > 0 %}
  <div class="post-list">
    {% for post in site.posts %}
      <article class="post-row">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
        <div>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          {% if post.description %}
            <p>{{ post.description }}</p>
          {% else %}
            <p>{{ post.excerpt | strip_html | normalize_whitespace | truncate: 220 }}</p>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
{% else %}
  <p>No notes published yet.</p>
{% endif %}
