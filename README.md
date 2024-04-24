# Useful Command Line Things 

## Overview

### Temporal Server Utilities

**tserve** - Run the Temporal command-line server unobtrusively and pull up the webpage on-demand without remembering the UI port you used.

```
$ tserve
Usage: tserve [--port PORT] command
Commands:
  start     Start Temporal Development Server
  stop      Stop Temporal Development Server
  check     Check if Temporal Development Server is running
  open      Open Temporal Development Server Web UI (requires Python)
  schedules Open Temporal Development Server Schedule Web UI (requires Python)
```

NOTE TO SELF: Add simple namespace creation and deletion support as I sometimes need that, so I don't have to start figuring it out each time.

### Authentication Support for GitHub

**sshgo** - I can never remember exactly how to run the ssh agent. This remembers it for me. Always check your keys after reboots.

```
$ sshgo
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

### Ticketing and Documentation Repository Utilities

**rgrep** - Recursive search in the file type I set, like Markdown-only or JSON-only. I use this multiple times a day.

```
Usage: rgrep [-cl] <file_extension> <search_pattern>
    Perform a recursive 'grep' search from the working directory.
    Restricts search to files matching your file extension.
    For example, "rgrep json phrase" searches JSON files.
    Use the -c flag to set case-sensitive search.
    Use the -l flag to output only file names.
    Phrases may include multiple words without quoting.
    Use single quotes with wildcard items to avoid expansion.
```

**jira** - Open ticket in JIRA

```
Usage: jira <ticket> [<ticket> ...]
   Open EDU tickets by name or number
   e.g. jira 1181 1659 2286
```

### Generally Useful

You may have to give things permission to open other things through System Preferences.

**rename** - Rename a bunch of files at once. Provide a source pattern, the replacement string, and the files to work on.

```
Usage: rename <pattern> <replacement> <paths>
Rename multiple files at once. For example:
    rename "[Oo]riginal" "NewName" Orig*
```

**cleanup** - Remove single matching lines from files in a folder using recursive search. _Case sensitive_.

```
Usage: cleanup directory_to_clean search_string
```

**pman** - Opens the output of `man` as a formatted PDF document in Preview. This version is Sonoma-and-later only.

```
$ pman
Usage: pman [-k] keyword
Options:
   -k      Run apropos instead.

Description: Open a man page in Preview as a PDF file
```

**snap** - Initiate dragged screen capture to PDF. Results left on the Desktop. Useful for screen-sharing sessions which put grabs onto the host computer instead of the shared one.

```
$ snap
Usage: snap [options]
  -d, --drag: Capture using drag-to-select
  -s, --select: Capture using interactive selection mode
  -v, --video: Capture video
 Space bar toggles between mouse and window capture
 Tap any key to finish video capture
```

### Deprecated

- `cites` - we no longer use Assembly. I'll see whether the URL functionality still works.
- `make.sh` - no assembly. I'll see if there should be a convenient system to be built for this or if the tooling is good.
- `flow`, `tflow`, `clflow` - these are all crying out for a good general rewrite. I'll get to it.