from dotenv import load_dotenv
from workflow.research_workflow import ResearchWorkflow

load_dotenv()

print("=" * 50)
print("🤖 Autonomous Research Agent")
print("=" * 50)

workflow = ResearchWorkflow()

topic = input("\nEnter Research Topic: ")

plan, research, report = workflow.run(topic)

print("\n")
print("=" * 50)
print("RESEARCH PLAN")
print("=" * 50)
print(plan)

print("\n")
print("=" * 50)
print("RESEARCH REPORT")
print("=" * 50)
print(research)

with open("reports/report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("\n✅ Report saved to reports/report.md")