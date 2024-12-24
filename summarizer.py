import google.generativeai as genai

# Configure the API key
genai.configure(api_key="your-api-key")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro")

# Function to summarize text
def summarize_text(text: str) -> str:
    prompt = f"Provide a summary for the following text: {text}"
    response = model.generate_content(prompt)
    return response.text

# Example text to summarize
text = (
    "Cloud computing has revolutionized the way businesses operate, offering scalable resources, reduced infrastructure "
    "costs, and improved operational efficiency. By leveraging cloud platforms like AWS, organizations can deploy applications "
    "faster and access a wide range of services, including storage, machine learning, and serverless computing. However, the "
    "shift to the cloud also introduces challenges such as security concerns, compliance requirements, and the need for skilled "
    "professionals to manage cloud environments. Despite these hurdles, the cloud continues to drive innovation, enabling "
    "businesses to adapt quickly to market demands and deliver enhanced customer experiences."
)

# Get the summary
summary = summarize_text(text)
print("Summary:")
print(summary)
