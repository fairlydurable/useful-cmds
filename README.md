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

**serve-temporal** - Run the Temporal command-line server unobtrusively and pull up the webpage on-demand without remembering the UI port you used. It's a hack and it runs the server without checking if you want it to.

At some future point, I will fix this to use a proper set of commands like 'start', 'stop', and so forth. 

For now, use '--help' or just 'help' to get the information on how it works.

```
Usage: serve-temporal [port_number] [web]
           Run temporal server.
       serve-temporal kill
           Terminate temporal server.
       serve-temporal web
           Open server web interface.
       serve-temporal help
           Show this message.
```

