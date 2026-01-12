import argparse
import asyncio
import nest_asyncio
from src.graph.builder import build_graph

nest_asyncio.apply()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--domain", default="general")
    parser.add_argument("--sections", type=int, default=4)
    return parser.parse_args()

async def main():
    args = parse_args()
    app = build_graph()

    result = await app.ainvoke({
        "topic": args.topic,
        "domain": args.domain,
        "sections": args.sections,
        "draft_sections": []
    })

    print("\nEXECUTIVE SUMMARY\n")
    print(result["final_report"].executive_summary)

    print("\nFULL REPORT\n")
    print(result["final_report"].full_report)

    print("\nRECOMMENDATIONS\n")
    for r in result["final_report"].strategic_recommendations:
        print("-", r)

if __name__ == "__main__":
    asyncio.run(main())
