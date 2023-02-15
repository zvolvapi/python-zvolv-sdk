# Python Zvolv SDK

The Zvolv Hyper automation platform offers several APIs to build apps. Each Zvolv API delivers part of the capabilities from the platform, so that you can pick just those that fit for your needs. This SDK offers a corresponding package for each of Zvolv’s APIs. They are small and powerful when used independently, and work seamlessly when used together, too.


[![pypi package][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Python Version][python-version]][pypi-url]
[![codecov][codecov-image]][codecov-url]
[![contact][contact-image]][contact-url]

Whether you're building a custom app for your team, or integrating a third party service into your Zvolv workflows, Zvolv Developer Kit for Python allows you to leverage the flexibility of Python to get your project up and running as quickly as possible.

## Table of contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Getting started tutorial](#getting-started-tutorial)
* [Basic Usage of the Web Client](#basic-usage-of-the-web-client)
  * [Sending a message to Slack](#sending-a-message-to-slack)
  * [Uploading files to Slack](#uploading-files-to-slack)
* [Support](#support)

### Requirements

---

This library requires Python 3.6 and above.

> **Note:** You may need to use `python3` before your commands to ensure you use the correct Python path. e.g. `python3 --version`

```bash
python --version

-- or --

python3 --version
```

### Installation

We recommend using [PyPI][pypi] to install the Zvolv Developer Kit for Python.

```bash
$ pip install zvolv_sdk
```

### Getting started tutorial

---

We've created this [tutorial](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial) to build a basic Slack app in less than 10 minutes. It requires some general programming knowledge, and Python basics. It focuses on the interacting with Slack's Web and RTM API. Use it to give you an idea of how to use this SDK.

**[Read the tutorial to get started!](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial)**

### Basic Usage of the Web Client

---

Slack provide a Web API that gives you the ability to build applications that interact with Slack in a variety of ways. This Development Kit is a module based wrapper that makes interaction with that API easier. We have a basic example here with some of the more common uses but a full list of the available methods are available [here][api-methods]. More detailed examples can be found in [our guide](https://slack.dev/python-slack-sdk/web/).

#### Sending a message to Slack

One of the most common use-cases is sending a message to Slack. If you want to send a message as your app, or as a user, this method can do both. In our examples, we specify the channel name, however it is recommended to use the `channel_id` where possible. Also, if your app's bot user is not in a channel yet, invite the bot user before running the code snippet (or add `chat:write.public` to Bot Token Scopes for posting in any public channels).

```python
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

try:
    response = client.chat_postMessage(channel='#random', text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
```

Here we also ensure that the response back from Slack is a successful one and that the message is the one we sent by using the `assert` statement.

### Support

---

If you get stuck, we’re here to help. The following are the best ways to get assistance working through your issue:

Use our [Github Issue Tracker][gh-issues] for reporting bugs or requesting features.
Visit the [Slack Community][slack-community] for getting help using Slack Developer Kit for Python or just generally bond with your fellow Slack developers.

<!-- Markdown links -->

[pypi-image]: https://badge.fury.io/py/slack-sdk.svg
[pypi-url]: https://pypi.org/project/slack-sdk/
[python-version]: https://img.shields.io/pypi/pyversions/slack-sdk.svg
[build-image]: https://github.com/slackapi/python-slack-sdk/workflows/CI%20Build/badge.svg
[build-url]: https://github.com/slackapi/python-slack-sdk/actions?query=workflow%3A%22CI+Build%22
[codecov-image]: https://codecov.io/gh/slackapi/python-slack-sdk/branch/main/graph/badge.svg
[codecov-url]: https://codecov.io/gh/slackapi/python-slack-sdk
[contact-image]: https://img.shields.io/badge/contact-support-green.svg
[contact-url]: https://slack.com/support
[slackclientv1]: https://github.com/slackapi/python-slackclient/tree/v1
[api-methods]: https://api.slack.com/methods
[rtm-docs]: https://api.slack.com/rtm
[events-docs]: https://api.slack.com/events-api
[bolt-python]: https://github.com/slackapi/bolt-python
[pypi]: https://pypi.org/
[gh-issues]: https://github.com/slackapi/python-slack-sdk/issues
[slack-community]: https://slackcommunity.com/
[files.upload]: https://api.slack.com/methods/files.upload
[aiohttp]: https://aiohttp.readthedocs.io/
[urllib]: https://docs.python.org/3/library/urllib.request.html
