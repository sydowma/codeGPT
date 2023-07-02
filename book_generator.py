import os
import subprocess


def generate_sphinx_project(input_dir, output_dir, project_name):
    # Create the Sphinx project
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(["sphinx-quickstart", "--quiet", "-p", project_name, "-a", "Author", "-v", "1.0", "--sep", "--dot=_", "--suffix=.md", "--master=index", "--makefile", "--no-batchfile", "--no-use-make-mode", output_dir], check=True)

    # Enable myst-parser in conf.py
    with open(os.path.join(output_dir, "source", "conf.py"), "a") as conf_file:
        conf_file.write("\nextensions.append('myst_parser')\n")

    # Copy Markdown files into the Sphinx project's source directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                input_file = os.path.join(root, file)
                relative_dir = os.path.relpath(root, input_dir)
                output_file = os.path.join(output_dir, "source", relative_dir, file)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                subprocess.run(["cp", input_file, output_file], check=True)

    # Generate the table of contents
    with open(os.path.join(output_dir, "source", "index.md"), "a") as index_file:
        index_file.write('.. toctree::\n   :maxdepth: 100\n   :caption: Contents:\n')
        for root, dirs, files in os.walk(os.path.join(output_dir, "source")):
            for file in sorted(files):
                if file.endswith(".md"):
                    relative_file = os.path.relpath(os.path.join(root, file), os.path.join(output_dir, "source"))
                    relative_file = os.path.splitext(relative_file)[0]  # Remove the file extension
                    index_file.write("  [{0}]({1})\n\n".format(file, relative_file))

    # Build the Sphinx project
    subprocess.run(["make", "-C", output_dir, "html"], check=True)