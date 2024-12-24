import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession

project_id = "xenon-petal-445620-c9"
location = "us-central1"
vertexai.init(project=project_id, location=location)

model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

def get_summary(chat: ChatSession, text: str):
    prompt = f"Provide a summary for the following text: {text}"
    response = chat.send_message(prompt)
    return response.text

# Example input text
text = (
    "Cloud computing has revolutionized the way businesses operate, offering scalable resources, reduced infrastructure "
    "costs, and improved operational efficiency. By leveraging cloud platforms like AWS, organizations can deploy applications "
    "faster and access a wide range of services, including storage, machine learning, and serverless computing. However, the "
    "shift to the cloud also introduces challenges such as security concerns, compliance requirements, and the need for skilled "
    "professionals to manage cloud environments. Despite these hurdles, the cloud continues to drive innovation, enabling "
    "businesses to adapt quickly to market demands and deliver enhanced customer experiences."
)

# Get the summary
summary = get_summary(chat, text)
print("Summary:")
print(summary)
