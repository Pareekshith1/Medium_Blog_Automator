import streamlit as st
from blog_generator import generate_blog
from medium_uploader import upload_blog
import tempfile
import os


# 🔧 Page Config
st.set_page_config(
    page_title="Medium Blog Automator",
    layout='wide',
    page_icon="📝"
)

st.title("Medium Blog Generator 📝")
st.markdown("Welcome to your AI-powered Medium blog writing tool.\n\nEnter a rich prompt below to generate and edit a full blog!")

# ✍️ Prompt Input
st.subheader("Step 1: Provide a Detailed Blog Prompt")
prompt = st.text_area(
    label="Describe what your blog should be about",
    height=150,
    placeholder="e.g., Write a blog on the top 5 gaming mice under ₹2000..."
)

# 🚀 Generate Button
generate_btn = st.button("✨ Generate Blog")

# ℹ️ Prompt Tip
st.info("Tip: Use Ctrl + Enter to submit the prompt quickly!")

# --- Helper Function to Parse Title + Paragraphs ---
def parse_blog(raw_text: str):
    lines = raw_text.strip().splitlines()
    title = lines[0].replace("# ", "") if lines[0].startswith("# ") else "Untitled"
    paragraphs = []
    buffer = ""
    for line in lines[1:]:
        if line.startswith("## "):
            if buffer:
                paragraphs.append(buffer.strip())
                buffer = ""
        else:
            buffer += line + "\n"
    if buffer:
        paragraphs.append(buffer.strip())
    return title, paragraphs

# --- Generate and Parse Blog ---
if generate_btn:
    if not prompt.strip():
        st.error("🚫 Please enter a valid prompt.")
    else:
        with st.spinner("Generating blog with AI..."):
            try:
                raw_output = generate_blog(prompt)
                blog_title_default, extracted_paragraphs = parse_blog(raw_output)
                st.session_state.raw_blog_output = raw_output
                st.session_state.title = blog_title_default
                st.session_state.paragraphs = extracted_paragraphs
                st.session_state.images = {}
                st.success("✅ Blog generated successfully!")
            except Exception as e:
                st.error(f"❌ Blog generation failed: {str(e)}")

# --- Editor UI ---
if "raw_blog_output" in st.session_state:
    st.subheader("📌 Blog Title")
    st.session_state.title = st.text_input("Edit Blog Title", value=st.session_state.title)

    st.subheader("🧾 Blog Content")
    updated_paragraphs = []

    for i, para in enumerate(st.session_state.paragraphs):
        st.markdown(f"**✏️ Paragraph {i + 1}**")
        updated = st.text_area(f"", value=para, key=f"para_{i}", height=150)
        updated_paragraphs.append(updated)

        st.markdown(f"📸 Add Image After Paragraph {i + 1}")
        with st.expander("Upload & Customize Image", expanded=False):
            uploaded_img = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], key=f"img_{i}")
            caption = st.text_input("Image Caption", key=f"caption_{i}")
            ref_link = st.text_input("Affiliate/Referral Link", key=f"link_{i}")

            if uploaded_img:
                st.session_state.images[i] = {
                    "image": uploaded_img,
                    "caption": caption,
                    "link": ref_link
                }

    st.session_state.paragraphs = updated_paragraphs

    st.markdown("---")
    st.header("👀 Blog Preview")
    st.markdown(f"# {st.session_state.title}")
    for i, para in enumerate(st.session_state.paragraphs):
        st.write(para)
        if i in st.session_state.images:
            img = st.session_state.images[i]
            st.image(img["image"], caption=img["caption"])
            if img["link"]:
                st.markdown(f"[🔗 Referral Link]({img['link']})")

    st.markdown("---")
    if st.button("✅ Save and Proceed to Upload"):
        try:
            title = st.session_state.title
            paragraphs = st.session_state.paragraphs
            images = []

            with st.spinner("Processing images..."):
                for i in range(len(paragraphs)):
                    if i in st.session_state.images:
                        image_data = st.session_state.images[i]
                        caption = image_data.get("caption", "")

                        # Save uploaded image to a temporary file
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                            tmp_file.write(image_data["image"].read())
                            temp_path = tmp_file.name
                            images.append((temp_path, caption))

            with st.spinner("🚀 Uploading blog to Medium..."):
                result = upload_blog(title, paragraphs, images, tags=["AI", "Automation", "Blogging"])

            # Clean up temporary image files
            for path, _ in images:
                if os.path.exists(path):
                    os.remove(path)

            if result:
                st.success("✅ Blog uploaded successfully!")
                st.markdown(f"🔗 [View Blog on Medium]({result['url']})")
            else:
                st.error("❌ Upload failed. Please check the logs or your RapidAPI quota.")

        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("🛠️ Developed with love by Kill_Switch")
