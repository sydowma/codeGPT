import os.path

from fastapi import FastAPI

import typer
import analysis_repository

app = typer.Typer()


@app.command()
def main(repo_path: str, is_private: str = 'false', branch: str = "master"):
    client_public = analysis_repository.GitHubClient(url="https://api.github.com")
    is_private = is_private.lower() == 'true'
    client_public.get_repo(repo_path, is_private=is_private,
                           branch=branch)  # replace with the public repo you want to download
    # replace with the repo you want to download

    # client_private = GitHubClient(url="https://api.github.com", token="your_github_token")
    # client_private.get_repo("username/private-repo")  # replace with the private repo you want to download

    dir_path = os.path.join("./downloaded_sources/", repo_path + "-" + branch)
    analysis = analysis_repository.AnalysisRepository(dir_path=dir_path)
    analysis.ask()


if __name__ == "__main__":
    app()
