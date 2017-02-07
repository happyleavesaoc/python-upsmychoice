# python-upsmychoice

Python 3 API for [UPS My Choice](https://www.ups.com/mychoice/), a way to track packages.

## Prerequisites

Sign up for UPS My Choice and verify your address.

## Install

`pip install upsmychoice`

## Usage

```python
import upsmychoice

# Establish a session.
# Use the login credentials you use to login to UPS My Choice via the web.
# A login failure raises a `UPSError`.
session = upsmychoice.get_session("username", "password")

# Get all packages that UPS My Choice knows about.
packages = upsmychoice.get_packages(session)
```

## Caching
Session cookies are cached by default in `./upsmychoice_cookies.pickle` and will be used if available instead of logging in. If the cookies expire, a new session will be established automatically.

## Development

### Lint

`tox`

### Release

`make release`

### Contributions

Contributions are welcome. Please submit a PR that passes `tox`.

## Disclaimer
Not affiliated with UPS.
