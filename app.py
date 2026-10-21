import streamlit as st
import ollama

MODEL_NAME = "llama3.2:1b"

st.set_page_config(
    page_title="Hybrid RAG with Reranking",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Hybrid RAG with Reranking")
st.caption("Ask questions over your documents using a local AI model.")

st.info(
    "Day 1 starter: this version tests the local LLM. "
    "PDF retrieval, hybrid search, and reranking will be added next."
)

# Check whether Ollama is running and the model is available.
try:
    available_models = ollama.list()
    model_names = [
        model.model for model in available_models.models
    ]

    if MODEL_NAME in model_names:
        st.success(f"Ollama is connected. Model: {MODEL_NAME}")
    else:
        st.warning(
            f"Ollama is running, but {MODEL_NAME} was not found. "
            "Run `ollama pull llama3.2:1b` in your terminal."
        )

except Exception as error:
    st.error(
        "Cannot connect to Ollama. Make sure it is installed "
        "and running, then restart this application."
    )
    st.caption(f"Connection details: {error}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a question about AI or RAG...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Generating a local response..."):
                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=st.session_state.messages,
                )

                answer = response.message.content
                st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as error:
            st.error(
                "The model could not generate a response. "
                "Check that Ollama is running and the model "
                "has been downloaded."
            )
            st.caption(f"Error details: {error}")