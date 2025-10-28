#!/usr/bin/env python3
"""
Script to download a Google Doc and convert it to PDF and DOCX formats.
"""

import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Google Drive API setup
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_drive_service():
    """Authenticate and return Google Drive service."""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=SCOPES)
        service = build('drive', 'v3', credentials=credentials)
        return service
    except Exception as e:
        print(f"Error authenticating with Google Drive: {e}")
        sys.exit(1)

def download_as_docx(service, file_id, output_path='William_Richards_Resume.docx'):
    """Download Google Doc as DOCX."""
    try:
        request = service.files().export_media(
            fileId=file_id,
            mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download progress: {int(status.progress() * 100)}%")
        
        # Write to file
        with open(output_path, 'wb') as f:
            f.write(fh.getvalue())
        
        print(f"Successfully downloaded DOCX to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error downloading DOCX: {e}")
        return False

def download_as_pdf(service, file_id, output_path='William_Richards_Resume.pdf'):
    """Download Google Doc as PDF."""
    try:
        request = service.files().export_media(
            fileId=file_id,
            mimeType='application/pdf'
        )
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download progress: {int(status.progress() * 100)}%")
        
        # Write to file
        with open(output_path, 'wb') as f:
            f.write(fh.getvalue())
        
        print(f"Successfully downloaded PDF to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error downloading PDF: {e}")
        return False

def main():
    # Get document ID from environment variable
    doc_id = os.environ.get('GOOGLE_DOC_ID')
    
    if not doc_id:
        print("Error: GOOGLE_DOC_ID environment variable not set")
        sys.exit(1)
    
    print(f"Syncing resume from Google Doc ID: {doc_id}")
    
    # Get Drive service
    service = get_drive_service()
    
    # Download both formats
    docx_success = download_as_docx(service, doc_id)
    pdf_success = download_as_pdf(service, doc_id)
    
    if docx_success and pdf_success:
        print("\n✓ Resume sync completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Resume sync failed")
        sys.exit(1)

if __name__ == '__main__':
    main()
