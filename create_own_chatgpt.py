# import openai library
import openai
# Set up the OpenAI API client
openai.api_key = ""

while True:
  # Set up the model and prompt
  model_engine_need_to_be_selected= "text-davinci-003"
  prompt_from_user = input('Enter what you want to ask: ')
  if 'exit' in prompt_from_user or 'quit' in prompt_from_user or 'escape' in prompt_from_user:
    break
  # Generate a response
  completion_response = openai.Completion.create(
  engine=model_engine_need_to_be_selected,
  prompt=prompt_from_user,
  max_tokens=2048,
  n=1, stop=None,
  temperature=0.5)
  # extracting useful part of response
  response = completion_response.choices[0].text
  # printing response
  print(response())



