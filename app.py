import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.video_utils import transcribe_video
from utils.qa_utils import get_answer_from_context

# Set page layout
st.set_page_config(layout="wide")
st.title("🎓 AI-Based Doubt Solver (Video + PDF)")

# Upload section
video_file = st.file_uploader("📹 Upload a Video file", type=["mp4", "mov"])
pdf_file = st.file_uploader("📄 Upload a PDF file", type=["pdf"])

if video_file and pdf_file:
    # Display video player
    st.subheader("🎥 Video Player")
    st.video(video_file)

    # Transcribe video (silently)
    with st.spinner("Transcribing video..."):
        video_text = transcribe_video(video_file)

    # Extract text from PDF
    st.subheader("📄 Extracting PDF Text")
    with st.spinner("Reading PDF..."):
        pdf_text = extract_text_from_pdf(pdf_file)

    # Combine both texts for context
    combined_context = f"{video_text}\n\n{pdf_text}"

    # Q&A Section
    st.subheader("❓ Ask Your Question")
    user_question = st.text_input("Enter your question related to the video or PDF")

    if user_question:
        st.subheader("🧠 AI Answer")
        with st.spinner("Thinking..."):
            answer = get_answer_from_context(user_question, combined_context)
        st.success(answer)
else:
    st.info("👆 Please upload both a video and a PDF to begin.")


