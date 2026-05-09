from app.models import ChatResponse, Recommendation
from app.services.intent_service import detect_intent
from app.retrieval.vector_store import search_catalog
from app.services.llm_service import generate_response


def process_chat(messages):

    latest_message = messages[-1].content

    intent = detect_intent(latest_message)

    # Clarification
    if intent == "clarify":
        return ChatResponse(
            reply="Could you share the role, skills, and seniority level?",
            recommendations=[],
            end_of_conversation=False
        )

    # Retrieval
    results = search_catalog(latest_message, k=5)

    recommendations = []

    for item in results:
        recommendations.append(
            Recommendation(
                name=item["name"],
                url=item["url"],
                test_type=item["test_type"]
            )
        )

    catalog_context = "\n".join([
        f"{r['name']} - {r['description']}"
        for r in results
    ])

    prompt = f"""
    User Query:
    {latest_message}

    Retrieved SHL Assessments:
    {catalog_context}

    Recommend suitable assessments.
    """

    reply = generate_response(prompt)

    return ChatResponse(
        reply=reply,
        recommendations=recommendations,
        end_of_conversation=False
    )
