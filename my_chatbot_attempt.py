import openai
import os

openai.api_key ='api-key'


agent_name = input("Enter the agent name: ")

## using chat gpt 3.5 as the llm 
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system-admin", "content": f'You are {agent_name}, who can answer anything from the files provided to you '},
    ],
)
##creating the agent 
agent_id = response['id']

## we will now get the file path and we will train gpt3.5 on it to answer question and answers
file_paths = []
num_files = int(input("Enter the number of files that should be used and their filepaths : "))


for i in range(num_files):
    file_path = input(f"Enter file path for file #{i+1}: ")
    file_paths.append(file_path)

# Processing the file content 
file_contents = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        content = file.read()
        file_contents.append(content)

##now comes the important part 
## will perform the interaction now that our model abstarction is ready and we have taken
##the files 
while 1:
    user_input = input("Your message : ")

    ## if the user types stop then we exit out of the loop 
    if user_input.lower() == "stop":
        break

    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f'You are {agent_name}, an agent that can answer questions based on uploaded files.'},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": file_contents},
        ],
        assistant_id=agent_id
    )

    # Get the agent's response
    agent_response = response['choices'][0]['message']['content']

  

    print("Agent:", agent_response)

print("Conversation ended.")
