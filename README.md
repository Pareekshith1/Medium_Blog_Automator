# 📝 AI Medium Blog Automator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

**A powerful AI-driven tool that generates, edits, and publishes SEO-optimized blog posts directly to Medium with zero hassle.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [API Setup](#-api-setup) • [Deployment](#-deployment)

</div>

---

## 🌟 Overview

AI Medium Blog Automator is an intelligent content creation and publishing platform that leverages the power of Meta's Llama 3.3 70B model to generate professional, SEO-optimized blog posts. With an intuitive Streamlit interface, you can create, edit, enhance with images, and publish directly to Medium—all in one seamless workflow.

### ✨ Key Highlights

- **AI-Powered Content Generation**: Utilizes Meta Llama 3.3 70B Instruct Turbo for high-quality, contextual blog writing
- **Interactive Editor**: Real-time blog editing with paragraph-level control
- **Image Integration**: Upload and position images with captions and affiliate links
- **SEO Optimization**: Built-in SEO best practices and keyword optimization
- **Direct Medium Publishing**: One-click publishing to Medium via RapidAPI
- **Live Preview**: See your blog as it will appear before publishing
- **Professional Templates**: Pre-configured templates for consistent, high-quality output

---

## 🚀 Features

### Content Generation
- ✍️ **AI-Powered Writing**: Generate comprehensive blog posts from simple prompts
- 🎯 **SEO Optimized**: Automatic keyword integration and meta tag generation
- 📊 **Structured Output**: Well-formatted blogs with proper headings and sections
- 🔄 **Continuation Detection**: Automatically handles long-form content generation
- 🎨 **Customizable Templates**: Modify blog structure and style via templates

### Content Editing
- ✏️ **Interactive Editor**: Edit title and each paragraph individually
- 🖼️ **Image Management**: Upload images with captions after any paragraph
- 🔗 **Affiliate Links**: Add referral/affiliate links to images
- 👁️ **Live Preview**: Real-time preview of your final blog post
- 💾 **Session State**: Your work is preserved during editing

### Publishing
- 📤 **Direct Medium Upload**: Publish directly to your Medium account
- 🏷️ **Tag Management**: Add custom tags for better discoverability
- 🌐 **HTML Formatting**: Automatic conversion to Medium-compatible HTML
- ☁️ **Image Hosting**: Automatic image upload to ImgBB for reliable hosting
- ✅ **Success Tracking**: Get direct links to your published posts

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8 or higher** installed on your system
- **pip** package manager
- **Git** (for cloning the repository)
- Active accounts and API keys for:
  - [Together AI](https://api.together.xyz/) (for Llama 3.3 70B model)
  - [RapidAPI](https://rapidapi.com/hub) (for Medium API access)
  - [ImgBB](https://api.imgbb.com/) (for image hosting)

---

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Medium-Blog-Automator.git
cd AI-Medium-Blog-Automator
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# For Windows
copy .env.example .env

# For macOS/Linux
cp .env.example .env
```

Edit the `.env` file and add your API keys:

```env
# Together AI API Key (for Llama 3.3 70B model)
TOGETHER_API_KEY=your_together_ai_api_key_here

# RapidAPI Key (for Medium publishing)
RAPIDAPI_KEY=your_rapidapi_key_here

# ImgBB API Key (for image hosting)
IMGBB_API_KEY=your_imgbb_api_key_here
```

---

## 🔑 API Setup

### 1. Together AI API Key

1. Visit [Together AI](https://api.together.xyz/)
2. Sign up or log in to your account
3. Navigate to **API Keys** section
4. Create a new API key
5. Copy the key and paste it in your `.env` file as `TOGETHER_API_KEY`

**Free Tier**: Together AI offers free credits for testing. The Llama 3.3 70B Turbo Free model is available for use.

### 2. RapidAPI Key (Medium API)

1. Go to [RapidAPI Hub](https://rapidapi.com/hub)
2. Sign up or log in
3. Search for "**Medium API**" or visit [Medium2 API](https://rapidapi.com/nedokingston/api/medium2)
4. Subscribe to a plan (free tier available)
5. Go to **Endpoints** and copy your `X-RapidAPI-Key`
6. Paste it in your `.env` file as `RAPIDAPI_KEY`

**Important**: You'll also need to authenticate your Medium account through the RapidAPI interface.

### 3. ImgBB API Key

1. Visit [ImgBB API](https://api.imgbb.com/)
2. Sign up for a free account
3. Navigate to **API** section
4. Copy your API key
5. Paste it in your `.env` file as `IMGBB_API_KEY`

**Free Tier**: ImgBB offers free image hosting with reasonable limits for personal projects.

---

## 🎮 Usage

### Running the Application

1. Make sure your virtual environment is activated
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Your default browser will open automatically at `http://localhost:8501`

### Creating Your First Blog

#### Step 1: Enter Your Prompt
In the text area, provide a detailed prompt for your blog. The more specific you are, the better the output.

**Example Prompts:**
```
Write a comprehensive blog about the top 5 gaming mice under ₹2000 in India, 
including their features, pros, cons, and where to buy them.

Create an in-depth guide on getting started with machine learning using Python, 
covering essential libraries, concepts, and a beginner project.

Write a blog post about sustainable fashion trends in 2024, including eco-friendly 
brands, materials, and tips for building a sustainable wardrobe.
```

#### Step 2: Generate the Blog
1. Click the **✨ Generate Blog** button
2. Wait for the AI to generate your content (usually 10-30 seconds)
3. The generated blog will appear in the editor below

#### Step 3: Edit Your Content
- **Edit Title**: Modify the blog title in the text input field
- **Edit Paragraphs**: Each paragraph has its own text area for editing
- **Add Images**: 
  - Expand the image section after any paragraph
  - Upload an image (JPG, JPEG, or PNG)
  - Add a caption
  - Optionally add an affiliate/referral link

#### Step 4: Preview Your Blog
Scroll to the **👀 Blog Preview** section to see how your blog will look when published.

#### Step 5: Publish to Medium
1. Click **✅ Save and Proceed to Upload**
2. Wait for the upload process to complete
3. You'll receive a success message with a link to your published blog

---

## ⚙️ Configuration

### Customizing the Blog Template

The blog generation follows a template located at `templates/blog_prompt_template.txt`. You can customize this template to change:

- Blog structure and sections
- SEO requirements
- Writing style and tone
- Content depth guidelines
- Call-to-action formats

**To edit the template:**

```bash
# Open the template file
notepad templates\blog_prompt_template.txt  # Windows
nano templates/blog_prompt_template.txt     # macOS/Linux
```

### Adjusting AI Parameters

In `blog_generator.py`, you can modify the AI model parameters:

```python
data = {
    "model": MODEL,
    "messages": [...],
    "max_tokens": 2048,      # Increase for longer blogs
    "temperature": 0.7,      # 0.0-1.0: Lower = more focused, Higher = more creative
    "top_p": 0.9,            # Nucleus sampling
    "frequency_penalty": 0.2, # Reduce repetition
    "presence_penalty": 0.1,  # Encourage topic diversity
}
```

### Changing the AI Model

The default model is `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`. You can change this in `blog_generator.py`:

```python
MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"  # Current model
# Or try other Together AI models:
# MODEL = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
# MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
```

---

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click **New app**
5. Select your repository and branch
6. Set **Main file path** to `app.py`
7. Click **Advanced settings**
8. Add your environment variables:
   - `TOGETHER_API_KEY`
   - `RAPIDAPI_KEY`
   - `IMGBB_API_KEY`
9. Click **Deploy**

### Deploy to Heroku

1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Login and create a new app:

```bash
heroku login
heroku create your-app-name
```

4. Set environment variables:

```bash
heroku config:set TOGETHER_API_KEY=your_key_here
heroku config:set RAPIDAPI_KEY=your_key_here
heroku config:set IMGBB_API_KEY=your_key_here
```

5. Deploy:

```bash
git push heroku main
```

**Note**: The `Procfile` is already configured for Streamlit on Heroku.

### Deploy to Railway

1. Visit [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repository
5. Add environment variables in the **Variables** tab
6. Railway will automatically detect and deploy your Streamlit app

---

## 📁 Project Structure

```
AI-Medium-Blog-Automator/
│
├── app.py                          # Main Streamlit application
├── blog_generator.py               # AI blog generation logic
├── medium_uploader.py              # Medium publishing functionality
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── .env                            # Environment variables (not in repo)
├── .gitignore                      # Git ignore file
│
├── templates/
│   └── blog_prompt_template.txt   # Blog generation template
│
└── README.md                       # This file
```

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Issue: "TOGETHER_API_KEY not found"
**Solution**: Ensure your `.env` file exists and contains the correct API key. Restart the Streamlit app after adding the key.

#### Issue: "Blog generation failed"
**Solutions**:
- Check your Together AI API key is valid
- Verify you have sufficient API credits
- Check your internet connection
- Try a shorter/simpler prompt

#### Issue: "Upload failed" or "Medium upload error"
**Solutions**:
- Verify your RapidAPI key is correct
- Check if you've authenticated your Medium account on RapidAPI
- Ensure you have remaining API calls in your RapidAPI plan
- Check the Medium API status on RapidAPI

#### Issue: "Image upload failed"
**Solutions**:
- Verify your ImgBB API key
- Check image file size (ImgBB has limits)
- Ensure image format is JPG, JPEG, or PNG
- Check your internet connection

#### Issue: Blog gets cut off
**Solution**: The app has automatic continuation detection. If it's still cutting off:
- Increase `max_tokens` in `blog_generator.py`
- Break your prompt into smaller, more specific sections

#### Issue: Streamlit app won't start
**Solutions**:
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Clear Streamlit cache
streamlit cache clear

# Check Python version
python --version  # Should be 3.8+
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Meta Llama 3.3 70B Instruct Turbo (via Together AI)
- **APIs**: 
  - Together AI API (LLM)
  - RapidAPI Medium API (Publishing)
  - ImgBB API (Image Hosting)
- **Languages**: Python 3.8+
- **Key Libraries**: 
  - `streamlit` - Web interface
  - `requests` - API calls
  - `python-dotenv` - Environment management
  - `Pillow` - Image processing

---

## 📊 Features in Development

- [ ] Multi-language blog generation
- [ ] Custom tag suggestions based on content
- [ ] Draft saving and loading
- [ ] Batch blog generation
- [ ] Analytics integration
- [ ] WordPress integration
- [ ] Twitter thread generation
- [ ] Content calendar planning

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update README.md for new features
- Test thoroughly before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Kill_Switch**

- GitHub: [@yourusername](https://github.com/yourusername)
- Medium: [@yourmedium](https://medium.com/@yourmedium)

---

## 🙏 Acknowledgments

- [Together AI](https://api.together.xyz/) for providing access to Llama 3.3 70B
- [Meta AI](https://ai.meta.com/) for the Llama model
- [Streamlit](https://streamlit.io/) for the amazing framework
- [RapidAPI](https://rapidapi.com/) for Medium API access
- [ImgBB](https://imgbb.com/) for free image hosting

---

## ⭐ Support

If you find this project helpful, please consider:

- Giving it a ⭐ on GitHub
- Sharing it with others
- Contributing to its development
- Reporting bugs and suggesting features

---

## 📞 Contact & Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: your.email@example.com

---

<div align="center">

**Made with ❤️ and AI**

[⬆ Back to Top](#-ai-medium-blog-automator)

</div>
