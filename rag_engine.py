import openai

def answer_query(query, context):
    prompt = f"""
    Use the following context to answer:
    {context}

    Question: {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
