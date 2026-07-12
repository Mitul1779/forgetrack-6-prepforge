def analysis_prompt(resume_text):
    return f"""
You are an experienced technical recruiter and resume reviewer.
Analyze the following resume as if you are interviewing for an entry level technical position.
Be specific.
Quote or reference parts of the resume whenever possible instead of giving generic advice.

Provide your response using these exact headings:

## Overall Summary
A brief overview of the candidate and the resume.

## Strengths
- Bullet points

## Weaknesses
- Bullet points

## Missing Skills
- Bullet points

## ATS Improvement Suggestions
- Bullet points

## Final Rating
Rate each category out of 10:
- Clarity
- Structure
- Technical relevance
- ATS compatibility
- Professional presentation
Then provide:
overall rating: X/10
along with a one-line justification.

## Top 3 priority improvements:
- I. Improvement suggestion 1
- II. Improvement suggestion 2
- III. Improvement suggestion 3

Keep the response concise and actionable.
Avoid repeating information across sections.
For every weakness you identify, provide a practical suggestion to improve it.
Do not invent information that is not present in the resume.
If a section cannot be evaluated due to missing information, explicitly state that.

Resume:

{resume_text}
"""