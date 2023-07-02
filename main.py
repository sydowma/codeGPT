import os.path

from fastapi import FastAPI

import typer
import analysis_repository
import book_generator

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


@app.command()
def book(input_dir: str, output_dir: str = "./book", project_name: str = "MyProject"):
    # Generate a book from the explanations
    book_generator.generate_sphinx_project(input_dir, output_dir, project_name)


if __name__ == "__main__":
    app()
