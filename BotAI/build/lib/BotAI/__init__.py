import openai

messages = []


def get_response(model, messages: list, temperature):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature  # 0.0 - 2.0
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
    def __init__(self, API_KEY, model="gpt-3.5-turbo", temperature=1.0):
        openai.api_key = API_KEY
        self.model = model
        self.temperature = temperature

    def defineBot(self, description):
        messages.append({"role": "system", "content": description})

    def ask(self, prompt):
        messages.append({"role": "user", "content": prompt})

        new_message = get_response(
            model=self.model,
            messages=messages,
            temperature=self.temperature
        )

        messages.append(new_message)
        return new_message["content"]

    def clear(self):
        messages.clear()

    def generateImage(self, prompt, image_count):
        image = get_image(prompt, image_count)
        return image
