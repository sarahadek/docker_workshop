FROM python:3.13.11-slim 

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Copy dependency files first (better layer caching)
COPY pyproject.toml .python-version uv.lock ./
# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Add this back!
RUN pip install pandas pyarrow

# set working directory and PATH
WORKDIR /code

# Create a virtual environment to path so we can install packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy the script into /code
COPY pipeline.py .

# Use the absolute path to be 100% safe
ENTRYPOINT ["python", "pipeline.py"] 