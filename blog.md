---
layout: default
title: Blog
permalink: /blog/
---

# My Blog

Welcome to my blog, where I explore various ideas and topics. Below you'll find curated reading lists on key themes, followed by a chronological list of all my posts.

## Featured Themes

### Discovering AI Chatbots
Other people will tell you about the technical and sociological fears. I'm interested in developing a rich and nuanced perspective on the immediate psychological implications of a current and future relationship with AI. 

- [Stop avoiding yourself: the AI in you]({% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %})

### Communication
Language is what humans do expertly, but it is a technology nonetheless. That means it has limitations, and certainly is subject to good and bad crafstmanship. These posts are light experiments meant to uncover the critical first-principles of language as a technology, with the goal of improving your relationships.

- [Not the Point]({% post_url 2022-11-20-2-not-the-point %})

### Deaf Culture
As a child of Deaf adults (CODA), I grew up in two worlds--hearing and deaf--translated between them, and spent a chunk of my late 20s and early 30s unpacking it in the form of blog posts. 

- [Deafhood Unheard]({% post_url 2014-10-04-deafhood-unheard %})

### Cognitive Growth  
Self-help but for people who are obsessed with analytical lifehacking. 

- [Bet your life]({% post_url 2020-10-26-bet-your-life %})

### Military
My first big-boy adventure out of high school was enlisting in the Marine Corps. My deployment to Afghanistan started and solidified my blogging habit. Writing post-deployment explores the psychology and existence of someone who participated in war, and tried to come back home.  

- [The Unedited War Story of a Veteran]({% post_url 2017-04-08-the-unedited-war-story-of-a-veteran %})

## All Blog Posts

{% for post in site.posts %}
<article class="post-preview">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}{% if post.tags.size > 0 %} • 
    {% for tag in post.tags %}
      <span class="post-tag">{{ tag }}</span>
    {% endfor %}
  {% endif %}</p>
  {{ post.excerpt }}
  <p><a href="{{ post.url | relative_url }}">Read more</a></p>
</article>
<hr>
{% endfor %}
