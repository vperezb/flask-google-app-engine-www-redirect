# Flask Google App Engine WWW Redirect

This Flask application allows you to create a service to redirect traffic from your naked domain (e.g., `example.com`) to your `www.` subdomain (e.g., `www.example.com`) using Google App Engine.

## Features
- Redirects all naked domain traffic to the `www.` subdomain.
- Uses a 301 permanent redirect for SEO-friendly redirection.

## Prerequisites
1. A Google Cloud Platform (GCP) project.
2. The [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed on your local machine.
3. A custom domain configured in your GCP project.
4. Your app is deployed in `default` service.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/flask-google-app-engine-www-redirect.git
cd flask-google-app-engine-www-redirect
```

### 2. Customize the dispatch.yaml to use your domain

```yaml
dispatch:
  - url: "www.example.com/*"
    service: default
  - url: "example.com/*"
    service: naked-domain-redirector
```
You just need to update to match your domain.

### 3. Deploy the application in the same project

Make sure you have selected the project you want to deploy in and just deploy this tiny application.

```bash
gcloud app deploy app.yaml
```

### 4. Deploy the dispatch functions

```bash
gcloud app deploy dispatch.yaml
```

### 5. That's it, now if you navigate to your "non-www" version it will redirect to www

Below is an example of how the configuration might look:

![Example Configuration](https://lh3.googleusercontent.com/BV827-7Wf0MOS4HuftQjQ9xfBLwFSxwuCgFIFaTXlORU2wE4obNnrXSgGaAH9edk4hmGrlgjEqMVpltiGuzpUGRJlA=s1600-w1600-h1000)

I've used this extension to check: https://chromewebstore.google.com/detail/aomidfkchockcldhbkggjokdkkebmdll?utm_source=item-share-cb