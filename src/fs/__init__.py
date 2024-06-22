# use `fs` as namespace pacakge for letting poetry editable installion work
__import__("pkg_resources").declare_namespace(__name__)  # type: ignore
