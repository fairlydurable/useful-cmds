# Useful Command Line Things 

## Overview

### Temporal Server Utilities

**tserve** - Run the Temporal command-line server unobtrusively and pull up the webpage on-demand without remembering the UI port you used.

```
$ tserve
Usage: tserve [--port PORT] COMMAND
Commands:
  start     Start temporal server
  stop      Stop temporal server
  check     Check if temporal server is running
  open      Open web UI of temporal server
```

**flow** - Interact with local and cloud-based Temporal workflows.
```
$ flow
Usage: flow command [flags|options]

Call Info
  --input input-value           only strings, use quotes
  --namespace namespace-value   set the namespace
  --port port-value             set the port value
  --workflow workflow-function  set the workflow type
  --workflow-id id-value        set the workflow id
Cloud
  --ca-base name                run on cloud, key/pem name in ~/.ssh
  --docs                        docs team cloud
Customization
  --json                        output JSON
  --result                      extract 'show' result via JSON

Examples
    flow 'list --color never --limit 10' [--docs]
    flow start --workflow TutorialWorkflow [--docs]
    flow show --workflow-id TutorialWorkflow-1709349797 [--docs]
    flow show --docs --result --workflow-id TutorialWorkflow-1709349797
Temporal Workflows With Less Typing
```

### Authentication Support for GitHub

**sshgo** - I can never remember exactly how to run the ssh agent. This remembers it for me.

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

### Documentation Repository Utilities

**rgrep** - Recursive search in the file type I set, like Markdown-only or JSON-only.

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

**cites** - Find URLs that might cite a docs-src sourcefile node. **Requires** `rgrep`.

```
$ cites
Usage: cites <path_to_text_file>
Match a Docusaurus node to temporal.io URLs
  Only run from the temporal.io Documents repo.
  Dupe nodes w/ the same 'id' may produce extraneous URLs
```

For example:

```
concepts% cites what-is-signal-with-start.md
https://docs.temporal.io/workflows
concepts% cites what-is-tctl-v1.md 
https://docs.temporal.io/tctl-v1
concepts% cd ../cloud
cloud% cites what-is-audit-logging.md 
https://docs.temporal.io/cloud/audit-logging
cloud% cites audit-logging-supported-integrations.md 
https://docs.temporal.io/cloud/audit-logging

Note: Dupe nodes w/ the same `id` may produce extraneous URLs

java% cites workers.md 
https://docs.temporal.io/dev-guide/go/features
https://docs.temporal.io/dev-guide/java/features
https://docs.temporal.io/dev-guide/java/foundations
https://docs.temporal.io/dev-guide/java/project-setup
https://docs.temporal.io/dev-guide/php/foundations
https://docs.temporal.io/dev-guide/typescript/foundations
https://docs.temporal.io/dev-guide/worker-performance
https://docs.temporal.io/retry-policies
https://docs.temporal.io/visibility
https://docs.temporal.io/workers
```

### Generally Useful

You may have to give things permission to open other things through System Preferences.

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
