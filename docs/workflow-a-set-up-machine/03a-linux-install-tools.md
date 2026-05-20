# 🟢 Linux: Install Tools

> Installation instructions for required tools on Linux systems.

Linux distributions vary, so follow the
vendor-recommended steps for your system.

<details>
<summary>WHY?</summary>

Professional analytics projects depend on local tools for running code,
managing packages, checking quality, and working with GitHub repositories.

Installing the required tools creates a consistent project environment
across machines and operating systems.

Correct tool installation reduces setup errors and makes later project
commands more predictable.

</details>

## Required Tools

### Git

Most Linux distributions include Git in their package manager.

Official instructions:
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

### Visual Studio Code

Follow Microsoft's official Linux setup instructions
for your distribution:
<https://code.visualstudio.com/docs/setup/linux>

### uv (Python environment and dependency manager)

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

## Verify

After installation, open a terminal and run:

```bash
git --version
code --version
uv --version
```
