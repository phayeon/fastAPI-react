import openai

openai.api_key = "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"


class CreatGPT(object):
    def generate_blog(self, topic, prompt):
        # 모델 엔진 선택
        model_engine = "text-davinci-003"

        # 맥스 토큰
        max_tokens = 2048

        # 블로그 생성
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.3,  # creativity
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return completion


if __name__ == '__main__':
    city = "New York"
    topic = f"Top 10 Restaurants you must visit when traveling to {city}"
    category = "travel"

    # 프롬프트 (내용 수정 가능)
    prompt = f"Write blog posts in markdown format. Write the theme of your blog as {topic}. Highlight, bold, or " \
             f"italicize important words or sentences. Please include the restaurant's address, menu recommendations " \
             f"and other helpful information(opening and closing hours) as a list style. Please make the entire blog " \
             f"less than 10 minutes long. The audience of this article is 20-40 years old. Create several hashtags " \
             f"and add them only at the end of the line. Add a summary of the entire article at the beginning of the " \
             f"blog post. "

    response = CreatGPT().generate_blog(topic, prompt)
    # 생성된 글 출력
    print(response.choices[0].text)
