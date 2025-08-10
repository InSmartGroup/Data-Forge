import requests
import secrets
import json


def verify_one_email_address(email_address: str, detailed_mode=False) -> str | object:
    """Accepts one email address and verifies it using EmailListVerify API.

    :param email_address: An email address you want to verify.
    :type email_address: str

    :param detailed_mode: If set to False, returns the result of email verification ("ok" = safe to send). If set to
    True, returns a detailed json report (applicable only if an email has "ok" status, otherwise returns only status).
    :type detailed_mode: bool

    :return: Returns the result of email verification, depending on the detailed_mode parameter.
    Common verification statuses:
    1) "ok" = an email is safe to send;
    2) "ok_for_all" = an email server accepts all emails, risky, can bounce back;
    3) "email_disabled" = an email address is disabled or doesn't exist, high risk.
    :rtype: str or json
    """

    params = {
        "secret": secrets.EMAILLISTVERIFY_API,
        "email": email_address
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }

    response = requests.get(secrets.URL_VERIFY_DETAILED, params=params, headers=headers)

    if detailed_mode and response.json()["result"] == "ok":
        report = {
            "email address": email_address,
            "validation status": response.json()["result"],
            "email service provider": response.json()["esp"],
            "MX server": response.json()["mxServer"],
            "MX server IP": response.json()["mxServerIp"],
        }

        return report

    else:
        return response.json()["result"]
