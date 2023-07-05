import g4f

from g4f.Provider import (
    Ails,
    You,
    Bing,
    Yqcloud,
    Theb,
    Aichat,
    Bard,
    Vercel,
    Forefront,
    Lockchat,
    Liaobots,
    H2o,
    ChatgptLogin,
    DeepAi,
    GetGpt
)


# Automatic selection of provider
print(dir(g4f.Model))   # 打印出所有支持的model列表--g4f.Model.gpt_35_turbo, g4f.Model.gpt_4
# raise
# streamed completion
stream = False
response = g4f.ChatCompletion.create(
    model=g4f.Model.gpt_4, 
    messages=[
        {"role": "user", "content": "你好,请帮我以夜晚美丽的月亮,令人神往的星空为题,作一首七言绝句的诗"},
        {"role":"ai",  "content":"你好，这是必应。我会尝试为你创作一首诗。😊\n\n夜晚美丽的月亮，令人神往的星空\n\n月色如水洒银河，星光点点映心中。\n仰望苍穹思无限，何处是我归宿空？\n"},
        {"role": "user", "content": "这首诗不太好, 字数不对,要求每句7个字，标题也不太好，标题要求4个字以内"},
        ],
    stream=stream, provider=Bing
)

if stream:
    for message in response:
        print("xx", message)
else:
    print("xx", response)
    print("yy", repr(response))
