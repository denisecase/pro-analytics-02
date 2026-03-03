# Hosting a Video on GitHub Using HTML5 and GitHub Pages

> How to host a video file in a GitHub repository using HTML5 and GitHub Pages.

Use HTML5 and GitHub pages to stream a video in the browser.

## Step 1: Prepare the Video File

Before uploading:

- Format: `.mp4`
- Video codec: H.264
- Audio codec: AAC
- Recommended resolution: 720p or 1080p
- Size: Under 100 MB (GitHub repository hard file limit. Large File Storage does not work with GitHub Pages.)

If needed, compress using a tool like HandBrake:

- Preset: General to HQ 720p30 or HQ 1080p30
- Format: MP4
- Video encoder: H.264

## Step 2: Create a New GitHub Repository with a Default README.md

When you create the new repo, ensure you add a default README.md.
These instructions will not work if you don't have an initial file.

## Step 3: Clone Repo To Your Machine

Clone your repo down to your Repos/ folder (not into a cloud-synced folder like Documents).
Open your machine terminal in your Repos/ folder and run (replace with your GitHub user name and repo name):

```shell
git clone https://github.com/yourusername/your-repo-name
```

## Step 4: Open the Repo in VS Code

Change directory from Repos into your repo (replace with the actual name of your new repo) and open in VS Code using code dot:

```shell
cd your-repo-name
code .
```

## Step 5: Create `docs/` Folder and add .mp4 file

Inside your repository, you'll need the following:

```text
docs/
    index.html
    demo.mp4
```

If `docs/` does not exist, create it.

Upload the compressed video file into the `docs/` folder.
This example assumes the video is named demo.mp4.

## Step 6: Create index.html Page

Inside `docs/`, create a file named `index.html`.

Add the following HTML5 code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Final Project Video</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <h1>Final Project Demonstration</h1>

    <video controls width="800">
      <source src="demo.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>

    <p>
      This video demonstrates the final project implementation and explains the
      design decisions, tooling choices, and deployment process.
    </p>
  </body>
</html>
```

Ensure the filename in `<source src="demo.mp4">` matches the actual video filename.

Git add-commit-push to GitHub:

```shell
git add .
git commit -m "Add video and index page"
git push
```

## Step 7: Enable GitHub Pages

1. Go to your repository on GitHub.
2. Click **Settings**.
3. Click **Pages** in the left sidebar.
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`
5. Click **Save**.

GitHub will generate a URL like:

```
https://yourusername.github.io/your-repo-name/
```

If the site does not appear immediately, refresh after 1–2 minutes.
GitHub may take time to deploy.

## Step 8: Verify Deployment

Open the GitHub Pages URL in a browser.

You should see:

- The page title
- The embedded video player
- Play/pause controls

The video should stream directly in the browser.

## Step 9 (Optional): Make the Page Cleaner

Add basic styling:

```html
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 40px;
    max-width: 900px;
  }
</style>
```

Place inside the `<head>` section.

## Step 10 (Optional): Add a Poster Image

You can add a thumbnail:

```html
<video controls width="800" poster="thumbnail.jpg"></video>
```

Upload `thumbnail.jpg` to the same `docs/` folder.

## Step 11 (Optional): Add a Transcript

Create transcript.txt and add it to `docs/` folder.
Add access to index.html.
See complete example at the end of this document.

<p>
  <a href="transcript.txt">Download transcript</a>
</p>


## Save Your Work and Verify

Git add-commit-push after all changes and verify the site looks correct.

```shell
git add .
git commit -m "Add extras"
git push
```

## Consider Alternatives

Consider alternatives if:

- The video exceeds 100 MB and cannot be compressed.
- You require advanced streaming analytics.
- You need privacy controls beyond public access.

In those cases, consider uploading your video to YouTube or other hosting platform.

## Possible Example index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Demonstration</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Optional Styling -->
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      margin: 40px;
      max-width: 900px;
      line-height: 1.6;
    }

    h1 {
      margin-bottom: 0.5em;
    }

    .video-container {
      margin: 20px 0;
    }

    video {
      width: 100%;
      max-width: 900px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .transcript-link {
      margin-top: 10px;
    }

    footer {
      margin-top: 40px;
      font-size: 0.9em;
      color: #555;
    }
  </style>
</head>

<body>

  <h1>TODO: Title of the Demonstration</h1>

  <p>
    This video demonstrates ...TODO: customize this and the h1 title above.
  </p>

  <div class="video-container">
    <video controls poster="thumbnail.jpg">
      <source src="demo.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <div class="transcript-link">
      <p>
        <a href="transcript.txt" target="_blank">Download Transcript (TXT)</a>
      </p>
    </div>
  </div>

  <footer>
    <p>
      Hosted using GitHub Pages and HTML5 video.
    </p>
  </footer>

</body>
</html>
```
