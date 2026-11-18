from data_loader import load_leads
from scorer import calculate_score
from scorer import classify_lead
from reporter import save_report
from outreach_generator import generate_outreach
from llm_processor import get_lead_reasoning


def main():

    print("Lead Intelligence System Started\n")

    df = load_leads("data/leads_full_scale_100.csv")

    results = []

    qualified = 0
    review = 0
    rejected = 0

    for _, lead in df.iterrows():

        score = calculate_score(lead)

        decision = classify_lead(score)

        reasoning = get_lead_reasoning(lead)

        outreach_message = ""

        if decision == "Qualified":
            outreach_message = generate_outreach(lead)

        result = {
            "name": lead["name"],
            "company": lead["company"],
            "company_size": lead["company_size"],
            "industry": lead["industry"],
            "source": lead["source"],
            "score": score,
            "decision": decision,
            "reasoning": reasoning,
            "outreach_message": outreach_message
        }

        results.append(result)

        if decision == "Qualified":
            qualified += 1
        elif decision == "Review":
            review += 1
        else:
            rejected += 1

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    for i, lead in enumerate(results, start=1):
        lead["priority_rank"] = i

    save_report(results)

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)

    print(f"Total Leads Processed : {len(results)}")
    print(f"Qualified             : {qualified}")
    print(f"Review Required       : {review}")
    print(f"Rejected              : {rejected}")

    qualification_rate = (
        qualified / len(results)
    ) * 100

    print(
        f"Qualification Rate    : "
        f"{qualification_rate:.2f}%"
    )

    print("\nTop 5 Priority Leads")

    for lead in results[:5]:
        print(
            f"Rank {lead['priority_rank']} | "
            f"{lead['company']} | "
            f"Score {lead['score']}"
        )

    print("\nReport saved to:")
    print("output/output_report.json")


if __name__ == "__main__":
    main()