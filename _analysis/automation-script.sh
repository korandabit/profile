#!/bin/bash
# Automated Metric Extraction (what can be computed)

POST_FILE="$1"

# === COMPUTABLE METRICS ===

# Word count (excluding YAML front matter)
WORD_COUNT=$(sed -n '/^---$/,/^---$/!p' "$POST_FILE" | wc -w)

# Sentence count (rough: count periods, question marks, exclamation points)
SENTENCE_COUNT=$(sed -n '/^---$/,/^---$/!p' "$POST_FILE" | tr -cd '?.!' | wc -c)

# Paragraph count (empty line separated blocks)
PARAGRAPH_COUNT=$(sed -n '/^---$/,/^---$/!p' "$POST_FILE" | awk 'BEGIN{RS="";ORS="\n"}1' | wc -l)

# Average sentence length
if [ "$SENTENCE_COUNT" -gt 0 ]; then
    AVG_SENTENCE=$(echo "scale=1; $WORD_COUNT / $SENTENCE_COUNT" | bc)
else
    AVG_SENTENCE=0
fi

# Citation count (footnote references)
CITATION_COUNT=$(grep -o '\[\^[0-9]\+\]' "$POST_FILE" | sort -u | wc -l)

# Internal reference count
INTERNAL_REF_COUNT=$(grep -c 'post_url' "$POST_FILE")

# Has lists
HAS_NUMBERED=$(grep -q '^[0-9]\+\.' "$POST_FILE" && echo true || echo false)
HAS_BULLETS=$(grep -q '^[-*]' "$POST_FILE" && echo true || echo false)

# Has code blocks
HAS_CODE=$(grep -q '```' "$POST_FILE" && echo true || echo false)

# Output in YAML-like format
cat << YAML
# Automated metrics for: $(basename "$POST_FILE")

computed:
  word_count: $WORD_COUNT
  sentence_count: $SENTENCE_COUNT
  paragraph_count: $PARAGRAPH_COUNT
  
  sentence_metrics:
    avg_sentence_length: $AVG_SENTENCE
  
  content_markers:
    has_numbered_list: $HAS_NUMBERED
    has_bullet_list: $HAS_BULLETS
    has_code_blocks: $HAS_CODE
    citation_count: $CITATION_COUNT
    
  references:
    internal_count: $INTERNAL_REF_COUNT

YAML

