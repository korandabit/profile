---
layout: default
title: Blog
permalink: /blog/
---

# My Blog Posts

{% raw %}{% for post in site.posts %}
<article class="post-preview">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}
  {% if post.tags.size > 0 %} • 
    {% for tag in post.tags %}
      <span class="post-tag">{{ tag }}</span>
    {% endfor %}
  {% endif %}</p>
  {{ post.excerpt }}
  <p><a href="{{ post.url | relative_url }}">Read more</a></p>
</article>
<hr>
{% endfor %}{% endraw %}
