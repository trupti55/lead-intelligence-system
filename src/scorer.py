from datetime import datetime


INDUSTRY_SCORES = {
    "SaaS": 10,
    "FinTech": 9,
    "Finance": 8,
    "Healthcare": 8,
    "EdTech": 8,
    "Retail": 6,
    "Manufacturing": 5
}

SOURCE_SCORES = {
    "Referral": 10,
    "Inbound demo request": 10,
    "Sales call": 8,
    "Webinar attendee": 7,
    "LinkedIn outreach": 6,
    "Content download": 5
}


def get_industry_score(industry):
    return INDUSTRY_SCORES.get(str(industry), 5)


def get_source_score(source):
    return SOURCE_SCORES.get(str(source), 5)


def get_company_size_score(size):
    try:
        size = int(size)

        if 50 <= size <= 500:
            return 10
        elif 501 <= size <= 5000:
            return 9
        elif 11 <= size < 50:
            return 7
        elif size > 5000:
            return 6
        else:
            return 4

    except:
        return 5


def get_recency_score(date_string):
    try:
        interaction_date = datetime.strptime(
            str(date_string),
            "%Y-%m-%d"
        )

        days_old = (
            datetime.today() - interaction_date
        ).days

        if days_old <= 7:
            return 10
        elif days_old <= 30:
            return 8
        elif days_old <= 90:
            return 6
        elif days_old <= 180:
            return 4
        else:
            return 2

    except:
        return 5


def calculate_score(lead):

    industry_score = get_industry_score(
        lead["industry"]
    )

    size_score = get_company_size_score(
        lead["company_size"]
    )

    source_score = get_source_score(
        lead["source"]
    )

    recency_score = get_recency_score(
        lead["last_interaction_date"]
    )

    final_score = (
        industry_score * 0.30 +
        size_score * 0.25 +
        source_score * 0.25 +
        recency_score * 0.20
    )

    return round(final_score, 2)


def classify_lead(score):

    if score >= 7:
        return "Qualified"

    elif score >= 5:
        return "Review"

    return "Rejected"