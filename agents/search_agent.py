from ddgs import DDGS


class SearchAgent:

    def search(self, topic):

        queries = [
            f"{topic} overview",
            f"{topic} architecture",
            f"{topic} working",
            f"{topic} advantages disadvantages",
            f"{topic} applications"
        ]

        results = []
        seen_urls = set()

        with DDGS() as ddgs:

            for query in queries:

                print(f"   Searching: {query}")

                search_results = ddgs.text(
                    query,
                    region="wt-wt",
                    safesearch="off",
                    max_results=3
                )

                for result in search_results:

                    url = result.get("href")

                    if url and url not in seen_urls:

                        seen_urls.add(url)

                        results.append({
                            "title": result.get("title", ""),
                            "url": url,
                            "body": result.get("body", "")
                        })

        return results