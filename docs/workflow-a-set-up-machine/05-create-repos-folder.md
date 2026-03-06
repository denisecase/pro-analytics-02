# 🟢 Create a Place for all Projects (Repos/)

Each project has its own folder. We need a place to keep all these shared folders on our machine.

This page talks about creating a folder to hold ALL our project folders.

We don't want to make this container folder in a place that is automatically synced because each Python project folder can get very large. Automatic syncing is NOT wanted.

## Windows Users
For Windows machines with OneDrive enabled, the `Documents` folder is NOT ideal for our GitHub projects.
OneDrive's automatic syncing slows things down when working with large Python projects and is not needed - we back up our work in GitHub.

We recommend creating a dedicated folder outside of OneDrive's sync scope, for example, a folder named `Repos` (short for *repositories*) in the root of your C: drive (i.e. `C:\Repos`, directions below).

### Windows Task 1. Create `C:\Repos` Directory

1. Open File Explorer.
2. Navigate to `C:\`.
3. Create a new folder named `Repos`.

Important

- Capitalize the "R" in Repos as programming is case-sensitive.
- Verify the folder is directly in C:\ (`C:\Repos`), not inside another folder such as Documents or Desktop.
- Optional: Ensure the new directory is NOT being backed up by OneDrive or other sync services. Check OneDrive settings.

### Verify on Windows

Your terminal should be your machine's PowerShell terminal, not the older Command Window and open in the Repos folder.

From in the Repos folder, should be able to see `C:\Repos>` in the terminal prompt.

---


## Mac/Linux Users
Keep your projects outside any cloud-sync folders like iCloud's Desktop or Documents.
This ensures smoother performance and avoids syncing unnecessary temporary files from your GitHub Python projects.

We recommend creating a dedicated folder outside of OneDrive's sync scope, for example, a folder named `Repos` (short for *repositories*) (i.e. `~/Repos`, directions below).

### Mac/Linux Task 1. Create `~/Repos` Directory

1. Click the Finder icon in your Dock to open a new Finder window.
2. Access Your Home Directory: In the Finder menu bar at the top of your screen, click Go, then select Home. Alternatively, press Command + Shift + H to open your Home folder.
3. Right-click (or Control-click) in the Home folder and select New Folder. Name the folder Repos.

Important

- Capitalize the "R" in Repos as programming is case-sensitive.
- Verify the folder is directly in your Home folder (~/Repos), not inside another folder like Documents or Desktop.
- Optional: Ensure this folder is NOT being backed up by iCloud if you have iCloud syncing enabled for your Desktop or Documents. To check: Go to System Settings > Apple ID > iCloud > iCloud Drive > Options and ensure "Desktop & Documents Folders" is unchecked.

### Verify on Mac/Linux

Your terminal should be your machine's native shell (usually `zsh` or `bash`) and open in the Repos folder.

From in the Repos directory, you should be able to see `~/Repos $` or `Repos %` in the terminal prompt.
