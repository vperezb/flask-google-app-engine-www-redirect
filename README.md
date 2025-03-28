# **Flask Google App Engine WWW Redirect**  

This Flask application redirects traffic from your **naked domain** (e.g., `example.com`) to the `www.` subdomain (e.g., `www.example.com`) using **Google App Engine (GAE)**.  

## **Features**  
✅ Redirects all traffic from `example.com` to `www.example.com`.  
✅ Uses **301 permanent redirects** for SEO benefits.  
✅ Lightweight and easy to deploy on **Google App Engine**.  

## **Prerequisites**  
Before deploying, ensure you have:  
1. A **Google Cloud Platform (GCP)** project.  
2. The [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed on your machine.  
3. A **custom domain** configured in your GCP project.  
4. Your app deployed in the `default` service.  

## **Setup Instructions**  

### **1. Clone the Repository**  
Download the repository and navigate to the project folder:  

```bash
git clone https://github.com/your-repo/flask-google-app-engine-www-redirect.git
cd flask-google-app-engine-www-redirect
```

### **2. Configure `dispatch.yaml`**  
Modify the `dispatch.yaml` file to match your domain:  

```yaml
dispatch:
  - url: "www.example.com/*"
    service: default
  - url: "example.com/*"
    service: naked-domain-redirector
```

> **Note:** The `default` service should handle requests for `www.example.com`, while the `naked-domain-redirector` service will process requests for the bare domain (`example.com`) and redirect them.

### **3. Deploy the Application**  
Ensure you are working within the correct GCP project, then deploy the Flask app:  

```bash
gcloud app deploy app.yaml
```

### **4. Deploy `dispatch.yaml`**  
Deploy the dispatch routing configuration:  

```bash
gcloud app deploy dispatch.yaml
```

### **5. Verify the Redirection**  
Now, if you navigate to your **naked domain** (`example.com`), it should redirect to `www.example.com`.  

### **Example Configuration**  
Here’s an example of how the setup should look:  

![Example Configuration](https://lh3.googleusercontent.com/BV827-7Wf0MOS4HuftQjQ9xfBLwFSxwuCgFIFaTXlORU2wE4obNnrXSgGaAH9edk4hmGrlgjEqMVpltiGuzpUGRJlA=s1600-w1600-h1000)  

To test if the redirection is working, you can use this Chrome extension:  
🔗 [Redirect Path](https://chromewebstore.google.com/detail/aomidfkchockcldhbkggjokdkkebmdll?utm_source=item-share-cb)  
