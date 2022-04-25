_ = lambda s: s  # NOQA

WAGTAIL_SITE_NAME = _("{{ cookiecutter.project_name_verbose }}")

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
