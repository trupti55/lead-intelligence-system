import json


def save_report(
    results,
    file_path="output/output_report.json"
):

    qualified = len(
        [r for r in results
         if r["decision"] == "Qualified"]
    )

    review = len(
        [r for r in results
         if r["decision"] == "Review"]
    )

    rejected = len(
        [r for r in results
         if r["decision"] == "Rejected"]
    )

    report = {
        "summary": {
            "total_processed": len(results),
            "qualified": qualified,
            "review": review,
            "rejected": rejected,
            "qualification_rate":
                round(
                    qualified /
                    len(results) * 100,
                    2
                )
        },
        "leads": results
    }

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )