import re


def domain_breakdown(website_url: str, title_name=False) -> tuple:
    """Accepts a website URL and breaks it down into a company name and domain extension.

    :param website_url: Website URL you need to break-down.
    :type website_url: str

    :param title_name: If True, returns capitalized company name; otherwise, returns lowercase company name.
    :type title_name: bool

    :return: Company name, domain extension, and full company domain name (name + extension combined)
    :rtype: tuple
    """

    domain_prefix = r"https://www\.|http://www\.|https://|http://"
    domain_suffix = r"com|org|co|io|edu|tech"

    company_domain_all = re.findall(rf"(({domain_prefix})([A-Za-z0-9_.-]+)\.({domain_suffix}))",
                                    website_url)

    company_name = company_domain_all[0][-2]
    domain_extension = company_domain_all[0][-1]

    if not title_name:
        return company_name, domain_extension
    else:
        return company_name.title(), domain_extension, f"{company_name.lower()}.{domain_extension.lower()}"


def identify_company_profile(domain_extension) -> str | None:
    """Checks a company website domain extension and returns its business profile.

    :param domain_extension: A company domain extension (e.g. "com", "edu").
    :type domain_extension: str

    :return: If found, returns a company business profile; otherwise, returns None.
    :rtype: str or None
    """

    profiles = {
        "Business": ["com", "co"],
        "Education": ["edu"],
        "Information Technology & Services": ["tech", "io"],
        "Non-Profit Organization or Community": ["org"],
    }

    for key, item in profiles.items():
        if domain_extension in item:
            return key

    return None


def get_emails_from_full_name(full_name: str, domain_name: str) -> list:
    """Accepts person's full name and suggests the most common email addresses.

    :param full_name: A person's full name.
    :type full_name: str

    :param domain_name: A full domain name of a company (e.g. "coco-cola.com" or "boeing.com")
    :type domain_name: str

    :return: A list of the most common email addresses.
    :rtype: list
    """

    first_name, last_name = full_name.split()

    options = [f"{first_name}@{domain_name}",
               f"{first_name}.{last_name}@{domain_name}",
               f"{last_name}.{first_name}@{domain_name}",
               f"{first_name[0]}{last_name}@{domain_name}",
               f"{last_name}{first_name[0]}@{domain_name}"]

    return [i.lower() for i in options]
