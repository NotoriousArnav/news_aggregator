from django.core.files.storage import Storage
from vercel_storage import blob

class VercelBlobStorage(Storage):
    def _save(self, name, content):
        # Save the file to Vercel Blob Storage
        response = blob.put(pathname=name, body=content.read())
        return response['pathname']

    def delete(self, name):
        # Delete the file from Vercel Blob Storage
        blob.delete(pathname=name)

    def url(self, name):
        # Return the URL to access the file
        return blob.get_public_url(pathname=name)

    def exists(self, name):
        # Check if the file exists in Vercel Blob Storage
        # You can use the head operation to check if the file exists
        try:
            blob.head(pathname=name)
            return True
        except Exception as e:
            return False
