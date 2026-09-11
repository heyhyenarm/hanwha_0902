from openai import OpenAI


def main():
    client = OpenAI()  # Uses the OPENAI_API_KEY environment variable.

    response = client.responses.create(
        model="gpt-5.6-luna",
        input="This is an OpenAI API connection test. Reply in one short sentence.",
    )

    print("API connection succeeded")
    print("Response:", response.output_text)
    print("Usage:", response.usage)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("API call failed:", e)
