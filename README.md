# privtext-python

A command line utility to create private text messages on privtext.com. A must have utility for sys admins.

[![PrivText command line utility: basic usage](https://img.youtube.com/vi/9GYRzT3mYsc/0.jpg)](https://www.youtube.com/watch?v=9GYRzT3mYsc "Everything Is AWESOME")

# Install

```bash
pip install privtext
```

# Use

Example shell command:

```bash
privtext "Hello world"
```

Will encrypt the text "Hello world" and save on server, a one-time URL will be displayed:
```
https://privtext.com/hJwMs9#RPQxSwqPaaR4tJEX
```

Open the link, the text "hello world" will be decrypted and displayed, the record on the server will be deleted immedately.

# Why?

Safely share your secrets in chats, emails, and social networks. Never send your passwords in plain text, the logs are left on servers, your desktop. Make sure your chat logs do not compromise your secrets.

# Links

 - [PrivText.com - privtext on the Web](https://privtext.com/)
 - [PyPI](https://pypi.org/project/privtext)
 - [Github](https://github.com/privtext/privtext-python)
 - [Issues](https://github.com/privtext/privtext-python/issues)
 
## Code of Conduct

Everyone interacting in the privtext project's codebases, issue trackers, chat rooms, and mailing lists is expected to
follow the [PSF Code of Conduct](https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md).
