import json
import pathlib

THIS_FILE = pathlib.PurePosixPath(
    pathlib.Path(__file__).relative_to(pathlib.Path().resolve())
)
ACTIONS_CHECKOUT = {"name": "Check out repository", "uses": "actions/checkout@v5"}


def gen(content: dict, target: str):
    pathlib.Path(target).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(target).write_text(
        json.dumps(content, indent=2, sort_keys=True), newline="\n"
    )


def gen_dependabot():
    target = ".github/dependabot.yaml"
    content = {
        "version": 2,
        "updates": [
            {
                "package-ecosystem": e,
                "allow": [{"dependency-type": "all"}],
                "directory": "/",
                "schedule": {"interval": "daily"},
            }
            for e in ["github-actions", "uv"]
        ],
    }
    gen(content, target)


def gen_pdf_workflow():
    target = ".github/workflows/gen-pdf.yaml"
    content = {
        "env": {
            "description": f"This workflow ({target}) was generated from {THIS_FILE}",
        },
        "name": "Generate PDF",
        "on": {
            "pull_request": {"branches": ["main"]},
            "push": {"branches": ["main"]},
            "workflow_dispatch": {},
        },
        "jobs": {
            "gen-pdf": {
                "name": "Generate PDF",
                "runs-on": "ubuntu-latest",
                "steps": [
                    ACTIONS_CHECKOUT,
                    {
                        "name": "Configure Actions cache for downloaded content",
                        "uses": "actions/cache@v4",
                        "with": {"key": "download-cache", "path": ".local"},
                    },
                    {"name": "Generate PDFs", "run": "sh ci/generate-pdfs.sh"},
                    {
                        "name": "Upload artifact",
                        "uses": "actions/upload-artifact@v4",
                        "if": "github.event_name == 'push' || github.event_name == 'workflow_dispatch'",
                        "with": {"name": "hymns", "path": "hymns*.pdf"},
                    },
                ],
            }
        },
    }
    gen(content, target)


def gen_ruff_workflow():
    target = ".github/workflows/ruff.yaml"
    content = {
        "name": "Ruff",
        "on": {
            "pull_request": {"branches": ["master"]},
            "push": {"branches": ["master"]},
        },
        "permissions": {"contents": "read"},
        "env": {
            "description": f"This workflow ({target}) was generated from {THIS_FILE}",
        },
        "jobs": {
            "ruff": {
                "name": "Run ruff linting and formatting checks",
                "runs-on": "ubuntu-latest",
                "steps": [
                    ACTIONS_CHECKOUT,
                    {
                        "name": "Run ruff check",
                        "uses": "astral-sh/ruff-action@v3",
                        "with": {"args": "check --output-format=github"},
                    },
                    {
                        "name": "Run ruff format",
                        "uses": "astral-sh/ruff-action@v3",
                        "with": {"args": "format --check"},
                    },
                ],
            }
        },
    }
    gen(content, target)


def main():
    gen_dependabot()
    gen_pdf_workflow()
    gen_ruff_workflow()


if __name__ == "__main__":
    main()
