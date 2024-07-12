---
layout: default
title: Blog
permalink: /blog/
---

# My Blog Posts

{% raw %}{% for post in site.posts %}
## [{{ post.title }}]({{ post.url | relative_url }})
{{ post.date | date: "%B %d, %Y" }}

{{ post.excerpt }}

[Read more]({{ post.url | relative_url }})

---
{% endfor %}{% endraw %}
