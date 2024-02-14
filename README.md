# Useful Command Line Things 

## Overview
**sshgo** - I can never remember exactly how to run the ssh agent. This remembers it for me.

```
Usage: sshgo [option]
Manage SSH agent and keys.
Options:
  check: Check if SSH agent is running.
  start: Start SSH agent.
  stop:  Stop SSH agent.
  add:   Add private key to SSH agent. May need authentication.
  list:  List SSH keys.
  info:  Display GitHub topic reference URL.
  help:  This help message.
```

**rgrep** - Recursive search in the file type I set, like Markdown-only or JSON-only.

```
Usage: rgrep [-c] <file_extension> <search_pattern>
    Perform a recursive 'grep' search from the working directory.
    Restricts search to files matching your file extension.
    For example, "rgrep json phrase" searches JSON files.
    Use the -c flag to set case-sensitive search.
    Phrases may include multiple words without quoting.
```

**serve-temporal** - Run the Temporal command-line server unobtrusively and pull up the webpage on-demand without remembering the UI port you used.

```
Usage: serve-temporal [--port PORT] COMMAND
Commands:
  start     - Start temporal server
  stop      - Stop temporal server
  info      - Check if temporal server is running
  web       - Open web UI of temporal server
```
