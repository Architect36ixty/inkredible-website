# Deploying to PythonAnywhere (Free Tier)

Here is how to deploy your Inkredible Website for free on PythonAnywhere.

## Step 1: Create an Account
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com/).
2. Click **Pricing & Signup**.
3. Click **Create a Beginner account** (Free).

## Step 2: Upload Your Code
You can upload your code in two ways. The easiest way without using Git commands is to upload a ZIP file.

1. **On your computer**: Zip up your `inkredible_website` folder.
2. **On PythonAnywhere**:
   - Go to the **Files** tab.
   - Click **Upload a file** and select your ZIP file.
   - Once uploaded, open a **Bash Console** (from the Consoles tab or Dashboard).
   - Run `unzip inkredible_website.zip` (adjust the name if different).

## Step 3: Install Dependencies
In the **Bash Console** on PythonAnywhere, run:

```bash
cd inkredible_website
pip3 install -r requirements.txt --user
```

## Step 4: Configure the Web App
1. Go to the **Web** tab.
2. Click **Add a new web app**.
3. Click **Next**, then select **Flask**, then select **Python 3.10** (or similar).
4. Change the "Path" to your project folder path (e.g., `/home/yourusername/inkredible_website/app.py` - but actually just accept the default for a moment, we will change it).
5. **Configuration**:
   - **Source code**: Enter the path to your folder (e.g., `/home/yourusername/inkredible_website`).
   - **Working directory**: Same as above (`/home/yourusername/inkredible_website`).
   - **WSGI configuration file**: Click the link to edit it.

## Step 5: Edit WSGI File
Delete everything in the WSGI file and replace it with this (replace `yourusername` with your actual username):

```python
import sys
import os
from dotenv import load_dotenv

# Add your project directory to the sys.path
project_home = '/home/yourusername/inkredible_website'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Load .env file
load_dotenv(os.path.join(project_home, '.env'))

# Import flask app but need to call it "application" for WSGI to work
from app import app as application
```

## Step 6: Create/Upload .env File
Since the `.env` file contains secrets, it might not be in your zip if you excluded it.
1. Go to the **Files** tab.
2. Navigate to your project folder.
3. Create a new file named `.env`.
4. Paste your `MAIL_USERNAME` and `MAIL_PASSWORD` inside.

## Step 7: Reload
1. Go back to the **Web** tab.
2. Click the big green **Reload** button at the top.
3. Click the link to your site (e.g., `yourusername.pythonanywhere.com`).

## Troubleshooting
- If you see an error, check the **Error Log** link on the Web tab.
- Ensure your `MAIL_PASSWORD` is the App Password without spaces.
