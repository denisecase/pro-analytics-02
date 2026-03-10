# Polars and Older Machines

Polars is a modern DataFrame library designed for high-performance data processing.
It is implemented in **Rust** and uses compiled native code and
CPU vector instructions to achieve **very fast execution**.

Because of this design, Polars may fail to import on some machines
that lack certain CPU instruction sets or that
run Python under unusual architectures or emulation layers.

This page explains what the issue is, how to recognize it, and how to proceed.

## Why This Happens

Unlike many Python libraries that are mostly pure Python,
Polars relies on **compiled native binaries**.
These binaries may expect specific CPU capabilities.

On some systems the library performs a **CPU capability check during import**.
If the check determines the system may not support the required instructions,
Polars may stop with an error.

This situation most commonly appears on:

- Older Intel CPUs
- Certain managed lab computers
- Some virtualized environments
- Python interpreters running under emulation
- Systems where the CPU detection incorrectly reports capabilities

The failure typically occurs **immediately when importing Polars**.

Example:

```python
import polars as pl
```

## Recommended Fix (Compatibility Build)

If Polars fails to import due to CPU compatibility,
install the **compatibility build** designed for older processors.

Run:

```bash
uv add "polars[rtcompat]"
```

This version uses a runtime configuration that works with a wider range of CPUs.

After installation, try importing Polars again.

---

## Temporary Workaround

If installation changes are not possible, you can temporarily bypass the CPU check.

Add the following **before importing Polars**:

```python
import os
os.environ["POLARS_SKIP_CPU_CHECK"] = "1"

import polars as pl
```

This tells Polars to **skip the CPU compatibility check** and attempt to load anyway.

Important:

- This does **not fix the underlying compatibility issue**
- It just bypasses the safety check
- If the CPU truly lacks required instructions, the program may still crash

## Which Option Should You Use?

Use the following order of preference:

1. **Normal installation**
   If Polars imports without issues, no changes are needed.

2. **Compatibility install**

   ```bash
   pip install "polars[rtcompat]"
   ```

3. **Temporary environment workaround**

   ```python
   import os
   os.environ["POLARS_SKIP_CPU_CHECK"] = "1"
   import polars as pl
   ```

## Good Practice for Projects

When working on shared projects or course repositories:

- Keep environment fixes **documented and minimal**
- Prefer **installation fixes** over runtime workarounds
- Place compatibility notes (like this) in your project documentation
- Ensure notebooks import libraries **only after environment configuration**
