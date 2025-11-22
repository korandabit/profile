---
layout: default
title: Blog
permalink: /blog/
---

<style>
/* Completely override layout for blog page - disable floating sidebar */
.wrapper {
    width: auto !important;
    max-width: 960px;
    margin: 0 auto;
}

header {
    position: static !important;
    float: none !important;
    width: auto !important;
    padding: 20px 0;
    text-align: center;
    border-bottom: 1px solid #e5e5e5;
    margin-bottom: 30px;
}

section {
    width: auto !important;
    float: none !important;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
}

footer {
    display: none !important;
}

/* Override all media queries for this page */
@media print, screen and (max-width: 960px) {
    .wrapper {
        width: auto;
        margin: 0;
    }
    
    header {
        padding: 20px !important;
        padding-right: 20px !important;
    }
    
    section {
        border: none !important;
        padding: 0 20px !important;
        margin: 0 !important;
    }
}

.theme-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.theme-box {
    width: 48%;
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    box-sizing: border-box;
}
@media (max-width: 768px) {
    .theme-box {
        width: 100%;
    }
}
.post-list {
    list-style-type: none;
    padding: 0;
}
.post-list li {
    margin-bottom: 10px;
}
.post-meta {
    font-size: 0.8em;
    color: #666;
}
</style>

# My Blog

Welcome to my blog, where I explore various ideas and topics. Below you'll find curated reading lists on key themes, followed by a chronological list of all my posts.

## Featured Themes

<div class="theme-container">
    <div class="theme-box">
        <h3>Discovering AI Chatbots</h3>
        <p>For millions who've never had anyone to talk to, chatbots aren't replacing therapy—they're creating conversation where silence existed.</p>
        <ul>
            <li><a href="{% post_url 2025-11-12-bot-therapy %}">From Silence to Bot Therapy</a></li>
            <li><a href="{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}">Stop avoiding yourself: the AI in you</a></li>
            <li><a href="{% post_url 2024-09-16-awakening-ai %}">Awakening the AI</a></li>
            <li><a href="{% post_url 2024-09-17-ai-zombie %}">AI Zombie</a></li>
            <li><a href="{% post_url 2024-08-30-ai-the-next-technological-leap %}">AI: The Next Technological Leap</a></li>
            <li><a href="{% post_url 2024-07-13-right-click-for-ai %}">Right-click for AI</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Communication</h3>
        <p>Dialog is two people saying words. The Point of dialog is an agreed-upon shared result. That said, many dialogs lose the Point because of Tangents.</p>
        <ul>
            <li><a href="{% post_url 2022-11-20-2-not-the-point %}">Not the Point</a></li>
            <li><a href="{% post_url 2023-08-08-read-receipts-irl %}">Read Receipts IRL</a></li>
            <li><a href="{% post_url 2022-04-18-the-agreement-between-reader-and-writer %}">Reader and Writer</a></li>
            <li><a href="{% post_url 2024-07-13-say-less-and-more %}">Say less and more</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Language Science</h3>
        <p>Bridging academic research and practical insights on how language shapes thought and reality.</p>
        <ul>
            <li><a href="{% post_url 2024-06-11-introduction-to-empirical-pragmatism %}">Introduction to Empirical Pragmatism</a></li>
            <li><a href="{% post_url 2024-06-06-words-youve-never-heard %}">Words you've never heard</a></li>
            <li><a href="{% post_url 2024-07-16-all-the-right-words-youve-said-or-read %}">All the right words you've said or read</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Cognitive Growth</h3>
        <p>Self-help for people who are obsessed with analytical lifehacking.</p>
        <ul>
            <li><a href="{% post_url 2020-10-26-bet-your-life %}">Bet your life</a></li>
            <li><a href="{% post_url 2023-11-14-know-thaiself %}">Know Thaiself</a></li>
            <li><a href="{% post_url 2024-07-20-questions-books %}">Questions Books</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Deaf Culture</h3>
        <p>Exploring the unique perspective of growing up as a child of Deaf adults (CODA) in two worlds.</p>
        <ul>
            <li><a href="{% post_url 2014-10-04-deafhood-unheard %}">Deafhood Unheard</a></li>
            <li><a href="{% post_url 2013-10-26-the-definition-of-deaf %}">The Definition of Deaf</a></li>
            <li><a href="{% post_url 2014-10-10-language-with-a-bionic-ear %}">Language with a Bionic Ear</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Military</h3>
        <p>Exploring the psychology and existence of someone who participated in war and tried to come back home.</p>
        <p><strong>Retrospective</strong></p>
        <ul>
            <li><a href="{% post_url 2017-04-08-the-unedited-war-story-of-a-veteran %}">The Unedited War Story of a Veteran</a></li>
            <li><a href="{% post_url 2017-07-28-the-intellectual-boot-camp %}">The Intellectual Boot Camp</a></li>
        </ul>
        <p><strong>Afghanistan 2013: Real-Time Deployment</strong></p>
        <ul>
            <li><a href="{% post_url 2013-04-17-preface-one-of-those-guys %}">Preface: One of Those Guys</a></li>
            <li><a href="{% post_url 2013-04-17-1-it-rained %}">1. It Rained</a></li>
            <li><a href="{% post_url 2013-04-18-5-webcam-starts-to-capture %}">5. Webcam Starts to Capture</a></li>
            <li><a href="{% post_url 2013-04-20-7-a-christmas-special %}">7. A Christmas Special</a></li>
            <li><a href="{% post_url 2013-04-23-9-emotional-warfare %}">9. Emotional Warfare</a></li>
            <li><a href="{% post_url 2013-04-25-10-a-fog-of-war %}">10. A Fog of War</a></li>
            <li><a href="{% post_url 2013-04-27-12-grenades-cigarettes-or-melons %}">12. Grenades, Cigarettes, or Melons</a></li>
            <li><a href="{% post_url 2013-05-12-14-everyday %}">14. Everyday</a></li>
            <li><a href="{% post_url 2013-05-16-15-lead-me-home %}">15. Lead Me Home</a></li>
            <li><a href="{% post_url 2013-05-02-a-need-for-combat %}">A Need for Combat</a></li>
        </ul>
    </div>
</div>

## All Blog Posts

<ul class="post-list">
{% for post in site.posts %}
    <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <br>
        <span class="post-meta">{{ post.date | date: "%B %d, %Y" }} • 
        {% for tag in post.tags limit:3 %}
            <span class="post-tag">{{ tag }}</span>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
        </span>
    </li>
{% endfor %}
</ul>
