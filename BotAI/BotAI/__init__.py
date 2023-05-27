import openai

messages = []


def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0  # 0.0 - 2.0
    )
    return response.choices[0].message


class BotAI:
    def SetAPIKey(API_KEY):
        openai.api_key = API_KEY

    def defineBot(description):
        messages.append({"role": "system", "content": description})

    def ask(user_input):
        messages.append({"role": "user", "content": user_input})
        new_message = get_response(messages=messages)
        messages.append(new_message)

        return new_message["content"]
