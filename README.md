# Resume Repository

This repository automatically syncs my resume from Google Docs to GitHub, keeping PDF and DOCX versions always up to date.

## How It Works

Every day at 2 AM UTC (and on-demand), a GitHub Actions workflow:

1. Connects to Google Drive using a service account
2. Downloads my resume from Google Docs
3. Exports it as both PDF and DOCX formats
4. Commits any changes back to this repository

## Files

- `resume.pdf` - PDF version of my resume
- `resume.docx` - Word document version of my resume
- `sync_resume.py` - Python script that handles the Google Docs download
- `.github/workflows/sync-resume.yml` - GitHub Actions workflow configuration

## Setup

This automation uses:

- **Google Cloud Service Account** - For authenticated access to Google Drive API
- **GitHub Secrets** - Securely stores credentials and document ID
  - `GOOGLE_CREDENTIALS` - Service account JSON credentials
  - `GOOGLE_DOC_ID` - The ID of the Google Doc to sync
- **GitHub Actions** - Runs the sync automatically on a schedule

## Benefits

- Single source of truth (Google Docs) with automatic distribution
- Version control for my resume via Git history
- Always-available public URLs for both formats
- No manual export/upload steps needed

## Manual Trigger

To manually sync the resume:

1. Go to the **Actions** tab
2. Select **Sync Resume from Google Docs**
3. Click **Run workflow**
