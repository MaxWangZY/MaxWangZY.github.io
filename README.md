# Zhengyang Wang personal website

This is a GitHub Pages site built with Jekyll.

## Edit content

- Home page: `index.md`
- Experience page: `experience.md`
- Blog index: `blog.md`
- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Homepage artifacts: `_data/artifacts.yml`
- CV PDF: `assets/cv/Zhengyang_Wang_CV.pdf`
- Portrait: `assets/images/portrait.jpg`
- Site settings: `_config.yml`
- Styles: `assets/css/style.css`

## Update CV and portrait

- Replace `assets/cv/Zhengyang_Wang_CV.pdf` with the latest CV PDF.
- Replace `assets/images/portrait.jpg` with the preferred portrait image.
- Keep those filenames stable so site links do not need to change.
- Update `experience.md` manually with concise highlights from the CV.

## Add a blog post

Create a Markdown file in `_posts` using this naming pattern:

```text
YYYY-MM-DD-short-title.md
```

For example:

```text
_posts/2026-06-06-my-first-post.md
```

Each post starts with front matter:

```markdown
---
layout: default
title: "My first post"
---

Write the post here.
```

`blog.md` is the blog index page. Do not put individual posts directly in
`blog.md` unless you want one long manual page instead of Jekyll blog posts.

## Publish

Push the repository to `https://github.com/MaxWangZY/MaxWangZY.github.io`.
GitHub Pages will build the site with Jekyll.

## Preview locally

If Ruby and Bundler are installed:

```bash
bundle init
bundle add github-pages --group "jekyll_plugins"
bundle exec jekyll serve
```

Then open `http://localhost:4000`.
