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


print(111111, g4f.Provider.Ails.params) # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print("xx", message)

# normal response
response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
                                     {"role": "user", "content": "hi"}]) # alterative model setting

print(response)


# Set with provider
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=g4f.Provider.Forefront, messages=[
                                     {"role": "user", "content": "Hello world"}], stream=True)

for message in response:
    print(message)