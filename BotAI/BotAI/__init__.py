import openai

messages = []


def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0  # 0.0 - 2.0
    )
    return response.choices[0].message


def get_image(prompt, image_count):
    response = openai.Image.create(
        prompt=prompt,
        n=image_count,
        size="256x256"
    )

    return response['data'][0]['url']


class BotAI:
    def SetAPIKey(self, API_KEY):
        openai.api_key = API_KEY

    def defineBot(self, description):
        messages.append({"role": "system", "content": description})

    def ask(self, prompt):
        messages.append({"role": "user", "content": prompt})
        new_message = get_response(messages=messages)
        messages.append(new_message)

        return new_message["content"]

    def generateImage(self, prompt, image_count):
        image = get_image(prompt, image_count)
        return image
