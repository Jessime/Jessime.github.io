#!/usr/bin/env python3
# /// script
# dependencies = [
#   "pandas",
#   "plotly",
# ]
# ///

import re
import sys
import datetime
from pathlib import Path
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def extract_date_title(filepath: Path):
    """
    Given a Path like '2014-10-12-a_prelude_(part_i).md', returns
    (date(2014, 10, 12), 'a prelude (part i)').
    """
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$", filepath.name)
    if not m:
        return None, None
    date = datetime.datetime.strptime(m.group(1), "%Y-%m-%d").date()
    title = m.group(2).replace("_", " ")
    return date, title


def tokenize(text: str):
    """
    Simple word tokenizer: grabs word characters (allowing apostrophes),
    lowercases everything.
    """
    return re.findall(r"\b\w[\w']*\b", text.lower())


def main(posts_dir: str):
    posts_path = Path(posts_dir)
    md_files = sorted(posts_path.glob("*.md"))

    posts = []
    for fp in md_files:
        date, title = extract_date_title(fp)
        if date:
            posts.append((date, title, fp))

    if not posts:
        print(f"No valid '*.md' files found in {posts_dir}", file=sys.stderr)
        sys.exit(1)

    seen_words = set()
    cum_new = 0
    cum_total = 0
    records = []

    for date, title, fp in posts:
        text = fp.read_text(encoding="utf-8")
        tokens = tokenize(text)
        unique = set(tokens)
        new_words = unique - seen_words
        cum_new += len(new_words)
        seen_words |= new_words

        cum_total += len(tokens)

        records.append(
            {
                "date": date,
                "title": title,
                "cumulative_new_words": cum_new,
                "cumulative_total_words": cum_total,
            }
        )

    df = pd.DataFrame(records)

    # Create a figure with a secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Trace for cumulative new words
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["cumulative_new_words"],
            mode="lines+markers",
            name="Cumulative New Words",
            hovertext=df["title"],
            hovertemplate="<b>%{hovertext}</b><br>Date: %{x}<br>New Words: %{y}<extra></extra>",
        ),
        secondary_y=False,
    )

    # Trace for cumulative total words
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["cumulative_total_words"],
            mode="lines+markers",
            name="Cumulative Total Words",
            hovertext=df["title"],
            hovertemplate="<b>%{hovertext}</b><br>Date: %{x}<br>Total Words: %{y}<extra></extra>",
        ),
        secondary_y=True,
    )

    # Update axes titles
    fig.update_layout(
        title="Cumulative New vs Total Words Over Time", xaxis_title="Date of Post", hovermode="x unified"
    )
    fig.update_yaxes(title_text="Total Unique Words Seen", secondary_y=False)
    fig.update_yaxes(title_text="Total Words Written", secondary_y=True)

    fig.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        prog = Path(sys.argv[0]).name
        print(f"Usage: {prog} /path/to/blog/posts", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
