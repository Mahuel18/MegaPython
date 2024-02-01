import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, prompt):
        response = (
            openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=3000,
                temperature=0.5,
            )
            .choices[0]
            .text
        )

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a list of pair numbers")
    print(response)
