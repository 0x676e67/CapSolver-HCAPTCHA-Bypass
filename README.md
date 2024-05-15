## Getting Started

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv

# With pipx.
pipx install uv

# With Homebrew.
brew install uv

# With Pacman.
pacman -S uv

```

To create a virtual environment:

```shell
uv venv  # Create a virtual environment at .venv.

```

To activate the virtual environment:

```shell
# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
    
```

```shell
python main.py
```
