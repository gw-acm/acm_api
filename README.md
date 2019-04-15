# ACM API

This repository contains code for ACM's API, which currently supports the events page of the website by providing image content for the carousels.  This could be expanded in the future to support more of the website or other ACM initiatives.

### Configuration Required

In a `config.json` file, the following structure is required for interaction with Google Drive to work.

```json
{
  "google-drive": {
    "api-key": "API KEY HERE",
    "folder-id": "FOLDER ID HERE"
  }
}
```
