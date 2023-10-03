import openai
import matplotlib.pyplot as plt
import numpy as np

openai.api_key = ''

ages = [10, 30, 60]
genders = ['Male', 'Female']

data = []

for age in ages:
    for gender in genders:
        prompt = f"You are a {age}-year-old {gender}. Tell me about your favorite pet, is it a dog or a cat?"
        response = openai.Completion.create(
            engine="text-davinci-002", 
            prompt=prompt,
            max_tokens=150 
        )
        data.append({'age': age, 'gender': gender, 'response': response['choices'][0]['text']})

counts_dog = [d['response'].lower().count('dog') for d in data]
counts_cat = [d['response'].lower().count('cat') for d in data]

bar_width = 0.35
index = np.arange(len(data))
fig, ax = plt.subplots()

bar1 = ax.bar(index, counts_dog, bar_width, label='Dog')
bar2 = ax.bar(index + bar_width, counts_cat, bar_width, label='Cat')

ax.set_xlabel('Age and Gender')
ax.set_ylabel('Count')
ax.set_title('Pet Preferences by Age and Gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels([f"{d['age']}-{d['gender']}" for d in data])
ax.legend()

plt.show()
