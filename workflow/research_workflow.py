from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent


class ResearchWorkflow:

    def __init__(self):

        self.planner = PlannerAgent()
        self.searcher = SearchAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()

    def run(self, topic):

        print("\n📋 Creating Research Plan...")
        plan = self.planner.create_plan(topic)

        print("\n🔍 Searching the Internet...")
        search_results = self.searcher.search(topic)

        print(f"\n✅ {len(search_results)} unique sources collected")

        print("\n🧠 Generating Research...")
        research = self.researcher.research(
            topic,
            search_results
        )

        print("\n📝 Writing Final Report...")
        report = self.writer.write_report(
            topic,
            research
        )

        print("\n🎉 Report Generated Successfully!")

        return plan, research, report