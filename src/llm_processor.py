import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-3.8-flash"
)

# =====================================================
# ORIGINAL GEMINI IMPLEMENTATION (TEMPORARILY DISABLED)
# =====================================================

# def get_lead_reasoning(lead):
#
#     prompt = f"""
#     Evaluate this sales lead.
#
#     Company: {lead['company']}
#     Industry: {lead['industry']}
#     Company Size: {lead['company_size']}
#     Source: {lead['source']}
#
#     Provide:
#     1. Qualification reason
#     2. Outreach priority
#
#     Keep response under 50 words.
#     """
#
#     try:
#
#         response = model.generate_content(
#             prompt,
#             request_options={"timeout": 15}
#         )
#
#         return (
#             response.candidates[0]
#             .content.parts[0]
#             .text
#         )
#
#     except Exception as e:
#
#         print(f"Gemini Error: {e}")
#
#         return (
#             f"Lead scored based on "
#             f"industry fit, company size, "
#             f"source quality and recency."
#         )

# =====================================================
# FALLBACK IMPLEMENTATION
# =====================================================

def get_lead_reasoning(lead):

    return (
        f"Lead scored based on "
        f"industry fit, company size, "
        f"source quality and recency."
    )


if __name__ == "__main__":

    sample_lead = {
        "company": "CloudScale AI",
        "industry": "SaaS",
        "company_size": 200,
        "source": "Referral"
    }

    print(
        get_lead_reasoning(sample_lead)
    )