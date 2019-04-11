## Roadmap
1. Problem: `intensity_threshold` is too sensitive.
Ex: `scout-m8-backside` needs < 40, but `house-with-variety` needs > 60.
Solution: Compare the first 5 px band with the remaining 15 px band.
Work from deepest part of 5 px band out to the edge.
Stop early as soon as a transition intensity is greater than the
max(transition intensity) of the remaining 15px band by x%.

## Developer Setup

### Python
Install [Python 3.6](https://www.python.org/downloads/).

### IntelliJ
Install [IntelliJ Community Edition](https://www.jetbrains.com/idea/download/#section=windows) w/ these plugins:
* [Python Community Edition](https://plugins.jetbrains.com/plugin/7322-python-community-edition)
* [Markdown Navigator](https://plugins.jetbrains.com/plugin/7896-markdown-navigator)

#### SDK
Set up the project's Python SDK:

1. Create a Python virtual environment for the project:
   * Project Structure > Platform Settings > SDK > + > Python SDK > New environment
1. Install these packages to the virtualenv:
   * Project Structure > Platform Settings > SDK > Python 3.6 (Heroes-System-Image-Cropper) > Packages > + 
   * `Pillow` (5.4) - See API: https://pillow.readthedocs.io/en/stable/reference/Image.html
   * `pytest`(4.2)
   * `PyInstaller` (3.4)
1. Select the Project SDK:
   * Project Structure > Project Settings > Project > Project SDK: > Python 3.6 (Heroes-System-Image-Cropper)
1. Apply

#### Activate Venv
To run commands like `pytest` and `pyinstaller` you need to activate the virtual environment.
1. Open a terminal at the root of the project `Heroes-System-Image-Cropper/`
1. Run `venv/Scripts/activate`

*This must be done each time you open IntelliJ.*

#### Run unit tests
1. Activate Venv
1. Run `pytest`

See also: https://docs.pytest.org/en/latest/

#### Building the Executable
1. Activate venv
1. Run: `pyinstaller src/image_cropper/main.py --name heroes-system-image-cropper --onefile`

See also: https://pyinstaller.readthedocs.io/en/stable/usage.html

#### Run via IntelliJ
Follow these steps in order to run the program through IntelliJ:
1. Open `src/image_cropper/main.py`.
1. Right click anywhere within the file and select **Run 'main'**.
1. At the top right, select the dropdown titled **main** and click **Edit Configurations...**.
1. In **Parameters:** enter one or more paths to the files to crop. The paths are relative and start from the working directory `src/image_cropper`.
  * Note: right now, the parameters are replaced with a hardcoded value at the start of `main()`.
    In this case, set a fake argument like `IGNORE_ME` and change the file path from within the code.
