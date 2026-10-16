from app.gemini_client import GeminiClient


class ResearchAgent:

    def __init__(self):
        self.client = GeminiClient()

    def research(self, topic, search_results):

        sources = ""
        references = ""

        for i, result in enumerate(search_results, start=1):

            sources += f"""
==========================
Source {i}

Title:
{result['title']}

URL:
{result['url']}

Summary:
{result['body']}
"""

            references += f"{i}. {result['title']}\n{result['url']}\n\n"

        prompt = f"""
You are an expert technical researcher and university professor.

Research Topic:
{topic}

Below are web search results collected from reliable sources.

{sources}

Instructions:

- Use ONLY the supplied search results.
- Ignore duplicate information.
- Prioritize fundamental concepts.
- Ignore insignificant implementation details.
- Write a technically accurate report.
- Do not hallucinate.
- Do not invent facts.

Generate a report using Markdown.

The report must contain:

# Executive Summary

# Introduction

# Background

# Architecture

# Working Principle

# Advantages

# Limitations

# Applications

# Future Scope

# Conclusion

Write detailed explanations for each section.

If information is unavailable, state that explicitly.
"""

        report = self.client.chat(prompt)

        report += f"""

---

# References

{references}
"""

        return report