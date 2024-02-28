# Useful Command Line Things 

## Overview

### Temporal Server Utilities

**tserve** - Run the Temporal command-line server unobtrusively and pull up the webpage on-demand without remembering the UI port you used.

```
Usage: tserve [--port PORT] COMMAND
Commands:
  start     Start temporal server
  stop      Stop temporal server
  info      Check if temporal server is running
  web       Open web UI of temporal server
```

**tflow** - Start, stop, list or inspect a Temporal tutorial Workflow. The Workflow JSON data defaults to _"Hello World"_, as a JSON string. The Task-Queue used is `io.temporal.TutorialTaskQueue`; the Workflow type is `TutorialWorkflow`. I may change this at some point.

```
$ tflow
Usage: tflow <command> [json|id-number]
  start [input]   Start new Workflow.
  terminate <id>  Terminate a Workflow.
  running         List active workflows.
  list            List up to 10 workflows from this server session.
  killall         Terminate all active Workflows.
  usage-long      More usage options.
```

Other options:

```
$ tflow usage-long
Usage: tflow <command> [json|id-number]
  usage-long      This message.
  latest          Show most recent Workflow.
  result          Show result of most recent Workflow.
  runid <id>      Show Workflow run-id.
  start [input]   Start new Workflow.
  cancel <id>     Cancel Workflow.
  cancelit        Cancel most recent Workflow.
  terminate <id>  Terminate a Workflow.
  describe <id>   Describe Workflow.
  describeit      Describe most recent Workflow.
  show <id>       Show Workflow details.
  showit          Show details for most recent Workflow.
  showlong        Show in-depth details for most recent Workflow.
  list            List up to 10 recent Workflows.
  running         List active workflows.
  killall         Terminate all active Workflows.
  signal          Not yet implemented.
```

### Authentication Support for GitHub

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