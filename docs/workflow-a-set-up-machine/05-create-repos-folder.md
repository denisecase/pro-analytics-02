# 🟢 Create a Place for all Projects (Repos/)

Each project has its own folder.
We need one place on the machine to keep all project folders together.

This page explains how to create a `Repos/` folder to hold project folders.

Do NOT create this folder inside a location that is automatically synced,
such as OneDrive, iCloud Drive, Google Drive, or Dropbox.

![steps](https://lh3.googleusercontent.com/notebooklm/AKXwDQF9GdiYZvNQdPqjicVi7fNgbdJFNmi8L7WBpJ4WuJ557893XTkRgitSxhP8GRKmMi47AanfUSVf54i6LnZGeRduV72c_QuaajVNWBCpcjK8X1dDLHHJ10RGnQ-5P4dKDgVt-F3x568Dhvt698WxLIF0qwab5kuOJPvMli4=w1376-h768?authuser=0)

<details>
<summary>WHY?</summary>

A dedicated `Repos/` folder provides a consistent location for cloned
GitHub repositories.

Keeping projects in one predictable folder makes commands, paths, tools,
and troubleshooting easier.

A consistent project location also helps separate code repositories from
downloads, documents, and temporary files.

It is important to avoid locations that are automatically synced because
Python project folders can become large,
and automatic syncing can cause slowdowns,
conflicts, or file-locking problems.

</details>

## Windows Users

For Windows machines with OneDrive enabled,
the `Documents` folder is NOT ideal for our GitHub projects.
OneDrive's automatic syncing slows things down when
working with large Python projects and
is not needed - we back up our work in GitHub.

We recommend creating a dedicated folder
outside of OneDrive's sync scope,
for example, a folder named `Repos` (short for *repositories*)
in the root of your C: drive (i.e. `C:\Repos`, directions below).

### Windows Task 1. Create `C:\Repos` Directory

1. Open File Explorer.
2. Navigate to `C:\`.
3. Create a new folder named `Repos`.

Important

- Capitalize the "R" in Repos as programming is case-sensitive.
- Verify the folder is directly in C:\ (`C:\Repos`),
  not inside another folder such as Documents or Desktop.
- Optional: Ensure the new directory is NOT being backed
  up by OneDrive or other sync services. Check OneDrive settings.

### Verify on Windows

Your terminal should be your machine's PowerShell terminal,
not the older Command Window and open in the Repos folder.

From in the Repos folder, should be able to see `C:\Repos>`
in the terminal prompt.

---

## Mac/Linux Users

Keep your projects outside any cloud-sync folders like iCloud's Desktop or Documents.
This ensures smoother performance and avoids syncing unnecessary
temporary files from your GitHub Python projects.

We recommend creating a dedicated folder outside of
OneDrive's sync scope, for example, a folder named
`Repos` (short for *repositories*) (i.e. `~/Repos`, directions below).

### Mac/Linux Task 1. Create `~/Repos` Directory

1. Click the Finder icon in your Dock to open a new Finder window.
2. Access Your Home Directory: In the Finder menu bar
3. at the top of your screen, click Go, then select Home.
4. Alternatively, press Command + Shift + H to open your Home folder.
5. Right-click (or Control-click) in the Home folder and select New Folder.
6. Name the folder Repos.

Important

- Capitalize the "R" in Repos as programming is case-sensitive.
- Verify the folder is directly in your Home folder (~/Repos),
- not inside another folder like Documents or Desktop.
- Optional: Ensure this folder is NOT being backed up by iCloud
  if you have iCloud syncing enabled for your Desktop or Documents.
  To check: Go to System Settings > Apple ID > iCloud > iCloud Drive > Options
  and ensure "Desktop & Documents Folders" is unchecked.

### Verify on Mac/Linux

Your terminal should be your machine's native shell
(usually `zsh` or `bash`) and open in the Repos folder.

From in the Repos directory, you should be able to
see `~/Repos $` or `Repos %` in the terminal prompt.
