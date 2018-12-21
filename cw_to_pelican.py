#!/usr/bin/env python3

import sys
from pathlib import Path
from pprint import pprint

import psycopg2
import psycopg2.extras
from slugify import slugify

conn = psycopg2.connect(f"dbname=pyconfr")
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def write(article, category="article"):
    slug = slugify(article["cw_title"])
    creation_date = article["cw_creation_date"]
    root = Path(f"{creation_date.year}/content/blog/")
    root.mkdir(parents=True, exist_ok=True)
    ext = (
        "rst"
        if "cw_content_format" not in article
        or article["cw_content_format"] == "text/rest"
        else ".md"
    )
    with open(root / f"{category}-{slug}.{ext}", "w") as contentfile:
        if ext == "rst":
            contentfile.write(article["cw_title"] + "\n")
            contentfile.write("#" * len(article["cw_title"]) + "\n")
            contentfile.write(f":date: {creation_date.isoformat()}\n")
            contentfile.write(f":category: {category}\n")
            contentfile.write(f":tags: {creation_date.year}\n")
        else:
            contentfile.write(f"---\nTitle: {article['cw_title']}\n")
            contentfile.write(f"Date: {creation_date.isoformat()}\n")
            contentfile.write(f"Category: {category}\n")
            contentfile.write(f"Tags: {creation_date.year}\n")
        contentfile.write("\n")
        if "cw_description" in article and article["cw_description"]:
            contentfile.write(article["cw_description"])
            contentfile.write("\n\n")
        if "cw_content" in article:
            contentfile.write(article["cw_content"])
            contentfile.write("\n\n")


cur.execute("SELECT * FROM cw_blogentry;")
for article in cur:
    write(article, "blog")


cur.execute("SELECT * FROM cw_conference;")
for article in cur:
    write(article, "conference")


cur.execute("SELECT * FROM cw_sponsor;")
for article in cur:
    write(article, "sponsor")


cur.execute("SELECT * FROM cw_talk;")
for article in cur:
    write(article, "talk")


cur.execute("SELECT * FROM cw_file;")
for f in cur:
    creation_date = f["cw_creation_date"]
    static = Path(f"{creation_date.year}/static")
    static.mkdir(exist_ok=True)
    with open(static / f["cw_data_name"], "wb") as datafile:
        datafile.write(f["cw_data"])
