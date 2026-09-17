# Set Up Google Analytics Page Views

> Enable per-page
> **view and unique-viewer counts**
> at the bottom of each documentation page.

Counts are read from Google Analytics 4 (GA4) **at build time** by
`build_analytics.py`, written to
`docs/assets/data/view-analytics.json`, and displayed by
`docs/javascripts/view-analytics.js`.

## Authentication

GitHub Actions authenticates to Google Cloud through Workload Identity
Federation.
No permanent service-account key is downloaded or stored.
GitHub supplies an OIDC identity, and
Google Cloud exchanges it for temporary credentials during the workflow run.
The browser never receives Google credentials.

## Overview: Configuration Values

Configure these GitHub Actions repository variables:

- `GA4_PROPERTY_ID`: numeric GA4 property ID
- `GA4_SERVICE_ACCOUNT`: service-account email address
- `GCP_WORKLOAD_IDENTITY_PROVIDER`: complete Workload Identity provider name

These values are identifiers, not secrets.
This integration requires no GitHub Actions repository secret.

## Google Analytics Links

- [analytics](https://developers.google.com/analytics) - learn
- [analytics/web/](https://analytics.google.com/analytics/web/) - GA app

## FIRST: Create GA Account for your.github.io

Use the analytics/web/ link above to create an account for your github.io (pages) account).

For example, I created an account for: denisecase.github.io.

GA app (analytics.google.com)
/ Admin (gear icon lower left)
/ Property / Property details
/ copy the numeric Property ID, e.g. 362221279.

This task is performed once for the GitHub Pages account.
Use the numeric property ID.
Do not use a measurement ID beginning with `G-`.

## Task 1. Google Cloud and GA4 (one-time)

### 1.1. In the Google Cloud Console, create a project

In the top-left corner (next to the "Google Cloud" logo), click the project dropdown and select New Project or useGoogle Cloud: [Create Project Wizard](https://console.cloud.google.com/projectcreate)

Name it something like `github-pages-analytics`, no organization, and click **Create**.

Once the project loads, use the top search bar to search for "Google Analytics Data API".

Click on it from the marketplace results and click the blue **Enable** button.

Confirm that `github-pages-analytics` is the selected project.

### 1.2. Create the Service Account

In Google Cloud Console, open:
IAM & Admin -> Service Accounts

Create a service account named `ga4-reader`.

The service-account email will resemble:
`ga4-reader@github-pages-analytics.iam.gserviceaccount.com`

Save this email for the GA4 Viewer permission and the
`GA4_SERVICE_ACCOUNT` GitHub variable.

### 1.3. Link the Service Account to GA4

Go to your Google Analytics Account.
Click the Admin (gear icon) in the lower-left corner.
Under the Property column, click Property access management.
Click the blue (+) button in the top right corner and choose Add users.
Paste the service account email address you copied.

Set the role to Viewer (uncheck any higher roles for security) and click Add.

Go back to the main Admin menu, click Property settings, and copy the Property ID (the long string of numbers) to save for Task 2.

## Task 2. Add the Repository Variables to GitHub

Keep Google and GitHub open in separate browser tabs.
Copy each value directly into GitHub before moving to the next value.

### 2.1. Find and add `GA4_PROPERTY_ID`

In Google **Analytics**:

1. Select the property for your GitHub Pages website.
2. Click **Admin**.
3. Open **Property details**.
4. Copy the numeric **Property ID** to the clipboard.
   Do not copy the Measurement ID beginning with `G-`.

Immediately switch to your GitHub repository:

1. Open **Settings -> Secrets and variables -> Actions**.
2. Select the **Variables** tab.
3. Click **New repository variable**.
4. Click **Value** and paste from the clipboard.
5. In **Name**, enter `GA4_PROPERTY_ID`.
6. Click **Add variable**.

### 2.2. Find and add `GA4_SERVICE_ACCOUNT`

In Google **Cloud Console**:

1. Select the `github-pages-analytics` project.
2. Open menu icon, then **IAM & Admin -> Service Accounts**.
3. Find `ga4-reader`.
4. Copy its full **email address** to the clipboard.

Immediately switch to your GitHub repository:

1. Open **Settings -> Secrets and variables -> Actions -> Variables**.
2. Click **New repository variable**.
3. Click **Value** and paste from the clipboard.
4. In **Name**, enter `GA4_SERVICE_ACCOUNT`.
5. Click **Add variable**.

### 2.3. Find and add `GCP_WORKLOAD_IDENTITY_PROVIDER`

The Workload Identity Pool and provider must already exist.
For this project, their names are `github-actions` and `github`.

In Google Cloud Console:

1. Click **Activate Cloud Shell** in the top toolbar (upper right terminal icon).
2. Wait for the terminal prompt.
3. Paste and run this command:

   ```bash
   gcloud iam workload-identity-pools providers describe "github" \
     --project="github-pages-analytics" \
     --location="global" \
     --workload-identity-pool="github-actions" \
     --format="value(name)"
   ```

4. Copy the entire output line to the clipboard.
   It begins with `projects/` and ends with `/providers/github`.
   Do not copy the terminal prompt.

Immediately switch to your GitHub repository:

1. Open **Settings -> Secrets and variables -> Actions -> Variables**.
2. Click **New repository variable**.
3. Click **Value** and paste from the clipboard.
4. In **Name**, enter `GCP_WORKLOAD_IDENTITY_PROVIDER`.
5. Click **Add variable**.

If the command reports that the provider does not exist, stop:
the Workload Identity setup must be completed before proceeding.

### 2.4. Verify

The GitHub **Variables** tab must now contain:

- `GA4_PROPERTY_ID`: a number
- `GA4_SERVICE_ACCOUNT`: an email address
- `GCP_WORKLOAD_IDENTITY_PROVIDER`: a path beginning with `projects/`

## Task 3. Verify Deploy Workflow

The action `.github/workflows/deploy-zensical-ga.yml`
includes steps **before** the `zensical build` step,
so the JSON exists when the site is built.
See the `.yml` file for details.

Counts update when the deploy workflow runs.
Check the schedule runs on a regular basis (e.g. daily).

## Task 4. Ignore the Generated File

Include the json data file in `.gitignore`
so counts don't churn git history
as CI regenerates it on each deploy:

```text
docs/assets/data/view-analytics.json
```

<!-- Local `zensical build` shows the 0/0 fallback; deploys show real counts. -->

## Task 5. Set/Verify Block Window and Enrollment

4.1. `data/academic_blocks.toml` - set the current block's **start date**.
4.2. `data/enrollment_estimates.toml` - set the **estimated students** for the block.

<!-- WHY: These drive "since the first day of this block" and the "~N viewers" line. -->****

## Task 6. Match the JSON Keys (most common mistake)

`build_analytics.py` MUST write the exact keys `view-analytics.js` reads.
Any mismatch makes every page silently fall back to `0 / 0`.

```json
{
  "estimated_viewers": 37,
  "period_start": "2026-08-18",
  "period_end": "2026-09-15",
  "pages": {
    "/pro-analytics-02/workflow-a-set-up-machine/": {
      "unique_visitors": 34,
      "page_views": 51
    }
  }
}
```

Required keys:
`estimated_viewers`, `period_start`, `period_end`, `pages`,
and per page `unique_visitors` and `page_views`.
Not `users` / `views` / `start` / `end`.

## Task 7. GA4 Query Reference (what build_analytics.py requests)

- **Endpoint**: `properties/{GA4_PROPERTY_ID}:runReport`
- **Date range**: `startDate` = block start, `endDate` = `today`
- **Dimension**: `pagePath`
- **Metrics**: `screenPageViews` -> `page_views`, `totalUsers` -> `unique_visitors`

## Task 8. Verify

8.1. Trigger the deploy workflow (push to `main`, or run it manually).
8.2. Confirm the step created `docs/assets/data/view-analytics.json`.
8.3. Load a page on the site and confirm the counts appear at the bottom.

## Google Analytics Data Notes

- **Delay**: GA4 processing lags a few hours, so same-day counts read low.
- **Threshold**: with Google Signals on, GA4 withholds rows with counts.
  A page expecting ~37 uniques may show nothing until it clears
  GA4's floor.
- **Unique is not headcount**: `totalUsers` counts browser client-ids, so a
  viewer on two devices counts twice, and ad blockers or cleared cookies
  drop or duplicate users.
